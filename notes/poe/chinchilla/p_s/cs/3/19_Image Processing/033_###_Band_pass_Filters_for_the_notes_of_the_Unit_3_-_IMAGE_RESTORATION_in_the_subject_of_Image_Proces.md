### Band pass Filters for the notes of the Unit 3 - IMAGE RESTORATION in the subject of Image Processing

In image processing, restoration is one of the most important tasks. It involves the removal of noise and other distortions that may have occurred during image capture or transmission. Band pass filters are one of the widely used filters for image restoration. Let's learn more about band pass filters in detail:

#### What are Band pass Filters?
Band pass filters are a type of filter used in signal processing that allows a certain range of frequencies to pass through while filtering out the remaining frequencies. In image processing, band pass filters are used to remove noise and other distortions from images that are located in a certain frequency range.

#### Types of Band pass Filters:
There are two types of band pass filters that are commonly used in image processing:

- Ideal Band pass Filter
- Butterworth Band pass Filter

#### Ideal Band pass Filter:
The ideal band pass filter is a theoretical filter that passes all frequencies within a certain range and blocks all other frequencies. It is also known as a rectangular filter because the frequency response of this filter looks like a rectangle.

#### Butterworth Band pass Filter:
The Butterworth band pass filter is a more practical filter than the ideal filter. It attenuates frequencies outside the passband and has a smooth transition between the passband and stopband. It is named after its inventor Stephen Butterworth.

#### Advantages of Band pass Filters:
- Band pass filters are useful in removing noise and other distortions that may have occurred during image capture or transmission.
- They are relatively easy to implement and can be used in real-time applications.
- Band pass filters can be used to extract specific frequency bands from an image.

#### Disadvantages of Band pass Filters:
- Band pass filters can remove important image details along with noise and distortions.
- The selection of the appropriate frequency range for the filter can be a challenging task.

#### Applications of Band pass Filters:
- Band pass filters are widely used in image restoration tasks.
- They can be used in medical imaging to enhance certain features of an image such as blood vessels or tumors.
- They can be used in image analysis to extract specific features from an image.

#### Example of Band pass Filter:
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Generate a test image
image = np.zeros((256, 256))
image[100:150, 100:150] = 255

# Define the band pass filter
low = 10
high = 50
order = 2
b, a = signal.butter(order, [low, high], btype='bandpass')

# Apply the filter to the image
filtered_image = signal.filtfilt(b, a, image)

# Plot the original and filtered images
fig, ax = plt.subplots(1, 2, figsize=(10, 5))
ax[0].imshow(image, cmap='gray')
ax[0].set_title('Original Image')
ax[1].imshow(filtered_image, cmap='gray')
ax[1].set_title('Filtered Image')
plt.show()
```

#### Conclusion:
Band pass filters are an important tool in image restoration tasks. They allow the extraction of specific frequency ranges from an image, which can be useful in removing noise and other distortions. However, the selection of the appropriate frequency range can be a challenging task, and it is important to carefully consider the trade-off between noise removal and the preservation of important image details.