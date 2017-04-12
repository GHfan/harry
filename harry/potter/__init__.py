#!/usr/bin/env python
#coding: utf-8
from __future__ import print_function

import os
import sys
import logging
from distutils import spawn

import argparse

debug = os.environ.get("HARRY_DEBUG", "off").lower() in ("on", "true", "1")

if debug:
    logging.basicConfig(level=logging.DEBUG)

log = logging.getLogger(__name__)

def get_version():
    return "0.0.0"

def _root():
    from harry import __file__
    return os.path.dirname(__file__)

def run(*cmds):
    log.debug("commands: %s", cmds)
    root_dir = _root()
    log.debug("harry root dir: %s", root_dir)

    bootstrap_dir = os.path.join(root_dir, "bootstrap")
    log.debug("harry bootstrap dir: %s", bootstrap_dir)

    python_path = os.environ.get('PYTHONPATH', '')

    if python_path:
        _path = "%s%s%s" % (bootstrap_dir, os.path.pathsep, python_path)
        os.environ["PYTHONPATH"] = _path
    else:
        os.environ["PYTHONPATH"] = bootstrap_dir

    log.debug("PYTHONPATH: %s", os.environ["PYTHONPATH"])
    log.debug("sys.path: %s", sys.path)

    executable = cmds[0]
    executable = spawn.find_executable(executable)
    log.debug("executable: %s", executable)

    # 1st arguments is the process name
    os.execl(executable, executable, *cmds[1:])

def main():
    parser = argparse.ArgumentParser(description="Well, depends on u")
    parser.add_argument("-v", "--version", help="Harry version",
                        action="version",
                        version="%(prog)s {0}".format(get_version()))


    subparsers = parser.add_subparsers(title="spells",
            description="harry's spells",
            dest="spell")
    subparsers.required = True
    parser_run = subparsers.add_parser("run", help="run run run")
    parser_run.add_argument('ingredients', nargs=argparse.REMAINDER)
    parser_run.set_defaults(func=run)

    args = parser.parse_args()
    print(args)
    args.func(*args.ingredients)
