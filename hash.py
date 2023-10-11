import hashlib


def sha_512(string: str):
    encoded_string = string.encode()
    hashed = hashlib.sha512(encoded_string)
    return str(hashed.hexdigest())
