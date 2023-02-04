Natural Language Translation: Build a system that can translate text from one language to another with high accuracy. Technologies: Python, NLP, TensorFlow, Numpy, Seq2Seq.

Here is an example code in Python using TensorFlow and Seq2Seq for a Natural Language Translation project:

```
import tensorflow as tf
import numpy as np

# Define the Seq2Seq model
class Seq2Seq(tf.keras.Model):
    def __init__(self, vocab_size, embedding_dim, units):
        super(Seq2Seq, self).__init__()
        self.units = units
        self.embedding = tf.keras.layers.Embedding(vocab_size, embedding_dim)
        self.encoder = tf.keras.layers.LSTM(self.units, return_sequences=True, return_state=True)
        self.decoder = tf.keras.layers.LSTM(self.units, return_sequences=True, return_state=True)
        self.fc = tf.keras.layers.Dense(vocab_size)
        
    def call(self, inputs, hidden, enc_output):
        x = self.embedding(inputs)
        x, state_h, state_c = self.encoder(x, initial_state=hidden)
        x = self.decoder(x, initial_state=[state_h, state_c])
        x = tf.reshape(x, (-1, x.shape[2]))
        x = self.fc(x)
        return x, state_h, state_c
    
    def initialize_hidden_state(self, batch_size):
        return (tf.zeros((batch_size, self.units)), tf.zeros((batch_size, self.units)))

# Define the loss function and the optimizer
def loss_function(real, pred):
    mask = tf.math.logical_not(tf.math.equal(real, 0))
    loss_ = tf.nn.sparse_softmax_cross_entropy_with_logits(labels=real, logits=pred)
    mask = tf.cast(mask, dtype=loss_.dtype)
    loss_ *= mask
    return tf.reduce_mean(loss_)

optimizer = tf.keras.optimizers.Adam()

# Train the model
@tf.function
def train_step(inputs, labels, enc_hidden):
    with tf.GradientTape() as tape:
        predictions, state_h, state_c = model(inputs, enc_hidden)
        loss = loss_function(labels, predictions)
    grads = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(grads, model.trainable_variables))
    return loss, state_h, state_c

# Translate the input text
def translate(inputs, enc_hidden):
    predictions, state_h, state_c = model(inputs, enc_hidden)
    predictions = tf.argmax(predictions, axis=-1)
    return predictions

# Define the parameters and build the model
vocab_size = 10000
embedding_dim = 256
units = 1024
model = Seq2Seq(vocab_size, embedding_dim, units)

# Load the data and train the model
input_tensor, target_tensor, inp_lang, targ_lang = load_dataset(path_to_dataset)
dataset = tf.data.Dataset.from_tensor_slices((input_tensor, target_tensor)).shuffle(len(input_tensor)).batch(64)

for epoch in range(EPOCHS):
    enc_hidden = model.initialize_hidden_state(BATCH_SIZE)
    total_loss = 0
    
    for (batch, (inputs, labels)) in enumerate(dataset):
        loss, state_h, state_c = train_step(inputs, labels, enc_hidden)
        total_loss += loss
        
        if batch % 100 == 0:
            print('Epoch {} Batch {} Loss {:.4f}'.format(epoch + 1, batch, loss.numpy()))
    
    print('Epoch {} Loss {:.4f}'.format(epoch + 1, total_loss / N_BATCHES))
    print('Time taken for 1 epoch {} sec\n'.format(time.time() - start))

# Test the model
inputs = [inp_lang.word_index[i] for i in input_sentence.split(' ')]
inputs = tf.keras.preprocessing.sequence.pad_sequences([inputs], maxlen=max_length_inp, padding='post')
inputs = tf.convert_to_tensor(inputs)

result = ''
enc_hidden = model.initialize_hidden_state(1)
predictions = translate(inputs, enc_hidden)
for i in predictions[0]:
    result += targ_lang.index_word[i] + ' '
print(result)
```

This code defines a Seq2Seq model using TensorFlow and trains it on a dataset of text translations. The model uses an encoder-decoder architecture, where the input text is passed through an encoder to produce a hidden state, and then passed through a decoder to produce the translated text. The model is trained using the Adam optimizer and the loss is calculated using the sparse categorical cross-entropy. The translate function can be used to translate an input sentence into the target language.
