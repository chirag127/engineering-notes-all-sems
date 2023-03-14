 Here is the content in markdown format:

### Filter-Bank And LPC Methods for the notes of the Unit 5 - BASIC CONCEPTS of Speech Processing in the subject of Natural Language Processing

Filter-bank method:
- Speech signal is passed through a bank of filters that divide the frequency spectrum into narrow bands.
- The output of each band-pass filter is rectified and integrated to get the energy of the signal in that band.
- These energies or amplitudes are then sampled to get spectral envelope of the speech signal.

LPC Method:
- In LPC method, the speech signal is modeled as the output of an all-pole filter excited by a periodic impulse train (for voiced speech) or noise (for unvoiced speech).
- The coefficients of the all-pole filter are calculated such that the difference between the actual speech signal and the reproduced speech signal is minimized in a least square sense.
- The all-pole filter thus models the spectral envelope of speech and its coefficients track the changes in the speech spectrum over time.

Advantages:
- Filter-bank method is simple and easy to implement.
- LPC method produces a more accurate replica of the spectral envelope.

Disadvantages:
- Filter-bank method gives a crude spectral envelope.
- LPC method is complex and computationally intensive.

Applications:
- Both methods are used to extract features from speech signal for speech recognition, speaker recognition, emotion recognition, etc.
- The spectral envelope obtained can be used to synthesize speech.

Mnemonics:
- For filter-bank: Think of bank of filters dividing frequency spectrum into bands.
- For LPC: Think of an all-pole filter whose coefficients minimize error between actual and reproduced speech.