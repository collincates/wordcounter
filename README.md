!WORDCOUNTER!

Inputs a text file and returns a total count for each unique word.

E.g. with "Hello Hi Hello World Hi There":

2 Hello
2 Hi
1 World
1 There

This initial version splits a file using whitespace only.

Future changes to make:

-Ignore punctuation (started on 20180811)
-Incorporate regex  (started on 20180811)
-Create option to ignore common prepositions (in, to, on, with)
                                conjunctions (but, if, for, or)
                                determiners  (a, the, this, many)
-Take into account file encoding type.
