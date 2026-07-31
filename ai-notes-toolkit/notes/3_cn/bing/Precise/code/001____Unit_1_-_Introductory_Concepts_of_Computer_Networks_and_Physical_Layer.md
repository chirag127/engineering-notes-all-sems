## Unit 1 - Introductory Concepts of Computer Networks and Physical Layer

```python
# A computer network is a group of interconnected devices that can communicate with each other and share resources.
# The physical layer is the first layer of the OSI model and is responsible for the transmission of data over a physical medium.

# Example of a simple computer network:
devices = ['computer1', 'computer2', 'printer', 'router']

connections = {
    'computer1': ['router'],
    'computer2': ['router'],
    'printer': ['router'],
    'router': ['computer1', 'computer2', 'printer']
}

def send_data(sender, receiver, data):
    if receiver in connections[sender]:
        print(f"{sender} sent data to {receiver}: {data}")
    else:
        print(f"{sender} cannot send data to {receiver}")

send_data('computer1', 'printer', 'print this document')
```