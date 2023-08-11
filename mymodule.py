import rsa
def encryption(string,publicKey):
        encrypedData = rsa.encrypt(string.encode(),publicKey)
        return encrypedData

def decryption(encryptedTxt,privateKey):
        decrypedData = rsa.decrypt(encryptedTxt,privateKey).decode()
        return decrypedData
def generateKey():
    publicKey,privateKey = rsa.newkeys(512)
    return publicKey,privateKey
def encryption_file(plainFile,cipherFile,publicKey):
    with open(plainFile,"r") as plain, open(cipherFile,"w") as cipher:
        content = plain.read()
        encrypted_data = encryption(content,publicKey)
        cipher.write(str(encrypted_data))
        return encrypted_data
def decryption_file(string,decodeFile,privateKey):
    decrypted_data = decryption(string,privateKey)
    with open(decodeFile,"w") as file:
        file.write(decrypted_data)
