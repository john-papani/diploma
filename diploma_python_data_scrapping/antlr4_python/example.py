from antlr4 import *
import graphviz
from DebateGrammarLexer import DebateGrammarLexer
from DebateGrammarParser import DebateGrammarParser
from antlr4.tree.Trees import Trees

# Create a stream of tokens from the input document
input_stream = FileStream('debate.txt', encoding='utf-8')
lexer = DebateGrammarLexer(input_stream)
token_stream = CommonTokenStream(lexer)

# Create a parser and parse the input document
parser = DebateGrammarParser(token_stream)
tree = parser.start()
print(tree.toStringTree())
print(tree)

# viewer = TreeViewer(["rule name", "token name"])
# viewer.setTree(tree)
# viewer.open()   
# Traverse the parse tree and extract the speaker and text from each statement
# for statement in tree.all():
#     speaker = statement.table_of_contents().getText().strip(':')
#     subject_item = statement.subject_item().getText()
#     print(r'{subject_item}')
