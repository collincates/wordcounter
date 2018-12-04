<h2>WORDCOUNTER!</h2>
<hr />
Inputs a text file and returns a total count for each unique word.
Either prints to shell or writes to a file depending on if
`display()` or `write_to_file()` are used.

E.g. with a file containing "Hello Hi Hello World Hi There":

`2 Hello`

`2 Hi`

`1 World`

`1 There`

<hr />
<h4>Future changes to make:</h4>

-Ignore punctuation

-Incorporate regex

-Create option to ignore common
<ul>
    <li>prepositions `(in, to, on, with)`</li>
    <li>conjunctions `(but, if, for, or)`</li>
    <li>determiners  `(a, the, this, many)`</li>
</ul>
-Take into account file encoding type.
