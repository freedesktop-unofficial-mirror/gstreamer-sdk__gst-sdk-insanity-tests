#!/usr/bin/env python

import os
import sys
import subprocess
import re
import string

mount_point=None

def unmount_media_root(location, silent=False):
    if not silent:
        print "Unmounting media root"
    try:
        if os.uname()[0] == 'Linux':
            subprocess.check_call(["fusermount", "-u", "-z", location])
        elif os.uname()[0] == 'Darwin':
            subprocess.check_call(["umount", location])
        else:
            raise Exception('%s not supported' % os.uname()[0]);
    except Exception,e:
        if not silent:
            print 'Failed to unmount media root: %s' % e

def set_media_root(location):
    global mount_point
    mount_point=None
    path=os.path.expanduser("~/mnt/insanity_tests_media_root")
    if not os.path.exists(path):
        os.makedirs(path)
    print "Mounting media root"
    unmount_media_root(path, True);
    subprocess.check_call(["sshfs", location, path])
    mount_point=path
    return mount_point

def expandvars(argument):
    return os.path.expandvars(argument)

def insanity(test,args):
    if len(sys.argv) > 1:
        testsdir = expandvars(sys.argv[1])
    else:
        testsdir = 'tests'

    cmd = ['insanity-run', '-T', testsdir, '-t', test]
    if args:
        cmd.append ('--args')
        cmd.extend (args)
    print 'Running command: %r' % cmd
    try:
        process = subprocess.check_call(cmd)
    except Exception,e:
        print 'Exception running %r: %s' % (cmd, e)
        raise

def summarize():
    cmd = ['insanity-dumpresults', 'testrun.db', '-l']
    #print 'Running command: %r' % cmd
    try:
        process = subprocess.check_call(cmd, stderr=subprocess.STDOUT)
    except Exception,e:
        print 'Exception running %r: %s' % (cmd, e)
        raise
    #if not line:
        #raise Exception("No output")
    #lines = string.split(line,"\n")
    # insanity-dumpresults prints an empty line after the last results line
    #if not lines or len(lines) <= 1:
    #    raise Exception("Output has less than two lines")
    #last_line = lines[len(lines)-2]
    #errors = int(re.sub(r'.*Failed:[^0-9]*([0-9]+).*', '\\1', last_line))
    #if errors != 0:
    #    raise Exception("One or more tests failed")

def done():
    global mount_point
    if mount_point:
        unmount_media_root(mount_point);
        mount_point = None
    try:
        summarize()
        sys.exit(0)
    except Exception,e:
        print 'Error:', e
        sys.exit(1)
