# coding=utf-8

from pingex import ping

with open("dnssvr.txt", encoding="utf8") as dnssvrf:
    for i in dnssvrf.readlines():
        if not (i[0] == "#" or i == "\n"):
            Ping = ping(i,5,10000)
            print("%-15s %6s %4s"%(Ping.addr, Ping.lag, Ping.lost))
