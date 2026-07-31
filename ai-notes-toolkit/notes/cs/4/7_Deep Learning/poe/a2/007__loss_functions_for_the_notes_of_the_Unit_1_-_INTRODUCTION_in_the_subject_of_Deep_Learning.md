 Here is the formal content in markdown format without any emojis or external links for the topic loss functions for the notes of the Unit 1 - INTRODUCTION in the subject of Deep Learning:

### Loss Functions

1. Mean Squared Error (MSE): It is the average of the squared differences between the predicted and actual values. It penalizes large errors more than small errors.

MSE = 1/n * sum(predicted - actual)^2

2. Mean Absolute Error (MAE): It is the average of the absolute differences between the predicted and actual values. It penalizes all errors equally.

MAE = 1/n * sum(abs(predicted - actual))

3. Hinge Loss: It is used for classification problems with linear output units. It penalizes predictions that are on the wrong side of the margin.

Hinge Loss = max(0, margin - prediction * label)

4. Cross-Entropy Loss: It is used for classification probabilistic predictions. It increases as the predicted probability diverges from the actual label. It gives a more log loss that depends on the confidence of the incorrect predictions.

Cross-Entropy Loss = -sum(label * log(prediction) + (1 - label) * log(1 - prediction))

The above content provides the formal study material in points without any feelings or friendliness as requested. The content is written in Markdown format and includes no emojis or external links. The requested topic of loss functions for the notes of Unit 1 - INTRODUCTION of Deep Learning is covered. Please let me know if you would like me to modify or expand the content in any way.