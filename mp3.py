#!.venv/bin/python
import argparse
import logging
import os

import eyed3

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler('mp3.log')
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def iterate_files(directory, overwrite_title):
    for dir_item in os.listdir(directory):
        file_path = os.path.join(directory, dir_item)

        if os.path.isdir(file_path):
            iterate_files(file_path, overwrite_title)
        elif os.path.isfile(file_path):
            audiofile = get_audiofile(file_path)
            if not audiofile:
                continue
            if not audiofile.tag:
                audiofile.initTag()
            set_album_tag(audiofile)
            set_title_tag(audiofile, overwrite_title)
            audiofile.tag.save()


def get_audiofile(file_path):
    audiofile = eyed3.load(file_path)
    return audiofile


def set_album_tag(audiofile):
    if audiofile.tag.album:
        logger.info(
            f'Ommiting file "{audiofile.path}" \
            with album name "{audiofile.tag.album}"')
        return

    audiofile.tag.album = audiofile.path.split(os.sep)[-2:-1].pop()
    logger.info(
        f'File "{audiofile.path}" \
        updated Album name to "{audiofile.tag.album}"')


def set_title_tag(audiofile, overwrite_title):
    if audiofile.tag.title:
        logger.info(
            f'Ommiting file "{audiofile.path}" \
            with album name "{audiofile.tag.album}"')
        return

    audiofile.tag.title = os.path.basename(audiofile.path)
    logger.info(
        f'File "{audiofile.path}" updated Title to "{audiofile.tag.title}"')


def main():
    parser = argparse.ArgumentParser(
        description="Use mp3 files parent directory name\
        to set album name for mp3 files with empty tag.")
    parser.add_argument('directory', type=str, help='mp3 main directory path')
    parser.add_argument(
        "--overwrite_title",
        help="Overwrites files title tag with filename",
        action="store_true")

    args = parser.parse_args()
    logger.debug(f'Running inside of: {args.directory}')

    iterate_files(args.directory, overwrite_title=args.overwrite_title)


if __name__ == '__main__':
    main()
