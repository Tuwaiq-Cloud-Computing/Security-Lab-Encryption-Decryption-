import rsa

publicKey, privateKey = rsa.newkeys(555)


message = input("Enter Message for Encrypt: ")


EncMessage = rsa.encrypt(message.encode(),publicKey)
						
print("Encrypted Message:\n", EncMessage)

decMessage = rsa.decrypt(EncMessage, privateKey).decode()

print("Decrypted Message:\n", decMessage)


