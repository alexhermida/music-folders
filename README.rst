POC tool to set album names to music files
==========================================

Tiny command line utility to set album name to
files that don't have it using eyeD3_.

.. _eyeD3: https://github.com/nicfit/eyeD3

If you have many downloaded `mp3` files without
album name you can organize them in folders and the
tool can set the name for you using the parent folder name.

This is specially useful when you have a music player
(car player, mp3 portable player, etc.) that it isn't
browsable between folders.

The goal of this tool is not only the above but
also to be an example of using Python with different
tools and modules like:

- pipenv
- flake8
- isort
- logging
- argparse


Requirements
------------

* Python >=3.6
* Pipenv https://github.com/pypa/pipenv/


Running the program
-------------------

Just use pipenv::

    $ pipenv run python mp3.py {directory_path}

Or, if you're using other virtualenv manager:

    $ python mp3.py {directory_path}
