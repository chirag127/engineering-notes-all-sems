 Here is the content in Markdown format without any emojis or external links:

### Non-convex optimization for deep networks

- Training deep networks is a non-convex optimization problem. The loss function has many local minima and saddle points.
- Gradient descent gets stuck in poor local minima leading to suboptimal solutions.
- Methods like momentum, RMSProp, Adam, etc. help escape saddle points but do not guarantee finding the global minimum.
- Non-convex optimization techniques try to find better local minima or even the global minimum:
-- Random restarts: Train multiple times from random initializations and pick the best local minimum.
-- Bayesian optimization: Use Bayesian optimization to search for the best hyperparameter values to optimize the loss function.
-- Activation regularization: Apply penalty terms to the activation values to smoothen the loss landscape.
-- Layer-wise training: Train one layer at a time to reach a better local minimum. The optimization is convex for each layer but not jointly convex for all layers.

The above points cover the key highlights of non-convex optimization for training deep neural networks. The methods aim to find better solutions than getting stuck in poor local minima using gradient descent. However, there is no guarantee of finding the global optimal solution. Research in this direction is ongoing to develop more powerful non-convex optimization techniques for training deep networks.

Hope this helps! Let me know if you would like me to modify or expand the answer.