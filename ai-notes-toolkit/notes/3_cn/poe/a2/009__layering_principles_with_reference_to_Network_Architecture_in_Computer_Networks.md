 Here is the content in markdown format with formal tone and without emojis or external links:

#### Layering principles with reference to Network Architecture in Computer Networks:

1. Layered architecture: The network architecture is divided into layers, each layer performing a distinct function. Information passes from one layer to the next, starting at the application layer in one host and proceeding down to the physical layer, across the transmission medium to the next host and back up the layer hierarchy.
2. Encapsulation: As information passes down through the layers, each layer prepends its own header to the data received from the upper layer. This is known as encapsulation. The headers are stripped off as the information passes up through the layers. This allows the layers to be oblivious of the internal structure of information used by the neighboring layers.
3. Well defined interfaces: Between each pair of adjacent layers there is an interface that defines which services the lower layer offers to the upper layer. This allows layers to operate independently as long as they adhere to the interface specifications.
4. Information hiding: By using encapsulation and well-defined interfaces, each layer hides its internal operation and data structures from the layers above and below. This information hiding principle simplifies system design and allows changes to be made in one layer without affecting the other layers.

The above points highlight the key layering principles followed in the network architecture to facilitate modular design, simplified operation and accommodate changes. The layered approach enables diverse technologies and protocols to be implemented at each layer to meet the required functions.