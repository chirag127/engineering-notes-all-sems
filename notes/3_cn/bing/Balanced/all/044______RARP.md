#### RARP

- RARP stands for **Reverse Address Resolution Protocol**  .
- It is a protocol that allows a **client computer** to request its **IP address** from a **gateway server** or a **RARP server** on the same **local area network (LAN)**  .
- It works by sending the **MAC address** of the client computer to the RARP server, which then looks up the corresponding IP address in a **table or cache** and sends it back to the client  .
- RARP is useful for **diskless workstations** or **bootstrapping** devices that do not have a permanent IP address or a configuration file  .
- RARP uses the same **packet format** as ARP, but with different **operation codes**. RARP request is 3 and RARP reply is 4  .
- RARP is an **obsolete** protocol that has been replaced by **BOOTP** and **DHCP**, which are more flexible and scalable  .

A possible mnemonic to remember RARP is:

**R**everse **A**ddress **R**esolution **P**rotocol: **R**equest **A**n **R**esponse **P**lease

A possible ASCII diagram to illustrate RARP is:

```
Client (MAC: AA-BB-CC-DD-EE-FF)              RARP Server (IP: 192.168.1.1)
|                                             |
| RARP request: AA-BB-CC-DD-EE-FF -> ?        |
|-------------------------------------------->|
|                                             |
|                                             | Lookup IP address for AA-BB-CC-DD-EE-FF
|                                             | in table or cache
|                                             |
| RARP reply: AA-BB-CC-DD-EE-FF -> 192.168.1.2|
|<--------------------------------------------|
|                                             |
```