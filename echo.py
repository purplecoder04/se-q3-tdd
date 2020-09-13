#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "purplelover04 and coach john and study hall"


import sys
import argparse


def create_parser():
    """Create a command line parser object with 2 argument definitions."""
    parser = argparse.ArgumentParser(
        description="Extracts and alphabetizes baby names from html.")
    parser.add_argument('-l', '--lower', help='lowercase', action='store_true')
    parser.add_argument('-u', '--upper', help='uppercase', action='store_true')
    parser.add_argument('-t', '--title', help='titlecase', action='store_true')
    parser.add_argument('text', help='filename(s) to parse', )
    return parser


def main(args):
    """Implementation of echo"""
    parser = create_parser()
    ns = parser.parse_args(args)
    if not ns:
        parser.print_usage(args)
        sys.exit(1)

    text = ns.text
    if ns.title:
        print(text.title())
    elif ns.lower:
        print(text.lower())
    elif ns.upper:
        print(text.upper())
    else:
        print(text)
    return


if __name__ == '__main__':
    main(sys.argv[1:])
