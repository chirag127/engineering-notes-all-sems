 Here are the notes for Generative Adversarial Networks (GAN) for Unit 2 - Deep Networks in Deep Learning:

### Generative Adversarial Networks (GAN)

1. GANs consist of two networks competing with each other:
- Generator network: Generates new data instances.
- Discriminator network: Evaluates the generated instances and classifies them as real or fake.

2. The training process is an adversarial game:
- The generator is trying to fool the discriminator by generating data that looks real.
- The discriminator is trying to correctly classify real and fake data.
- This process leads the generator to produce more and more realistic data.

3. Applications of GANs:
- Generating synthetic yet realistic images, videos, speech, etc.
- Image editing and manipulation.
- Medical image synthesis.
- Drug discovery.
- etc.

4. Challenges with GANs:
- Mode collapsing: The generator gets stuck in a limited number of modes and is unable to produce diverse outputs.
- Training instability: The adversarial game can lead to unstable training processes that don't converge.
- Evaluation metrics: It is difficult to quantitatively evaluate how realistic the generated samples are.

5. Recent advances and trends:
- Conditional GANs: Generate data based on conditions or inputs.
- Cycle-consistent GANs: Enforce consistency between input and output via a cycle consistency loss.
- Progress with training stability and mode collapse.
- Higher resolution image generation.
- Generating images from semantic layouts or sketches.
- Synthesizing videos, speech, and other sequential or time-series data.