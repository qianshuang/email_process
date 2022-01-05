# -*- coding: utf-8 -*-

import datetime
import re


def open_file(filename, mode='r'):
    return open(filename, mode, encoding='utf-8', errors='ignore')


def read_file(filename):
    return [line.strip() for line in open(filename).readlines()]


def write_file(filename, content):
    open_file(filename, mode="w").write(content)


def write_lines(filename, list_res):
    test_w = open_file(filename, mode="w")
    for j in list_res:
        test_w.write(j + "\n")


def get_text_content(msgMessage):
    data = msgMessage.get_payload(decode=True)

    try:
        encoding = msgMessage.get_charsets()[0]
        if not encoding:
            encoding = "gb2312"
        return str(data, encoding=encoding)
    except:
        # print(data)
        # print(msgMessage.get_charsets())
        return "decode failed..."
    # return data


def time_process(gmt_time):
    try:
        GMT_FORMAT = '%a, %d %b %Y %H:%M:%S'
        return str(datetime.datetime.strptime(" ".join(gmt_time.split()[:5]), GMT_FORMAT))
    except:
        GMT_FORMAT = '%d %b %Y %H:%M:%S'
        return str(datetime.datetime.strptime(" ".join(gmt_time.split()[:4]), GMT_FORMAT))


def process_cont(conts):
    final_conts = []
    conts = conts.split("&&&&&&")[:-1]
    for cont in conts:
        cont = cont.replace("\n", " ")

        # 剔除style及html标签
        cont = re.sub(r'<style.+?</style>', '', cont)
        cont = re.sub(r'<(.|\n)+?>', '', cont)
        cont = re.sub(r'CAUTION:.*know the content is safe', '', cont)
        cont = re.sub(r'(&nbsp;|‌|&#8204;|‌ )', ' ', cont)
        cont = re.sub(r'\s+', ' ', cont)

        final_conts.append(cont)
    return final_conts
