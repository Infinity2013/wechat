import hashlib

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import wechatmsg
WECHAT_TOKEN = "weixinpublicplatform2016"
isVacation = False

def logd(msg):
    with open("/home/wxl/wechat/logs", "a+") as f:
        f.write(msg)
        f.write('\n')


@csrf_exempt
def index(request):
    logd(request.method)
    if request.method == 'GET':
        response = HttpResponse(checkSignature(request))
        return response
    elif request.method == 'POST':
        return HttpResponse(handleMsg(request.body))
    else:
        return HttpResponse('Hello World')


def checkSignature(request):
    signature = request.GET.get('signature', None)
    timestamp = request.GET.get('timestamp', None)
    nonce = request.GET.get('nonce', None)
    echostr = request.GET.get('echostr', None)
    token = WECHAT_TOKEN
    tmplist = [token, timestamp, nonce]
    tmplist.sort()
    tmpstr = "%s%s%s" % tuple(tmplist)
    tmpstr = hashlib.sha1(tmpstr).hexdigest()
    if tmpstr == signature:
        return echostr
    else:
        return None


def handleMsg(postCont):
    logd(str(postCont))
    msgDict = wechatmsg.parseMsg(postCont)
    msgType = msgDict['MsgType']
    msg = ""
    if msgType == 'text':
        msg = handleTextMsg(msgDict)
    elif msgType == 'event':
        msg = handleEventMsg(msgDict)
    return msg


def handleTextMsg(msgDict):
    global isVacation
    cont = msgDict['Content']
    if cont == '0':
        return wechatmsg.textMsg(msgDict, help())
    if cont == '1':
        return wechatmsg.textMsg(msgDict, account())
    if cont == '2':
        return wechatmsg.textMsg(msgDict, currentShuttle())
    if cont == 'vacation':
        isVacation = True
        return wechatmsg.textMsg(msgDict, "It's on vacation")
    if cont == 'over':
        isVacation = False
        return wechatmsg.textMsg(msgDict, "Vacation is over")
    else:
        return wechatmsg.textMsg(msgDict, "Error: Invalid")


def help():
    msg = u'1. 帐号信息\n2. 最近的交大校车\n0.显示此帮助'
    return msg


def account():
    with open('account.prop', 'r') as f:
        return "".join(f.readlines())


def currentShuttle():
    if isVacation:
        return "on vacation"
    else:
        return "vacation over"


def handleEventMsg(msgDict):
    pass


def handleImageMsg(msgDict):
    pass


def handleVoiceMsg(msgDict):
    pass


def handleVideoMsg(msgDict):
    pass


def handleShortvideoMsg(msgDict):
    pass


def handleLocationMsg(msgDict):
    pass


def handleLinkMsg(msgDict):
    pass
