 Here is the content in markdown format for the given topic:

### Optimum Notch Filtering for IMAGE RESTORATION

- Notch filtering is a filtering technique used to remove unwanted sinusoidal components (called as noise) from a signal.
- In image restoration, notch filtering is used to remove specific frequency components (like power line interference) from the degraded image to restore it.
- The optimum notch filter has a null (zero value) at the frequency which needs to be removed and has a peak at other frequencies to produce least distortion in the signal.
- The transfer function of an optimum notch filter is given by:

H(ω) = 1 - ωn2/ω2

Where, ωn is the frequency to be removed (notch frequency)
- The above transfer function gives a null at ωn and a peak at other frequencies, thus eliminating only the required frequency component.
- This technique is easy to implement but fails if multiple frequency components need to be removed as it can remove only one particular frequency.
- Notch filtering has applications in removing power line interference, unwanted color casts, etc. from images. It gives good results if the frequency to remove is known and only one frequency needs removal.
- The key advantages are:

1. Easy and efficient to implement.
2. Causes least distortion to other frequency components.
3. Inexpensive.

The key disadvantages are:

1. Can remove only one particular frequency.
2. Performance degrades if the frequency to remove is not exactly known.
3. May not remove closely spaced multiple frequency components.

[Include diagrams/images/codes/tables etc if required]