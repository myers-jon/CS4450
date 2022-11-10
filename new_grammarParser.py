# Generated from new_grammar.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\24")
        buf.write("\u0095\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\5\2\34\n\2\3\2\3\2\3\3\3\3\6\3\"\n\3\r\3\16\3#\7\3&\n")
        buf.write("\3\f\3\16\3)\13\3\3\3\3\3\7\3-\n\3\f\3\16\3\60\13\3\3")
        buf.write("\4\3\4\5\4\64\n\4\3\5\7\5\67\n\5\f\5\16\5:\13\5\3\5\3")
        buf.write("\5\7\5>\n\5\f\5\16\5A\13\5\3\5\7\5D\n\5\f\5\16\5G\13\5")
        buf.write("\3\5\3\5\7\5K\n\5\f\5\16\5N\13\5\5\5P\n\5\3\6\3\6\7\6")
        buf.write("T\n\6\f\6\16\6W\13\6\3\6\3\6\7\6[\n\6\f\6\16\6^\13\6\3")
        buf.write("\6\3\6\3\7\3\7\5\7d\n\7\3\b\3\b\7\bh\n\b\f\b\16\bk\13")
        buf.write("\b\3\b\3\b\7\bo\n\b\f\b\16\br\13\b\3\b\3\b\3\t\3\t\3\n")
        buf.write("\3\n\7\nz\n\n\f\n\16\n}\13\n\3\n\3\n\7\n\u0081\n\n\f\n")
        buf.write("\16\n\u0084\13\n\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3\f\7\f")
        buf.write("\u008e\n\f\f\f\16\f\u0091\13\f\3\r\3\r\3\r\2\2\16\2\4")
        buf.write("\6\b\n\f\16\20\22\24\26\30\2\5\3\2\7\n\3\2\20\24\3\2\3")
        buf.write("\5\2\u009a\2\33\3\2\2\2\4\'\3\2\2\2\6\63\3\2\2\2\bO\3")
        buf.write("\2\2\2\nQ\3\2\2\2\fc\3\2\2\2\16e\3\2\2\2\20u\3\2\2\2\22")
        buf.write("w\3\2\2\2\24\u0087\3\2\2\2\26\u0089\3\2\2\2\30\u0092\3")
        buf.write("\2\2\2\32\34\5\4\3\2\33\32\3\2\2\2\33\34\3\2\2\2\34\35")
        buf.write("\3\2\2\2\35\36\7\2\2\3\36\3\3\2\2\2\37!\5\6\4\2 \"\7\f")
        buf.write("\2\2! \3\2\2\2\"#\3\2\2\2#!\3\2\2\2#$\3\2\2\2$&\3\2\2")
        buf.write("\2%\37\3\2\2\2&)\3\2\2\2\'%\3\2\2\2\'(\3\2\2\2(*\3\2\2")
        buf.write("\2)\'\3\2\2\2*.\5\6\4\2+-\7\f\2\2,+\3\2\2\2-\60\3\2\2")
        buf.write("\2.,\3\2\2\2./\3\2\2\2/\5\3\2\2\2\60.\3\2\2\2\61\64\5")
        buf.write("\b\5\2\62\64\5\26\f\2\63\61\3\2\2\2\63\62\3\2\2\2\64\7")
        buf.write("\3\2\2\2\65\67\7\6\2\2\66\65\3\2\2\2\67:\3\2\2\28\66\3")
        buf.write("\2\2\289\3\2\2\29;\3\2\2\2:8\3\2\2\2;?\5\n\6\2<>\7\6\2")
        buf.write("\2=<\3\2\2\2>A\3\2\2\2?=\3\2\2\2?@\3\2\2\2@P\3\2\2\2A")
        buf.write("?\3\2\2\2BD\7\6\2\2CB\3\2\2\2DG\3\2\2\2EC\3\2\2\2EF\3")
        buf.write("\2\2\2FH\3\2\2\2GE\3\2\2\2HL\5\16\b\2IK\7\6\2\2JI\3\2")
        buf.write("\2\2KN\3\2\2\2LJ\3\2\2\2LM\3\2\2\2MP\3\2\2\2NL\3\2\2\2")
        buf.write("O8\3\2\2\2OE\3\2\2\2P\t\3\2\2\2QU\7\5\2\2RT\7\6\2\2SR")
        buf.write("\3\2\2\2TW\3\2\2\2US\3\2\2\2UV\3\2\2\2VX\3\2\2\2WU\3\2")
        buf.write("\2\2X\\\7\13\2\2Y[\7\6\2\2ZY\3\2\2\2[^\3\2\2\2\\Z\3\2")
        buf.write("\2\2\\]\3\2\2\2]_\3\2\2\2^\\\3\2\2\2_`\5\f\7\2`\13\3\2")
        buf.write("\2\2ad\5\22\n\2bd\5\30\r\2ca\3\2\2\2cb\3\2\2\2d\r\3\2")
        buf.write("\2\2ei\7\5\2\2fh\7\6\2\2gf\3\2\2\2hk\3\2\2\2ig\3\2\2\2")
        buf.write("ij\3\2\2\2jl\3\2\2\2ki\3\2\2\2lp\5\20\t\2mo\7\6\2\2nm")
        buf.write("\3\2\2\2or\3\2\2\2pn\3\2\2\2pq\3\2\2\2qs\3\2\2\2rp\3\2")
        buf.write("\2\2st\5\30\r\2t\17\3\2\2\2uv\t\2\2\2v\21\3\2\2\2w{\5")
        buf.write("\30\r\2xz\7\6\2\2yx\3\2\2\2z}\3\2\2\2{y\3\2\2\2{|\3\2")
        buf.write("\2\2|~\3\2\2\2}{\3\2\2\2~\u0082\5\24\13\2\177\u0081\7")
        buf.write("\6\2\2\u0080\177\3\2\2\2\u0081\u0084\3\2\2\2\u0082\u0080")
        buf.write("\3\2\2\2\u0082\u0083\3\2\2\2\u0083\u0085\3\2\2\2\u0084")
        buf.write("\u0082\3\2\2\2\u0085\u0086\5\30\r\2\u0086\23\3\2\2\2\u0087")
        buf.write("\u0088\t\3\2\2\u0088\25\3\2\2\2\u0089\u008a\7\r\2\2\u008a")
        buf.write("\u008b\5\30\r\2\u008b\u008f\7\17\2\2\u008c\u008e\7\6\2")
        buf.write("\2\u008d\u008c\3\2\2\2\u008e\u0091\3\2\2\2\u008f\u008d")
        buf.write("\3\2\2\2\u008f\u0090\3\2\2\2\u0090\27\3\2\2\2\u0091\u008f")
        buf.write("\3\2\2\2\u0092\u0093\t\4\2\2\u0093\31\3\2\2\2\24\33#\'")
        buf.write(".\638?ELOU\\cip{\u0082\u008f")
        return buf.getvalue()


class new_grammarParser ( Parser ):

    grammarFileName = "new_grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "' '", "'/='", "'*='", "'+='", "'-='", "'='", "'\n'", 
                     "'print('", "'('", "')'", "'+'", "'-'", "'*'", "'/'", 
                     "'%'" ]

    symbolicNames = [ "<INVALID>", "INT", "FLOAT", "VARNAME", "WS", "DIVASSIGN", 
                      "MULTASSIGN", "ADDASSIGN", "SUBASSIGN", "ASSIGN", 
                      "NL", "PRNT", "LPAREN", "RPAREN", "ADD", "SUB", "MULT", 
                      "DIV", "MOD" ]

    RULE_parse = 0
    RULE_block = 1
    RULE_statement = 2
    RULE_operation = 3
    RULE_definition = 4
    RULE_expression = 5
    RULE_assignment = 6
    RULE_assop = 7
    RULE_arithmetic = 8
    RULE_op = 9
    RULE_print_out = 10
    RULE_value = 11

    ruleNames =  [ "parse", "block", "statement", "operation", "definition", 
                   "expression", "assignment", "assop", "arithmetic", "op", 
                   "print_out", "value" ]

    EOF = Token.EOF
    INT=1
    FLOAT=2
    VARNAME=3
    WS=4
    DIVASSIGN=5
    MULTASSIGN=6
    ADDASSIGN=7
    SUBASSIGN=8
    ASSIGN=9
    NL=10
    PRNT=11
    LPAREN=12
    RPAREN=13
    ADD=14
    SUB=15
    MULT=16
    DIV=17
    MOD=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ParseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(new_grammarParser.EOF, 0)

        def block(self):
            return self.getTypedRuleContext(new_grammarParser.BlockContext,0)


        def getRuleIndex(self):
            return new_grammarParser.RULE_parse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParse" ):
                listener.enterParse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParse" ):
                listener.exitParse(self)




    def parse(self):

        localctx = new_grammarParser.ParseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_parse)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << new_grammarParser.VARNAME) | (1 << new_grammarParser.WS) | (1 << new_grammarParser.PRNT))) != 0):
                self.state = 24
                self.block()


            self.state = 27
            self.match(new_grammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(new_grammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(new_grammarParser.StatementContext,i)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(new_grammarParser.NL)
            else:
                return self.getToken(new_grammarParser.NL, i)

        def getRuleIndex(self):
            return new_grammarParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = new_grammarParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 29
                    self.statement()
                    self.state = 31 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 30
                        self.match(new_grammarParser.NL)
                        self.state = 33 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==new_grammarParser.NL):
                            break
             
                self.state = 39
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 40
            self.statement()
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==new_grammarParser.NL:
                self.state = 41
                self.match(new_grammarParser.NL)
                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operation(self):
            return self.getTypedRuleContext(new_grammarParser.OperationContext,0)


        def print_out(self):
            return self.getTypedRuleContext(new_grammarParser.Print_outContext,0)


        def getRuleIndex(self):
            return new_grammarParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = new_grammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 49
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [new_grammarParser.VARNAME, new_grammarParser.WS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.operation()
                pass
            elif token in [new_grammarParser.PRNT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                self.print_out()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def definition(self):
            return self.getTypedRuleContext(new_grammarParser.DefinitionContext,0)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(new_grammarParser.WS)
            else:
                return self.getToken(new_grammarParser.WS, i)

        def assignment(self):
            return self.getTypedRuleContext(new_grammarParser.AssignmentContext,0)


        def getRuleIndex(self):
            return new_grammarParser.RULE_operation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperation" ):
                listener.enterOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperation" ):
                listener.exitOperation(self)




    def operation(self):

        localctx = new_grammarParser.OperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_operation)
        self._la = 0 # Token type
        try:
            self.state = 77
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==new_grammarParser.WS:
                    self.state = 51
                    self.match(new_grammarParser.WS)
                    self.state = 56
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 57
                self.definition()
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==new_grammarParser.WS:
                    self.state = 58
                    self.match(new_grammarParser.WS)
                    self.state = 63
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==new_grammarParser.WS:
                    self.state = 64
                    self.match(new_grammarParser.WS)
                    self.state = 69
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 70
                self.assignment()
                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==new_grammarParser.WS:
                    self.state = 71
                    self.match(new_grammarParser.WS)
                    self.state = 76
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARNAME(self):
            return self.getToken(new_grammarParser.VARNAME, 0)

        def ASSIGN(self):
            return self.getToken(new_grammarParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(new_grammarParser.ExpressionContext,0)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(new_grammarParser.WS)
            else:
                return self.getToken(new_grammarParser.WS, i)

        def getRuleIndex(self):
            return new_grammarParser.RULE_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefinition" ):
                listener.enterDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefinition" ):
                listener.exitDefinition(self)




    def definition(self):

        localctx = new_grammarParser.DefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_definition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(new_grammarParser.VARNAME)
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==new_grammarParser.WS:
                self.state = 80
                self.match(new_grammarParser.WS)
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 86
            self.match(new_grammarParser.ASSIGN)
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==new_grammarParser.WS:
                self.state = 87
                self.match(new_grammarParser.WS)
                self.state = 92
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 93
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arithmetic(self):
            return self.getTypedRuleContext(new_grammarParser.ArithmeticContext,0)


        def value(self):
            return self.getTypedRuleContext(new_grammarParser.ValueContext,0)


        def getRuleIndex(self):
            return new_grammarParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = new_grammarParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expression)
        try:
            self.state = 97
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.arithmetic()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.value()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARNAME(self):
            return self.getToken(new_grammarParser.VARNAME, 0)

        def assop(self):
            return self.getTypedRuleContext(new_grammarParser.AssopContext,0)


        def value(self):
            return self.getTypedRuleContext(new_grammarParser.ValueContext,0)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(new_grammarParser.WS)
            else:
                return self.getToken(new_grammarParser.WS, i)

        def getRuleIndex(self):
            return new_grammarParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = new_grammarParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(new_grammarParser.VARNAME)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==new_grammarParser.WS:
                self.state = 100
                self.match(new_grammarParser.WS)
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 106
            self.assop()
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==new_grammarParser.WS:
                self.state = 107
                self.match(new_grammarParser.WS)
                self.state = 112
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 113
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIVASSIGN(self):
            return self.getToken(new_grammarParser.DIVASSIGN, 0)

        def MULTASSIGN(self):
            return self.getToken(new_grammarParser.MULTASSIGN, 0)

        def ADDASSIGN(self):
            return self.getToken(new_grammarParser.ADDASSIGN, 0)

        def SUBASSIGN(self):
            return self.getToken(new_grammarParser.SUBASSIGN, 0)

        def getRuleIndex(self):
            return new_grammarParser.RULE_assop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssop" ):
                listener.enterAssop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssop" ):
                listener.exitAssop(self)




    def assop(self):

        localctx = new_grammarParser.AssopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_assop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << new_grammarParser.DIVASSIGN) | (1 << new_grammarParser.MULTASSIGN) | (1 << new_grammarParser.ADDASSIGN) | (1 << new_grammarParser.SUBASSIGN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArithmeticContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(new_grammarParser.ValueContext)
            else:
                return self.getTypedRuleContext(new_grammarParser.ValueContext,i)


        def op(self):
            return self.getTypedRuleContext(new_grammarParser.OpContext,0)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(new_grammarParser.WS)
            else:
                return self.getToken(new_grammarParser.WS, i)

        def getRuleIndex(self):
            return new_grammarParser.RULE_arithmetic

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmetic" ):
                listener.enterArithmetic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmetic" ):
                listener.exitArithmetic(self)




    def arithmetic(self):

        localctx = new_grammarParser.ArithmeticContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_arithmetic)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.value()
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==new_grammarParser.WS:
                self.state = 118
                self.match(new_grammarParser.WS)
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 124
            self.op()
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==new_grammarParser.WS:
                self.state = 125
                self.match(new_grammarParser.WS)
                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 131
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(new_grammarParser.ADD, 0)

        def SUB(self):
            return self.getToken(new_grammarParser.SUB, 0)

        def MULT(self):
            return self.getToken(new_grammarParser.MULT, 0)

        def DIV(self):
            return self.getToken(new_grammarParser.DIV, 0)

        def MOD(self):
            return self.getToken(new_grammarParser.MOD, 0)

        def getRuleIndex(self):
            return new_grammarParser.RULE_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp" ):
                listener.enterOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp" ):
                listener.exitOp(self)




    def op(self):

        localctx = new_grammarParser.OpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << new_grammarParser.ADD) | (1 << new_grammarParser.SUB) | (1 << new_grammarParser.MULT) | (1 << new_grammarParser.DIV) | (1 << new_grammarParser.MOD))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print_outContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRNT(self):
            return self.getToken(new_grammarParser.PRNT, 0)

        def value(self):
            return self.getTypedRuleContext(new_grammarParser.ValueContext,0)


        def RPAREN(self):
            return self.getToken(new_grammarParser.RPAREN, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(new_grammarParser.WS)
            else:
                return self.getToken(new_grammarParser.WS, i)

        def getRuleIndex(self):
            return new_grammarParser.RULE_print_out

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint_out" ):
                listener.enterPrint_out(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint_out" ):
                listener.exitPrint_out(self)




    def print_out(self):

        localctx = new_grammarParser.Print_outContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_print_out)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(new_grammarParser.PRNT)
            self.state = 136
            self.value()
            self.state = 137
            self.match(new_grammarParser.RPAREN)
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==new_grammarParser.WS:
                self.state = 138
                self.match(new_grammarParser.WS)
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARNAME(self):
            return self.getToken(new_grammarParser.VARNAME, 0)

        def INT(self):
            return self.getToken(new_grammarParser.INT, 0)

        def FLOAT(self):
            return self.getToken(new_grammarParser.FLOAT, 0)

        def getRuleIndex(self):
            return new_grammarParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = new_grammarParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << new_grammarParser.INT) | (1 << new_grammarParser.FLOAT) | (1 << new_grammarParser.VARNAME))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





