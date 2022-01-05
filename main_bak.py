# -*- coding: utf-8 -*-

import base64


# import email


class myEml:
    mFrom = {}
    mTo = []
    mCc = []
    mDate = ""
    mSubject = ""
    mBody = []
    mAtta = []

    msg = None
    needSaveFile = False

    # base64解码
    def myDecoder(self, bStr, bCode='us-ascii'):
        if bStr == None:
            return ""

        myStr = bStr.replace("\"", "")
        print(myStr)
        fflist = myStr.split('?')
        if (len(fflist) > 2):
            coder = fflist[1]
            print(coder)
            strmsg = fflist[3]
            print(strmsg)
            aa = base64.b64decode(strmsg).decode(coder)
        else:
            aa = ""
        return aa

    # 保存附件到本地或者获取数据流
    def SaveFile(self, data, filename):
        if (self.needSaveFile == True):
            with open(filename, 'wb') as f:
                f.write(data)
        else:
            self.mAtta.append({'filename': filename, 'data': data})

    # 解析出附件的内容并解码
    def GetAttachmentData(self, msgMessage, filename, maintype='application'):
        if (maintype == 'application'):
            data = self.Get_ApplicationContent(msgMessage)

        elif (maintype == 'text'):
            data = self.Get_TextContent(msgMessage)
        self.SaveFile(data, filename)

        return None

    # 判断是否是附件
    def IsAttachment(self, msgMsagess):
        if (msgMsagess.get_content_disposition() == 'attachment'):
            charset = msgMsagess.get_charsets()[0]
            filename = self.myDecoder(msgMsagess.get_filename(), charset)
            self.GetAttachmentData(msgMsagess, filename)
        return None

    def Get_All(self, msgMessage):
        self.IsAttachment(msgMessage)

    # 解析应用附件
    def Get_ApplicationContent(self, msgMessage):
        data = msgMessage.get_payload(i=None, decode=True)

        return data

    # 解析文本类内容
    def Get_TextContent(self, msgMessage):
        data = msgMessage.get_payload(decode=True)
        encording = msgMessage.get_charsets()
        text = (str(data, encoding=encording[0]))
        return text

    # 解析所有类型的数据，目前实现的部分为text、application
    #
    # 此处解析逻辑可能有问题，需要验证调整
    # 判断是附件则走附件流程，否则走非附件流程
    #
    def Get_ContentType(self, msgMessage):
        if (msgMessage == None):
            return ''
        print('```````````````````````````````````````````````````````````')
        print('')
        print('........Content Main Type........')
        content_maintype = msgMessage.get_content_maintype()
        if (content_maintype == 'multipart'):
            print('multipart')
        elif (content_maintype == 'text'):
            print('text')
            self.mBody.append(self.Get_TextContent(msgMessage))

        elif (content_maintype == 'application'):
            print('application')
        elif (content_maintype == 'image'):
            print('image')
        elif (content_maintype == 'audio'):
            print('audio')
        elif (content_maintype == 'video'):
            print('video')
        elif (content_maintype == 'message'):
            print('message')
        else:
            print('multiple')
        self.Get_All(msgMessage)

        return ''

    # 获取发送人
    def GetFrom(self):
        strFrom = self.msg.get("From")
        if strFrom != None:
            listFrom = strFrom.split(" ")
            # name = self.myDecoder(listFrom[0])
            name = listFrom[0]
            email = listFrom[-1]
            email = email[1:-1]
            self.mFrom = {"name": name, "email": email}

    # 获取接收人列表
    def GetTo(self):
        global email
        dictTo = []
        strTo = self.msg.get("To")
        if strTo != None:
            listStrTo = strTo.split(", ")
            for i in range(0, len(listStrTo)):
                to = listStrTo[i].split(" ")
                email = to[-1]
                dictTo.append(email)
        self.mTo = dictTo

    # 获取抄送人列表
    def GetCc(self):
        dictCc = []
        strCc = self.msg.get("CC")
        if strCc != None:
            listStrCc = strCc.split(", ")

            for i in range(0, len(listStrCc) - 1):
                to = listStrCc[i].split(" ")
                name = to[0]
                email = to[1]
                email = email[1:-1]
                dictCc.append({"name": name, "email": email})
        self.mCc = dictCc

    # 获取时间
    def GetTime(self):
        strTime = self.msg.get("DATE")
        self.mDate = strTime

    # 获取标题
    def GetSubject(self):
        strSubject = self.msg.get("SUBJECT")
        # strSubject = strSubject.replace(" ", "")
        # strSubject = strSubject.replace("\n", "|")
        # strSubject = strSubject.replace("\r", "|")
        # strSubject = strSubject.replace("||", "|")
        # dictSubject = strSubject.split("|")

        # subject = ''
        # for i in range(0, len(dictSubject)):
        #     name = self.myDecoder(dictSubject[i])
        #     subject = subject + name
        # self.mSubject = subject
        self.mSubject = strSubject

    # 获取邮件内容和附件内容
    def GetContent(self):
        self.GetFrom()
        self.GetTo()
        self.GetCc()
        self.GetTime()
        self.GetSubject()
        for part in self.msg.walk():  # 循环信件中的每一个mime的数据块
            self.Get_ContentType(part)
        return None

    # 设置message
    def SetMessageByBinary(self, binary):
        self.msg = email.message_from_binary_file(binary)

    # 设置Message
    def SetMessageByText(self, text):
        self.msg = email.message_from_string(text)


myeml = myEml()
myeml.needSaveFile = False  # 是否保存附件到本地
fp = open('data/bb.eml', 'rb')
myeml.SetMessageByBinary(fp)
fp.close()
myeml.GetContent()
print('...........GET FROM..........')
print(myeml.mFrom)
print('')
print('...........GET TO..........')
print(myeml.mTo)
print('')
print('...........GET   DATE..........')
print(myeml.mDate)
print('')
print('...........GET SUBJECT..........')
print(myeml.mSubject)
print('')
print('...........GET CONTENT..........')
print(myeml.mBody)
print('')
print('...........GET FILENAME..........')
print(myeml.mAtta)
