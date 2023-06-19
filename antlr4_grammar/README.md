## How to run ANTLR4 locally?
Run this commad:
```
antlr4 -encoding utf8 -Dlanguage=Python3 DebateGrammarLexer.g4 DebateGrammarParser.g4  & antlr4-parse DebateGrammarLexer.g4 DebateGrammarParser.g4 start -gui -encoding utf8 debate.txt
 ```
---