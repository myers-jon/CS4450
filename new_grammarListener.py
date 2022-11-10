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


    # Enter a parse tree produced by new_grammarParser#definition.
    def enterDefinition(self, ctx:new_grammarParser.DefinitionContext):
        pass

    # Exit a parse tree produced by new_grammarParser#definition.
    def exitDefinition(self, ctx:new_grammarParser.DefinitionContext):
        pass



del new_grammarParser