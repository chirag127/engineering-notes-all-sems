## Experiment 3 - Write a code simulating ARP /RARP protocols

ARP (Address Resolution Protocol) and RARP (Reverse Address Resolution Protocol) are two networking protocols that are used to resolve the IP address and the MAC address of a device in a local area network (LAN).

- ARP is used to find the MAC address of a device that has a known IP address. ARP works by broadcasting an ARP request packet to all devices on the LAN, asking for the MAC address of the device that has the IP address specified in the request. The device that has the matching IP address replies with an ARP reply packet, containing its MAC address. The sender then updates its ARP cache with the IP-MAC mapping and uses it for future communication.
- RARP is used to find the IP address of a device that has a known MAC address. RARP works by sending a RARP request packet to a RARP server on the LAN, containing the MAC address of the device. The RARP server looks up its RARP table and finds the IP address that corresponds to the MAC address. The RARP server then sends a RARP reply packet, containing the IP address of the device. The device then configures its IP address and uses it for future communication.

The following is a pseudocode for simulating the ARP and RARP protocols:

```python
# Define a class for a device on the LAN
class Device:
  # Initialize the device with its MAC address and IP address
  def __init__(self, mac, ip):
    self.mac = mac
    self.ip = ip
    self.arp_cache = {} # A dictionary to store the IP-MAC mappings

  # Define a method to send an ARP request
  def send_arp_request(self, target_ip):
    # Create an ARP request packet with the sender's MAC and IP address and the target IP address
    arp_request = {
      "sender_mac": self.mac,
      "sender_ip": self.ip,
      "target_mac": "FF:FF:FF:FF:FF:FF", # Broadcast MAC address
      "target_ip": target_ip
    }
    # Broadcast the ARP request packet to all devices on the LAN
    broadcast(arp_request)

  # Define a method to receive an ARP request
  def receive_arp_request(self, arp_request):
    # Check if the target IP address matches the device's IP address
    if arp_request["target_ip"] == self.ip:
      # Create an ARP reply packet with the sender's MAC and IP address and the target MAC and IP address
      arp_reply = {
        "sender_mac": self.mac,
        "sender_ip": self.ip,
        "target_mac": arp_request["sender_mac"],
        "target_ip": arp_request["sender_ip"]
      }
      # Send the ARP reply packet to the sender
      send(arp_reply, arp_request["sender_mac"])

  # Define a method to receive an ARP reply
  def receive_arp_reply(self, arp_reply):
    # Check if the target IP address matches the device's IP address
    if arp_reply["target_ip"] == self.ip:
      # Update the ARP cache with the sender's IP and MAC address
      self.arp_cache[arp_reply["sender_ip"]] = arp_reply["sender_mac"]

  # Define a method to send a RARP request
  def send_rarp_request(self):
    # Create a RARP request packet with the sender's MAC address
    rarp_request = {
      "sender_mac": self.mac,
      "sender_ip": "0.0.0.0", # Unspecified IP address
      "target_mac": "FF:FF:FF:FF:FF:FF", # Broadcast MAC address
      "target_ip": "0.0.0.0" # Unspecified IP address
    }
    # Broadcast the RARP request packet to all devices on the LAN
    broadcast(rarp_request)

  # Define a method to receive a RARP request
  def receive_rarp_request(self, rarp_request):
    # Check if the sender MAC address matches the RARP server's MAC address
    if rarp_request["sender_mac"] == self.mac:
      # Look up the RARP table and find the IP address that corresponds to the sender MAC address
      sender_ip = rarp_table[rarp_request["sender_mac"]]
      # Create a RARP reply packet with the sender's MAC and IP address and the target MAC and IP address
      rarp_reply = {
        "sender_mac": self.mac,
        "sender_ip