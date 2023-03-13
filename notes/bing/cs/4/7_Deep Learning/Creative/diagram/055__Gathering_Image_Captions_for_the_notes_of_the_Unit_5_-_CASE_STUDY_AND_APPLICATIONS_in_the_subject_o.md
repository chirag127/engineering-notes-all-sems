The following diagram illustrates the basic architecture of a deep learning model for image captioning using a CNN-RNN approach. The CNN is used to extract features from the image, and the RNN is used to generate a sequence of words based on the features. The RNN can be a simple LSTM or a more complex attention-based model.

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|     Image       |    |    CNN          |    |    RNN          |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       +--------------------->+--------------------->+
                             |                      |
                             |                      |
                             |                      |
                             |                      |
                             |                      |
                             |                      |
                             |                      |
                             |                      |
                             |                      |
                             |                      |
                             |                      |
                             |                      |
                             |                      |
                             |                      |
                             |                      |
                             |                      |
                             +--------------------->+
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |
                                                   |