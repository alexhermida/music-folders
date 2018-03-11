#!.venv/bin/python
import argparse
import logging
from os import listdir, path, sep

import eyed3


def iterate_files(directory):
    for dir_item in listdir(directory):
        file_path = path.join(directory, dir_item)

        if path.isdir(file_path):
            iterate_files(file_path)
            print('isdir')
        elif path.isfile(file_path):
            audiofile = get_audiofile(file_path)
            if audiofile:
                directory_name = file_path.split(sep)[-2:-1].pop()
                set_tags(audiofile, directory_name)


def get_audiofile(file_path):
    audiofile = eyed3.load(file_path)
    return audiofile

def set_tags(audiofile, album):
    if not audiofile.tag:
        audiofile.initTag()
    if not audiofile.tag.album:
        print('Setting album name to:', album)
        audiofile.tag.album = album
        audiofile.tag.save()

def main():
    parser = argparse.ArgumentParser(description='Use mp3 files parent directory name to set album name for mp3 files with empty tag.')
    parser.add_argument('directory', type=str, help='mp3 main directory path')
    args = parser.parse_args()
    print(args.dir)
    iterate_files(args.dir)

if __name__ == '__main__':
    main()
