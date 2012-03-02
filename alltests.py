#!/usr/bin/env python

import os
import helper

MEDIA_ROOT=os.path.expanduser("~/mnt/keema")

helper.insanity(
    test = "blank-c-gst-test",
    args = [
      'pipeline-launch-line:constant:fakesrc num-buffers=1 ! fakesink'
    ],
)

helper.insanity(
    test = "blank-c-gst-test",
    args = [
      'uri:filesystem:'+MEDIA_ROOT+'/srv/shared/media-samples'
    ],
)

helper.done()

