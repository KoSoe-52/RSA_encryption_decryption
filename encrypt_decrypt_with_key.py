import rsa
def encryption_file(string,publicKey):
        encrypedData = rsa.encrypt(string.encode(),publicKey)
        return encrypedData

def decryption_file(encryptedTxt,privateKey):
        decrypedData = rsa.decrypt(encryptedTxt,privateKey).decode()
        return decrypedData
def generateKey():
    publicKey,privateKey = rsa.newkeys(512)
    return publicKey,privateKey

public,private = generateKey()
originalData = "I\'m learning python programming language!"
print("Original Data ",originalData)
encrypted_data = encryption_file(originalData,public)
print("Encrypted Data",encrypted_data)
decryption_data = decryption_file(encrypted_data,private)
print("Decrypted Data ",decryption_data)
