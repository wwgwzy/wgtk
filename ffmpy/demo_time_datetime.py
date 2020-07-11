# coding=utf-8

str_time = '0:5:2.55'

def strftime_get_second(strftime):

        strftime_l = strftime.split(':')

        hour = int(strftime_l[0])
        min = int(strftime_l[1])
        sec = int(float(strftime_l[2]))

        return hour * 3600 + min *60 + sec