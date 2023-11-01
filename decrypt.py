#import the libraries needed
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os
import sys


def decrypt_file(file_path, private_key):
    with open(file_path, 'rb') as encrypted_file:
        encrypted_content = encrypted_file.read()

    key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(key)
    decrypted_content = cipher.decrypt(encrypted_content)

    with open(file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_content)

def decrypt_directory(directory, private_key):
    for root, dirs, files in os.walk(directory):
        print(f"Scanning directory: {root}")
        for file in files:
            file_path = os.path.join(root, file)
            print(f"Found encrypted file: {file_path}")

            decrypt_file(file_path, private_key)

# # we will use the command line arguments to get the directory to encrypt
if len(sys.argv) < 2:
    print("Usage: python decrypt.py <directory>")
    sys.exit(1)

directory = sys.argv[1]

# # if the directory does not exist, we will exit the program
if not os.path.exists(directory):
    print("Directory does not exist")
    sys.exit(1)


#reading the private key from the file
with open('privateKey.pem', 'rb') as priv:
    private_key = priv.read()
    
decrypt_directory(directory, private_key)
