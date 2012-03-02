#!/usr/bin/env python

import helper

MEDIA_ROOT="~/mnt/keema"

helper.insanity(
    test = "blank-c-gst-test",
    args = [
      'pipeline-launch-line:constant:fakesrc num-buffers=1 ! fakesink'
    ],
#  Hopefully something like:
#    test = "discoverer",
#    args = [
#      'uri:filesystem:/mnt/keema/srv/shared/media-samples
#    ],
)

helper.done()

