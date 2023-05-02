## How to run ANTLR4 locally?
Run this commad:
```
antlr4 -encoding utf-8 -Dlanguage=Python3 DebateGrammar.g4 & antlr4-parse DebateGrammar.g4 start -gui -encoding utf8 debate.txt 
 ```
---

### Known Bugs _(DebateGrammar.g4)_
1. Στα Θέματα δεν γίνονται parser, οι 'προτάσεις' που δεν ξεκινάνε με enumeration (1,2,3 / α,β,γ / i,ii,iii).
`3. Κατάθεση σχεδίου νόμου:`
_`Οι Υπουργοί Εξωτερικών, Οικονομικών, Ανάπτυξης και Επενδύσεων, Προστασίας του Πολίτη, ...`_

2. Στους ομιλητές ~~ΔΕΝ ΘΑ~~ πρέπει να υπάρχει το `, σελ`