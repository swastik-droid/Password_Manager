# import base64
from base64 import b64encode
from base64 import b64decode
# import hashlib
from hashlib import sha256
from Crypto.Random import new
from Crypto.Cipher import AES


class AESCipher(object):

    def __init__(self, key):
        self.bs = AES.block_size
        self.key = sha256(key.encode()).digest()
        # print("key: ",self.key)

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        # print(str(base64.b64encode(iv + cipher.encrypt(raw.encode()))))
        # return base64.b64encode(iv + cipher.encrypt(raw.encode()))
        return str(b64encode(iv + cipher.encrypt(raw.encode())))

    def decrypt(self, enc):
        enc = bytes((enc[2:-1]).encode())
        # print(enc)
        enc = b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):

        return s[:-ord(s[len(s) - 1:])]

