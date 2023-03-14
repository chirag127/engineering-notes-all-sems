### Computational & Artificial Neuroscience for the notes of the Unit 4 - OPTIMIZATION AND GENERALIZATION in the subject of Deep Learning

- Computational neuroscience is a branch of neuroscience that studies the brain function in terms of the information processing properties of the structures that make up the nervous system.
- Artificial neuroscience is a branch of artificial intelligence that attempts to design computational systems based on the tasks they will have to solve, using brain-inspired architectures, objective functions, learning rules and optimization methods.
- Optimization and generalization are two key aspects of deep learning that are closely related to computational and artificial neuroscience.
- Optimization refers to the process of finding the optimal parameters of a neural network that minimize a loss function on a given dataset.
- Generalization refers to the ability of a neural network to perform well on new and unseen data that are not part of the training dataset.
- Some of the topics that are relevant for computational and artificial neuroscience in the context of optimization and generalization are:

  - The issue of gradient explosion/vanishing and the more general issue of undesirable spectrum, which affect the stability and convergence of neural network training.
  - The practical solutions to the above issue, such as careful initialization, normalization methods, and skip connections, which aim to improve the conditioning and information flow of neural networks.
  - The generic optimization methods used in training neural networks, such as stochastic gradient descent (SGD) and adaptive gradient methods, and their theoretical properties and limitations.
  - The global issues of neural network training, such as the landscape, mode connectivity, lottery ticket hypothesis and neural tangent kernel (NTK), which shed light on the tractability and generalization of neural networks despite their non-convexity.
  - The biological plausibility and relevance of the above topics, such as how the brain may implement similar or different optimization and generalization mechanisms, and what insights can be gained from comparing artificial and natural neural systems .

- Some of the mnemonics and learning tricks that may help to remember the above topics are:

  - Gradient explosion/vanishing: Think of a rocket that either explodes or vanishes when its thrust is too high or too low, respectively. The thrust is analogous to the gradient, and the rocket is analogous to the neural network.
  - Initialization: Think of a seed that needs to be planted in a good soil and watered properly to grow into a healthy plant. The seed is analogous to the initial parameters, the soil is analogous to the loss landscape, and the water is analogous to the gradient.
  - Normalization: Think of a group of people that need to communicate with each other using a common language and scale. The people are analogous to the neurons, the language is analogous to the activation function, and the scale is analogous to the statistics of the inputs and outputs.
  - Skip connections: Think of a shortcut that allows you to bypass a long and congested road and reach your destination faster. The shortcut is analogous to the skip connection, the road is analogous to the neural network layers, and the destination is analogous to the output.
  - SGD: Think of a ball that rolls down a hill and follows the steepest direction at each point. The ball is analogous to the parameters, the hill is analogous to the loss function, and the direction is analogous to the gradient.
  - Adaptive gradient methods: Think of a ball that rolls down a hill and adapts its speed and direction according to the shape and curvature of the hill. The speed and direction are analogous to the learning rate and the gradient, and the shape and curvature are analogous to the second-order information of the loss function.
  - Landscape: Think of a map that shows the elevation and terrain of a region. The map is analogous to the landscape, the elevation is analogous to the loss value, and the terrain is analogous to the local features of the loss function.
  - Mode connectivity: Think of a network of roads that connect different cities. The roads are analogous to the mode connectivity, and the cities are analogous to the local minima of the loss function.
  - Lottery ticket hypothesis: Think of a lottery ticket that wins a big prize if it matches a certain combination of numbers. The lottery ticket is analogous to a subnetwork of the neural network, and the combination of numbers is analogous to the initial parameters that lead to good performance.
  - Neural tangent kernel (NTK): Think of a linear approximation of a nonlinear function that is valid in a small neighborhood of a point. The linear approximation is analogous to the NTK