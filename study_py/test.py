# -*- UTF-8 -*-
import time
import pandas as pd

with open("./data/原始数据.csv", "r", encoding="utf-8") as file:
    END = []
    lines = file.readlines()
    num = len(lines)
    END = [[0]] * num

    for i in range(num):
        data = lines[i].split(",")

        timestamp = round(int(data[0]) / 1000.0)
        time_local = time.localtime(timestamp)
        times1 = time.strftime("%Y-%m-%d %H:%M:%S", time_local)

        timestamp = round(int(data[5]) / 1000.0)
        time_local = time.localtime(timestamp)
        times2 = time.strftime("%Y-%m-%d %H:%M:%S", time_local)

        loc = data[2] + "-" + data[3]

        END[i] = [times1, data[1], loc, data[4][2:], times2]