### Semi-Supervised Learning for the Notes of Unit 2 - Deep Networks in the Subject of Deep Learning

Semi-supervised learning is a type of machine learning that falls between supervised and unsupervised learning. It is used when there are not enough labeled data points available for supervised learning, but there is a large amount of unlabeled data available. 

Here are some key points to remember about semi-supervised learning:

1. Semi-supervised learning is useful when a large amount of unlabeled data is available, but labeling all of it is time-consuming and expensive.

2. In semi-supervised learning, a small amount of labeled data is used along with a much larger amount of unlabeled data to train a model.

3. The model learns to generalize from the labeled data to the unlabeled data, making predictions on the unlabeled data based on what it has learned from the labeled data.

4. There are several approaches to semi-supervised learning, including self-training, co-training, and multi-view learning.

5. In self-training, a model is trained on the labeled data and then used to make predictions on the unlabeled data. The most confident predictions are added to the labeled data and the model is retrained.

6. In co-training, multiple models are trained on different subsets of the data, and each model makes predictions on the unlabeled data. The predictions from one model are used to label the data for the other model, and vice versa.

7. In multi-view learning, multiple views of the data are used to train a model. For example, in image classification, one view might be the raw pixels, while another view might be a set of hand-crafted features.

Mnemonics and learning tricks:

- One way to remember the different approaches to semi-supervised learning is to think of them as different ways to use the unlabeled data. Self-training uses the most confident predictions, co-training uses two models to label each other's data, and multi-view learning uses different perspectives on the data.

- Another way to remember semi-supervised learning is to think of it as a way to get more bang for your buck. By using unlabeled data in addition to labeled data, you can train a more accurate model without having to label all of the data.

Semi-supervised learning has several advantages over supervised learning, including:

- It can be used when labeled data is scarce, which is often the case in real-world applications.

- It can lead to better generalization, as the model is forced to learn from the unlabeled data in addition to the labeled data.

However, there are also some disadvantages to semi-supervised learning, including:

- It can be difficult to know when to stop adding unlabeled data, as too much unlabeled data can lead to overfitting.

- It can be difficult to know which unlabeled data to use, as not all unlabeled data is equally informative.

Overall, semi-supervised learning is a powerful tool for machine learning, and is particularly useful when labeled data is scarce. By using a combination of labeled and unlabeled data, it is possible to train more accurate models that generalize better to new data.