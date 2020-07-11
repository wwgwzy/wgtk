# coding=utf-8

import os
import re

class ping():
    def __init__(self, addr, count=3, timeout=1000):

        self.addr = addr.strip()

        rslt = os.popen("ping -n %s -w %s %s"%(count, timeout, addr)).read()
        
        if re.search(r"100% 丢失", rslt):
            self.lost = 100
            self.lag = timeout

        else:
            pattern = re.compile(r'''
    数据包: 已发送 = \d*，已接收 = \d*，丢失 = \d* \((\d*)% 丢失\)，
往返行程的估计时间\(以毫秒为单位\):
    最短 = \d*ms，最长 = \d*ms，平均 = (\d*)ms
''')
            rslt_match = pattern.search(rslt)
            try:
                self.lag = rslt_match.group(2)
            except:
                print(rslt)
            self.lost = rslt_match.group(1)
