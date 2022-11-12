import sys
from antlr4 import *
from antlr4.tree.Trees import Trees
from new_grammarLexer import new_grammarLexer
from new_grammarParser import new_grammarParser
from new_grammarListener import new_grammarListener


class new_grammarPrintListener(new_grammarListener):
    def enterParse(self, ctx):
        if ctx.block():
            print("\n----------------------------------")
            print("Operations:\n")


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
            print("expression.")

    
    def enterAssignment(self, ctx):
        vn = ctx.value().VARNAME()
        i = ctx.value().INT()
        f = ctx.value().FLOAT()

        val = vn if vn else (i if i else (f if f else ""))
        if ctx.assop().DIVASSIGN():
            print("dividing ",end='')
            print(ctx.VARNAME(),end='')
            print(" by ",end='')
            print(val)
        if ctx.assop().MULTASSIGN():
            print("multiplying ",end='')
            print(ctx.VARNAME(),end='')
            print(" by ",end='')
            print(val)
        if ctx.assop().ADDASSIGN():
            print("adding ",end='')
            print(val,end='')
            print(" to ",end='')
            print(ctx.VARNAME())
        if ctx.assop().SUBASSIGN():
            print("subtracting ",end='')
            print(val,end='')
            print(" from ",end='')
            print(ctx.VARNAME())


    def enterPrint_out(self, ctx):
        # prints a value
        if not ctx.expression().value():
            print("printing arithmetic")
            return

        vn = ctx.expression().value().VARNAME()
        i = ctx.expression().value().INT()
        f = ctx.expression().value().FLOAT()
        
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
    print(Trees.toStringTree(tree, None, parser))
    printer = new_grammarPrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    print("\n----------------------------------\n")


if __name__ == '__main__':
    main(sys.argv)
        
