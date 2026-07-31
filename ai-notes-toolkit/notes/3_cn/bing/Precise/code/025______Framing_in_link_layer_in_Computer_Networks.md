#### Framing in link layer in Computer Networks

Framing is the process of encapsulating data into a frame at the link layer of the OSI model. A frame is a unit of data transmission that includes not only the data itself, but also additional information such as the source and destination addresses, error detection and correction information, and control information.

Here is an example of how framing can be implemented in C:

```c
#include <stdio.h>
#include <string.h>

#define MAX_FRAME_SIZE 1024

typedef struct {
    char source[6];
    char destination[6];
    char data[MAX_FRAME_SIZE];
    int data_size;
    char checksum[4];
} frame_t;

void create_frame(frame_t *frame, char *source, char *destination, char *data, int data_size) {
    memcpy(frame->source, source, 6);
    memcpy(frame->destination, destination, 6);
    memcpy(frame->data, data, data_size);
    frame->data_size = data_size;
    // Calculate checksum here
}

void print_frame(frame_t *frame) {
    printf("Source: %s\n", frame->source);
    printf("Destination: %s\n", frame->destination);
    printf("Data: %s\n", frame->data);
    printf("Data size: %d\n", frame->data_size);
    printf("Checksum: %s\n", frame->checksum);
}

int main() {
    frame_t frame;
    create_frame(&frame, "Alice", "Bob", "Hello, Bob!", strlen("Hello, Bob!"));
    print_frame(&frame);
    return 0;
}
```

This code defines a `frame_t` structure that represents a frame, with fields for the source and destination addresses, the data, the data size, and the checksum. The `create_frame` function takes a pointer to a `frame_t` structure, the source and destination addresses, the data, and the data size as arguments, and initializes the frame with the given values. The `print_frame` function takes a pointer to a `frame_t` structure as an argument and prints the contents of the frame.
