import sys
from antlr4 import *
from new_grammarLexer import new_grammarLexer
from new_grammarParser import new_grammarParser

def main(argv):

    lexer = new_grammarLexer("var = 3")
    tokens = CommonTokenStream(lexer)
    parser = new_grammarParser(tokens)
    tree = parser.prog()
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main(sys.argv)
        
