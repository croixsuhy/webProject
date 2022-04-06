from cryptography.fernet import Fernet as Fer

raw = "Hello, World!"
raw = raw.encode()
key = Fer.generate_key()
f = Fer(key)

encryptedString = f.encrypt(raw)
decryptedString = f.decrypt(encryptedString)

print(encryptedString, decryptedString, key)
