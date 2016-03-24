import json
import time
import urllib2
import sys

PROP_PATH = '/home/wxl/wechat/fulindaily'
class Secure():
    def __init__(self):
        tmpDict = {}
        with open('%s/secure_common.prop' % PROP_PATH, 'r') as f:
            for line in f.readlines():
                tmp = line.split()
                tmpDict[tmp[0]] = tmp[1]
        self._WECHAT_TOKEN = tmpDict['WECHAT_TOKEN']
        self._APP_ID = tmpDict['APP_ID']
        self._APP_SECRET = tmpDict['APP_SECRET']
        self._TOKEN_URL = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (self._APP_ID, self.APP_SECRET)
        tmpList = []
        with open('%s/secure_token.prop' % PROP_PATH, 'r') as f:
            tmpList = f.readline().split()
        if int(time.time()) - int(tmpList[2]) > int(tmpList[1]) * 0.95:
            jData = urllib2.urlopen(self._TOKEN_URL).read()
            jDict = json.loads(jData)
            with open('%s/secure_token.prop'% PROP_PATH, 'w') as f:
                f.write('%s %s %d' % (jDict['access_token'], jDict['expires_in'], int(time.time())))
            self._ACCESS_TOKEN = jDict['access_token']
            print 'refresh token'
        else:
            self._ACCESS_TOKEN = tmpList[0]
            print 'reuse token'

    @property
    def WECHAT_TOKEN(self):
        return self._WECHAT_TOKEN

    @property
    def APP_ID(self):
        return self._APP_ID

    @property
    def APP_SECRET(self):
        return self._APP_SECRET

    @property
    def ACCESS_TOKEN(self):
        tmpList = []
        with open('%s/secure_token.prop' % PROP_PATH, 'r') as f:
            tmpList = f.readline().split()
        if int(time.time()) - int(tmpList[2]) > int(tmpList[1]) * 0.95:
            jData = urllib2.urlopen(self._TOKEN_URL).read()
            jDict = json.loads(jData)
            with open('%s/secure_token.prop' % PROP_PATH, 'w') as f:
                f.write('%s %s %d' % (jDict['access_token'], jDict['expires_in'], int(time.time())))
            self._ACCESS_TOKEN = jDict['access_token']
            print 'refresh token'
        else:
            self._ACCESS_TOKEN = tmpList[0]
            print 'reuse token'
        return self._ACCESS_TOKEN

secure = Secure()

