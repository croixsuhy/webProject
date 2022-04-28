from cryptography.fernet import Fernet as Fer
# import os

# TEMP
key = b'E4ihHNSICFo5cSdlu-yjAvBUomqNVaaPRKcp_MCmfB4='
enList = [b'gAAAAABiO6MLiIFBsg7qq12QIndbG9G4PZyzbBFyyooyj0520cpqNAKG2KlqrqVEdXAYgKXT_0b17-VagsfZDIAEoda8CbyEVQ==',
          b'gAAAAABiO6MLpdE25sdlvvODUM3gHmeobzjlPX-nM5MsjXl6uV_GbuLJLbB3Ig2jKDLV4Uu1wopV8lvFSk-Ur3ZK-SgDwhNJkA==',
          b'gAAAAABiO6MLf_U532KwiZiUOvXoMdhcGN6Qy5omv5mZQBwcvT-kL8dXrVR6vctMwYBikvCTcT81Cwk4BVz6XFRwDytQUYz96Ewa50nwTo2FhuJm9j9hfQQ=',
          b'gAAAAABiO6MLYwZN9XGrF2rQmNf36yPhbdk13Dm8U5A0JOu8amZZT0u2nlQGHbeSa8IJQAHtCPY4Yv3V4RlNptlJLsDsZsOuJQ==',
          b'gAAAAABiO6MLNXBURRrRzxQ3HNV7e0Qzta2WPHbUVN7IDn8mUNFSPXMLOtNhzoQUUoKktuwgRg2oYPCGT1i9wK3b_sHibZcjng==']
decryptedList = []

# for eTxt in enList:
#     f = Fer(key)
#     decryptedList.append(f.decrypt(eTxt))
#
# print(decryptedList)

f = Fer(key)
print(f.decrypt(b'gAAAAABiO6MLiIFBsg7qq12QIndbG9G4PZyzbBFyyooyj0520cpqNAKG2KlqrqVEdXAYgKXT_0b17-VagsfZDIAEoda8CbyEVQ=='))
