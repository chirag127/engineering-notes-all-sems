### Ideal, Butterworth and Gaussian filters

- Filters are used to enhance or modify images in the frequency domain by attenuating or amplifying certain frequency components.
- Ideal, Butterworth and Gaussian filters are three types of filters that differ in their transfer functions and their effects on the image.
- Ideal filter: A filter that has a sharp cutoff at a specified cutoff frequency, and passes or blocks all frequencies above or below the cutoff frequency. It is also called a brick-wall filter.
- Butterworth filter: A filter that has a smooth transition between the passband and the stopband, and has a maximum flat response in the passband. It is characterized by an order parameter that controls the steepness of the transition. A low order Butterworth filter is close to a Gaussian filter, and a high order Butterworth filter is close to an ideal filter.
- Gaussian filter: A filter that has a bell-shaped transfer function that decreases exponentially from the center frequency. It has no ringing artifacts, but it also has a slow rolloff in the frequency domain.

- Some examples of these filters are:

  - Low-pass filter: A filter that passes low frequencies and blocks high frequencies. It can be used to smooth or blur an image by removing high-frequency noise or details.
  - High-pass filter: A filter that passes high frequencies and blocks low frequencies. It can be used to sharpen or enhance an image by emphasizing high-frequency edges or details.
  - Band-pass filter: A filter that passes a band of frequencies and blocks frequencies outside the band. It can be used to isolate or extract certain frequency components from an image.

- The following figures show the perspective 3D plots of ideal, Butterworth and Gaussian low-pass and high-pass filters, respectively:

  - Ideal low-pass filter (ILPF):

    ```
    ![ILPF](https://biomedpharmajournal.org/wp-content/uploads/2015/12/fig20.jpg)
    ```

  - Butterworth low-pass filter (BLPF):

    ```
    ![BLPF](https://biomedpharmajournal.org/wp-content/uploads/2015/12/fig21.jpg)
    ```

  - Gaussian low-pass filter (GLPF):

    ```
    ![GLPF](https://biomedpharmajournal.org/wp-content/uploads/2015/12/fig22.jpg)
    ```

  - Ideal high-pass filter (IHPF):

    ```
    ![IHPF](https://biomedpharmajournal.org/wp-content/uploads/2015/12/fig23.jpg)
    ```

  - Butterworth high-pass filter (BHPF):

    ```
    ![BHPF](https://biomedpharmajournal.org/wp-content/uploads/2015/12/fig24.jpg)
    ```

  - Gaussian high-pass filter (GHPF):

    ```
    ![GHPF](https://biomedpharmajournal.org/wp-content/uploads/2015/12/fig25.jpg)
    ```

- The advantages and disadvantages of these filters are:

  - Ideal filter: It has a simple and clear design, but it introduces ringing artifacts (Gibbs phenomenon) in the spatial domain due to the discontinuities in the frequency domain. It is also not realizable in practice.
  - Butterworth filter: It has a smooth and flat response in the passband, and it avoids ringing artifacts. However, it has a slower rolloff than the ideal filter, and it may introduce some blurring or distortion in the image.
  - Gaussian filter: It has a smooth and exponential response in the frequency domain, and it preserves the image shape and continuity. However, it has a very slow rolloff, and it may attenuate some useful frequency components in the image.