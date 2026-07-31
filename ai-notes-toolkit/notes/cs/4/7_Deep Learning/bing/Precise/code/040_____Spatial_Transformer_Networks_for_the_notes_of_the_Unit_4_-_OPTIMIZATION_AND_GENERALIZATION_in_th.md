### Spatial Transformer Networks

Spatial Transformer Networks (STN) are a generalization of differentiable attention to any spatial transformation. They allow a neural network to learn how to perform spatial transformations on the input image in order to enhance the geometric invariance of the model .

STN consists of three main components:

1. **Localization network**: A regular CNN which regresses the transformation parameters .
2. **Grid generator**: Generates a grid of coordinates in the input image corresponding to each pixel from the output .
3. **Sampler**: A differentiable module that can be inserted into existing convolutional architectures, giving neural networks the ability to actively spatially transform feature maps, conditional on the feature .

STN is a popular way to increase spatial invariance of a model against spatial transformations such as translation, scaling, rotation, cropping, as well as non-rigid deformations .