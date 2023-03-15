# Unit 4 - ARTIFICIAL NEURAL NETWORKS

## Introduction

- Artificial neural networks (ANNs) are computational models inspired by biological neural networks, such as the brain and the nervous system.
- ANNs are used to approximate functions that are generally unknown, such as pattern recognition, classification, regression, forecasting, etc.
- ANNs consist of a collection of connected units or nodes called artificial neurons, which loosely model the neurons in a biological brain.
- Each artificial neuron receives a set of inputs, performs a weighted sum, and applies a non-linear activation function to produce an output.
- The artificial neurons are arranged in layers, containing an input layer, one or more hidden layers, and an output layer.
- The connections between the artificial neurons have associated weights and thresholds, which are adjusted during the learning process to minimize the error between the desired and the actual output.

## Types of ANNs

- There are many types of ANNs, depending on the architecture, the learning algorithm, the activation function, the application domain, etc.
- Some of the common types of ANNs are:

  - Feedforward neural networks: The simplest type of ANNs, where the information flows only in one direction, from the input layer to the output layer, without any feedback loops.
  - Recurrent neural networks: A type of ANNs, where the information can flow in both directions, allowing the network to have memory and learn from sequential data, such as natural language or time series.
  - Convolutional neural networks: A type of ANNs, where the artificial neurons are organized in a grid-like structure, and the connections are local and shared, allowing the network to learn from spatial data, such as images or videos.
  - Self-organizing maps: A type of ANNs, where the artificial neurons are arranged in a low-dimensional grid, and the network learns to map high-dimensional input data to the grid, preserving the topological features of the data.
  - Radial basis function networks: A type of ANNs, where the artificial neurons in the hidden layer use radial basis functions as activation functions, allowing the network to learn from non-linear and multidimensional data.

## Learning Algorithms

- Learning algorithms are the methods that are used to adjust the weights and thresholds of the artificial neurons in order to minimize the error between the desired and the actual output.
- There are two main categories of learning algorithms: supervised and unsupervised.
- Supervised learning algorithms are the ones that require a set of labeled input-output pairs, and the network learns to map the input to the output by comparing its output with the desired output.
- Unsupervised learning algorithms are the ones that do not require any labels, and the network learns to discover the underlying structure or patterns in the input data.
- Some of the common learning algorithms are:

  - Gradient descent: A supervised learning algorithm, where the network updates its weights and thresholds by moving in the opposite direction of the gradient of the error function with respect to the parameters.
  - Backpropagation: A supervised learning algorithm, where the network updates its weights and thresholds by propagating the error from the output layer to the input layer, using the chain rule of differentiation.
  - Hebbian learning: An unsupervised learning algorithm, where the network updates its weights and thresholds by increasing the strength of the connections that are active at the same time, following the principle of "cells that fire together, wire together".
  - Competitive learning: An unsupervised learning algorithm, where the network updates its weights and thresholds by activating only one or a few artificial neurons in the output layer, following the principle of "winner takes all".

## Applications

- ANNs have a wide range of applications in various domains, such as computer vision, natural language processing, speech recognition, robotics, bioinformatics, etc.
- Some of the examples of applications are:

  - Face recognition: A computer vision task, where the network learns to identify and verify the faces of people from images or videos, using convolutional neural networks.
  - Machine translation: A natural language processing task, where the network learns to translate text or speech from one language to another, using recurrent neural networks.
  - Speech synthesis: A speech recognition task, where the network learns to generate human-like speech from text or other