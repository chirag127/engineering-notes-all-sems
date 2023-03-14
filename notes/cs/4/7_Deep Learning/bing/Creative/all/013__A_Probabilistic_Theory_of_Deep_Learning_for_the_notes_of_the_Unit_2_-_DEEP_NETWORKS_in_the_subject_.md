### A Probabilistic Theory of Deep Learning for the notes of the Unit 2 - DEEP NETWORKS in the subject of Deep Learning

- A probabilistic theory of deep learning is a framework that explains the success and limitations of deep learning models by relating them to probabilistic models and inference algorithms.
- The main idea is to view deep learning as a form of probabilistic inference, where the goal is to infer the hidden variables (such as class labels, object positions, etc.) from the observed variables (such as images, speech, etc.) in the presence of nuisance variables (such as illumination, noise, etc.).
- A key concept in this theory is the deep rendering model (DRM), which is a generative probabilistic model that explicitly captures the nuisance variation in the data by using a hierarchy of latent variables.
- The DRM consists of two parts: a class appearance model (CAM) and a rendering function (RF). The CAM defines the distribution of the latent variables given the class label, and the RF defines the distribution of the observed variables given the latent variables.
- The DRM can be learned from data using the expectation-maximization (EM) algorithm, which alternates between inferring the latent variables (E-step) and updating the model parameters (M-step).
- The DRM can also be relaxed to a discriminative model, which directly predicts the class label from the observed variables, by using the Bayes rule and the maximum a posteriori (MAP) principle.
- The DRM can recover two of the current leading deep learning systems, deep convolutional neural networks (DCNs) and random decision forests (RDFs), by making different assumptions and approximations.
- DCNs are obtained by assuming that the RF is a convolutional neural network (CNN) and that the CAM is a multivariate Gaussian distribution. The EM algorithm for the DRM then reduces to the backpropagation algorithm for the DCN.
- RDFs are obtained by assuming that the RF is a decision tree and that the CAM is a categorical distribution. The EM algorithm for the DRM then reduces to the information maximization principle for the RDF.
- The probabilistic theory of deep learning provides new insights into the properties and limitations of deep learning models, such as their probabilistic semantics, their entanglement of supervised and unsupervised learning, and their sensitivity to overfitting and adversarial examples.
- The probabilistic theory of deep learning also suggests new directions for improving and extending deep learning models, such as incorporating uncertainty, incorporating prior knowledge, and combining generative and discriminative models .

: A Probabilistic Theory of Deep Learning, Ankit B. Patel, Tan Nguyen, Richard G. Baraniuk, arXiv:1504.00641v1 [stat.ML] 2 Apr 2015
: Probabilistic Deep Learning with Probabilistic Neural Networks, Max Welling, arXiv:2106.00120 [cs.LG] 31 May 2021