 Here is the content written in Markdown format for the topic "Band pass Filters" under the notes of Unit 3 - IMAGE RESTORATION in the subject of Image Processing:

### Band pass Filters

- Band pass filters allow only a certain band of frequencies to pass through and attenuate frequencies outside the selected band.
- They are used to filter out noise from an image by allowing the frequencies of the signal (image) to pass while suppressing the frequencies of noise.
- The two parameters that characterize a band pass filter are -
	- Lower cut-off frequency (Flower) - Frequencies below this will be attenuated.
	- Upper cut-off frequency (Fupper) - Frequencies above this will be attenuated.
- The pass band is the range of frequencies between Flower and Fupper that are allowed to pass through.
- Types of Band pass filters:
	- Butterworth filter - Has a maximally flat pass band (linear phase response) but the roll-off is slow.
	- Chebyshev filter - Has a faster roll-off than Butterworth filter but the pass band is not maximally flat.
	- Elliptic filter - Has the fastest roll-off but the pass band ripples the most.

**Advantages:**
- Effective in noise removal as they can separate the signal frequencies from the noise frequencies.
- Can be designed with varying and controllable pass bands and roll-off rates based on the application.

**Disadvantages:**
- May distort the signal if not designed properly as they attenuate frequencies outside the pass band.
- Require precise specifications of pass band and roll-off which may not always be possible.

**Examples:** Band pass filters are used in -
- Radar systems
- Medical imaging
- Seismic data processing
- Speech processing

[Detailed diagrams and examples can be added here for more clarity.]