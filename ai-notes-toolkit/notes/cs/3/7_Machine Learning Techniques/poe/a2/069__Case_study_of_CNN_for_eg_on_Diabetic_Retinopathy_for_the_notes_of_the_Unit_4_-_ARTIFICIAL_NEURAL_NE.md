 Here is the formal markdown format notes on the given topic:

### Case study of CNN for Diabetic Retinopathy

Diabetic Retinopathy (DR) is a vision-threatening complication of diabetes which affects the retinal blood vessels. Early detection of DR is critical to prevent vision loss. Here we discuss a convolutional neural network (CNN) approach to automatically detect DR.

* Data: The dataset consists of retinal fundus images with diabetic retinopathy from various severity levels including minimal, mild, moderate, severe and proliferative DR along with normal cases. A total of 35,126 images were used for training and validation.
* CNN Architecture: The CNN has the following layers -

1. Convolutional layer 1 - 32 filters of size 3x3
2. ReLU activation
3. Max pooling of size 2x2
4. Convolutional layer 2 - 64 filters of size 3x3
5. ReLU activation
6. Max pooling of size 2x2
7. Fully connected layer - 512 units
8. Batch Normalization
9. ReLU activation
10. Fully connected layer - 256 units
11. Batch Normalization
12. ReLU activation
13. Output layer - 5 units (for 5 classes)

* Training: The network was trained with Adam Optimizer and categorical cross-entropy loss. Data augmentation techniques like random rotations, shifts, zooming and flipping were used to prevent overfitting.
* Results: The model achieved an accuracy of 93% on validation set in detecting normal cases and DR cases of varying severity. The high accuracy demonstrates the effectiveness of CNNs in automated DR detection which can aid doctors in fast and accurate diagnosis and treatment.

The notes are written in a formal tone with point wise explanations of the key steps - data, architecture and training of the CNN model for Diabetic Retinopathy detection. No emojis or external links are included as per the given requirements. Let me know if you would like me to modify or expand the notes in any way.