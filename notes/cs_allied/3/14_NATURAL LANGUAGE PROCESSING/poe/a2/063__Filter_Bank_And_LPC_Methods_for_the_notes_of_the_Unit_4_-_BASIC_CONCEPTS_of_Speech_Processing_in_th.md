 Here is the content in Markdown format without any emojis or external links and in a formal tone:

### Filter-Bank And LPC Methods

#### Filter-Bank Method

- Speech signal is passed through a bank of filters that divide the spectrum into frequency bands.
- The output of each filter is then squared and integrated over a short time interval to get the energy in each frequency band.
- The pattern of energies in the frequency bands is used as a spectral representation of the speech signal.
- This method is simple but the frequency resolution is limited by the number of filters used.

#### Linear Predictive Coding (LPC)

- The speech signal is modeled as the output of an all-pole filter.
- The parameters of the all-pole filter are estimated to minimize the difference between the actual speech signal and the modeled signal.
- The all-pole filter has a transfer function of the form 1/A(z) where A(z) is a polynomial in z.
- The coefficients of the polynomial A(z) provide a spectral representation of the speech signal.
- LPC provides a good spectral representation of the speech signal with a small number of parameters.

The above points cover the key features and steps involved in the Filter-Bank and LPC methods for spectral representation of speech signals as a part of the Basic Concepts of Speech Processing. The methods are written about in a formal tone with points and without any emojis or links for the purpose of study material for exams. Please let me know if you would like me to elaborate on any of the points or modify the content in any way.