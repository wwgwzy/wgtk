import ffmpeg
import sys
import subprocess
import re
import os
from tqdm import *
from datetime import datetime

class ffmedia():
    def __init__(self, video_file):
        self.path = video_file
        self.get_info()
        self.basename = os.path.basename(self.path)

    # get info from stream
    def get_info(self):
        self.ext = os.path.splitext(self.path)[1]
        self.stream = self.get_stream()
        #self.num_frames = self.stream['nb_frames'] if 'nb_frames' in self.stream else None
        self.codec_name = self.stream['codec_name']
        #self.codec_long_name = self.stream['codec_long_name']
        self.duration = self.stream['duration'] if 'duration' in self.stream else None
        #self.is_avc = self.codec_name in ['h264', 'hevc']

    def get_stream(self):
        probe = ffmpeg.probe(self.path)
        video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
        if video_stream is None:
            print('No video stream found', file=sys.stderr)
            sys.exit(1)
        return video_stream

    # transcode and yield output info (frames, time, speed), exec by subprocess.Popen()
    def real_transcode_1(self, output_file, over_write=False):
        input_file = self.path
        theCMD = ['ffmpeg', '-i', input_file, output_file]
        if over_write : theCMD.append('-y')
        p = subprocess.Popen(theCMD,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT,
                             bufsize=1,
                             universal_newlines=True)
        optinfo_pattern = re.compile(r'frame=\s*(\d+).*time=(.+) bitrate.*speed=(.*)x')
        for line in iter(p.stdout.readline, b''):
            line = line.strip()
            if not line.startswith('frame'): continue
            optinfo_match = optinfo_pattern.match(line)
            optinfo = (optinfo_match.group(1), optinfo_match.group(2), optinfo_match.group(3))
            yield optinfo

    def transcode_with_tqdm(self, output_file, over_write=False):
        with tqdm(total=int(float(self.duration)) if self.duration else None,
                  desc='%-24s %-5s'%(self.basename, self.codec_name),
                  ncols=None,
                  unit='sec',
                  mininterval=0.1,
                  bar_format='{desc} [ {percentage:2.0f}% ] [{bar}] [{n}/{total}] [{elapsed} -> {remaining}] [{rate_fmt} {rate_inv_fmt}]') as pbar:
            for optinfo in self.real_transcode(output_file, over_write=over_write):
                print(optinfo[1])
                pbar.update(strftime_get_sec(optinfo[1]))

    def transcode(self, output_file, over_write=False, vcodec_copy=False, loglevel='info'):
        input_file = self.path
        theCMD = ['ffmpeg', '-i', '"%s"'%input_file]
        if vcodec_copy:
            theCMD.extend(['-vcodec', 'copy'])
        if over_write:
            theCMD.append('-y')
        theCMD.extend(['"%s"'%output_file, '-loglevel', loglevel])
        theCMD_str = ' '.join(theCMD)
        #print(theCMD)
        ret = os.system(theCMD_str)