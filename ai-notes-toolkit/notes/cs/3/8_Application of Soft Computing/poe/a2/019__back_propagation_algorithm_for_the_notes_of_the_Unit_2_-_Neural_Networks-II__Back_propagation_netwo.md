 Here is the content in Markdown format without any emojis or external links and in a formal tone:

### Backpropagation Algorithm

1. Backpropagation is a method used to train neural networks by calculating gradient of loss function with respect to weights.
2. It calculates gradient using chain rule. The output derivative is propagated back to hidden layers to update weights and minimize loss.
3. The steps involved are:

- Forward pass: Calculate outputs for each layer.
- Backward pass: Calculate error at output layer and propagate back to update weights.
- Update weights: Use gradient descent to update weights and minimize loss.

4. The backward pass involves calculating error term for each layer and updating weights. The error term for a layer is calculated as:

$\delta^L = \frac{\partial \text{loss}}{\partial a^L} = \left(\frac{\partial loss}{\partial {y}}\right)\left({y}-a^L\right)$ 

$\delta^j = \left({w^{[j+1]}}^T\delta^{j+1}\right) \odot \frac{\partial {a^j}}{\partial {x^j}}$

where $L$ is output layer, $j$ is hidden layer and $\odot$ is elementwise product.
5. The weights are updated as:

${w^{[j]}}_{i,k} \leftarrow {w^{[j]}}_{i,k} - \eta \frac{\partial {L}}{\partial {w^{[j]}}_{i,k}}$

where $\eta$ is learning rate.

This process is repeated over many iterations until loss is minimized. Backpropagation is a powerful technique and forms the foundation for training deep neural networks.