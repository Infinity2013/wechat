import hashlib

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

WECHAT_TOKEN = "weixinpublicplatform2016"


@csrf_exempt
def index(request):
    return HttpResponse('Hellow World')
    if request.method == 'GET':
        response = HttpResponse(checkSignature(request))
        return response
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
