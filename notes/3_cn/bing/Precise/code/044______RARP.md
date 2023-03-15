#### RARP
RARP (Reverse Address Resolution Protocol) is a protocol used to resolve an IP address from a given hardware address (such as an Ethernet address). Here is an example of RARP code in C:

```c
#include <stdio.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <net/if_arp.h>
#include <string.h>

int main() {
    int s;
    struct arpreq arpreq;
    struct sockaddr_in *sin;
    unsigned char *eap;

    s = socket(AF_INET, SOCK_DGRAM, 0);
    if (s == -1) {
        perror("socket");
        return 1;
    }

    memset(&arpreq, 0, sizeof(arpreq));
    sin = (struct sockaddr_in *) &arpreq.arp_pa;
    sin->sin_family = AF_INET;
    sin->sin_addr.s_addr = inet_addr("192.168.1.1");
    strcpy(arpreq.arp_dev, "eth0");

    if (ioctl(s, SIOCGARP, &arpreq) == -1) {
        perror("ioctl");
        return 1;
    }

    eap = (unsigned char *) &arpreq.arp_ha.sa_data[0];
    printf("HW address is %02X:%02X:%02X:%02X:%02X:%02X\n",
           eap[0], eap[1], eap[2], eap[3], eap[4], eap[5]);

    return 0;
}
```
This code creates a socket and uses the `ioctl` function to send a `SIOCGARP` request to the kernel to retrieve the hardware address associated with the given IP address (`192.168.1.1` in this example). The hardware address is then printed in the standard format.