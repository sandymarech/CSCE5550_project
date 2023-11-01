from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os
import sys

with open('privateKey.pem', 'rb') as priv:
    private_key = priv.read()

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

if len(sys.argv) < 2:
    print("Usage: python decrypt.py <directory>")
    sys.exit(1)

directory = sys.argv[1]

if not os.path.exists(directory):
    print("Directory does not exist")
    sys.exit(1)



decrypt_directory(directory, private_key)