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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\24")
        buf.write("f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\3\2\6\2)\n\2\r\2\16\2*\3\3\6\3.\n\3\r\3\16\3/\3\3\3\3")
        buf.write("\7\3\64\n\3\f\3\16\3\67\13\3\3\4\3\4\7\4;\n\4\f\4\16\4")
        buf.write(">\13\4\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\t")
        buf.write("\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22")
        buf.write("\3\22\3\23\3\23\2\2\24\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24")
        buf.write("\3\2\5\3\2\62;\5\2C\\aac|\6\2\62;C\\aac|\2i\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\3")
        buf.write("(\3\2\2\2\5-\3\2\2\2\78\3\2\2\2\t?\3\2\2\2\13A\3\2\2\2")
        buf.write("\rD\3\2\2\2\17G\3\2\2\2\21J\3\2\2\2\23M\3\2\2\2\25O\3")
        buf.write("\2\2\2\27Q\3\2\2\2\31X\3\2\2\2\33Z\3\2\2\2\35\\\3\2\2")
        buf.write("\2\37^\3\2\2\2!`\3\2\2\2#b\3\2\2\2%d\3\2\2\2\')\t\2\2")
        buf.write("\2(\'\3\2\2\2)*\3\2\2\2*(\3\2\2\2*+\3\2\2\2+\4\3\2\2\2")
        buf.write(",.\t\2\2\2-,\3\2\2\2./\3\2\2\2/-\3\2\2\2/\60\3\2\2\2\60")
        buf.write("\61\3\2\2\2\61\65\7\60\2\2\62\64\t\2\2\2\63\62\3\2\2\2")
        buf.write("\64\67\3\2\2\2\65\63\3\2\2\2\65\66\3\2\2\2\66\6\3\2\2")
        buf.write("\2\67\65\3\2\2\28<\t\3\2\29;\t\4\2\2:9\3\2\2\2;>\3\2\2")
        buf.write("\2<:\3\2\2\2<=\3\2\2\2=\b\3\2\2\2><\3\2\2\2?@\7\"\2\2")
        buf.write("@\n\3\2\2\2AB\7\61\2\2BC\7?\2\2C\f\3\2\2\2DE\7,\2\2EF")
        buf.write("\7?\2\2F\16\3\2\2\2GH\7-\2\2HI\7?\2\2I\20\3\2\2\2JK\7")
        buf.write("/\2\2KL\7?\2\2L\22\3\2\2\2MN\7?\2\2N\24\3\2\2\2OP\7\f")
        buf.write("\2\2P\26\3\2\2\2QR\7r\2\2RS\7t\2\2ST\7k\2\2TU\7p\2\2U")
        buf.write("V\7v\2\2VW\7*\2\2W\30\3\2\2\2XY\7*\2\2Y\32\3\2\2\2Z[\7")
        buf.write("+\2\2[\34\3\2\2\2\\]\7-\2\2]\36\3\2\2\2^_\7/\2\2_ \3\2")
        buf.write("\2\2`a\7,\2\2a\"\3\2\2\2bc\7\61\2\2c$\3\2\2\2de\7\'\2")
        buf.write("\2e&\3\2\2\2\7\2*/\65<\2")
        return buf.getvalue()


class new_grammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INT = 1
    FLOAT = 2
    VARNAME = 3
    WS = 4
    DIVASSIGN = 5
    MULTASSIGN = 6
    ADDASSIGN = 7
    SUBASSIGN = 8
    ASSIGN = 9
    NL = 10
    PRNT = 11
    LPAREN = 12
    RPAREN = 13
    ADD = 14
    SUB = 15
    MULT = 16
    DIV = 17
    MOD = 18

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "' '", "'/='", "'*='", "'+='", "'-='", "'='", "'\n'", "'print('", 
            "'('", "')'", "'+'", "'-'", "'*'", "'/'", "'%'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "FLOAT", "VARNAME", "WS", "DIVASSIGN", "MULTASSIGN", 
            "ADDASSIGN", "SUBASSIGN", "ASSIGN", "NL", "PRNT", "LPAREN", 
            "RPAREN", "ADD", "SUB", "MULT", "DIV", "MOD" ]

    ruleNames = [ "INT", "FLOAT", "VARNAME", "WS", "DIVASSIGN", "MULTASSIGN", 
                  "ADDASSIGN", "SUBASSIGN", "ASSIGN", "NL", "PRNT", "LPAREN", 
                  "RPAREN", "ADD", "SUB", "MULT", "DIV", "MOD" ]

    grammarFileName = "new_grammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


