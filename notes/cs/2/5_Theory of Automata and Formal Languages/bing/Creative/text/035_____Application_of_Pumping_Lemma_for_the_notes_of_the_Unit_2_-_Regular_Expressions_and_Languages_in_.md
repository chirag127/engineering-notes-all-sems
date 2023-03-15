### Application of Pumping Lemma for Regular Languages

- The pumping lemma for regular languages is a theorem that describes an essential property of all regular languages .
- Informally, it says that all sufficiently long words in a regular language may be pumped —that is, have a middle section of the word repeated an arbitrary number of times—to produce a new word that also lies within the same language.
- Formally, it says that for any regular language L, there exists a constant p (pumping length) >= 1 such that for every string STR in L with length of STR >= p, STR can be written as STR = XYZ, where:
  - Y is not null / empty string
  - Length of XY <= p
  - For all i >= 0, XY<sup>i</sup>Z is a part of L
- The pumping lemma is often used to prove that a particular language is non-regular: a proof by contradiction may consist of exhibiting a string (of the required length) in the language that lacks the property outlined in the pumping lemma.
- For example, the language L = {a<sup>n</sup>b<sup>n</sup> : n >= 0} over the alphabet Σ = {a, b} can be shown to be non-regular as follows:
  - Assume L is regular and let p be the pumping length.
  - Choose the string STR = a<sup>p</sup>b<sup>p</sup> which is in L and has length 2p >= p.
  - By the pumping lemma, STR can be written as STR = XYZ, where Y is not empty, XY has length at most p, and XY<sup>i</sup>Z is in L for all i >= 0.
  - Since XY has length at most p, it must consist of only a's, so Y = a<sup>k</sup> for some k > 0.
  - Then, XY<sup>2</sup>Z = a<sup>p+k</sup>b<sup>p</sup>, which is not in L, since it has more a's than b's.
  - This contradicts the pumping lemma, so L is not regular.