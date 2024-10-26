# obfuscator 

## Table of Contents
- [General Information](#general-information)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Usage](#usage)

### General Information

This project demonstrates a reverse shell that uses polymorphic encryption to change its signature with each execution. The reverse shell connects to a listener on a specified port and allows command execution on the host machine.

### Prerequisites

- **Python 3.10+**: Ensure Python is installed on your system.
- **Ncat or Netcat**: Install to listen on a specified port.
- **Virtual Machine**: It is recommended to test the program in a Windows virtual machine for safety.

## Setup

1. **Clone the Repository**:
    ```bash
    git clone https://01.kood.tech/git/Ragnar/obfuscator
    ```

2. **Setup the Environment**:
    - Ensure that Python is installed and available in the terminal.
    - Clone or download the program files to your virtual machine.

3. **Run the Listener**
    Open a terminal and start the Ncat listener:
      ```bash
      ncat -lvnp 4444
      ```

4. **Run the Program**:
    - Open the terminal in the project directory.
    - Execute the Python script:
      ```bash
      python obfuscator.py 
      ```

## Usage

After running the Python script, the reverse shell will attempt to connect to the Ncat listener on port 4444. You can type commands into the Ncat window to be executed on the host machine.

Example Commands:

    dir - List the contents of the current directory.
    whoami - Display the current user.
    ipconfig - Show network configuration.

To close the reverse shell session, type exit in the Ncat window.