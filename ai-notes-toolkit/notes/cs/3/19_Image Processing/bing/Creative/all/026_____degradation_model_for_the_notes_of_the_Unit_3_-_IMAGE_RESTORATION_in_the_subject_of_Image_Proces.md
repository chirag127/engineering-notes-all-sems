# Degradation Model for Image Restoration

Image restoration is the process of recovering an image that has been degraded by some factors, such as noise, blur, distortion, etc. Image degradation can occur during image acquisition, transmission, storage, or processing. Image restoration aims to restore the original image as much as possible by using some knowledge of the degradation process and the image characteristics.

A common way to model the image degradation and restoration process is as follows :

- Let f(x,y) be the original image and g(x,y) be the degraded image.
- Let h(x,y) be the degradation function that describes how the original image is degraded by some physical phenomenon, such as motion blur, atmospheric turbulence, lens aberration, etc.
- Let n(x,y) be the additive noise that contaminates the image during the degradation process, such as sensor noise, quantization noise, channel noise, etc.
- Then, the degraded image can be expressed as:

g(x,y) = h(x,y) * f(x,y) + n(x,y)

where * denotes the convolution operation.

- The image restoration problem can be formulated as finding an estimate f^(x,y) of the original image f(x,y) given the degraded image g(x,y) and some information about the degradation function h(x,y) and the noise n(x,y).
- A common way to find the estimate f^(x,y) is to use a restoration filter that operates on the frequency domain of the images. Let F(u,v), G(u,v), H(u,v), and N(u,v) be the Fourier transforms of f(x,y), g(x,y), h(x,y), and n(x,y), respectively. Then, the degradation model can be written as:

G(u,v) = H(u,v) F(u,v) + N(u,v)

- The restoration filter can be designed to invert the degradation function H(u,v) and suppress the noise N(u,v) in the frequency domain. Let R(u,v) be the restoration filter. Then, the estimate F^(u,v) can be obtained as:

F^(u,v) = R(u,v) G(u,v)

- The restored image f^(x,y) can be obtained by applying the inverse Fourier transform to F^(u,v).

Some examples of restoration filters are:

- Inverse filter: R(u,v) = 1 / H(u,v)
- Wiener filter: R(u,v) = H*(u,v) / (|H(u,v)|^2 + K)
- Constrained least squares filter: R(u,v) = H*(u,v) / (|H(u,v)|^2 + K |P(u,v)|^2)

where H*(u,v) is the complex conjugate of H(u,v), K is a constant that controls the trade-off between noise reduction and image fidelity, and P(u,v) is a regularization term that imposes some constraints on the restored image, such as smoothness, edge preservation, etc.

The performance of the image restoration methods depends on the accuracy of the degradation model and the restoration filter. If the degradation function h(x,y) and the noise n(x,y) are known or can be estimated, the restoration filter can be designed to match the degradation model. However, in many practical situations, the degradation function and the noise are unknown or vary spatially, which makes the restoration problem more challenging and requires more advanced methods, such as learning-based methods .