### Image Negatives

- An image negative is a photographic image that reproduces the bright portions of the photographed subject as dark and the dark parts as light areas .
- Image negatives are usually formed on a transparent material, such as plastic or glass.
- A negative color image is additionally color-reversed, with red areas appearing cyan, greens appearing magenta, and blues appearing yellow, and vice versa.
- Image negatives can be produced by subtracting each pixel from the maximum intensity value.
- For example, for an 8-bit image, the max intensity value is 2^8^ – 1 = 255, thus each pixel is subtracted from 255 to produce the output image.
- The transformation function used in image negative is:

```
s = L - 1 - r
```

where s is the output pixel value, L is the maximum intensity value, and r is the input pixel value.

- Here is an example of an image and its negative:
