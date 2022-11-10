import sys
from antlr4 import *
from new_grammarLexer import new_grammarLexer
from new_grammarParser import new_grammarParser
from new_grammarListener import new_grammarListener



class new_grammarPrintListener(new_grammarListener):
    def enterParse(self, ctx):
        print("> %s" % ctx.block())



def main(argv):


    lexer = new_grammarLexer(StdinStream())
    tokens = CommonTokenStream(lexer)
    parser = new_grammarParser(tokens)
    tree = parser.parse()
    printer = new_grammarPrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)


if __name__ == '__main__':
    main(sys.argv)
        
