 Here are the notes for Unit 6 - Speech Analysis in Natural Language Processing:

### Features
1. Extracting Audio Features
- Frames: Audio is divided into small frames of 20-40ms
- Windowing: Each frame is multiplied by a window function to reduce discontinuities
- Spectral Features: Frequency domain features extracted using FFT
    - Mel-Frequency Cepstral Coefficients (MFCCs): Captures vocal tract characteristics
    - Linear Predictive Coding (LPC) coefficients: Model vocal tract as an all-pole filter
- Prosodic Features: Features related to rhythm, stress, and intonation of speech
    - Pitch: Fundamental frequency of speech signal
    - Energy: Loudness/amplitude of speech signal
    - Speaking rate: Number of phonemes/frames per second

2. Acoustic Modeling
- HMMs/DNNs are trained to predict the next likely phonetic segment given acoustic features
- Triphone Models: Extend monophone models to include context (previous/next phones) to handle coarticulation effects
- Decision Trees/State Tying: Cluster similar HMM states to reduce parameters and avoid overfitting
- Speaker Adaptation: Customize acoustic models for a new speaker quickly using limited data

3. Language Modeling
- Sequence of words predicted using previous words
- N-gram models: Probability of next word depends on previous N words
- Smoothing: Handle unknown N-grams/rare events by interpolating with lower order N-grams
- Perplexity: Measure of how well a language model predicts a test set, lower is better

Does this look okay? Let me know if you would like me to modify or add anything.