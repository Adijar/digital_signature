from Crypto.PublicKey import RSA as rsa
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256 as sha256

## Generating DIGITAL SIGNATURE KEYS
# generated_key = rsa.generate(2048)

# private_k = generated_key.export_key()
# public_k = generated_key.publickey().export_key()

# with open("private_key.pem", "wb") as file:
#  file.write(private_k)
  
# with open("public_key.pem", "wb") as file:
#  file.write(public_k)

## SIGN
## sending message
plaintext = b"I am Adil Ergazin"

## importing private_key
# private_k = rsa.import_key(open("private_key.pem").read())
  
## encrypting the message with SHA256 hash function (creating hash of message to compare in the end)
# encrypted_plaintext = sha256.new(plaintext)

## signing
# signer = pkcs1_15.new(private_k)
# signature = signer.sign(encrypted_plaintext)

# with open("signature.pem", "wb") as file:
#  file.write(signature)

## VERIFY
## importing public key
public_k = rsa.import_key(open("public_key.pem").read())

## importing signature
with open("signature.pem", "rb") as file:
  signature = file.read()

## verifying
encrypted_plaintext2 = sha256.new(plaintext)

try:
  pkcs1_15.new(public_k).verify(encrypted_plaintext2, signature)
  print("The signature is valid. Hashes are same, message is received succesfully!")
except (ValueError, TypeError):
  print("The message has been changed!")
  