#glyphs

An imaginary system of glyphs I wanted to prototype.  Might use it for a game in the future.  

Each glyph is made up of a grid of 3 by 3 squares, which can be be separated or joined with any adjacent square.  There are 12 different joining points (diagonals don't count), giving a grand total of 2^12 = 4096 different unique symbols.  

These symbols are highly dependent on their orientation to determine their meaning (if they ever get assigned one).  If we wanted more flexibility in use (and more difficulty in programming a way to generate them) we could throw out 3/4 of them to remove rotationally symmetric dublicates.  This would leave us with 1024 total glyphs.  

Either way there's enough symbols to form a rudimentary [logography.](https://en.wikipedia.org/wiki/Logogram)  I intended to pseudorandomly encode the n most common english words (or maybe just nouns, adjectives, and verbs?) into these symbols, with a separate system corresponding to the latin alphabet for words not contained within the n most common list.  

[Here](https://raw.githubusercontent.com/koneill1994/glyphs/master/all_possible.png) is a chart of all possible glyphs.  

![Looks a bit like a geometric Maya script](https://raw.githubusercontent.com/koneill1994/glyphs/master/test.png)
