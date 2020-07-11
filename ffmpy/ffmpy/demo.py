import ffmpy

video_stream = ffmpy.get_info('D:\\wwg\\Box\\ffmpy\\tst_vid\\1pondo-012415_016.avi')

width = int(video_stream['width'])
height = int(video_stream['height'])
num_frames = int(video_stream['nb_frames'])
duration = (video_stream['duration'])
bitrate = (video_stream['bit_rate'])