#### Link layer switches & bridges in local area network

Link layer switches and bridges are used in local area networks (LANs) to connect multiple devices and facilitate communication between them. These devices operate at the link layer (layer 2) of the OSI model and are responsible for forwarding data frames between devices on the same network.

Here is an example of how a link layer switch can be implemented in a local area network using the C programming language:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_DEVICES 10
#define MAX_FRAME_SIZE 1500

typedef struct {
    char src[6];
    char dst[6];
    char data[MAX_FRAME_SIZE];
} frame_t;

typedef struct {
    char mac[6];
    int port;
} device_t;

device_t devices[MAX_DEVICES];
int device_count = 0;

void add_device(char *mac, int port) {
    if (device_count >= MAX_DEVICES) {
        printf("Error: Maximum number of devices reached\n");
        return;
    }
    memcpy(devices[device_count].mac, mac, 6);
    devices[device_count].port = port;
    device_count++;
}

int get_device_port(char *mac) {
    for (int i = 0; i < device_count; i++) {
        if (memcmp(devices[i].mac, mac, 6) == 0) {
            return devices[i].port;
        }
    }
    return -1;
}

void forward_frame(frame_t *frame) {
    int dst_port = get_device_port(frame->dst);
    if (dst_port == -1) {
        printf("Error: Destination device not found\n");
        return;
    }
    printf("Forwarding frame from port %d to port %d\n", get_device_port(frame->src), dst_port);
}

int main() {
    add_device("\x00\x11\x22\x33\x44\x55", 1);
    add_device("\x66\x77\x88\x99\xaa\xbb", 2);

    frame_t frame;
    memcpy(frame.src, "\x00\x11\x22\x33\x44\x55", 6);
    memcpy(frame.dst, "\x66\x77\x88\x99\xaa\xbb", 6);
    strcpy(frame.data, "Hello, world!");

    forward_frame(&frame);

    return 0;
}
```

This code defines a `frame_t` structure to represent a data frame, and a `device_t` structure to represent a device on the network. The `add_device` function is used to add devices to the network, and the `get_device_port` function is used to find the port number of a device based on its MAC address. The `forward_frame` function is responsible for forwarding a frame from its source to its destination by looking up the destination device's port number and forwarding the frame accordingly.

This is just one example of how link layer switches and bridges can be implemented in a local area network. There are many other ways to implement these devices, and the specific implementation will depend on the requirements of the network and the devices being used.