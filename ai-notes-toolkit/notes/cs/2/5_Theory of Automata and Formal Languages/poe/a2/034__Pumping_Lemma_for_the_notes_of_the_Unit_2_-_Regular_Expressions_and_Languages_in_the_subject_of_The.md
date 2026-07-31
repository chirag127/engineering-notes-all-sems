 Here is the content in markdown format without any emojis or external links and in a formal tone:

### Pumping Lemma

* Pumping Lemma states that if a language L is regular, then there exists a number p such that any string w in L of length at least p can be "pumped" (repeating/stretching) to generate a new string of larger length that is also in L.
* Formally, if L is regular, then there exists p >= 0 such that for all w in L where |w| >= p, there exist strings x, y, z such that:
** w = xyz
** |xy| <= p
** For all i >= 0, xyy^iz is in L
* The pumping length p depends only on the regular language L and not on the particular string w.
* Pumping Lemma is used to prove that a language is not regular by assuming it is regular and arriving at a contradiction. If a language does not satisfy the Pumping Lemma, then it is not regular.
* For example, the language {ww: w is in {a,b}*} containing double occurrences of strings is not regular as the pumping length p would have to depend on the string w.

* Key points:
** Pumping Lemma is used to prove non-regularity
** It states that sufficiently long strings in a regular language can be pumped to get longer strings in the same language
** The pumping length p is independent of the string and depends only on the language
** Languages not satisfying the Pumping Lemma are not regular