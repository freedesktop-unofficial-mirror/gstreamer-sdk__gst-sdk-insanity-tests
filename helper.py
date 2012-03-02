#!/usr/bin/env python

import sys
import subprocess
import re

def insanity(test,args):
    if len(sys.argv) > 1:
        testsdir = sys.argv[1]
    else:
        testsdir = 'tests'

    cmd = ['insanity-run', '-T', testsdir, '-t', test]
    if args:
        cmd.append ('--args')
        cmd.extend (args)
    #print 'Running command: %r' % cmd
    try:
        process = subprocess.check_call(cmd)
    except Exception,e:
        print 'Exception running %r: %s' % (cmd, e)
        raise

def summarize():
    cmd = ['insanity-dumpresults', 'testrun.db', '-l']
    #print 'Running command: %r' % cmd
    try:
        line = subprocess.check_output(cmd, universal_newlines=True)
    except Exception,e:
        print 'Exception running %r: %s' % (cmd, e)
        raise
    errors = int(re.sub(r'.*Failed:[^0-9]*([0-9]+).*', '\\1', line))
    if errors != 0:
        raise Exception("One or more tests failed")

def done():
    try:
        summarize()
        sys.exit(0)
    except Exception,e:
        print 'Error:', e
        sys.exit(1)

