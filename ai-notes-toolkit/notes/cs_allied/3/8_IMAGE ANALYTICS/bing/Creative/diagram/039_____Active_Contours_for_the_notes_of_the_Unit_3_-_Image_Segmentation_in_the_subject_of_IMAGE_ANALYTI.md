### Active Contours for the notes of the Unit 3 - Image Segmentation in the subject of IMAGE ANALYTICS

- Active contours, also known as snakes, are a technique for image segmentation that uses iterative region-growing algorithms  .
- The main idea of active contours is to specify initial curves on an image and then evolve them towards the object boundaries by minimizing an energy function .
- The energy function consists of two terms: internal energy and external energy.
- The internal energy term controls the smoothness and continuity of the curves, while the external energy term attracts the curves to the image features, such as edges, corners, or intensity gradients.
- The active contour model can be formulated as a variational problem, a partial differential equation, or a level set method.
- The advantages of active contours are that they can handle complex shapes, adapt to image noise and occlusion, and incorporate prior knowledge and constraints .
- The disadvantages of active contours are that they require manual initialization, are sensitive to local minima, and are computationally expensive .
- Some applications of active contours are object tracking, shape recognition, medical image analysis, and image editing  .

: https://www.mathworks.com/help/images/ref/activecontour.html
: https://www.analyticsvidhya.com/blog/2021/09/active-contours-a-method-for-image-segmentation-in-computer-vision/
: https://www.intechopen.com/chapters/59741
: https://arxiv.org/abs/1909.13359
: https://en.wikipedia.org/wiki/Active_contour_model