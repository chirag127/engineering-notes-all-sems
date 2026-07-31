# The Burrows-Wheeler Transform

The Burrows-Wheeler Transform (BWT) is an algorithm that rearranges a string of characters into runs of similar characters. This is useful for data compression, since it tends to be easy to compress a string that has runs of repeated characters by techniques such as move-to-front transform and run-length encoding .

The BWT is based on a reversible permutation of the characters of a string, which is obtained by sorting all the cyclic rotations of the string lexicographically and taking the last column of the sorted matrix  .

For example, the BWT of the string "banana" is obtained as follows:

1. Append a special symbol, such as "$", to the end of the string to mark the end of the string and to ensure that the symbol is lexicographically smaller than any other character in the string. The string becomes "banana$".
2. Generate all the cyclic rotations of the string by shifting the characters one by one to the left and wrapping around the last character to the beginning. The cyclic rotations are:

```
banana$
anana$b
nana$ba
ana$ban
na$bana
a$banan
$banana
```

3. Sort the cyclic rotations lexicographically (alphabetically) and form a matrix with each rotation as a row. The sorted matrix is:

```
$banana
a$banan
ana$ban
anana$b
banana$
na$bana
nana$ba
```

4. Take the last column of the matrix as the BWT of the string. The last column is "annb$aa", which is the BWT of "banana$".

The BWT can be reversed by using the fact that the first column of the sorted matrix is the same as the sorted BWT, and that each character in the BWT corresponds to a unique character in the first column by following the same cyclic order .

For example, to reverse the BWT of "annb$aa", we can do the following:

1. Sort the BWT lexicographically and form the first column of the matrix. The first column is "$aaaaabn".
2. Pair each character in the BWT with the corresponding character in the first column by following the same cyclic order. For example, the first "a" in the BWT corresponds to the first "a" in the first column, the second "a" in the BWT corresponds to the second "a" in the first column, and so on. The pairs are:

```
a - $
n - a
n - a
b - a
$ - a
a - b
a - n
```

3. Sort the pairs lexicographically by the first element and form the second column of the matrix. The second column is "a$aaabn".
4. Repeat steps 2 and 3 until the matrix is complete. The complete matrix is:

```
$ - a - n - a - n - a - $
a - $ - a - a - a - b - n
a - a - $ - b - a - n - a
a - a - a - n - a - $ - b
a - b - a - n - a - n - $
b - n - a - $ - a - a - a
n - a - a - a - b - $ - a
```

5. Find the row that ends with the special symbol "$" and take the rest of the row as the original string. The row that ends with "$" is the first row, and the rest of the row is "banana", which is the original string.

The BWT has some properties that make it suitable for data compression, such as:

- The BWT tends to group similar characters together, which makes it easier to apply other compression techniques such as move-to-front transform and run-length encoding .
- The BWT preserves the relative order of the characters in the original string, which makes it possible to reverse the transformation without any additional information .
- The BWT is independent of the alphabet size and the frequency distribution of the characters, which makes it adaptable to different types of data .

The BWT is the basis of some popular compression algorithms, such as bzip2 and FM-index. The BWT can also be