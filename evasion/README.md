# Evasion

## Table of Contents
- [General Information](#general-information)
- [Setup](#setup)
- [Usage](#usage)

### General Information

This project demonstrates techniques for evading antivirus detection by encrypting a target binary, modifying its size, and delaying its execution. The program runs in a Windows environment using Python and can work with any executable file, such as `calc.exe`. The encryption process uses AES encryption and delays execution by 101 seconds before decrypting and running the file.

## Setup

**Clone the Repository**:
    ```bash
    git clone https://01.kood.tech/git/Ragnar/evasion
    ```

### Prerequisites

- **Python 3.10+**: Ensure Python is installed on your system.
- **pycryptodome Module**: Install the required module using pip:
    ```bash
    pip install pycryptodome
    ```
- **Virtual Machine**: It is recommended to test the program in a Windows virtual machine for safety.

## Usage

1. **Setup the Environment**:
    - Ensure that Python is installed and available in the terminal.
    - Clone or download the program files to your virtual machine.
    - Ensure the file path in the code points to `calc.exe` or another executable you wish to encrypt.

2. **Run the Program**:
    - Open the terminal in the project directory.
    - Execute the Python script:
      ```bash
      python evasion.py <path_to_program>
      ```

3. **Program Output**:
    - The program will:
      - Encrypt the specified executable file.
      - Increase the size of the encrypted file by 101 MB.
      - Wait for 101 seconds before decrypting.
      - Execute the decrypted file (e.g., `calc.exe` will launch).

4. **Files Produced**:
    - **`encrypted_file.exe`**: The encrypted version of the specified executable.
    - **`decrypted_file.exe`**: The decrypted version that will be executed after the delay.