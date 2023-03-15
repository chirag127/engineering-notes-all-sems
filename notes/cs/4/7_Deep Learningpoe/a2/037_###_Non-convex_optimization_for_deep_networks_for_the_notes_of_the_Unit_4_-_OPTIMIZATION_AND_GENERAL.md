 Here is the content in markdown format for the topic ### Non-convex optimization for deep networks for the notes of the Unit 4 - OPTIMIZATION AND GENERALIZATION in the subject of Deep Learning:

### Non-convex optimization for deep networks

- Deep neural networks have multiple layers of parameters and are highly non-convex functions of these parameters.
- This makes optimization challenging as local minima are common and global minima are difficult to find.
- Some strategies to deal with this:
    - Initialization: Choosing good initial parameters can help optimization land in a good local minimum. Methods like Xavier initialization are used.
    - Gradient descent tricks: Using momentum, adaptive learning rate, etc. can help avoid getting stuck in bad local minima.
    - Batch normalization: This makes the loss surface smoother and can help optimization.
- For very deep or complex networks,these methods may not be sufficient and more sophisticated optimizers like Adam may be needed.
- Some networks like residual networks are designed to be easier to optimize by having a less extreme loss surface.
- In the end, non-convex optimization of deep networks is difficult and remains an open research problem to develop more powerful and efficient optimizers.

Advantages:
- When optimization succeeds, deep networks can learn complex patterns and achieve state-of-the-art results.

Disadvantages:
- No guarantees of finding the global minimum.
- May take a long time to optimize and require carefully tweaking the process.
- May be sensitive to hyperparameters and random seeds due to the non-convexity.

Examples:
- Optimizing a deep convolutional network or recurrent network for image or speech tasks.

Applications:
- Pretty much all modern deep learning systems which use complex multi-layer architectures.