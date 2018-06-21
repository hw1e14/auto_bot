#!/usr/bin/python
# -*- coding: utf-8 -*-

from itchat.content import *
import requests
import json
import itchat

itchat.auto_login(hotReload=True)


def tuling(info):
    appkey = "*******"
    url = "http://www.tuling123.com/openapi/api?key=%s&info=%s&userid=%s" % (appkey, info, "wechat-robot85")
    req = requests.get(url)
    content = req.text
    data = json.loads(content)
    answer = data['text']
    return answer


def group_id(name):
    df = itchat.search_chatrooms(name=name)
    return df[0]['UserName']


# @itchat.msg_register([TEXT,MAP,CARD,NOTE,SHARING])
# def text_reply(msg):
#     itchat.send('%s' % tuling(msg['Text']),msg['FromUserName'])
#
# @itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
# def download_files(msg):
#     msg['Text'](msg['FileName'])
#     return '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])
#
# @itchat.msg_register(TEXT, isGroupChat=True)
# def group_text_reply(msg):
#     item = group_id(u'英语朗读群')
#     # if msg['ToUserName'] == item:
#     if msg['isAt']:
#         itchat.send(u'%s' % tuling(msg['Text']), item)

global is_auto_reply
is_auto_reply = True

commands = {
    "--switch": "auto reply switched"
}


@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    # if (msg['ToUserName'] == u"filehelper".encode('utf-8') & msg['Text'].encode('utf8') == "switch"):
    if (msg['ToUserName'] == itchat.search_friends()['UserName'] & msg['Text'].encode('utf8') == u"switch"):
        global is_auto_reply
        is_auto_reply = switcher(is_auto_reply)
        # itchat.send('%s' % "auto reply switched", itchat.search_friends())
        # itchat.send('%s' % "auto reply switched", "filehelper")
    else:
        itchat.send('%s' % tuling(msg['Text']), msg['FromUserName'])


if is_auto_reply:
    # @itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
    # def text_reply(msg):
    #     itchat.send('%s' % tuling(msg['Text']), msg['FromUserName'])

    @itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
    def download_files(msg):
        msg['Text'](msg['FileName'])
        return '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])


    @itchat.msg_register(TEXT, isGroupChat=True)
    def group_text_reply(msg):
        item = group_id(u'英语朗读群')
        # if msg['ToUserName'] == item:
        if msg['isAt']:
            itchat.send(u'%s' % tuling(msg['Text']), item)


def switcher(var):
    if var:
        return False
    else:
        return True


itchat.run()
