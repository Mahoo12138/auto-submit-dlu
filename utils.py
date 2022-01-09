import json
from base64 import b64encode
from Crypto.Cipher import AES, DES
from Crypto.Util.Padding import pad
from Crypto.Hash import MD5
from urllib.parse import quote


### 用于加密生成 Cpdaily-Extension，传入表单以及个人配置数据
def extensionEncrypt(data):
    key = b"b3L26XNL"
    iv = bytes([1, 2, 3, 4, 5, 6, 7, 8])
    data = bytes(json.dumps(data), encoding='utf-8')
    print(data)
    cipher = DES.new(key, DES.MODE_CBC, iv)
    secret_bytes = cipher.encrypt(pad(data, DES.block_size))
    encrypted = b64encode(secret_bytes).decode('utf-8')
    return encrypted


def formBodyEncrypt(data):
    key = b'ytUQ7l2ZZu8mLvJZ'
    iv = bytes([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7])
    data = bytes(json.dumps(data), encoding='utf-8')
    cipher = AES.new(key, AES.MODE_CBC, iv)
    secret_bytes = cipher.encrypt(pad(data, AES.block_size))
    encrypted = b64encode(secret_bytes).decode('utf-8')
    return encrypted


def getSignHash(str):
    jstr = json.dumps(str)
    temp = bytes(quote(jstr) + '=&ytUQ7l2ZZu8mLvJZ', encoding='utf-8')
    h = MD5.new(data=temp)
    return h.hexdigest()

