### Batch Normalization for the notes of the Unit 2 - DEEP NETWORKS in the subject of Deep Learning

- Batch normalization is a technique for training very deep neural networks that standardizes the inputs to a layer for each mini-batch .
- This has the effect of stabilizing the learning process and dramatically reducing the number of training epochs required to train deep networks .
- Batch normalization also provides some regularization effect, reducing the need for dropout or other techniques .
- Batch normalization can be applied to either the activations of a prior layer or the inputs directly.
- The idea of batch normalization is to transform the inputs of each layer so that they have a mean of zero and a standard deviation of one .
- This is done by subtracting the batch mean and dividing by the batch standard deviation for each input feature .
- The batch mean and standard deviation are computed using the statistics of the current mini-batch of samples .
- Batch normalization also introduces two learnable parameters, gamma and beta, for each input feature .
- Gamma is a scaling factor that allows the model to adjust the variance of the normalized inputs .
- Beta is a shifting factor that allows the model to adjust the mean of the normalized inputs .
- These parameters are updated during the backpropagation process along with the other model weights .
- Batch normalization can be implemented in Keras and TensorFlow 2 using the BatchNormalization layer.
- The layer can be added after a convolutional or dense layer, and before the activation function.
- The layer takes an argument axis, which specifies the feature axis to normalize.
- For example, if the input is a 4D tensor with shape (batch_size, height, width, channels), then axis should be set to -1 (or 3) to normalize along the channel dimension.
- Here is an example of a convolutional neural network with batch normalization in Keras and TensorFlow 2:

```python
# import libraries
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, BatchNormalization, Activation

# define model
model = Sequential()
# add first convolutional layer with batch normalization and relu activation
model.add(Conv2D(32, (3, 3), padding='same', input_shape=(32, 32, 3)))
model.add(BatchNormalization(axis=-1))
model.add(Activation('relu'))
# add second convolutional layer with batch normalization and relu activation
model.add(Conv2D(32, (3, 3), padding='same'))
model.add(BatchNormalization(axis=-1))
model.add(Activation('relu'))
# add max pooling layer
model.add(MaxPooling2D(pool_size=(2, 2)))
# add flatten layer
model.add(Flatten())
# add dense layer with batch normalization and relu activation
model.add(Dense(64))
model.add(BatchNormalization())
model.add(Activation('relu'))
# add output layer with softmax activation
model.add(Dense(10, activation='softmax'))
# compile model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
# summarize model
model.summary()
```

- Some possible mnemonics and learning tricks for batch normalization are:

  - Batch normalization is like **B**alancing the **N**umbers in each layer.
  - Batch normalization uses the **B**atch statistics to **N**ormalize the inputs .
  - Batch normalization has two parameters: **G**amma for scaling and **B**eta for shifting .
  - Batch normalization can be applied before or after the activation function, but usually before .
  - Batch normalization can reduce the need for dropout, as it has a regularization effect .