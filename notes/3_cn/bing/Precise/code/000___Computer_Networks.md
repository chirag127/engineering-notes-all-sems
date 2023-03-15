# Computer Networks

Here is an example of code that can be used in the context of computer networks:

```python
import socket

def get_local_ip():
    """
    Function to get the local IP address of the machine
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

print(get_local_ip())
```
