# Using Correlation for 2-D Prototype Matching

- Correlation is a measure of similarity between two signals or images.
- Correlation can be used for pattern matching or prototype matching, which is the task of finding a given template or pattern in a larger image or signal.
- Correlation can be performed in the spatial domain or the frequency domain, depending on the efficiency and accuracy required.
- Correlation can be normalized or unnormalized, depending on the scale and intensity variations of the signals or images.
- Correlation can be linear or nonlinear, depending on the type of relationship between the signals or images.

## 2-D Correlation in the Spatial Domain

- 2-D correlation in the spatial domain is the process of sliding a template or kernel over an image and computing the correlation coefficient at each position.
- The correlation coefficient is given by the formula:

![formula](https://latex.codecogs.com/png.latex?C%28x%2Cy%29%20%3D%20%5Cfrac%7B%5Csum_%7Bi%2Cj%7D%20f%28x&plus;i%2Cy&plus;j%29t%28i%2Cj%29%7D%7B%5Csqrt%7B%5Csum_%7Bi%2Cj%7D%20f%28x&plus;i%2Cy&plus;j%29%5E2%5Csum_%7Bi%2Cj%7D%20t%28i%2Cj%29%5E2%7D%7D)

where f(x,y) is the image, t(i,j) is the template, and the summation is over the template size.

- The correlation coefficient ranges from -1 to 1, where 1 indicates a perfect match, 0 indicates no match, and -1 indicates a perfect inverse match.
- The correlation coefficient can be normalized by subtracting the mean and dividing by the standard deviation of the image and the template, to account for scale and intensity variations.
- The correlation coefficient can be plotted as a 2-D surface, where peaks indicate the locations of the best matches.

## Example: 2-D Correlation for Prototype Matching

- Suppose we want to find a prototype of a letter 'A' in an image of a text document.
- We can use the 2-D correlation in the spatial domain to perform the prototype matching.
- We can use the following steps:

  1. Read the image and the prototype using the READ_IMAGE function.
  2. Convert the image and the prototype to grayscale using the RGB2GRAY function.
  3. Normalize the image and the prototype by subtracting the mean and dividing by the standard deviation using the MEAN and STD functions.
  4. Perform the 2-D correlation using the XCORR2 function.
  5. Plot the correlation surface using the SURF function.
  6. Find the peaks of the correlation surface using the FINDPEAKS function.
  7. Mark the locations of the peaks on the image using the PLOT function.

- The code and the output are shown below:

```matlab
% Read the image and the prototype
img = read_image('text.bmp');
proto = read_image('A.bmp');

% Convert to grayscale
img = rgb2gray(img);
proto = rgb2gray(proto);

% Normalize the image and the prototype
img = (img - mean(img(:))) / std(img(:));
proto = (proto - mean(proto(:))) / std(proto(:));

% Perform the 2-D correlation
corr = xcorr2(img, proto);

% Plot the correlation surface
surf(corr);
xlabel('x');
ylabel('y');
zlabel('correlation');

% Find the peaks of the correlation surface
[peaks, locs] = findpeaks(corr(:), 'MinPeakHeight', 0.9);
[x, y] = ind2sub(size(corr), locs);

% Mark the locations of the peaks on the image
figure;
imshow(img);
hold on;
plot(y - size(proto, 2) + 1, x - size(proto, 1) + 1, 'ro');
hold off;
```

![output](output.png)