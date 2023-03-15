#### Network performance and transmission impairments in Computer Networks

Network performance refers to the level of quality of service of a telecommunications product as seen by the customer. It should not be seen merely as an attempt to get "more through" the network. Performance can also be modeled and predicted instead of measured; one example of this is using state transition diagrams to model queuing performance or to use a Network Simulator.

Transmission impairments are any factors that negatively affect the quality of the transmitted signal. These impairments can include attenuation, distortion, noise, and interference. Attenuation is the loss of signal strength as it travels through the transmission medium. Distortion is the alteration of the original signal, which can be caused by a variety of factors, including the characteristics of the transmission medium and the presence of other signals. Noise is any unwanted signal that interferes with the transmission of the desired signal. Interference is the presence of other signals that can disrupt the transmission of the desired signal.

Here is an example of a Python code that calculates the network performance based on the transmission impairments:

```python
def network_performance(attenuation, distortion, noise, interference):
    performance = 100 - (attenuation + distortion + noise + interference)
    return performance

attenuation = 10
distortion = 5
noise = 15
interference = 20

performance = network_performance(attenuation, distortion, noise, interference)
print("Network performance:", performance)
```