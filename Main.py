import sys
import ast
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


    def enterAssignment(self, ctx):
        expr = ctx.expression()
        val = "boolean"
        a = expr.arith()
        val = "arithmetic" if a else val
        
        if expr.value():
            vn = expr.value().VARNAME()
            i = expr.value().INT()
            f = expr.value().FLOAT()
            val = "value" if vn else ("INT" if i else ("FLOAT" if f else val))

        if ctx.assop().ASSIGN():
            print("declaring ",end='')
            print(ctx.VARNAME(),end='')
            print(" as ",end='')
            print(val)
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
        
