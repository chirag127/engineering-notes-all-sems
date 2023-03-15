### Notch Filters for the notes of the Unit 3 - IMAGE RESTORATION in the subject of Image Processing

- A notch filter is an image processing filter that is used to remove specific frequency components from an image.
- A notch filter is a type of band-stop filter that is designed to remove a specific range of frequencies from an image while leaving the rest of the image unaffected.
- A notch filter can be used to remove periodic noise or unwanted patterns from an image .
- A notch filter can be implemented in the frequency domain by multiplying the Fourier transform of the image by a notch filter function .
- A notch filter function can be designed using different methods, such as ideal, Butterworth, or Gaussian .
- An ideal notch filter function is a binary function that has a value of zero at the frequencies to be removed and a value of one elsewhere.
- A Butterworth notch filter function is a continuous function that has a smooth transition from zero to one at the frequencies to be removed.
- A Gaussian notch filter function is a continuous function that has a bell-shaped curve at the frequencies to be removed.
- The choice of the notch filter function depends on the trade-off between the sharpness of the frequency response and the ringing artifacts in the spatial domain.
- A notch filter can be applied to multiple frequency bands by using a combination of notch filter functions .
- A notch filter can be adaptive to the local frequency characteristics of the image by using a variable notch width.
- A notch filter can be improved by using a notch reject filter, which is a complementary filter that passes the frequencies to be removed and rejects the rest.