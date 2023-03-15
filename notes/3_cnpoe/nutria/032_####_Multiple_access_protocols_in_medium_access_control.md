
#### Multiple Access Protocols in Medium Access Control

* **Carrier Sense Multiple Access (CSMA):** This protocol is based on the principle of "listen before you talk." All nodes in the network listen to the channel before transmitting. If the channel is busy, the node will wait until the channel is free before transmitting. 

* **Carrier Sense Multiple Access with Collision Detection (CSMA/CD):** This protocol is an extension of CSMA. In addition to listening before transmitting, nodes also detect collisions. If a collision is detected, the nodes will stop transmitting and wait for a random amount of time before attempting to transmit again.

* **Token Passing:** This protocol requires the use of a "token" that is passed from one node to another. Each node is only allowed to transmit when it has the token. This protocol is used in networks with a large number of nodes, as the token prevents collisions by ensuring that only one node is transmitting at a time.

* **Polling:** This protocol requires the use of a central controller, which polls each node in the network in a predetermined order. The controller will wait for a response from each node before moving on to the next node. This protocol is used in networks with a small number of nodes, as it eliminates the need for a token.

* **Mnemonics:**
  * CSMA: "Listen Before You Talk"
  * CSMA/CD: "Listen Before You Talk, and Detect Collisions"
  * Token Passing: "Pass the Token"
  * Polling: "Let the Controller Ask"