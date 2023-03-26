 Here is the content in Markdown format without any emojis or external links:

### Moment Invariants for the notes of the Unit 4 - Feature Extraction in the subject of IMAGE ANALYTICS

1. Moment Invariants: Moment invariants are certain functions of the moments of a shape. They have the property of invariance under scaling, translation and rotation. This property makes them useful for shape recognition and classification.
2. Central Moments: The (p+q)th central moment μpq of a 2D shape is defined as:
μpq = ∑∑(x - x̅)(y - y̅)p yq f(x, y) dxdy
Where (x̅, y̅) is the centroid of the shape. The central moments are translation invariant.
3. Seven Hu Invariants: Hu proposed a set of seven invariants (functions of central moments) that are also scale and rotation invariant. They are given by:
η1 = μ20 + μ02
η2 = (μ20 - μ02)2 + 4μ11μ10
η3 = (μ30 - 3μ12)2 + (3μ21 - μ03)2
η4 = (μ30 + μ12)2 + (μ03 + μ21)2
η5 = (μ30 - 3μ12)(μ30 + μ12)[(μ30 + μ12)2 - 3(μ21 + μ03)2]
η6 = (μ20 - μ02)[(μ30 + μ12)2 - (μ03 + μ21)2]
η7 = (3μ21 - μ03)(μ30 + μ12)[3(μ30 + μ12)2 - (μ03 + μ21)2]

4. Applications: Moment invariants are used for:
- Shape recognition and classification. The invariant properties enable matching shapes without regard to translation, scale and rotation.
- Object recognition in images. The moments of an object can be used as features to recognize the object in an image.
- Texture analysis. The moments of the gray level co-occurrence matrix can be used as texture features.