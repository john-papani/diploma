## How to run ANTLR4 locally?
Run this commad:
```
antlr4 -encoding utf8 -Dlanguage=Python3 DebateGrammarLexer.g4 DebateGrammarParser.g4  & antlr4-parse DebateGrammarLexer.g4 DebateGrammarParser.g4 start -gui -encoding utf8 debate.txt
 ```
---

### Known Bugs _(DebateGrammar.g4)_
- [x] Στα Θέματα δεν γίνονται parser, οι 'προτάσεις' που δεν ξεκινάνε με enumeration (1,2,3 / α,β,γ / i,ii,iii).
`3. Κατάθεση σχεδίου νόμου:`
_`Οι Υπουργοί Εξωτερικών, Οικονομικών, Ανάπτυξης και Επενδύσεων, Προστασίας του Πολίτη, ...`_

- [x]  Στους ομιλητές  πρέπει να υπάρχει το `, σελ` 