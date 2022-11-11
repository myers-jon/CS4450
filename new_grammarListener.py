# Generated from new_grammar.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .new_grammarParser import new_grammarParser
else:
    from new_grammarParser import new_grammarParser

# This class defines a complete listener for a parse tree produced by new_grammarParser.
class new_grammarListener(ParseTreeListener):

    # Enter a parse tree produced by new_grammarParser#parse.
    def enterParse(self, ctx:new_grammarParser.ParseContext):
        pass

    # Exit a parse tree produced by new_grammarParser#parse.
    def exitParse(self, ctx:new_grammarParser.ParseContext):
        pass


    # Enter a parse tree produced by new_grammarParser#block.
    def enterBlock(self, ctx:new_grammarParser.BlockContext):
        pass

    # Exit a parse tree produced by new_grammarParser#block.
    def exitBlock(self, ctx:new_grammarParser.BlockContext):
        pass


    # Enter a parse tree produced by new_grammarParser#statement.
    def enterStatement(self, ctx:new_grammarParser.StatementContext):
        pass

    # Exit a parse tree produced by new_grammarParser#statement.
    def exitStatement(self, ctx:new_grammarParser.StatementContext):
        pass


    # Enter a parse tree produced by new_grammarParser#operation.
    def enterOperation(self, ctx:new_grammarParser.OperationContext):
        pass

    # Exit a parse tree produced by new_grammarParser#operation.
    def exitOperation(self, ctx:new_grammarParser.OperationContext):
        pass


    # Enter a parse tree produced by new_grammarParser#definition.
    def enterDefinition(self, ctx:new_grammarParser.DefinitionContext):
        pass

    # Exit a parse tree produced by new_grammarParser#definition.
    def exitDefinition(self, ctx:new_grammarParser.DefinitionContext):
        pass


    # Enter a parse tree produced by new_grammarParser#expression.
    def enterExpression(self, ctx:new_grammarParser.ExpressionContext):
        pass

    # Exit a parse tree produced by new_grammarParser#expression.
    def exitExpression(self, ctx:new_grammarParser.ExpressionContext):
        pass


    # Enter a parse tree produced by new_grammarParser#assignment.
    def enterAssignment(self, ctx:new_grammarParser.AssignmentContext):
        pass

    # Exit a parse tree produced by new_grammarParser#assignment.
    def exitAssignment(self, ctx:new_grammarParser.AssignmentContext):
        pass


    # Enter a parse tree produced by new_grammarParser#assop.
    def enterAssop(self, ctx:new_grammarParser.AssopContext):
        pass

    # Exit a parse tree produced by new_grammarParser#assop.
    def exitAssop(self, ctx:new_grammarParser.AssopContext):
        pass


    # Enter a parse tree produced by new_grammarParser#arith.
    def enterArith(self, ctx:new_grammarParser.ArithContext):
        pass

    # Exit a parse tree produced by new_grammarParser#arith.
    def exitArith(self, ctx:new_grammarParser.ArithContext):
        pass


    # Enter a parse tree produced by new_grammarParser#arith1.
    def enterArith1(self, ctx:new_grammarParser.Arith1Context):
        pass

    # Exit a parse tree produced by new_grammarParser#arith1.
    def exitArith1(self, ctx:new_grammarParser.Arith1Context):
        pass


    # Enter a parse tree produced by new_grammarParser#arith2.
    def enterArith2(self, ctx:new_grammarParser.Arith2Context):
        pass

    # Exit a parse tree produced by new_grammarParser#arith2.
    def exitArith2(self, ctx:new_grammarParser.Arith2Context):
        pass


    # Enter a parse tree produced by new_grammarParser#print_out.
    def enterPrint_out(self, ctx:new_grammarParser.Print_outContext):
        pass

    # Exit a parse tree produced by new_grammarParser#print_out.
    def exitPrint_out(self, ctx:new_grammarParser.Print_outContext):
        pass


    # Enter a parse tree produced by new_grammarParser#value.
    def enterValue(self, ctx:new_grammarParser.ValueContext):
        pass

    # Exit a parse tree produced by new_grammarParser#value.
    def exitValue(self, ctx:new_grammarParser.ValueContext):
        pass



del new_grammarParser