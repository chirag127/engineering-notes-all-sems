### Semi-Supervised Learning for the notes of the Unit 2 - DEEP NETWORKS in the subject of Deep Learning

- Semi-supervised learning is a learning paradigm that combines supervised learning and unsupervised learning in deep neural networks .
- Semi-supervised learning aims to leverage both labeled and unlabeled data to improve the performance and generalization of deep networks on tasks such as image classification, natural language processing, and speech recognition.
- Semi-supervised learning can be useful when the labeled data is scarce, expensive, or noisy, and when the unlabeled data is abundant, cheap, or clean.
- Semi-supervised learning can be implemented by various methods, such as self-training, co-training, graph-based methods, generative models, and consistency regularization.
- Self-training is a method that iteratively trains a classifier on the labeled data, and then uses the classifier to label the most confident unlabeled data, and adds them to the training set.
- Co-training is a method that trains two classifiers on two different views of the data, and then uses each classifier to label the unlabeled data for the other classifier, and adds them to the training set.
- Graph-based methods are methods that construct a graph that represents the similarity between the data points, and then propagate the labels from the labeled nodes to the unlabeled nodes based on the graph structure.
- Generative models are models that learn the joint distribution of the data and the labels, and then use the model to infer the labels for the unlabeled data.
- Consistency regularization is a method that enforces the classifier to produce consistent outputs for the unlabeled data under different perturbations, such as noise, augmentation, or dropout.
- Ladder networks are an example of semi-supervised learning with consistency regularization, which combine supervised learning with unsupervised learning in a single network architecture.
- Ladder networks consist of an encoder that maps the input to a latent representation, and a decoder that reconstructs the input from the latent representation.
- Ladder networks use a cost function that combines the supervised loss on the labeled data and the unsupervised loss on the unlabeled data, which measures the reconstruction error between the input and the output of the decoder.
- Ladder networks use a denoising process that injects noise to the input and the latent representation, and then removes the noise by the decoder, which encourages the network to learn robust and invariant features.
- Ladder networks have shown state-of-the-art results on various semi-supervised learning benchmarks, such as MNIST, CIFAR-10, and SVHN.