# Secrecy and Secret-Key Capacity

- Secrecy and secret-key capacity are two important concepts in information-theoretic security, which studies the fundamental limits of secure communications over noisy channels or networks.
- Secrecy capacity is the maximum rate at which a sender can transmit a message to a receiver over a noisy channel, such that an eavesdropper who observes the channel output cannot learn any information about the message.
- Secret-key capacity is the maximum rate at which two or more parties can generate a common secret key by exchanging messages over a noisy network, such that an eavesdropper who observes the network traffic cannot learn any information about the key.
- Both secrecy and secret-key capacity depend on the channel or network model, the assumptions about the eavesdropper's knowledge and capabilities, and the secrecy criterion used to measure the information leakage.
- Three common secrecy criteria are:
  - Perfect secrecy: the eavesdropper's uncertainty about the message or the key is the same before and after observing the channel or network output.
  - Strong secrecy: the eavesdropper's information about the message or the key is negligible compared to its length.
  - Weak secrecy: the eavesdropper's information about the message or the key vanishes asymptotically as the length goes to infinity.
- Secrecy and secret-key capacity can be characterized by single-letter expressions or achievable schemes in some special cases, such as when the eavesdropper is absent, reveals itself, or is passive. However, in general, they are difficult to compute or bound, and require multi-letter or random coding techniques.