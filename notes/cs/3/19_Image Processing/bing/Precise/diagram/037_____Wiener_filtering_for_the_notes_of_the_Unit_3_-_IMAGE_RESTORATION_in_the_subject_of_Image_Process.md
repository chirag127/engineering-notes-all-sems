### Unit 3 - IMAGE RESTORATION: Wiener filtering

Wiener filtering is a technique used in image restoration to reduce the impact of noise and blurring in an image. It is based on the concept of minimizing the mean square error between the original image and the restored image.

Some key points to note about Wiener filtering are:
- It is a linear estimation technique that assumes the noise and signal are stationary linear stochastic processes.
- It requires knowledge of the power spectra of the noise and the original signal.
- It can be applied in both the spatial and frequency domains.
- In the frequency domain, the Wiener filter is given by the ratio of the power spectrum of the original signal to the sum of the power spectra of the original signal and the noise.
- In the spatial domain, the Wiener filter can be implemented using a convolution operation with a kernel that is derived from the power spectra of the noise and the original signal.

Wiener filtering is a powerful technique for image restoration, but it does have some limitations. It assumes that the noise and signal are stationary, which may not always be the case in real-world scenarios. Additionally, it requires knowledge of the power spectra of the noise and the original signal, which may not always be available.

Overall, Wiener filtering is an important tool in the field of image restoration and can be very effective in reducing the impact of noise and blurring in an image. However, it is important to carefully consider its assumptions and limitations when applying it to real-world scenarios.