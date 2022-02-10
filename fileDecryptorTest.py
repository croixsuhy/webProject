from cryptography.fernet import Fernet as Fer
# import os

# TEMP
key = b"mQW1kFEDSTIMPe9clRLG5WVhFZJdLL2zKRRXFRZj090="
enList = [
        b"gAAAAABh-xqXEzxzdVfK_4aslP9IdFK5rkUDYHhV9cecbnoS_9GDdFUfMCZIlq11G8d-N3Els3pGu584HUp4BUIGr9kVXDtWHA==",
        b"gAAAAABh-xqXPQKeLJvyhut4UkBhjx1wEVZFFMEPmXtG8TXFCF4dLueKxjh4RDJEPOaQd4yNh8VZdeU5OtyYo_ciRO2p8YNtdA==",
        b"gAAAAABh-xqXPPvi8a6P7ccZT9Wu9V5ZWiLwFeA8xZgovhgoxeLaQXEVTaAnIBk76MrFmPvn9NYnmHzAwhr80ug1PDAXkr7Xzd1H_sjVkNSHMRpGXekKgpQ=",
        b"gAAAAABh-xqXml-NgXbE1IJ577JXbPjl74xFWGjuDb7w7fdsxgXhEvMMih1VzR3TnFLm_hqC5atjkLuF-2UlwYyLefw_KnWyvQ==",
        b"gAAAAABh-xqXa_71UGlV2yjemzXJn_RjDpFRCBB8J9fdwAqRTrb6Zje7ydI6C2vIBBGQaymYYunBRtHHDbphEx_PmjDmekFklw=="
        ]

decryptedList = []

for eTxt in enList:
    f = Fer(key)
    decryptedList.append(f.decrypt(eTxt))

print(decryptedList)
