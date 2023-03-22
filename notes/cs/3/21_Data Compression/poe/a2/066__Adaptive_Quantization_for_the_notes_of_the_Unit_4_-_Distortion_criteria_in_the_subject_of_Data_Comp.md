 Here is the content in Markdown format without any emojis or external links, written in a formal tone with points:

### Adaptive Quantization for the notes of the Unit 4 - Distortion criteria in the subject of Data Compression

1. Quantization is a lossy compression technique where the input is an analog signal or a sequence of numbers, and the output is a sequence of quantization levels.
2. Adaptive quantization varies the quantization intervals based on the input data statistics. It achieves higher compression than fixed quantization as it allocates smaller intervals to input ranges with higher probability mass and larger intervals to input ranges with lower probability mass.
3. The most widely used adaptive quantization techniques are scalar quantization and vector quantization.
4. In scalar quantization, each sample is quantized independently. The quantization intervals are adapted based on the probability density function (pdf) of the input. In vector quantization, a group of samples is quantized together. The quantization intervals take the form of codevectors in a codebook. The codebook is designed based on the joint pdf of the input vectors.
5. The performance of adaptive quantization depends on how well the quantization intervals are adapted to the changing input statistics. There is a trade-off between the compression performance and the complexity of adapting the quantizer to changing input statistics. The adaptation has to be done in real-time using a limited amount of data to control the complexity.

Does this look okay? Let me know if you would like me to modify or expand the content in any way.