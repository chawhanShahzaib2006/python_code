import rsa

publicKey, privateKey = rsa.newkeys(300)

message = str(input("Enter a message only consisting of words"))

enkMessage = rsa.encrypt(message.encode(), publicKey)

print("orginal message is :", message)
print("encrypted message is : ", enkMessage)
