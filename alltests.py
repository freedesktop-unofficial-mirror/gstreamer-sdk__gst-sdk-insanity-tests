#!/usr/bin/env python

import os
import helper

MEDIA_ROOT = helper.set_media_root("keema.collabora.co.uk:/")

try:
    helper.insanity(
        test = "play-test",
        args = [
            'uri:urifilesystem:'+MEDIA_ROOT+'/srv/shared/media-samples/sorted/WebM'
        ],
    )

    #helper.insanity(
    #    test = "blank-c-gst-test",
    #    args = [
    #      'pipeline-launch-line:constant:fakesrc num-buffers=1 ! fakesink',
    #      'uri:filesystem:'+MEDIA_ROOT+'/srv/shared/media-samples'
    #    ],
    #)
finally:
    helper.done()

