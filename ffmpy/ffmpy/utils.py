import os

def find_files(thePath, the_specific_ext=[]):
    for walkr in os.walk(thePath):
        for file in walkr[2]:
            if the_specific_ext:
                if os.path.splitext(file)[1] in the_specific_ext:
                    yield os.path.join(walkr[0], file)
            else:
                yield os.path.join(walkr[0], file)

def find_video_files(thePath, the_specific_ext=None):
    if the_specific_ext is None:
        the_specific_ext = ['.avi', '.flv', '.m2t', '.mp4', '.mkv', '.mov', '.mpeg', '.mpg', '.rmvb', '.wmv', '.webm']
    return find_files(thePath, the_specific_ext=the_specific_ext)