# Generated from grammar.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\b")
        buf.write("-\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\3\2\3\2\3\3\3\3\3\4\3\4\5\4\26\n\4\3\5\6\5\31\n\5\r\5")
        buf.write("\16\5\32\3\6\6\6\36\n\6\r\6\16\6\37\3\6\3\6\7\6$\n\6\f")
        buf.write("\6\16\6\'\13\6\3\7\6\7*\n\7\r\7\16\7+\2\2\b\3\3\5\4\7")
        buf.write("\5\t\6\13\7\r\b\3\2\5\4\2\f\f\"\"\3\2\62;\3\2c|\2\61\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\3\17\3\2\2\2\5\21\3\2\2\2\7\25\3\2")
        buf.write("\2\2\t\30\3\2\2\2\13\35\3\2\2\2\r)\3\2\2\2\17\20\7?\2")
        buf.write("\2\20\4\3\2\2\2\21\22\t\2\2\2\22\6\3\2\2\2\23\26\5\t\5")
        buf.write("\2\24\26\5\13\6\2\25\23\3\2\2\2\25\24\3\2\2\2\26\b\3\2")
        buf.write("\2\2\27\31\t\3\2\2\30\27\3\2\2\2\31\32\3\2\2\2\32\30\3")
        buf.write("\2\2\2\32\33\3\2\2\2\33\n\3\2\2\2\34\36\t\3\2\2\35\34")
        buf.write("\3\2\2\2\36\37\3\2\2\2\37\35\3\2\2\2\37 \3\2\2\2 !\3\2")
        buf.write("\2\2!%\7\60\2\2\"$\t\3\2\2#\"\3\2\2\2$\'\3\2\2\2%#\3\2")
        buf.write("\2\2%&\3\2\2\2&\f\3\2\2\2\'%\3\2\2\2(*\t\4\2\2)(\3\2\2")
        buf.write("\2*+\3\2\2\2+)\3\2\2\2+,\3\2\2\2,\16\3\2\2\2\b\2\25\32")
        buf.write("\37%+\2")
        return buf.getvalue()


class java_pythonLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    WS = 2
    NUMBER = 3
    INT = 4
    FLOAT = 5
    VAR = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='" ]

    symbolicNames = [ "<INVALID>",
            "WS", "NUMBER", "INT", "FLOAT", "VAR" ]

    ruleNames = [ "T__0", "WS", "NUMBER", "INT", "FLOAT", "VAR" ]

    grammarFileName = "grammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


