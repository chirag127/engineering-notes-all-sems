### Frequency Domain

- The frequency domain is a space which is defined by **Fourier transform** . Fourier transform has a very wide application in image processing.
- Frequency domain analysis is used to indicate how **signal energy** can be distributed in a range of **frequency** .
- Frequency filters process an image in the frequency domain. The image is **Fourier transformed**, multiplied with the **filter function** and then **re-transformed** into the spatial domain.
- Attenuating high frequencies results in a **smoother image** in the spatial domain, attenuating low frequencies enhances the **edges**.
- Frequency domain filtering process can be summarized as follows:
  - Multiply input image by (-1)<sup>x+y</sup>
  - Compute **DFT** (Discrete Fourier Transform) F (u,v) of input image.
  - Multiply F (u,v) by a filter function H (u,v).
  - Compute the **inverse DFT** of the product.
  - Obtain the real part of the result and multiply it by (-1)<sup>x+y</sup>
- Frequency-domain analysis is widely used in such areas as **communications, geology, remote sensing, and image processing**.
- Some specialized signal processing techniques use transforms that result in a **joint time–frequency domain**, with the **instantaneous frequency** being a key link between the time domain and the frequency domain.