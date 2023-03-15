# DFT, DCT for the notes of the Unit 1 - DIGITAL IMAGE FUNDAMENTALS in the subject of Image Processing

- **DFT (Discrete Fourier Transform)** is a mathematical technique used to convert a discrete signal from the time domain to the frequency domain.
- The DFT is defined as: X(k) = sum from n=0 to N-1 of x(n) * exp(-j*2*pi*k*n/N), where x(n) is the discrete signal in the time domain, N is the number of samples, and X(k) is the DFT of the signal.
- The DFT is commonly used in image processing to analyze the frequency content of an image and to perform filtering operations.
- The **DCT (Discrete Cosine Transform)** is another mathematical technique used to convert a discrete signal from the time domain to the frequency domain.
- The DCT is defined as: X(k) = sum from n=0 to N-1 of x(n) * cos(pi*(2n+1)*k/2N), where x(n) is the discrete signal in the time domain, N is the number of samples, and X(k) is the DCT of the signal.
- The DCT is commonly used in image compression, as it has the property of concentrating most of the signal energy in a few coefficients, allowing for efficient encoding of the image data.
- Both the DFT and DCT are important tools in the field of digital image processing and are used in a variety of applications.
