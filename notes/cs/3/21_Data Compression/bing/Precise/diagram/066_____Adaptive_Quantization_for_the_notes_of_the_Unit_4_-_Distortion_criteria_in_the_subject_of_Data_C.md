### Adaptive Quantization

Adaptive quantization is a technique used in data compression to change the quantization parameters based on the data being compressed. It can be used in both forward and backward adaptive quantization schemes.

- In forward adaptive quantization, the input is divided into blocks and the quantizer parameters are estimated for each block. These parameters are transmitted to the receiver as side information .
- In backward adaptive quantization, the algorithm is used to adapt the quantizer to the local behavior of nonstationary inputs .
- Adaptive compression is a type of data compression which changes compression algorithms based on the type of data being compressed .
- This enables selecting an appropriate compression for incoming samples, while taking into account overall memory constraints and current progress of the learned compression .

Adaptive quantization can be used in DPCM systems to improve compression efficiency. It is a key technique in the hybrid video coding framework .