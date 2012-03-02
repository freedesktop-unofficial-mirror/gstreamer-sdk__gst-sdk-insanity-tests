import subprocess

def insanity(test,args):
    cmd = ['insanity-run', '-T', 'tests', '-t', test]
    if args:
        cmd.extend (args)
    print 'Running command: %r' % cmd
    try:
        process = subprocess.Popen(cmd)
    except Exception,e:
        print 'Exception running %r: %s' % (cmd, e)
        return
    if process.stdin:
        process.stdin.close()
    if process.stdout:
        process.stdout.close()
    if process.stderr:
        process.stderr.close()

insanity(
    test = "blank-c-gst-test",
    args = [
      'pipeline-launch-line:constant:"fakesrc num-buffers=1 ! fakesink"'
    ],
#  Hopefully something like:
#    test = "discoverer",
#    args = [
#      'uri:filesystem:/mnt/keema/srv/shared/media-samples
#    ],
)


