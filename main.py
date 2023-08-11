import mymodule
publicKey,privateKey = mymodule.generateKey()
plainFile = input("Enter plain text file : ")
cipherFile = input("Enter cipher file : ")
decodeFile = input("Enter decode file : ")
encryptedData = mymodule.encryption_file(plainFile,cipherFile,publicKey)
mymodule.decryption_file(encryptedData,decodeFile,privateKey)
