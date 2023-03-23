 Here is the formal notes on Principal Component Analysis and Neural Networks for Unit 3 - Data Analysis:

### Principal Component Analysis

1. PCA is a statistical procedure that uses an orthogonal transformation to convert a set of observations of possibly correlated variables into a set of values of linearly uncorrelated variables called principal components.
2. The number of principal components is less than or equal to the number of original variables. This transformation is defined in such a way that the first principal component has the largest possible variance, and each succeeding component in turn has the highest variance possible under the constraint that it is orthogonal to the preceding components.
3. PCA is used to simplify data and extract important variables (called principal components) from a large set of variables in a data matrix. It can reduce the dimensionality of a data set consisting of a large number of interrelated variables, while retaining as much as possible of the variation present in the data set.
4. Steps involved in PCA:

a) Standardize the data (scale the variables)
b) Find the correlation matrix of the variables
c) Calculate the eigenvectors and eigenvalues of the correlation matrix
d) Sort the eigenvectors by decreasing eigenvalues and choose k eigenvectors with the largest eigenvalues to form a new set of k principal components
e) The variance of the data is preserved in the principal components

5. Applications of PCA: Dimension reduction, Feature extraction, Data visualization

### Neural Networks

1. A neural network is a series of algorithms that attempts to identify relationships between inputs and outputs and uses those relationships to make predictions or decisions on new data.
2. They are inspired by biological neural networks in the brain that are made up of interconnected nodes that must process information to learn how to perform a task.
3. The three types of layers in a neural network are:

a) Input layer: The input features of the data
b) Hidden layer: The layers between the input and output layers that help learn the patterns in the data
c) Output layer: Produces the output prediction or decision

4. The learning process involves adjusting the connections between nodes in an iterative process using a loss function to determine how well the network is modeling the data. As the network is exposed to large amounts of data, it independently learns the features and patterns to make predictions on new data.
5. Applications of Neural Networks: Image classification, Speech recognition, Machine translation, Time series forecasting, etc.