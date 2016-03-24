import time


class Secure():
    def __init__(self):
        tmpDict = {}
        with open('secure_common.prop', 'r') as f:
            for line in f.readlines():
                tmp = line.split()
                tmpDict[tmp[0]] = tmp[1]
        self._WECHAT_TOKEN = tmpDict['WECHAT_TOKEN']
        self._APP_ID = tmpDict['APP_ID']
        self._APP_SECRET = tmpDict['APP_SECRET']

        tmpList = []
        with open('secure_token.prop', 'r') as f:
            tmpList = f.readline.split()
        if int(time.time()) - int(tmpList[1]) > int(tmpList[2]) * 0.95:
            self._LAST_TOKEN_TS = int(time.time())

        else:
            self._ACCESS_TOKEN = tmpList[0]
            self._LAST_TOKEN_TS = int(tmpList[1])

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
        pass

secure = Secure()






