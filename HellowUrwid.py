#!/usr/bin/env python

"""A simple python script template.
"""

from __future__ import print_function
import os
import sys
import argparse
from unicodedata import numeric

import urwid

txt = urwid.Text(u"Hello World")
fill = urwid.Filler(txt, 'top')

def show_or_exit(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()
    txt.set_text(repr(key))

def urwid_test():
    loop = urwid.MainLoop(fill, unhandled_input=show_or_exit)
    loop.run()

def main(arguments):
    # parser = argparse.ArgumentParser(
    #     description=__doc__,
    #     formatter_class=argparse.RawDescriptionHelpFormatter)
    #
    # parser.add_argument('-h', '--help', help='show help')
    urwid_test()

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))