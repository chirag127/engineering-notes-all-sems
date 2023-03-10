 Here is the content in markdown format for the topic ### Scalar Quantization for the notes of the Unit 4 - Distortion criteria in the subject of Data Compression:

### Scalar Quantization

- Scalar quantization is the simplest form of quantization where the input is mapped to the closest output level.
- The input signal is divided into intervals and each interval is mapped to a single output level.
- The number of intervals (quantization levels) determines the quantization error and bitrate. Higher number of levels leads to lower quantization error but higher bitrate and vice-versa.
- The input range is divided into intervals of equal size. The midpoint of each interval is selected as the quantization level.
- For example, if we use 4 quantization levels (2 bits), the input range will be divided into 4 equal intervals and the midpoints will be the quantization output levels.
- The main advantage is simplicity in implementation. The main disadvantage is that it does not utilize the probability distribution of the input and can lead to higher quantization error than other advanced quantization techniques like vector quantization.
- Scalar quantization is used in low bitrate coding of speech and audio signals where the complexity requirements are stringent andsome amount of quantization error can be tolerated.

[Diagrams and examples can be added here to aid understanding]

[Mention applications and advantages/disadvantages in more detail]