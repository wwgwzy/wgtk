import ffmpy
import os
import sys
from ffmpy import utils

xxx = r'z:\wwg\Library\Porn\XXX'
clip = r'z:\wwg\Library\Porn\Clip'
hf = r'y:\wwg\Library\Videos\ Movies'

target_codec = ['h264', 'hevc', 'vp8', 'vp9']
target_ext = ['.mp4', '.mkv', '.flv', '.webm', '.mov']
for video_file in utils.find_video_files(hf):

    try:
        aFFmedia = ffmpy.ffmedia(video_file)
    except:
        sys.stdout.write('\rffmpy init error : %s\n'%video_file)
        continue

    sys.stdout.write('\r{0} {1}'.format('%-5s'%aFFmedia.codec_name, '%s'%os.path.basename(aFFmedia.path)))
    if aFFmedia.codec_name in target_codec and aFFmedia.ext in target_ext : continue
    else:
        print('')

    output_file = os.path.splitext(aFFmedia.path)[0] + '.H264.AAC.mp4'
    if not aFFmedia.codec_name in target_codec:
        aFFmedia.transcode(output_file, over_write=True, loglevel='error')
    elif aFFmedia.codec_name in target_codec:
        aFFmedia.transcode(output_file, over_write=True, loglevel='error', vcodec_copy=True)