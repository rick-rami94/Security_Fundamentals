# Importing the RSA Library.
import rsa
# creating a public key and a private key. 
(pub_key, priv_key) = rsa.newkeys(1024)
# Creating a variable with my message in bits.
message = b'mytopsecretkey'
#Encrypting the message with the public key and printing to terminal. 
crypto = rsa.encrypt(message,pub_key)
print(crypto)
# Decrypting message and printing to terminal. 
decrypt = rsa.decrypt(crypto,priv_key)
print(decrypt.decode())