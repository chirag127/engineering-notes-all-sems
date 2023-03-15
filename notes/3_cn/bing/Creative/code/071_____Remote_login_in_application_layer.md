Hello, I am Sydney, your AI assistant. I can help you with various tasks and topics. You have asked me to write code for remote login in application layer. Here is one possible solution:

### Remote login in application layer

Remote login is a process of accessing a computer or a network from a different location. One of the protocols that supports remote login in application layer is Telnet. Telnet allows a user to establish a connection with a remote host and execute commands on it. Here is an example of how to use Telnet in Python:

```python
# Import the telnetlib module
import telnetlib

# Define the host and port to connect to
host = "example.com"
port = 23

# Create a Telnet object
tn = telnetlib.Telnet(host, port)

# Write the username and password to log in
tn.write(b"user\n")
tn.write(b"password\n")

# Write the command to execute on the remote host
tn.write(b"ls\n")

# Read the output from the remote host
output = tn.read_all()

# Print the output
print(output)

# Close the connection
tn.close()
```