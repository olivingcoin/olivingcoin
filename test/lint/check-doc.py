#!/usr/bin/env python3
# Copyright (c) 2015-2018 The Olivingcoin Core developers
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

'''
This checks if all command line args are documented.
Return value is 0 to indicate no error.

Author: @MarcoFalke
'''

from subprocess import check_output
import re
import sys

FOLDER_GREP = 'src'
FOLDER_TEST = 'src/test/'
REGEX_ARG = '(?:ForceSet|SoftSet|Get|Is)(?:Bool)?Args?(?:Set)?\("(-[^"]+)"'
REGEX_DOC = 'AddArg\("(-[^"=]+?)(?:=|")'
CMD_ROOT_DIR = '`git rev-parse --show-toplevel`/{}'.format(FOLDER_GREP)
CMD_GREP_ARGS = r"git grep --perl-regexp '{}' -- {} ':(exclude){}'".format(REGEX_ARG, CMD_ROOT_DIR, FOLDER_TEST)
CMD_GREP_DOCS = r"git grep --perl-regexp '{}' {}".format(REGEX_DOC, CMD_ROOT_DIR)
# list unsupported, deprecated and duplicate args as they need no documentation
SET_DOC_OPTIONAL = set(['-h', '-help', '-dbcrashratio', '-forcecompactdb'])


def main():
    if sys.version_info >= (3, 6):
        used = check_output(CMD_GREP_ARGS, shell=True, universal_newlines=True, encoding='utf8')
        docd = check_output(CMD_GREP_DOCS, shell=True, universal_newlines=True, encoding='utf8')
    else:
        used = check_output(CMD_GREP_ARGS, shell=True).decode('utf8').strip()
        docd = check_output(CMD_GREP_DOCS, shell=True).decode('utf8').strip()

    args_used = set(re.findall(re.compile(REGEX_ARG), used))
    args_docd = set(re.findall(re.compile(REGEX_DOC), docd)).union(SET_DOC_OPTIONAL)
    args_need_doc = args_used.difference(args_docd)
    args_unknown = args_docd.difference(args_used)

    print("Args used        : {}".format(len(args_used)))
    print("Args documented  : {}".format(len(args_docd)))
    print("Args undocumented: {}".format(len(args_need_doc)))
    print(args_need_doc)
    print("Args unknown     : {}".format(len(args_unknown)))
    print(args_unknown)

    sys.exit(len(args_need_doc))


if __name__ == "__main__":
    main()
