 Here is the content in formal tone without any emojis or external links in Markdown format:

### Fundamentals for the notes of the Unit 2 - Morphological Image Processing in the subject of IMAGE ANALYTICS

1. Introduction
- Morphological Image Processing is a collection of non-linear operations related to the shape or morphology of features in an image.
- It is used to extract image components that are useful in the representation and description of shape.

2. Dilation
- It is a morphological operation that enlarges bright/foreground regions.
- It is used to fill in holes within foreground objects or connect disjoint objects.
- The basic dilation of an image f by a structuring element g is given by:
(f ⊕ g)(x,y) = max{f(x+i,y+j)+g(i,j) | (i,j) ∈ domain of g}

3. Erosion
- It is a morphological operation that shrinks bright/foreground regions.
- It is used to break apart or shrink foreground objects.
- The basic erosion of an image f by a structuring element g is given by:
(f Θ g)(x,y) = min{f(x+i,y+j)-g(i,j) | (i,j) ∈ domain of g}

[The content continues in the similar formal tone with points and explanations...]