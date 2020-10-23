"""
Although the idea of the Vigenere Cipher is very basic it took humanity over 300 years to break it. Ultimately, frequency analysis broke it. Develop the class to encrypt and decrypt using the cipher developed by Vigenere.
"""

def populate(plaintext: str, key: str) -> str:
    keystream = "".join([key[i%len(key)] for i in range(len(plaintext))])
    return keystream

def encrypt(plaintext: str, key: str) -> str:
    keystream = populate(plaintext, key)
    plaintext_ord = [ord(p) for p in plaintext]
    keystream_ord = [ord(k) for k in keystream]
    cipher_ord = [p+k-65 if p+k-65<=90 else (p+k-65)%90+65 for p, k in zip(plaintext_ord, keystream_ord)]
    cipher_text = [chr(o) for o in cipher_ord] 
    return "".join(cipher_text)
    return cipher_ord

def decrypt(ciphertext: str, key: str) -> str:
    return plaintext
