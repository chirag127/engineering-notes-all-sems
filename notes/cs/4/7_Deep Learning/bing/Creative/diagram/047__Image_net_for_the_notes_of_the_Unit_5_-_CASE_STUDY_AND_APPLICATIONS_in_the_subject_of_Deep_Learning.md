ImageNet is a large-scale dataset of over 15 million labeled high-resolution images belonging to roughly 22,000 categories. The dataset is used in the ImageNet Large Scale Visual Recognition Challenge (ILSVRC), a benchmark in image classification and object detection. The challenge tasks include image classification, single-object localization, and object detection. The images are organized according to the WordNet hierarchy, which is a lexical database of English words grouped by meanings and relations.

The following ASCII diagram illustrates the basic architecture of a convolutional neural network (CNN) that can be used for image classification on ImageNet. The network consists of several convolutional layers, pooling layers, fully connected layers, and a softmax layer. The input is an image of size 224 x 224 x 3, and the output is a vector of 1000 probabilities corresponding to the 1000 classes in ImageNet.

```
+---------------------+     +---------------------+     +---------------------+
|                     |     |                     |     |                     |
|                     |     |                     |     |                     |
|                     |     |                     |     |                     |
|                     |     |                     |     |                     |
|                     |     |                     |     |                     |
|                     |     |                     |     |                     |
|                     |     |                     |     |                     |
|                     |     |                     |     |                     |
|                     |     |                     |     |                     |
|                     |     |                     |     |                     |
|                     |     |                     |     |                     |
|                     | 224x224x3                |     |                     |
|                     |     |                     |     |                     |
|                     |     |                     |     |                     |
|                     |     |                     |     |                     |
|                     +----->                     +----->                     |
|                     |     |                     |     |                     |
|                     |     |                     |     |                     |
|                     |     |                     |     |                     |
|                     |     |                     |     |                     |
|                     |     |                     | 55x55x96                 |
|                     |     |                     |     |                     |
|                     |     |                     |     |                     |
|                     |     |                     |     |                     |
|                     |     |                     |     |                     |
+---------------------+     +---------------------+     +---------------------+
    Input image            Convolutional layer 1       Pooling layer 1

+---------------------+     +---------------------+     +---------------------+
|                     |     |                     |     |                     |
|                     |     |                     |     |                     |
|                     |     |                     |     |                     |
|                     | 27x27x96                 |     |                     |
|                     |     |                     |     |                     |
|                     +----->                     +----->                     |
|                     |     |                     |     |                     |
|                     |     |                     |     |                     |
|                     |     |                     | 27x27x256                |
|                     |     |                     |     |                     |
|                     |     |                     |     |                     |
+---------------------+     +---------------------+     +---------------------+
   Pooling layer 1         Convolutional layer 2       Pooling layer 2

+---------------------+     +---------------------+     +---------------------+
|                     |     |                     |     |                     |
|                     |     |                     |     |                     |
|                     | 13x13x256                |     |                     |
|                     |     |                     |     |                     |
|                     +----->                     +----->                     |
|                     |     |                     |     |                     |
|                     |     |                     |     |                     |
|                     |     |                     | 13x13x384                |
|                     |     |                     |     |                     |
|                     |     |                     |     |                     |
+---------------------+     +---------------------+     +---------------------+
   Pooling layer 2         Convolutional layer 3       Convolutional layer 4

+---------------------+     +---------------------+     +---------------------+
|                     |     |                     |     |                     |
|                     |     |                     |     |                     |
|                     | 13x13x384                |     |                     |
|                     |     |                     |     |                     |
|                     +----->                     +----->                     |
|                     |     |                     |     |                     |
|                     |     |                     |     |                     |
|                     |     |                     | 13x13x256                |
|                     |     |                     |     |                     |
|                     |     |                     |