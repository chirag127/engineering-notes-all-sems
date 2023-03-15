### Connecting to Internet
Here is an example of how to connect to the internet using Python:

```python
import socket

def check_internet():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False

if check_internet():
    print("Connected to the internet")
else:
    print("Not connected to the internet")
```