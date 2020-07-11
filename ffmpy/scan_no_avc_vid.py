import ffmpy
import os
import sys
from ffmpy import utils

xxx = r'z:\wwg\Library\Porn\XXX\kksk\[Lucy-Cat]'
thePath = r'z:\wwg'
for video_file in utils.find_video_files(thePath):

    try:
        aFFmedia = ffmpy.ffmedia(video_file)
    except:
        sys.stdout.write('\rffmpy init error : %s\n'%video_file)
        continue

    sys.stdout.write('\r{0} {1}'.format('%-5s'%aFFmedia.codec_name, '%s'%os.path.basename(aFFmedia.path)))
    if aFFmedia.is_AVCorHEVC and (aFFmedia.ext in ['.flv', '.mp4', '.mkv']) : continue
    else:
        print('')