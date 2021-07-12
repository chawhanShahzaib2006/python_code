from cryptography.fernet import Fernet

message = "Hi there!"

randomKey = Fernet.generate_key

fernet = Fernet(randomKey)

EncMessage = fernet.encrypt(message.encode())

print("Original message inputted :", message)
print("Message inputed encrypted :", EncMessage)
