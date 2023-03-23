 Here are the notes for Liang Barsky algorithm in Markdown format:

### Liang Barsky algorithm

Liang Barsky algorithm is used to clip a line segment against a rectangle (viewport) and determine if the line segment is visible or not.

- It accepts the co-ordinates of the line segment endpoints and the co-ordinates of the viewport rectangle.
- It works by determining if either of the endpoints lies inside the viewport. If yes, the line segment is fully visible.
- If not, it calculates and compares the parameters `t1` and `t2` to check if the line segment intersects the viewport.
- `t1` and `t2` are calculated using the following conditions:

$$
t_1 = \frac{p_1 − q_1}{p_2 − p_1} \\
t_2 = \frac{p_3 − q_2}{p_4 − p_3}
$$

Where `p1`, `p2`, `p3` and `p4` are the co-ordinates of the viewport edges and `q1` and `q2` are the co-ordinates of the line segment endpoints.
- If `0 <= t1 <= 1` and `0 <= t2 <= 1`, the line segment intersects the viewport and is visible.
- If not, the line segment lies completely outside the viewport.

This is how the Liang Barsky algorithm clips a line segment against a rectangle and determines its visibility.