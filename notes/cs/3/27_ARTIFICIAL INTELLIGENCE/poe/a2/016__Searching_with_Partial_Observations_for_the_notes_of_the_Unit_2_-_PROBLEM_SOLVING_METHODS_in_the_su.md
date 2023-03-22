 Here is the content in markdown format without any emojis or external links:

### Searching with Partial Observations

- In many real-world problems, the state of the world is not fully observable. We may only have access to partial observations or sensory data about the world.
- Search algorithms must be modified to handle such partial observability.
- Based on the observations available, we maintain a distribution over possible world states. As new observations come in, we update the distribution using Bayesian methods.
- The search then proceeds based on the current distribution. Actions are selected to maximize the expected utility based on the distribution.
- After taking an action and making new observations, the distribution is updated again. This process repeats until a goal state is reached or a time/resource limit is exceeded.
- Partial observability greatly increases the difficulty of searching/planning since we have uncertainty/multiple hypotheses about the actual state of the world. Managing this uncertainty is key to practical systems.
- Example: Partially observable maze (only local observations available)

The above content is written in formal tone with points and without any emojis or external links as per the given instructions. Please let me know if you would like me to modify or expand the answer.