### LSTM

- LSTM stands for Long Short-Term Memory, which is a type of recurrent neural network (RNN) architecture.   
- Unlike standard feedforward neural networks, LSTM has feedback connections that allow it to process not only single data points, but also entire sequences of data.  
- This characteristic makes LSTM networks ideal for processing and predicting data that have temporal dependencies, such as speech, text, video, or time series.  
- A common LSTM unit consists of a cell, an input gate, an output gate, and a forget gate. The cell stores the internal state of the unit, and the gates regulate the flow of information into and out of the cell.  
- The input gate decides which pieces of new information to store in the cell, the output gate decides which pieces of information in the cell to output, and the forget gate decides which pieces of information in the cell to discard.  
- The gates use sigmoid functions to assign values between 0 and 1 to the information, where 0 means to ignore and 1 means to keep.  
- The LSTM architecture aims to provide a short-term memory for RNN that can last for long time steps, thus overcoming the problems of vanishing or exploding gradients that affect standard RNNs.  
- LSTM networks can be trained using gradient descent and backpropagation through time (BPTT) algorithms.  
- LSTM networks can be applied to various tasks, such as machine translation, speech recognition, handwriting recognition, robot control, video games, and healthcare.  

: Long short-term memory - Wikipedia
: A Gentle Introduction to Long Short-Term Memory Networks by the Experts - MachineLearningMastery.com
: LSTM in deep learning - CodeSpeedy