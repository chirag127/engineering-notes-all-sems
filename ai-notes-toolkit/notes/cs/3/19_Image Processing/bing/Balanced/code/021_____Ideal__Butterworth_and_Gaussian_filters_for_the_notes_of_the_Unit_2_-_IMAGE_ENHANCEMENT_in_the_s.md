# Ideal, Butterworth and Gaussian filters for the notes of the Unit 2 - IMAGE ENHANCEMENT in the subject of Image Processing

- Image enhancement is the process of improving the quality of an image by modifying its contrast, brightness, sharpness, etc.
- Image enhancement can be done in either spatial domain or frequency domain.
- Spatial domain methods operate directly on the pixel values of the image, while frequency domain methods transform the image into its frequency components and apply filters on them.
- Filters are functions that modify the amplitude or phase of the frequency components of an image, depending on their frequency, orientation, or location.
- Filters can be classified into low-pass, high-pass, band-pass, or band-reject filters, depending on which frequency components they allow or reject.
- Filters can also be classified into ideal, Butterworth, or Gaussian filters, depending on the shape of their frequency response.

## Ideal filters

- Ideal filters have a rectangular frequency response, meaning that they have a sharp transition between the passband and the stopband.
- Ideal filters are easy to design and implement, but they have some drawbacks, such as:
  - They introduce ringing artifacts (oscillations) in the spatial domain, due to the Gibbs phenomenon.
  - They are sensitive to noise, since they do not attenuate any frequency component in the passband, regardless of its magnitude.
  - They are not realizable in practice, since they require infinite impulse response (IIR) filters.

## Butterworth filters

- Butterworth filters have a smooth frequency response, meaning that they have a gradual transition between the passband and the stopband.
- Butterworth filters are more realistic and practical than ideal filters, but they have some drawbacks, such as:
  - They have a slower roll-off rate, meaning that they require a larger transition band to achieve the same attenuation as ideal filters.
  - They have a non-flat passband, meaning that they distort the frequency components in the passband by changing their magnitude.

## Gaussian filters

- Gaussian filters have a bell-shaped frequency response, meaning that they have a smooth and symmetric transition between the passband and the stopband.
- Gaussian filters have some advantages over ideal and Butterworth filters, such as:
  - They do not introduce ringing artifacts in the spatial domain, since they have a minimum phase response.
  - They are less sensitive to noise, since they attenuate the frequency components in the passband according to their magnitude.
  - They are realizable in practice, since they require finite impulse response (FIR) filters.