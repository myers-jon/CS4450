# Generated from new_grammar.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("R\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\6\2!\n\2\r\2\16\2\"\3\3\6\3&\n\3\r")
        buf.write("\3\16\3\'\3\3\3\3\7\3,\n\3\f\3\16\3/\13\3\3\4\3\4\7\4")
        buf.write("\63\n\4\f\4\16\4\66\13\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3")
        buf.write("\f\3\r\3\r\3\16\3\16\3\17\3\17\2\2\20\3\3\5\4\7\5\t\6")
        buf.write("\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\3\2\5\3\2\62;\5\2C\\aac|\6\2\62;C\\aac|\2U\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\3 \3\2\2\2\5%\3\2\2\2\7\60\3\2\2\2\t\67\3\2\2\2")
        buf.write("\139\3\2\2\2\r;\3\2\2\2\17=\3\2\2\2\21D\3\2\2\2\23F\3")
        buf.write("\2\2\2\25H\3\2\2\2\27J\3\2\2\2\31L\3\2\2\2\33N\3\2\2\2")
        buf.write("\35P\3\2\2\2\37!\t\2\2\2 \37\3\2\2\2!\"\3\2\2\2\" \3\2")
        buf.write("\2\2\"#\3\2\2\2#\4\3\2\2\2$&\t\2\2\2%$\3\2\2\2&\'\3\2")
        buf.write("\2\2\'%\3\2\2\2\'(\3\2\2\2()\3\2\2\2)-\7\60\2\2*,\t\2")
        buf.write("\2\2+*\3\2\2\2,/\3\2\2\2-+\3\2\2\2-.\3\2\2\2.\6\3\2\2")
        buf.write("\2/-\3\2\2\2\60\64\t\3\2\2\61\63\t\4\2\2\62\61\3\2\2\2")
        buf.write("\63\66\3\2\2\2\64\62\3\2\2\2\64\65\3\2\2\2\65\b\3\2\2")
        buf.write("\2\66\64\3\2\2\2\678\7\"\2\28\n\3\2\2\29:\7?\2\2:\f\3")
        buf.write("\2\2\2;<\7\f\2\2<\16\3\2\2\2=>\7r\2\2>?\7t\2\2?@\7k\2")
        buf.write("\2@A\7p\2\2AB\7v\2\2BC\7*\2\2C\20\3\2\2\2DE\7*\2\2E\22")
        buf.write("\3\2\2\2FG\7+\2\2G\24\3\2\2\2HI\7-\2\2I\26\3\2\2\2JK\7")
        buf.write("/\2\2K\30\3\2\2\2LM\7,\2\2M\32\3\2\2\2NO\7\61\2\2O\34")
        buf.write("\3\2\2\2PQ\7\'\2\2Q\36\3\2\2\2\7\2\"\'-\64\2")
        return buf.getvalue()


class new_grammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INT = 1
    FLOAT = 2
    VARNAME = 3
    WS = 4
    ASSIGN = 5
    NL = 6
    PRNT = 7
    LPAREN = 8
    RPAREN = 9
    PLUS = 10
    MINUS = 11
    MULT = 12
    DIV = 13
    MOD = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "' '", "'='", "'\n'", "'print('", "'('", "')'", "'+'", "'-'", 
            "'*'", "'/'", "'%'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "FLOAT", "VARNAME", "WS", "ASSIGN", "NL", "PRNT", "LPAREN", 
            "RPAREN", "PLUS", "MINUS", "MULT", "DIV", "MOD" ]

    ruleNames = [ "INT", "FLOAT", "VARNAME", "WS", "ASSIGN", "NL", "PRNT", 
                  "LPAREN", "RPAREN", "PLUS", "MINUS", "MULT", "DIV", "MOD" ]

    grammarFileName = "new_grammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


