import sys
import ast
import graphviz
from antlr4 import *
from antlr4.tree.Trees import Trees
from new_grammarLexer import new_grammarLexer
from new_grammarParser import new_grammarParser
from new_grammarListener import new_grammarListener

ind = 'b'

class new_grammarPrintListener(new_grammarListener):
    def enterParse(self, ctx):
        if ctx.block():
            print("\n----------------------------------")
            print("Operations:\n")


    def enterAssignment(self, ctx):
        expr = ctx.expression()
        val = "boolean"
        if expr:
            a = expr.arith()
            val = "arithmetic" if a else val
        
        if expr and expr.value():
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



def r_get_nodes(s, parent = 'a', node = None, depth = 0):
    global ind

    rets = get_nodes(s)

    arr = rets[0]
    types = rets[1]
    length = len(arr)

    print("---------------------")
    print(arr)
    print("---------------------")


    if depth == 0:
        print("initializing")
        node = graphviz.Digraph(comment = "parse tree visualization")
        node.node('a', "root")
        r_get_nodes(arr[0], 'a', node, 1)

    for i in range(length):
        if types[i] == 0:
            self_val = ind
            ind = chr(ord(ind) + 1)
            if i < length-1:
                # if next is a parenthesised
                if types[i+1] == 1:
                    print("expanding")
                    node.node(self_val, arr[i])
                    node.edge(parent, self_val)
                    r_get_nodes(arr[i+1], self_val, node, 1)
                else:
                    print("adding")
                    node.node(self_val, arr[i])
                    node.edge(parent, self_val)
            else:
                print("adding last")
                node.node(self_val, arr[i])
                node.edge(parent, self_val)

    if depth == 0:
        node.render('doctest-output/round-table.gv', view=True)
        #print(node)



def get_nodes(s):
    arr = []
    types = [] # 0 is literal, 1 is commands
    f = True
    while(f):
        p = s.find('(')
        space = s.find(' ')
        if p < space and not p == -1:
            if s[p+1] == ' ':
                # still need to test
                arr.append("(")
                types.append(0)
                continue;
            else:
                substr = strip_parenthesis(s)
                arr.append(substr)
                types.append(1)
                s = s[len(substr)+2:] #+1?
        elif not space == -1:
            substr = s[:space]
            if substr:
                arr.append(substr)
                types.append(0)
            s = s[space+1:]
        else:
            if s:
                arr.append(s)
                types.append(0)
            f = False
    return [arr, types]


def strip_parenthesis(s):
    rparen = s.find('(')
    if rparen == -1:


        return ""
    t = s[rparen+1:]
    num = 1
    while num > 0:
        r = t.find('(')
        l = t.find(')')
        # if theres a right parenthesis
        if r < l and not r == -1:
            t = t[r+1:]
            num = num + 1
        elif not l == -1:
            t = t[l+1:]
            num = num - 1
        else:
            print("error")

    lparen = s.rfind(t)

    if s[rparen+1:lparen-1]:
        return s[rparen+1:lparen-1]
    else:
        print("error")




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
    r_get_nodes(Trees.toStringTree(tree, None, parser))

    
if __name__ == '__main__':
    main(sys.argv)
        
