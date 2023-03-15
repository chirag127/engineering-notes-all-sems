# Unit 4 - ARTIFICIAL NEURAL NETWORKS

## Introduction

- Artificial neural networks (ANNs) are computational models inspired by the structure and function of biological neural networks that constitute the human brain.
- ANNs consist of layers of interconnected nodes, also called neurons, that process and transmit information. Each node has an activation function that determines its output based on its inputs and a bias term.
- ANNs can learn from data and perform tasks such as classification, regression, clustering, dimensionality reduction, etc. by adjusting the weights of the connections between the nodes.
- ANNs are the core component of deep learning, which is a subfield of machine learning that deals with complex and high-dimensional data.

## Types of ANNs

- There are different types of ANNs based on their architecture, learning algorithm, and application domain. Some of the common types are:

  - Feedforward neural networks (FNNs): These are the simplest and most widely used type of ANNs, where the information flows only in one direction, from the input layer to the output layer, through one or more hidden layers. There are no feedback loops or cycles in FNNs. FNNs can be trained using gradient-based methods such as backpropagation.
  - Recurrent neural networks (RNNs): These are a type of ANNs that allow for feedback loops or cycles in the network, which enable them to store and process sequential data such as text, speech, or video. RNNs can learn long-term dependencies and temporal patterns in the data, but they also suffer from the problems of vanishing and exploding gradients. RNNs can be trained using variants of backpropagation such as backpropagation through time (BPTT) or truncated BPTT.
  - Convolutional neural networks (CNNs): These are a type of ANNs that are specially designed for processing image data, but can also be applied to other types of data such as text or audio. CNNs use convolutional layers that apply filters to the input data and produce feature maps that capture the local patterns and structures in the data. CNNs also use pooling layers that reduce the dimensionality and complexity of the feature maps. CNNs can be trained using gradient-based methods such as backpropagation.
  - Self-organizing maps (SOMs): These are a type of ANNs that are based on unsupervised learning, where the network learns to organize the input data into clusters or categories without any labels or supervision. SOMs use a competitive learning algorithm that adjusts the weights of the nodes based on their similarity to the input data. SOMs can be used for data visualization, dimensionality reduction, clustering, etc..

## Applications of ANNs

- ANNs have a wide range of applications in various domains such as computer vision, natural language processing, speech recognition, recommender systems, bioinformatics, etc. Some of the examples are:

  - Face recognition: CNNs can be used to detect and recognize faces in images or videos by learning the features and characteristics of different faces.
  - Machine translation: RNNs can be used to translate text or speech from one language to another by learning the semantic and syntactic rules of different languages.
  - Sentiment analysis: FNNs or CNNs can be used to classify the sentiment or emotion of a text or speech by learning the words and phrases that indicate positive or negative sentiment.
  - Image captioning: CNNs and RNNs can be combined to generate captions or descriptions for images or videos by learning the visual and linguistic features of the data.
  - Anomaly detection: SOMs can be used to detect anomalies or outliers in the data by learning the normal patterns and distributions of the data.