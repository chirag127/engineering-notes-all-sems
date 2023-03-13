A Convolutional Neural Network (CNN) or ConvNet is a type of deep neural network that specializes in processing data that has a grid-like topology, such as an image. A ConvNet consists of multiple layers, including Convolutional layers, Pooling layers, and Fully Connected layers. Each layer performs a specific function on the input data and passes the output to the next layer. The following diagram illustrates the basic architecture of a ConvNet using ASCII art:

```
Input Image
+------------------------+
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
+------------------------+

Convolutional Layer
+------------------------+    +------------------------+
|                        |    |                        |
|                        |    |                        |
|                        |    |                        |
|                        |    |                        |
|                        |    |                        |
|                        |    |                        |
|                        |    |                        |
|                        |    |                        |
+------------------------+    +------------------------+
|                        |    |                        |
|                        |    |                        |
|                        |    |                        |
|                        |    |                        |
|                        |    |                        |
|                        |    |                        |
|                        |    |                        |
|                        |    |                        |
+------------------------+    +------------------------+
|                        |    |                        |
|                        |    |                        |
|                        |    |                        |
|                        |    |                        |
|                        |    |                        |
|                        |    |                        |
|                        |    |                        |
|                        |    |                        |
+------------------------+    +------------------------+

Pooling Layer
+------------------------+    +------------------------+
|                        |    |                        |
|                        |    |                        |
|                        |    |                        |
|                        |    |                        |
+------------------------+    +------------------------+
|                        |    |                        |
|                        |    |                        |
|                        |    |                        |
|                        |    |                        |
+------------------------+    +------------------------+
|                        |    |                        |
|                        |    |                        |
|                        |    |                        |
|                        |    |                        |
+------------------------+    +------------------------+

Fully Connected Layer
+------------------------+
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
+------------------------+
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
+------------------------+
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
+------------------------+

Output Layer
+------------------------+
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
+------------------------+
```

A ConvNet works by applying a series of filters to the input image, which extract features such as edges, shapes, colors, etc. The filters are learned during the training process, and they become more complex and abstract as the network goes deeper. The Convolutional layer is followed by a Pooling layer, which reduces the spatial dimensions of the feature maps and makes the network more efficient and invariant to small transformations. The Fully Connected layer is the final layer of the network, which takes the flattened feature maps as input and produces the output vector, which can be used for classification or regression tasks. The Output layer is the last layer of the network, which gives the final prediction or score for the input image. The ConvNet can be trained using backpropagation and gradient descent algorithms, which update the weights of the filters and the fully connected layer based on the error between the predicted output and the actual output. The ConvNet can be used for various applications, such as image recognition, face detection, object detection, segmentation, etc.