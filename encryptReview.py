from cryptography.fernet import Fernet as Fer

key = b'E4ihHNSICFo5cSdlu-yjAvBUomqNVaaPRKcp_MCmfB4='

decryptMsg = b'gAAAAABiO6MLiIFBsg7qq12QIndbG9G4PZyzbBFyyooyj0520cpqNAKG2KlqrqVEdXAYgKXT_0b17-VagsfZDIAEoda8CbyEVQ=='

f = Fer(key)

decryptedMessage = f.decrypt(decryptMsg)

print(decryptedMessage)
