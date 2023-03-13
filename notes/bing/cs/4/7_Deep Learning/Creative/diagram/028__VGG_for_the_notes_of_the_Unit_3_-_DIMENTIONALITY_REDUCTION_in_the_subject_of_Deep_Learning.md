VGG is a standard deep convolutional neural network architecture with multiple layers. It was proposed by Karen Simonyan and Andrew Zisserman of Visual Geometry Group (VGG), Oxford University, in 2014. It consists of 16 or 19 convolutional layers, depending on the variant (VGG-16 or VGG-19), followed by 3 fully connected layers. The convolutional layers use small 3 x 3 filters, and the pooling layers use 2 x 2 filters with a stride of 2. The input size of the network is 224 x 224 x 3, and the output size is 1000, corresponding to the number of classes in ImageNet.

The following diagram illustrates the basic architecture of a VGG-16 network using ASCII characters:

```
Input: 224 x 224 x 3
|-----------------|
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|-----------------|

Conv1: 64 filters of 3 x 3, stride 1, padding 1
|-----------------|
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|-----------------|

Conv2: 64 filters of 3 x 3, stride 1, padding 1
|-----------------|
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|-----------------|

Pool1: 2 x 2 filters, stride 2
|---------|
|         |
|         |
|         |
|         |
|         |
|         |
|         |
|---------|

Conv3: 128 filters of 3 x 3, stride 1, padding 1
|---------|
|         |
|         |
|         |
|         |
|         |
|         |
|         |
|---------|

Conv4: 128 filters of 3 x 3, stride 1, padding 1
|---------|
|         |
|         |
|         |
|         |
|         |
|         |
|         |
|---------|

Pool2: 2 x 2 filters, stride 2
|-----|
|     |
|     |
|     |
|     |
|-----|

Conv5: 256 filters of 3 x 3, stride 1, padding 1
|-----|
|     |
|     |
|     |
|     |
|-----|

Conv6: 256 filters of 3 x 3, stride 1, padding 1
|-----|
|     |
|     |
|     |
|     |
|-----|

Conv7: 256 filters of 3 x 3, stride 1, padding 1
|-----|
|     |
|     |
|     |
|     |
|-----|

Pool3: 2 x 2 filters, stride 2
|--|
|  |
|  |
|--|

Conv8: 512 filters of 3 x 3, stride 1, padding 1
|--|
|  |
|  |
|--|

Conv9: 512 filters of 3 x 3, stride 1, padding 1
|--|
|  |
|  |
|--|

Conv10: 512 filters of 3 x 3, stride 1, padding 1
|--|
|  |
|  |
|--|

Pool4: 2 x 2 filters, stride 2
| |
| |
| |

Conv11: 512 filters of 3 x 3, stride 1, padding 1
| |
| |
| |

Conv12: 512 filters of 3 x 3, stride 1, padding 1
| |
| |
| |

Conv13: 512 filters of 3 x 3, stride 1, padding 1
| |
| |
| |

Pool5: 2 x 2 filters, stride 2
|

FC1: 4096 neurons
|-----------------|

FC2: 4096 neurons
|-----------------|

FC3: 1000 neurons
|-----------------|

Output: 1000 classes
|-----------------|
|                 |
|