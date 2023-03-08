 Here is the content in markdown format for the given topic:

### Composite transformations for the notes of the Unit 2 - Transformations in Computer Graphics

Composite transformations refer to applying more than one transformation on an object sequentially to get the desired transformed output. The transformations can be applied in any order and the final outcome will be the combined effect of all the transformations.

For example:
1. Translating an object followed by rotating it.
2. Scaling an object followed by translating it.
3. Rotating an object followed by reflecting it.

The order of transformations matters in composite transformations. For example, rotating an object followed by translating it will give a different output than translating the object first followed by rotating it.

The composite transformation can be represented mathematically by multiplying the individual transformation matrices. The multiplication order is same as the order of applying the transformations.

Advantages:
- Composite transformations provide more flexibility to transform objects as per the requirements.
- They enable creating complex transformations by combining simple transformations.

Disadvantages:
- The order of transformations matters which can sometimes lead to confusion or unwanted outputs if not carefully handled.
- Calculating the composite transformation matrix manually for complex transformations can be tedious and error-prone. Programming tools can be used to handle composite transformations to avoid these issues.

Examples:
- Rotate an object by 30?? around X-axis, then translate it by (5, 3)
- Scale an object by (2, 1.5), then reflect it along Y-axis
- Translate an object to the origin, then rotate and scale it, then translate back to the original position.

Applications:
- Rendering 3D scenes using transformations.
- Image processing techniques like rotating, scaling and translating images.
- Creating animated graphics with smooth transition effects using composite transformations.