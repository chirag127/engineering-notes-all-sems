### Hit or Miss Transform

- Hit or miss transform is a morphological operation that detects a given configuration or pattern in a binary image, using the morphological erosion operator and a pair of disjoint structuring elements  .
- A structuring element is a small binary image that defines the shape and size of the region of interest for the morphological operation.
- A disjoint pair of structuring elements means that one structuring element is the complement of the other, i.e., the foreground pixels of one are the background pixels of the other.
- The hit or miss transform can be defined as follows :

  - Let A be the input binary image and B be the composite structuring element, which consists of two disjoint structuring elements B1 and B2.
  - The hit or miss transform of A by B is given by: `A ⊗ B = (A ⊖ B1) ∩ (Ac ⊖ B2)`, where `⊗` is the hit or miss operator, `⊖` is the erosion operator, `∩` is the intersection operator, and `Ac` is the complement of A.
  - The hit or miss transform indicates the positions where the pattern characterized by B occurs in the input image A.
  - The hit or miss transform can be implemented using the OpenCV function `cv::morphologyEx` with the flag `cv::MORPH_HITMISS`.

- The hit or miss transform can be used for various applications, such as:

  - Pruning: identifying and removing the end-points of a line to eliminate unwanted branches.
  - Thinning: iteratively removing the boundary pixels of a region to obtain a skeleton.
  - Thickening: iteratively adding pixels to the boundary of a region to obtain a thicker shape.
  - Corner detection: finding the locations where two edges meet at an angle.

- An example of the hit or miss transform is shown below:

  - Input image:

    ```
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 1 1 1 0 0 0
    0 0 0 1 1 1 1 1 0 0
    0 0 1 1 1 1 1 1 1 0
    0 0 1 1 1 1 1 1 1 0
    0 0 0 1 1 1 1 1 0 0
    0 0 0 0 1 1 1 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    ```

  - Composite structuring element B:

    ```
    B1:     B2:
    0 0 0   1 1 1
    0 1 0   1 0 1
    0 0 0   1 1 1
    ```

  - Hit or miss transform of the input image by B:

    ```
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 1 0 0 0 0 0
    0 0 0 1 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0

```
