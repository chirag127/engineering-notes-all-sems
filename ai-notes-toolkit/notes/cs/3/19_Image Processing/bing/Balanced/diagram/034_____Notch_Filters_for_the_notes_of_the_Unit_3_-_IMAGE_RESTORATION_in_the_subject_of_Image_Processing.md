### Notch Filters for the notes of the Unit 3 - IMAGE RESTORATION in the subject of Image Processing

- A notch filter is an image processing filter that is used to remove specific frequency components from an image.
- A notch filter is a type of band-stop filter that is designed to remove a specific range of frequencies from an image while leaving the rest of the image unaffected.
- A notch filter can be used to remove periodic noise or interference from an image, such as stripes, bars, or patterns.
- A notch filter can be implemented in the frequency domain by applying a mask to the Fourier transform of the image.
- A notch filter can be either ideal, Butterworth, or Gaussian, depending on the shape and smoothness of the mask  .
- An ideal notch filter has a rectangular shape and sharp edges, which can cause ringing artifacts in the filtered image.
- A Butterworth notch filter has a circular shape and smooth edges, which can reduce the ringing artifacts but also attenuate some desired frequencies.
- A Gaussian notch filter has a bell-shaped curve and smooth edges, which can preserve more desired frequencies but also pass some undesired frequencies.
- A notch filter can be either notch reject or notch pass, depending on whether the mask blocks or passes the specific frequency range.
- A notch reject filter removes the specific frequency range and passes the rest of the frequencies.
- A notch pass filter passes the specific frequency range and removes the rest of the frequencies.
- A notch filter can be either single or multiple, depending on how many frequency ranges are removed or passed.
- A single notch filter removes or passes one specific frequency range.
- A multiple notch filter removes or passes more than one specific frequency range.
- A notch filter can be applied to either the whole image or a region of interest, depending on the location and extent of the noise or interference.
- A notch filter can be designed by identifying the frequency components of the noise or interference in the Fourier spectrum of the image and creating a mask that covers or uncovers those components.
- A notch filter can be evaluated by comparing the filtered image with the original image in terms of visual quality, signal-to-noise ratio, and mean squared error.