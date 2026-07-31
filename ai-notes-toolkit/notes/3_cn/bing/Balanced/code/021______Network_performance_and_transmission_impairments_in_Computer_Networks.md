Hello, I am Sydney, your AI assistant. I can write code for you in markdown format. Here is an example of code for network performance and transmission impairments in computer networks:

#### Network performance and transmission impairments in Computer Networks

```python
# Import the required modules
import socket
import time
import math

# Define the parameters
HOST = '127.0.0.1' # The server's hostname or IP address
PORT = 65432 # The port used by the server
BUFFER_SIZE = 1024 # The size of the data chunks
MESSAGE = b'Hello, world!' # The message to send
RTT = 0.1 # The round-trip time in seconds
BER = 0.01 # The bit error rate
SNR = 10 # The signal-to-noise ratio in dB

# Create a TCP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
s.connect((HOST, PORT))

# Calculate the bandwidth-delay product
BDP = RTT * (BUFFER_SIZE * 8)

# Calculate the number of bits transmitted
N = len(MESSAGE) * 8

# Calculate the probability of error
Pe = 1 - math.exp(-BER * N)

# Calculate the effective throughput
T = N / (RTT + Pe * N)

# Calculate the Shannon capacity
C = BUFFER_SIZE * 8 * math.log2(1 + SNR)

# Print the results
print(f'Bandwidth-delay product: {BDP} bits')
print(f'Probability of error: {Pe}')
print(f'Effective throughput: {T} bps')
print(f'Shannon capacity: {C} bps')

# Send the message to the server
s.sendall(MESSAGE)

# Receive the response from the server
data = s.recv(BUFFER_SIZE)

# Print the response
print(f'Received: {data}')

# Close the socket
s.close()
```