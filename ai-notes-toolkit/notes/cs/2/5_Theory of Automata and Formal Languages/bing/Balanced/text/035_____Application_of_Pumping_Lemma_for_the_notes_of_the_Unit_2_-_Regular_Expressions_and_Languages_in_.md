### Application of Pumping Lemma for Regular Languages

- The pumping lemma for regular languages is a theorem that states a property that all regular languages must satisfy, and can be used to prove that some languages are not regular.
- The property is that for any regular language L, there exists a constant p (called the pumping length) such that any string w in L with length at least p can be split into three substrings, w = xyz, where y is not empty, xy has length at most p, and xy<sup>i</sup>z is in L for any non-negative integer i .
- The process of repeating y zero or more times is called "pumping", and the substring y is called the "pumpable" part of w.
- The pumping lemma can be used to prove that a language is not regular by contradiction: assume that the language is regular, find a string w in the language that violates the pumping property, and conclude that the language is not regular .
- For example, consider the language L = {a<sup>n</sup>b<sup>n</sup> | n >= 0} over the alphabet {a, b}. To prove that L is not regular, we can use the following steps:
  - Assume that L is regular, and let p be the pumping length.
  - Choose a string w in L with length at least p, such as w = a<sup>p</sup>b<sup>p</sup>.
  - Split w into xyz, where y is not empty and xy has length at most p. Since xy has only a's, y must also have only a's, and we can write y = a<sup>k</sup> for some k > 0.
  - Pump y by choosing i = 2, and obtain a new string w' = xy<sup>2</sup>z = a<sup>p+k</sup>b<sup>p</sup>.
  - Observe that w' is not in L, because it has more a's than b's.
  - Contradict the assumption that L is regular, and conclude that L is not regular.