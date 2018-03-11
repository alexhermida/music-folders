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


def iterate_files(directory):
    for dir_item in os.listdir(directory):
        file_path = os.path.join(directory, dir_item)

        if os.path.isdir(file_path):
            iterate_files(file_path)
        elif os.path.isfile(file_path):
            audiofile = get_audiofile(file_path)
            if audiofile:
                directory_name = file_path.split(os.sep)[-2:-1].pop()
                set_tags(audiofile, directory_name)


def get_audiofile(file_path):
    audiofile = eyed3.load(file_path)
    return audiofile


def set_tags(audiofile, album):
    if not audiofile.tag:
        audiofile.initTag()
    if not audiofile.tag.album:
        filename = os.path.basename(audiofile.path)
        # audiofile.tag.album = album
        # audiofile.tag.save()
        logger.info(f'Album of "{filename}" updated to "{album}"')


def main():
    parser = argparse.ArgumentParser(
        description="Use mp3 files parent directory name\
        to set album name for mp3 files with empty tag.")
    parser.add_argument('directory', type=str, help='mp3 main directory path')
    args = parser.parse_args()
    logger.debug(f'Running inside of: {args.directory}')
    iterate_files(args.directory)


if __name__ == '__main__':
    main()
