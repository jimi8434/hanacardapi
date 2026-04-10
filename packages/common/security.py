import base64
import hashlib

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def _derive_key(secret: str) -> bytes:
    return hashlib.sha256(secret.encode("utf-8")).digest()


def encrypt_aes_cbc(plaintext: str, secret: str, iv: bytes) -> str:
    cipher = AES.new(_derive_key(secret), AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad(plaintext.encode("utf-8"), AES.block_size))
    return base64.b64encode(encrypted).decode("utf-8")


def decrypt_aes_cbc(ciphertext_b64: str, secret: str, iv: bytes) -> str:
    cipher = AES.new(_derive_key(secret), AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(base64.b64decode(ciphertext_b64)), AES.block_size)
    return decrypted.decode("utf-8")
