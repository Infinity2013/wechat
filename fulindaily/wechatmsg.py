import time
import xml.etree.ElementTree as ET

def textMsg(attrDict, content):
    pattern = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[%s]]></MsgType><Content><![CDATA[%s]]></Content></xml>"
    msg = pattern % (attrDict['FromUserName'],attrDict['ToUserName'],
                     str(int(time.time())), 'text',
                     content)
    return msg

def parseMsg(msg):
    msgDict = {}
    elementTree = ET.fromstring(msg)
    for child in elementTree:
        msgDict[child.tag] = child.text
    return msgDict
        
    
