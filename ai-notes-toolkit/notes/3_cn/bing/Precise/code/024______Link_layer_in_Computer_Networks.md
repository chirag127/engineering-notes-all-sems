#### Link layer in Computer Networks

The link layer is the lowest layer in the OSI model of computer networking. It is responsible for the transmission of data between two directly connected nodes. This layer is responsible for the physical addressing of the data, error detection and correction, and flow control.

Here is an example of a simple link layer protocol written in C:

```c
#include <stdio.h>
#include <string.h>

#define MAX_PACKET_SIZE 1024

typedef struct {
    char dest[6];
    char src[6];
    unsigned short type;
    char data[MAX_PACKET_SIZE];
    unsigned int crc;
} packet_t;

void send_packet(packet_t *packet) {
    // implementation of sending packet over the physical link
}

void receive_packet(packet_t *packet) {
    // implementation of receiving packet from the physical link
}

int main() {
    packet_t packet;
    strcpy(packet.dest, "00:11:22:33:44:55");
    strcpy(packet.src, "AA:BB:CC:DD:EE:FF");
    packet.type = 0x0800; // IPv4
    strcpy(packet.data, "Hello, World!");
    packet.crc = 0; // calculate CRC

    send_packet(&packet);

    return 0;
}
```
