"""
Although the idea of the Vigenere Cipher is very basic it took humanity over 300 years to break it. Ultimately, frequency analysis broke it. Develop the class to encrypt and decrypt using the cipher developed by Vigenere.
"""

def populate(plaintext: str, key: str) -> str:
    keystream = key
    return keystream

def encrypt(plaintext: str, key: str) -> str:
    keystream = populate(plaintext, key)
    plaintext_ord = [ord(p) for p in plaintext]
    keystream_ord = [ord(k) for k in keystream]
    ciphertext = [chr(p-65+k) for p, k in zip(plaintext_ord, keystream_ord)]
    return "".join(ciphertext)

def decrypt(ciphertext: str, key: str) -> str:
    return plaintext
