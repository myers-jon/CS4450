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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\b")
        buf.write("+\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\3\7\3")
        buf.write("\17\n\3\f\3\16\3\22\13\3\3\4\3\4\7\4\26\n\4\f\4\16\4\31")
        buf.write("\13\4\3\5\3\5\7\5\35\n\5\f\5\16\5 \13\5\3\5\3\5\7\5$\n")
        buf.write("\5\f\5\16\5\'\13\5\3\5\3\5\3\5\2\2\6\2\4\6\b\2\2\2*\2")
        buf.write("\n\3\2\2\2\4\20\3\2\2\2\6\23\3\2\2\2\b\32\3\2\2\2\n\13")
        buf.write("\5\4\3\2\13\f\7\2\2\3\f\3\3\2\2\2\r\17\5\6\4\2\16\r\3")
        buf.write("\2\2\2\17\22\3\2\2\2\20\16\3\2\2\2\20\21\3\2\2\2\21\5")
        buf.write("\3\2\2\2\22\20\3\2\2\2\23\27\5\b\5\2\24\26\7\4\2\2\25")
        buf.write("\24\3\2\2\2\26\31\3\2\2\2\27\25\3\2\2\2\27\30\3\2\2\2")
        buf.write("\30\7\3\2\2\2\31\27\3\2\2\2\32\36\7\b\2\2\33\35\7\4\2")
        buf.write("\2\34\33\3\2\2\2\35 \3\2\2\2\36\34\3\2\2\2\36\37\3\2\2")
        buf.write("\2\37!\3\2\2\2 \36\3\2\2\2!%\7\3\2\2\"$\7\4\2\2#\"\3\2")
        buf.write("\2\2$\'\3\2\2\2%#\3\2\2\2%&\3\2\2\2&(\3\2\2\2\'%\3\2\2")
        buf.write("\2()\7\5\2\2)\t\3\2\2\2\6\20\27\36%")
        return buf.getvalue()


class new_grammarParser ( Parser ):

    grammarFileName = "new_grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "WS", "NUMBER", "INT", "FLOAT", 
                      "VAR" ]

    RULE_parse = 0
    RULE_block = 1
    RULE_statement = 2
    RULE_definition = 3

    ruleNames =  [ "parse", "block", "statement", "definition" ]

    EOF = Token.EOF
    T__0=1
    WS=2
    NUMBER=3
    INT=4
    FLOAT=5
    VAR=6

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

        def block(self):
            return self.getTypedRuleContext(new_grammarParser.BlockContext,0)


        def EOF(self):
            return self.getToken(new_grammarParser.EOF, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.block()
            self.state = 9
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
            self.state = 14
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==new_grammarParser.VAR:
                self.state = 11
                self.statement()
                self.state = 16
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

        def definition(self):
            return self.getTypedRuleContext(new_grammarParser.DefinitionContext,0)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(new_grammarParser.WS)
            else:
                return self.getToken(new_grammarParser.WS, i)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.definition()
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==new_grammarParser.WS:
                self.state = 18
                self.match(new_grammarParser.WS)
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def VAR(self):
            return self.getToken(new_grammarParser.VAR, 0)

        def NUMBER(self):
            return self.getToken(new_grammarParser.NUMBER, 0)

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
        self.enterRule(localctx, 6, self.RULE_definition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(new_grammarParser.VAR)
            self.state = 28
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==new_grammarParser.WS:
                self.state = 25
                self.match(new_grammarParser.WS)
                self.state = 30
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 31
            self.match(new_grammarParser.T__0)
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==new_grammarParser.WS:
                self.state = 32
                self.match(new_grammarParser.WS)
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 38
            self.match(new_grammarParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





