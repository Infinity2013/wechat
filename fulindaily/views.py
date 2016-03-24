import hashlib
import wechatmsg
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

WECHAT_TOKEN = "weixinpublicplatform2016"

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
    if msgType == 'text':
        msg = ""
        if msgDict['Content'] == 'account':
            msg = wechatmsg.textMsg(msgDict, "iqiyi")
        else:
            msg =  wechatmsg.textMsg(msgDict, "nothing")
        logd(msg)
        return msg
