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
        buf.write("\u00e8\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\5\2\36\n\2\3\2\3\2\3\3\3\3\6\3$\n\3\r\3\16\3")
        buf.write("%\7\3(\n\3\f\3\16\3+\13\3\3\3\3\3\7\3/\n\3\f\3\16\3\62")
        buf.write("\13\3\3\4\3\4\5\4\66\n\4\3\5\7\59\n\5\f\5\16\5<\13\5\3")
        buf.write("\5\3\5\7\5@\n\5\f\5\16\5C\13\5\3\5\7\5F\n\5\f\5\16\5I")
        buf.write("\13\5\3\5\3\5\7\5M\n\5\f\5\16\5P\13\5\5\5R\n\5\3\6\3\6")
        buf.write("\7\6V\n\6\f\6\16\6Y\13\6\3\6\3\6\7\6]\n\6\f\6\16\6`\13")
        buf.write("\6\3\6\3\6\3\7\3\7\5\7f\n\7\3\b\3\b\7\bj\n\b\f\b\16\b")
        buf.write("m\13\b\3\b\3\b\7\bq\n\b\f\b\16\bt\13\b\3\b\3\b\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\n\3\n\7\n\177\n\n\f\n\16\n\u0082\13\n\3")
        buf.write("\n\3\n\7\n\u0086\n\n\f\n\16\n\u0089\13\n\3\n\7\n\u008c")
        buf.write("\n\n\f\n\16\n\u008f\13\n\3\13\3\13\3\13\3\13\3\13\7\13")
        buf.write("\u0096\n\13\f\13\16\13\u0099\13\13\3\13\3\13\7\13\u009d")
        buf.write("\n\13\f\13\16\13\u00a0\13\13\3\13\3\13\3\13\7\13\u00a5")
        buf.write("\n\13\f\13\16\13\u00a8\13\13\3\13\3\13\7\13\u00ac\n\13")
        buf.write("\f\13\16\13\u00af\13\13\3\13\7\13\u00b2\n\13\f\13\16\13")
        buf.write("\u00b5\13\13\3\f\3\f\3\f\3\f\3\f\7\f\u00bc\n\f\f\f\16")
        buf.write("\f\u00bf\13\f\3\f\3\f\7\f\u00c3\n\f\f\f\16\f\u00c6\13")
        buf.write("\f\3\f\3\f\3\f\7\f\u00cb\n\f\f\f\16\f\u00ce\13\f\3\f\3")
        buf.write("\f\7\f\u00d2\n\f\f\f\16\f\u00d5\13\f\3\f\7\f\u00d8\n\f")
        buf.write("\f\f\16\f\u00db\13\f\3\r\3\r\3\r\3\r\7\r\u00e1\n\r\f\r")
        buf.write("\16\r\u00e4\13\r\3\16\3\16\3\16\2\5\22\24\26\17\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\32\2\4\3\2\7\n\3\2\3\5\2\u00f9")
        buf.write("\2\35\3\2\2\2\4)\3\2\2\2\6\65\3\2\2\2\bQ\3\2\2\2\nS\3")
        buf.write("\2\2\2\fe\3\2\2\2\16g\3\2\2\2\20w\3\2\2\2\22y\3\2\2\2")
        buf.write("\24\u0090\3\2\2\2\26\u00b6\3\2\2\2\30\u00dc\3\2\2\2\32")
        buf.write("\u00e5\3\2\2\2\34\36\5\4\3\2\35\34\3\2\2\2\35\36\3\2\2")
        buf.write("\2\36\37\3\2\2\2\37 \7\2\2\3 \3\3\2\2\2!#\5\6\4\2\"$\7")
        buf.write("\f\2\2#\"\3\2\2\2$%\3\2\2\2%#\3\2\2\2%&\3\2\2\2&(\3\2")
        buf.write("\2\2\'!\3\2\2\2(+\3\2\2\2)\'\3\2\2\2)*\3\2\2\2*,\3\2\2")
        buf.write("\2+)\3\2\2\2,\60\5\6\4\2-/\7\f\2\2.-\3\2\2\2/\62\3\2\2")
        buf.write("\2\60.\3\2\2\2\60\61\3\2\2\2\61\5\3\2\2\2\62\60\3\2\2")
        buf.write("\2\63\66\5\b\5\2\64\66\5\30\r\2\65\63\3\2\2\2\65\64\3")
        buf.write("\2\2\2\66\7\3\2\2\2\679\7\6\2\28\67\3\2\2\29<\3\2\2\2")
        buf.write(":8\3\2\2\2:;\3\2\2\2;=\3\2\2\2<:\3\2\2\2=A\5\n\6\2>@\7")
        buf.write("\6\2\2?>\3\2\2\2@C\3\2\2\2A?\3\2\2\2AB\3\2\2\2BR\3\2\2")
        buf.write("\2CA\3\2\2\2DF\7\6\2\2ED\3\2\2\2FI\3\2\2\2GE\3\2\2\2G")
        buf.write("H\3\2\2\2HJ\3\2\2\2IG\3\2\2\2JN\5\16\b\2KM\7\6\2\2LK\3")
        buf.write("\2\2\2MP\3\2\2\2NL\3\2\2\2NO\3\2\2\2OR\3\2\2\2PN\3\2\2")
        buf.write("\2Q:\3\2\2\2QG\3\2\2\2R\t\3\2\2\2SW\7\5\2\2TV\7\6\2\2")
        buf.write("UT\3\2\2\2VY\3\2\2\2WU\3\2\2\2WX\3\2\2\2XZ\3\2\2\2YW\3")
        buf.write("\2\2\2Z^\7\13\2\2[]\7\6\2\2\\[\3\2\2\2]`\3\2\2\2^\\\3")
        buf.write("\2\2\2^_\3\2\2\2_a\3\2\2\2`^\3\2\2\2ab\5\f\7\2b\13\3\2")
        buf.write("\2\2cf\5\22\n\2df\5\32\16\2ec\3\2\2\2ed\3\2\2\2f\r\3\2")
        buf.write("\2\2gk\7\5\2\2hj\7\6\2\2ih\3\2\2\2jm\3\2\2\2ki\3\2\2\2")
        buf.write("kl\3\2\2\2ln\3\2\2\2mk\3\2\2\2nr\5\20\t\2oq\7\6\2\2po")
        buf.write("\3\2\2\2qt\3\2\2\2rp\3\2\2\2rs\3\2\2\2su\3\2\2\2tr\3\2")
        buf.write("\2\2uv\5\32\16\2v\17\3\2\2\2wx\t\2\2\2x\21\3\2\2\2yz\b")
        buf.write("\n\1\2z{\5\24\13\2{\u008d\3\2\2\2|\u0080\f\4\2\2}\177")
        buf.write("\7\6\2\2~}\3\2\2\2\177\u0082\3\2\2\2\u0080~\3\2\2\2\u0080")
        buf.write("\u0081\3\2\2\2\u0081\u0083\3\2\2\2\u0082\u0080\3\2\2\2")
        buf.write("\u0083\u0087\7\24\2\2\u0084\u0086\7\6\2\2\u0085\u0084")
        buf.write("\3\2\2\2\u0086\u0089\3\2\2\2\u0087\u0085\3\2\2\2\u0087")
        buf.write("\u0088\3\2\2\2\u0088\u008a\3\2\2\2\u0089\u0087\3\2\2\2")
        buf.write("\u008a\u008c\5\22\n\5\u008b|\3\2\2\2\u008c\u008f\3\2\2")
        buf.write("\2\u008d\u008b\3\2\2\2\u008d\u008e\3\2\2\2\u008e\23\3")
        buf.write("\2\2\2\u008f\u008d\3\2\2\2\u0090\u0091\b\13\1\2\u0091")
        buf.write("\u0092\5\26\f\2\u0092\u00b3\3\2\2\2\u0093\u0097\f\5\2")
        buf.write("\2\u0094\u0096\7\6\2\2\u0095\u0094\3\2\2\2\u0096\u0099")
        buf.write("\3\2\2\2\u0097\u0095\3\2\2\2\u0097\u0098\3\2\2\2\u0098")
        buf.write("\u009a\3\2\2\2\u0099\u0097\3\2\2\2\u009a\u009e\7\21\2")
        buf.write("\2\u009b\u009d\7\6\2\2\u009c\u009b\3\2\2\2\u009d\u00a0")
        buf.write("\3\2\2\2\u009e\u009c\3\2\2\2\u009e\u009f\3\2\2\2\u009f")
        buf.write("\u00a1\3\2\2\2\u00a0\u009e\3\2\2\2\u00a1\u00b2\5\24\13")
        buf.write("\6\u00a2\u00a6\f\4\2\2\u00a3\u00a5\7\6\2\2\u00a4\u00a3")
        buf.write("\3\2\2\2\u00a5\u00a8\3\2\2\2\u00a6\u00a4\3\2\2\2\u00a6")
        buf.write("\u00a7\3\2\2\2\u00a7\u00a9\3\2\2\2\u00a8\u00a6\3\2\2\2")
        buf.write("\u00a9\u00ad\7\20\2\2\u00aa\u00ac\7\6\2\2\u00ab\u00aa")
        buf.write("\3\2\2\2\u00ac\u00af\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ad")
        buf.write("\u00ae\3\2\2\2\u00ae\u00b0\3\2\2\2\u00af\u00ad\3\2\2\2")
        buf.write("\u00b0\u00b2\5\24\13\5\u00b1\u0093\3\2\2\2\u00b1\u00a2")
        buf.write("\3\2\2\2\u00b2\u00b5\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b3")
        buf.write("\u00b4\3\2\2\2\u00b4\25\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b6")
        buf.write("\u00b7\b\f\1\2\u00b7\u00b8\5\32\16\2\u00b8\u00d9\3\2\2")
        buf.write("\2\u00b9\u00bd\f\5\2\2\u00ba\u00bc\7\6\2\2\u00bb\u00ba")
        buf.write("\3\2\2\2\u00bc\u00bf\3\2\2\2\u00bd\u00bb\3\2\2\2\u00bd")
        buf.write("\u00be\3\2\2\2\u00be\u00c0\3\2\2\2\u00bf\u00bd\3\2\2\2")
        buf.write("\u00c0\u00c4\7\22\2\2\u00c1\u00c3\7\6\2\2\u00c2\u00c1")
        buf.write("\3\2\2\2\u00c3\u00c6\3\2\2\2\u00c4\u00c2\3\2\2\2\u00c4")
        buf.write("\u00c5\3\2\2\2\u00c5\u00c7\3\2\2\2\u00c6\u00c4\3\2\2\2")
        buf.write("\u00c7\u00d8\5\26\f\6\u00c8\u00cc\f\4\2\2\u00c9\u00cb")
        buf.write("\7\6\2\2\u00ca\u00c9\3\2\2\2\u00cb\u00ce\3\2\2\2\u00cc")
        buf.write("\u00ca\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd\u00cf\3\2\2\2")
        buf.write("\u00ce\u00cc\3\2\2\2\u00cf\u00d3\7\23\2\2\u00d0\u00d2")
        buf.write("\7\6\2\2\u00d1\u00d0\3\2\2\2\u00d2\u00d5\3\2\2\2\u00d3")
        buf.write("\u00d1\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\u00d6\3\2\2\2")
        buf.write("\u00d5\u00d3\3\2\2\2\u00d6\u00d8\5\26\f\5\u00d7\u00b9")
        buf.write("\3\2\2\2\u00d7\u00c8\3\2\2\2\u00d8\u00db\3\2\2\2\u00d9")
        buf.write("\u00d7\3\2\2\2\u00d9\u00da\3\2\2\2\u00da\27\3\2\2\2\u00db")
        buf.write("\u00d9\3\2\2\2\u00dc\u00dd\7\r\2\2\u00dd\u00de\5\32\16")
        buf.write("\2\u00de\u00e2\7\17\2\2\u00df\u00e1\7\6\2\2\u00e0\u00df")
        buf.write("\3\2\2\2\u00e1\u00e4\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e2")
        buf.write("\u00e3\3\2\2\2\u00e3\31\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e5")
        buf.write("\u00e6\t\3\2\2\u00e6\33\3\2\2\2!\35%)\60\65:AGNQW^ekr")
        buf.write("\u0080\u0087\u008d\u0097\u009e\u00a6\u00ad\u00b1\u00b3")
        buf.write("\u00bd\u00c4\u00cc\u00d3\u00d7\u00d9\u00e2")
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
    RULE_arith = 8
    RULE_arith1 = 9
    RULE_arith2 = 10
    RULE_print_out = 11
    RULE_value = 12

    ruleNames =  [ "parse", "block", "statement", "operation", "definition", 
                   "expression", "assignment", "assop", "arith", "arith1", 
                   "arith2", "print_out", "value" ]

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
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << new_grammarParser.VARNAME) | (1 << new_grammarParser.WS) | (1 << new_grammarParser.PRNT))) != 0):
                self.state = 26
                self.block()


            self.state = 29
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
            self.state = 39
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 31
                    self.statement()
                    self.state = 33 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 32
                        self.match(new_grammarParser.NL)
                        self.state = 35 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==new_grammarParser.NL):
                            break
             
                self.state = 41
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 42
            self.statement()
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==new_grammarParser.NL:
                self.state = 43
                self.match(new_grammarParser.NL)
                self.state = 48
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
            self.state = 51
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [new_grammarParser.VARNAME, new_grammarParser.WS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.operation()
                pass
            elif token in [new_grammarParser.PRNT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 50
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
            self.state = 79
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==new_grammarParser.WS:
                    self.state = 53
                    self.match(new_grammarParser.WS)
                    self.state = 58
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 59
                self.definition()
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==new_grammarParser.WS:
                    self.state = 60
                    self.match(new_grammarParser.WS)
                    self.state = 65
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==new_grammarParser.WS:
                    self.state = 66
                    self.match(new_grammarParser.WS)
                    self.state = 71
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 72
                self.assignment()
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==new_grammarParser.WS:
                    self.state = 73
                    self.match(new_grammarParser.WS)
                    self.state = 78
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
            self.state = 81
            self.match(new_grammarParser.VARNAME)
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==new_grammarParser.WS:
                self.state = 82
                self.match(new_grammarParser.WS)
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 88
            self.match(new_grammarParser.ASSIGN)
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==new_grammarParser.WS:
                self.state = 89
                self.match(new_grammarParser.WS)
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 95
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

        def arith(self):
            return self.getTypedRuleContext(new_grammarParser.ArithContext,0)


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
            self.state = 99
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 97
                self.arith(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 98
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
            self.state = 101
            self.match(new_grammarParser.VARNAME)
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==new_grammarParser.WS:
                self.state = 102
                self.match(new_grammarParser.WS)
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 108
            self.assop()
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==new_grammarParser.WS:
                self.state = 109
                self.match(new_grammarParser.WS)
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 115
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
            self.state = 117
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


    class ArithContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arith1(self):
            return self.getTypedRuleContext(new_grammarParser.Arith1Context,0)


        def arith(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(new_grammarParser.ArithContext)
            else:
                return self.getTypedRuleContext(new_grammarParser.ArithContext,i)


        def MOD(self):
            return self.getToken(new_grammarParser.MOD, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(new_grammarParser.WS)
            else:
                return self.getToken(new_grammarParser.WS, i)

        def getRuleIndex(self):
            return new_grammarParser.RULE_arith

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArith" ):
                listener.enterArith(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArith" ):
                listener.exitArith(self)



    def arith(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = new_grammarParser.ArithContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_arith, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.arith1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 139
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = new_grammarParser.ArithContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_arith)
                    self.state = 122
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 126
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==new_grammarParser.WS:
                        self.state = 123
                        self.match(new_grammarParser.WS)
                        self.state = 128
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 129
                    self.match(new_grammarParser.MOD)
                    self.state = 133
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==new_grammarParser.WS:
                        self.state = 130
                        self.match(new_grammarParser.WS)
                        self.state = 135
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 136
                    self.arith(3) 
                self.state = 141
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Arith1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arith2(self):
            return self.getTypedRuleContext(new_grammarParser.Arith2Context,0)


        def arith1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(new_grammarParser.Arith1Context)
            else:
                return self.getTypedRuleContext(new_grammarParser.Arith1Context,i)


        def SUB(self):
            return self.getToken(new_grammarParser.SUB, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(new_grammarParser.WS)
            else:
                return self.getToken(new_grammarParser.WS, i)

        def ADD(self):
            return self.getToken(new_grammarParser.ADD, 0)

        def getRuleIndex(self):
            return new_grammarParser.RULE_arith1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArith1" ):
                listener.enterArith1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArith1" ):
                listener.exitArith1(self)



    def arith1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = new_grammarParser.Arith1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_arith1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.arith2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 177
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 175
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                    if la_ == 1:
                        localctx = new_grammarParser.Arith1Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arith1)
                        self.state = 145
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 149
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==new_grammarParser.WS:
                            self.state = 146
                            self.match(new_grammarParser.WS)
                            self.state = 151
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 152
                        self.match(new_grammarParser.SUB)
                        self.state = 156
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==new_grammarParser.WS:
                            self.state = 153
                            self.match(new_grammarParser.WS)
                            self.state = 158
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 159
                        self.arith1(4)
                        pass

                    elif la_ == 2:
                        localctx = new_grammarParser.Arith1Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arith1)
                        self.state = 160
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 164
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==new_grammarParser.WS:
                            self.state = 161
                            self.match(new_grammarParser.WS)
                            self.state = 166
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 167
                        self.match(new_grammarParser.ADD)
                        self.state = 171
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==new_grammarParser.WS:
                            self.state = 168
                            self.match(new_grammarParser.WS)
                            self.state = 173
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 174
                        self.arith1(3)
                        pass

             
                self.state = 179
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Arith2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(new_grammarParser.ValueContext,0)


        def arith2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(new_grammarParser.Arith2Context)
            else:
                return self.getTypedRuleContext(new_grammarParser.Arith2Context,i)


        def MULT(self):
            return self.getToken(new_grammarParser.MULT, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(new_grammarParser.WS)
            else:
                return self.getToken(new_grammarParser.WS, i)

        def DIV(self):
            return self.getToken(new_grammarParser.DIV, 0)

        def getRuleIndex(self):
            return new_grammarParser.RULE_arith2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArith2" ):
                listener.enterArith2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArith2" ):
                listener.exitArith2(self)



    def arith2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = new_grammarParser.Arith2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_arith2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.value()
            self._ctx.stop = self._input.LT(-1)
            self.state = 215
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 213
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                    if la_ == 1:
                        localctx = new_grammarParser.Arith2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arith2)
                        self.state = 183
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 187
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==new_grammarParser.WS:
                            self.state = 184
                            self.match(new_grammarParser.WS)
                            self.state = 189
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 190
                        self.match(new_grammarParser.MULT)
                        self.state = 194
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==new_grammarParser.WS:
                            self.state = 191
                            self.match(new_grammarParser.WS)
                            self.state = 196
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 197
                        self.arith2(4)
                        pass

                    elif la_ == 2:
                        localctx = new_grammarParser.Arith2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arith2)
                        self.state = 198
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 202
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==new_grammarParser.WS:
                            self.state = 199
                            self.match(new_grammarParser.WS)
                            self.state = 204
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 205
                        self.match(new_grammarParser.DIV)
                        self.state = 209
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==new_grammarParser.WS:
                            self.state = 206
                            self.match(new_grammarParser.WS)
                            self.state = 211
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 212
                        self.arith2(3)
                        pass

             
                self.state = 217
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 22, self.RULE_print_out)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(new_grammarParser.PRNT)
            self.state = 219
            self.value()
            self.state = 220
            self.match(new_grammarParser.RPAREN)
            self.state = 224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==new_grammarParser.WS:
                self.state = 221
                self.match(new_grammarParser.WS)
                self.state = 226
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
        self.enterRule(localctx, 24, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[8] = self.arith_sempred
        self._predicates[9] = self.arith1_sempred
        self._predicates[10] = self.arith2_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def arith_sempred(self, localctx:ArithContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def arith1_sempred(self, localctx:Arith1Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def arith2_sempred(self, localctx:Arith2Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




