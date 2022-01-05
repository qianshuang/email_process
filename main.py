# -*- coding: utf-8 -*-

import email
import os

from common import *

import pandas as pd

ORI_DATA = "ori_data"

df_final = pd.DataFrame()
subjects = []
contents = []
times = []

for file_name in os.listdir(ORI_DATA):
    file_path = os.path.join(ORI_DATA, file_name)
    with open(file_path, 'rb') as f:
        eml = email.message_from_binary_file(f)

        mBody = []
        for part in eml.walk():  # 循环信件中的每一个mime的数据块
            content_maintype = part.get_content_maintype()
            if content_maintype == 'text':
                cont = get_text_content(part).strip()
                if cont != "" and (not cont.startswith("<html")) and (not cont.startswith("<?xml")):
                    mBody.append(cont)
        cont = "@@@".join(mBody)
        if cont != "":
            subjects.append(eml.get("SUBJECT").replace("\n", " "))
            times.append(time_process(eml.get("DATE")))
            contents.append(cont + "&&&&&&")

write_lines("subject.txt", subjects)
write_lines("content.txt", contents)
write_lines("time.txt", times)
write_lines("content.txt", process_cont(open_file("content.txt").read()))

df_final = pd.DataFrame()
df_final["subject"] = read_file("subject.txt")
df_final["content"] = read_file("content.txt")
df_final["time"] = read_file("time.txt")

df_final = df_final.groupby('subject').apply(lambda x: x.sort_values('time'))
print(df_final)
df_final.to_csv("emails.txt", sep="\t", index=False)

os.remove("subject.txt")
os.remove("content.txt")
os.remove("time.txt")
