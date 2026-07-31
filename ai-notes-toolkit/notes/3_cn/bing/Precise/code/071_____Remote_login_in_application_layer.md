### Remote login in application layer

One way to implement remote login in the application layer is by using the Telnet protocol. Here is an example of how to use Telnet in Python to log in to a remote server:

```python
import telnetlib

HOST = "your_remote_host"
user = "your_username"
password = "your_password"

tn = telnetlib.Telnet(HOST)

tn.read_until(b"login: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"ls\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
tn.close()
```

This code establishes a Telnet connection to the remote host, logs in with the provided username and password, executes the `ls` command to list the contents of the current directory, and then exits the connection. The output is printed to the console.