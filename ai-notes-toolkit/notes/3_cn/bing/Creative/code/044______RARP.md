#### RARP

RARP stands for Reverse Address Resolution Protocol, which is a protocol that allows a device to obtain its IP address from a server that has a table mapping the device's MAC address to its IP address . RARP is used by devices that do not have a permanent IP address, such as diskless workstations.

RARP operates on the network access layer of the TCP/IP protocol stack, and uses the same packet format as ARP. RARP packets have an operation code field that indicates the type of RARP message, such as request or reply. A RARP request contains the MAC address of the sender and an empty IP address field, and is broadcast to all devices on the same LAN. A RARP reply contains the MAC address and the IP address of the sender, and is sent to the device that made the request.

A possible code for RARP in C is:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <net/if.h>
#include <net/if_arp.h>
#include <arpa/inet.h>
#include <unistd.h>

#define RARP_REQUEST 3 // RARP operation code for request
#define RARP_REPLY 4 // RARP operation code for reply
#define ETH_P_RARP 0x8035 // Ethernet protocol type for RARP

// Structure for an Ethernet header
struct ethhdr {
    unsigned char h_dest[6]; // Destination MAC address
    unsigned char h_source[6]; // Source MAC address
    unsigned short h_proto; // Protocol type
};

// Structure for an ARP/RARP header
struct arphdr {
    unsigned short ar_hrd; // Hardware type
    unsigned short ar_pro; // Protocol type
    unsigned char ar_hln; // Hardware address length
    unsigned char ar_pln; // Protocol address length
    unsigned short ar_op; // Operation code
    unsigned char ar_sha[6]; // Sender hardware address
    unsigned char ar_sip[4]; // Sender protocol address
    unsigned char ar_tha[6]; // Target hardware address
    unsigned char ar_tip[4]; // Target protocol address
};

// Function to create a RARP request packet
void create_rarp_request(unsigned char *packet, unsigned char *mac) {
    struct ethhdr *eth = (struct ethhdr *)packet;
    struct arphdr *arp = (struct arphdr *)(packet + sizeof(struct ethhdr));

    // Fill the Ethernet header
    memset(eth->h_dest, 0xff, 6); // Broadcast destination MAC address
    memcpy(eth->h_source, mac, 6); // Source MAC address
    eth->h_proto = htons(ETH_P_RARP); // Protocol type

    // Fill the RARP header
    arp->ar_hrd = htons(ARPHRD_ETHER); // Hardware type
    arp->ar_pro = htons(ETH_P_IP); // Protocol type
    arp->ar_hln = 6; // Hardware address length
    arp->ar_pln = 4; // Protocol address length
    arp->ar_op = htons(RARP_REQUEST); // Operation code
    memcpy(arp->ar_sha, mac, 6); // Sender hardware address
    memset(arp->ar_sip, 0, 4); // Sender protocol address
    memset(arp->ar_tha, 0, 6); // Target hardware address
    memset(arp->ar_tip, 0, 4); // Target protocol address
}

// Function to parse a RARP reply packet
void parse_rarp_reply(unsigned char *packet, unsigned char *mac, unsigned char *ip) {
    struct ethhdr *eth = (struct ethhdr *)packet;
    struct arphdr *arp = (struct arphdr *)(packet + sizeof(struct ethhdr));

    // Check the Ethernet header
    if (ntohs(eth->h_proto) != ETH_P_RARP) {
        printf("Not a RARP packet\n");
        return;
    }

    // Check the RARP header
    if (ntohs(arp->ar_op) != RARP_REPLY) {
        printf("Not a RARP reply\n");
        return;
    }
    if (memcmp(arp->ar_tha, mac, 6) != 0) {
        printf("Not for me\n");
        return

```
