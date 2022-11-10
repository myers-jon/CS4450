import sys
from antlr4 import *
from new_grammarLexer import new_grammarLexer
from new_grammarParser import new_grammarParser
from new_grammarListener import new_grammarListener


class new_grammarPrintListener(new_grammarListener):
    def enterParse(self, ctx):
        if ctx.block():
            print("\n----------------------------------")
            print("Parse Successful!\n")
            print("Operations:")


    def enterDefinition(self, ctx):
        print(ctx.VARNAME(), end='')
        print(" defined as ", end='')
        val = ctx.expression().value()
        vartype = "-"
        varvalue = "-"

        if val:
            print("value. ", end='')
            if val.VARNAME():
                vartype = "varname"
                varvalue = val.VARNAME()
            if val.INT():
                vartype = "int"
                varvalue = val.INT()
            if val.FLOAT():
                vartype = "float"
                varvalue = val.FLOAT()
            print("vartype: ", end='')
            print(vartype, end='')
            print(", value: ",end='')
            print(varvalue)
        else:
            print("expression. ", end='')


    def enterPrint_out(self, ctx):
        # prints a value
        vn = ctx.value().VARNAME()
        i = ctx.value().INT()
        f = ctx.value().FLOAT()
        
        if vn: 
            print("printing varname: ", end='')
            print(vn)
        elif i:
            print("printing int: ", end='')
            print(i)
        elif f:
            print("printing float: ", end='')
            print(f)



def main(argv):

    lexer = new_grammarLexer(StdinStream())
    tokens = CommonTokenStream(lexer)
    parser = new_grammarParser(tokens)
    parser.errorHandler = BailErrorStrategy()
    tree = parser.parse()
    printer = new_grammarPrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)


if __name__ == '__main__':
    main(sys.argv)
        
