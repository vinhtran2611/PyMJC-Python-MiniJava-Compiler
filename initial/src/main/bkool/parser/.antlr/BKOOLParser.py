# Generated from c:\Users\tranq\workspace\HK221\PPL\Assignment\assignment3\initial\src\main\bkool\parser\BKOOL.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3@")
        buf.write("\u0151\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\3\2\6\2\64\n\2\r\2\16\2\65\3\2\3\2\3\3\3\3\3\3\3")
        buf.write("\3\5\3>\n\3\3\3\3\3\7\3B\n\3\f\3\16\3E\13\3\3\3\3\3\3")
        buf.write("\4\3\4\5\4K\n\4\3\5\3\5\5\5O\n\5\3\6\5\6R\n\6\3\6\3\6")
        buf.write("\3\6\5\6W\n\6\5\6Y\n\6\3\6\3\6\3\6\3\7\5\7_\n\7\3\7\3")
        buf.write("\7\3\7\3\b\3\b\3\b\3\t\5\th\n\t\3\t\3\t\3\t\3\n\5\nn\n")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\5\nv\n\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\5\n}\n\n\5\n\177\n\n\3\13\3\13\3\13\7\13\u0084\n\13")
        buf.write("\f\13\16\13\u0087\13\13\5\13\u0089\n\13\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\6\r\u0097\n\r\r\r\16")
        buf.write("\r\u0098\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00a3")
        buf.write("\n\16\3\17\3\17\3\17\3\17\3\17\5\17\u00aa\n\17\3\17\3")
        buf.write("\17\3\20\3\20\3\20\3\20\3\20\5\20\u00b3\n\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\7\21\u00ba\n\21\f\21\16\21\u00bd\13\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u00d2\n")
        buf.write("\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23")
        buf.write("\u00dd\n\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3")
        buf.write("\23\5\23\u00e8\n\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\5\23\u0101\n\23\3\23\5\23\u0104")
        buf.write("\n\23\3\23\3\23\3\23\3\23\3\23\7\23\u010b\n\23\f\23\16")
        buf.write("\23\u010e\13\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\5\24\u011a\n\24\3\25\3\25\3\26\3\26\3\26\3")
        buf.write("\26\3\26\5\26\u0123\n\26\3\27\3\27\3\27\3\27\5\27\u0129")
        buf.write("\n\27\3\27\7\27\u012c\n\27\f\27\16\27\u012f\13\27\5\27")
        buf.write("\u0131\n\27\3\27\3\27\3\30\3\30\3\30\5\30\u0138\n\30\3")
        buf.write("\30\3\30\3\30\3\30\3\30\5\30\u013f\n\30\5\30\u0141\n\30")
        buf.write("\3\31\3\31\3\31\5\31\u0146\n\31\3\31\3\31\3\31\3\31\3")
        buf.write("\31\5\31\u014d\n\31\5\31\u014f\n\31\3\31\2\3$\32\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\2\n\3\2")
        buf.write("9:\3\2\5\6\3\2\7\n\3\2\21\22\3\2\13\f\3\2\r\20\3\2 #\4")
        buf.write("\2$(<<\2\u0173\2\63\3\2\2\2\49\3\2\2\2\6J\3\2\2\2\bN\3")
        buf.write("\2\2\2\nX\3\2\2\2\f^\3\2\2\2\16c\3\2\2\2\20g\3\2\2\2\22")
        buf.write("~\3\2\2\2\24\u0088\3\2\2\2\26\u008a\3\2\2\2\30\u0096\3")
        buf.write("\2\2\2\32\u009c\3\2\2\2\34\u00a4\3\2\2\2\36\u00b2\3\2")
        buf.write("\2\2 \u00b4\3\2\2\2\"\u00d1\3\2\2\2$\u00e7\3\2\2\2&\u0119")
        buf.write("\3\2\2\2(\u011b\3\2\2\2*\u011d\3\2\2\2,\u0124\3\2\2\2")
        buf.write(".\u0140\3\2\2\2\60\u014e\3\2\2\2\62\64\5\4\3\2\63\62\3")
        buf.write("\2\2\2\64\65\3\2\2\2\65\63\3\2\2\2\65\66\3\2\2\2\66\67")
        buf.write("\3\2\2\2\678\7\2\2\38\3\3\2\2\29:\7,\2\2:=\7<\2\2;<\7")
        buf.write("\60\2\2<>\7<\2\2=;\3\2\2\2=>\3\2\2\2>?\3\2\2\2?C\7\33")
        buf.write("\2\2@B\5\6\4\2A@\3\2\2\2BE\3\2\2\2CA\3\2\2\2CD\3\2\2\2")
        buf.write("DF\3\2\2\2EC\3\2\2\2FG\7\34\2\2G\5\3\2\2\2HK\5\b\5\2I")
        buf.write("K\5\22\n\2JH\3\2\2\2JI\3\2\2\2K\7\3\2\2\2LO\5\f\7\2MO")
        buf.write("\5\n\6\2NL\3\2\2\2NM\3\2\2\2O\t\3\2\2\2PR\7/\2\2QP\3\2")
        buf.write("\2\2QR\3\2\2\2RS\3\2\2\2SY\7.\2\2TV\7.\2\2UW\7/\2\2VU")
        buf.write("\3\2\2\2VW\3\2\2\2WY\3\2\2\2XQ\3\2\2\2XT\3\2\2\2YZ\3\2")
        buf.write("\2\2Z[\5\16\b\2[\\\7\35\2\2\\\13\3\2\2\2]_\7/\2\2^]\3")
        buf.write("\2\2\2^_\3\2\2\2_`\3\2\2\2`a\5\16\b\2ab\7\35\2\2b\r\3")
        buf.write("\2\2\2cd\5*\26\2de\5\60\31\2e\17\3\2\2\2fh\7.\2\2gf\3")
        buf.write("\2\2\2gh\3\2\2\2hi\3\2\2\2ij\5*\26\2jk\5.\30\2k\21\3\2")
        buf.write("\2\2ln\7/\2\2ml\3\2\2\2mn\3\2\2\2no\3\2\2\2op\5*\26\2")
        buf.write("pq\7<\2\2qr\7\31\2\2rs\5\24\13\2su\7\32\2\2tv\5 \21\2")
        buf.write("ut\3\2\2\2uv\3\2\2\2v\177\3\2\2\2wx\7<\2\2xy\7\31\2\2")
        buf.write("yz\5\24\13\2z|\7\32\2\2{}\5 \21\2|{\3\2\2\2|}\3\2\2\2")
        buf.write("}\177\3\2\2\2~m\3\2\2\2~w\3\2\2\2\177\23\3\2\2\2\u0080")
        buf.write("\u0085\5\20\t\2\u0081\u0082\7\35\2\2\u0082\u0084\5\20")
        buf.write("\t\2\u0083\u0081\3\2\2\2\u0084\u0087\3\2\2\2\u0085\u0083")
        buf.write("\3\2\2\2\u0085\u0086\3\2\2\2\u0086\u0089\3\2\2\2\u0087")
        buf.write("\u0085\3\2\2\2\u0088\u0080\3\2\2\2\u0088\u0089\3\2\2\2")
        buf.write("\u0089\25\3\2\2\2\u008a\u008b\78\2\2\u008b\u008c\7<\2")
        buf.write("\2\u008c\u008d\7\25\2\2\u008d\u008e\5$\23\2\u008e\u008f")
        buf.write("\t\2\2\2\u008f\u0090\5$\23\2\u0090\u0091\7\64\2\2\u0091")
        buf.write("\u0092\5\"\22\2\u0092\27\3\2\2\2\u0093\u0094\5&\24\2\u0094")
        buf.write("\u0095\7\25\2\2\u0095\u0097\3\2\2\2\u0096\u0093\3\2\2")
        buf.write("\2\u0097\u0098\3\2\2\2\u0098\u0096\3\2\2\2\u0098\u0099")
        buf.write("\3\2\2\2\u0099\u009a\3\2\2\2\u009a\u009b\5$\23\2\u009b")
        buf.write("\31\3\2\2\2\u009c\u009d\7\66\2\2\u009d\u009e\5$\23\2\u009e")
        buf.write("\u009f\7\67\2\2\u009f\u00a2\5\"\22\2\u00a0\u00a1\7\65")
        buf.write("\2\2\u00a1\u00a3\5\"\22\2\u00a2\u00a0\3\2\2\2\u00a2\u00a3")
        buf.write("\3\2\2\2\u00a3\33\3\2\2\2\u00a4\u00a5\5$\23\2\u00a5\u00a6")
        buf.write("\7\36\2\2\u00a6\u00a7\7<\2\2\u00a7\u00a9\7\31\2\2\u00a8")
        buf.write("\u00aa\5\36\20\2\u00a9\u00a8\3\2\2\2\u00a9\u00aa\3\2\2")
        buf.write("\2\u00aa\u00ab\3\2\2\2\u00ab\u00ac\7\32\2\2\u00ac\35\3")
        buf.write("\2\2\2\u00ad\u00ae\5$\23\2\u00ae\u00af\7\37\2\2\u00af")
        buf.write("\u00b0\5\36\20\2\u00b0\u00b3\3\2\2\2\u00b1\u00b3\5$\23")
        buf.write("\2\u00b2\u00ad\3\2\2\2\u00b2\u00b1\3\2\2\2\u00b3\37\3")
        buf.write("\2\2\2\u00b4\u00bb\7\33\2\2\u00b5\u00ba\5\"\22\2\u00b6")
        buf.write("\u00b7\5\20\t\2\u00b7\u00b8\7\35\2\2\u00b8\u00ba\3\2\2")
        buf.write("\2\u00b9\u00b5\3\2\2\2\u00b9\u00b6\3\2\2\2\u00ba\u00bd")
        buf.write("\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc")
        buf.write("\u00be\3\2\2\2\u00bd\u00bb\3\2\2\2\u00be\u00bf\7\34\2")
        buf.write("\2\u00bf!\3\2\2\2\u00c0\u00d2\5 \21\2\u00c1\u00c2\5\30")
        buf.write("\r\2\u00c2\u00c3\7\35\2\2\u00c3\u00d2\3\2\2\2\u00c4\u00d2")
        buf.write("\5\32\16\2\u00c5\u00d2\5\26\f\2\u00c6\u00c7\7\62\2\2\u00c7")
        buf.write("\u00d2\7\35\2\2\u00c8\u00c9\7\63\2\2\u00c9\u00d2\7\35")
        buf.write("\2\2\u00ca\u00cb\7;\2\2\u00cb\u00cc\5$\23\2\u00cc\u00cd")
        buf.write("\7\35\2\2\u00cd\u00d2\3\2\2\2\u00ce\u00cf\5\34\17\2\u00cf")
        buf.write("\u00d0\7\35\2\2\u00d0\u00d2\3\2\2\2\u00d1\u00c0\3\2\2")
        buf.write("\2\u00d1\u00c1\3\2\2\2\u00d1\u00c4\3\2\2\2\u00d1\u00c5")
        buf.write("\3\2\2\2\u00d1\u00c6\3\2\2\2\u00d1\u00c8\3\2\2\2\u00d1")
        buf.write("\u00ca\3\2\2\2\u00d1\u00ce\3\2\2\2\u00d2#\3\2\2\2\u00d3")
        buf.write("\u00d4\b\23\1\2\u00d4\u00d5\7\31\2\2\u00d5\u00d6\5$\23")
        buf.write("\2\u00d6\u00d7\7\32\2\2\u00d7\u00e8\3\2\2\2\u00d8\u00d9")
        buf.write("\7-\2\2\u00d9\u00da\7<\2\2\u00da\u00dc\7\31\2\2\u00db")
        buf.write("\u00dd\5\36\20\2\u00dc\u00db\3\2\2\2\u00dc\u00dd\3\2\2")
        buf.write("\2\u00dd\u00de\3\2\2\2\u00de\u00e8\7\32\2\2\u00df\u00e0")
        buf.write("\t\3\2\2\u00e0\u00e8\5$\23\16\u00e1\u00e2\7\23\2\2\u00e2")
        buf.write("\u00e8\5$\23\r\u00e3\u00e8\7<\2\2\u00e4\u00e8\5(\25\2")
        buf.write("\u00e5\u00e8\5,\27\2\u00e6\u00e8\7\61\2\2\u00e7\u00d3")
        buf.write("\3\2\2\2\u00e7\u00d8\3\2\2\2\u00e7\u00df\3\2\2\2\u00e7")
        buf.write("\u00e1\3\2\2\2\u00e7\u00e3\3\2\2\2\u00e7\u00e4\3\2\2\2")
        buf.write("\u00e7\u00e5\3\2\2\2\u00e7\u00e6\3\2\2\2\u00e8\u010c\3")
        buf.write("\2\2\2\u00e9\u00ea\f\f\2\2\u00ea\u00eb\7\24\2\2\u00eb")
        buf.write("\u010b\5$\23\r\u00ec\u00ed\f\13\2\2\u00ed\u00ee\t\4\2")
        buf.write("\2\u00ee\u010b\5$\23\f\u00ef\u00f0\f\n\2\2\u00f0\u00f1")
        buf.write("\t\3\2\2\u00f1\u010b\5$\23\13\u00f2\u00f3\f\t\2\2\u00f3")
        buf.write("\u00f4\t\5\2\2\u00f4\u010b\5$\23\n\u00f5\u00f6\f\b\2\2")
        buf.write("\u00f6\u00f7\t\6\2\2\u00f7\u010b\5$\23\t\u00f8\u00f9\f")
        buf.write("\7\2\2\u00f9\u00fa\t\7\2\2\u00fa\u010b\5$\23\b\u00fb\u00fc")
        buf.write("\f\20\2\2\u00fc\u00fd\7\36\2\2\u00fd\u0103\7<\2\2\u00fe")
        buf.write("\u0100\7\31\2\2\u00ff\u0101\5\36\20\2\u0100\u00ff\3\2")
        buf.write("\2\2\u0100\u0101\3\2\2\2\u0101\u0102\3\2\2\2\u0102\u0104")
        buf.write("\7\32\2\2\u0103\u00fe\3\2\2\2\u0103\u0104\3\2\2\2\u0104")
        buf.write("\u010b\3\2\2\2\u0105\u0106\f\17\2\2\u0106\u0107\7\27\2")
        buf.write("\2\u0107\u0108\5$\23\2\u0108\u0109\7\30\2\2\u0109\u010b")
        buf.write("\3\2\2\2\u010a\u00e9\3\2\2\2\u010a\u00ec\3\2\2\2\u010a")
        buf.write("\u00ef\3\2\2\2\u010a\u00f2\3\2\2\2\u010a\u00f5\3\2\2\2")
        buf.write("\u010a\u00f8\3\2\2\2\u010a\u00fb\3\2\2\2\u010a\u0105\3")
        buf.write("\2\2\2\u010b\u010e\3\2\2\2\u010c\u010a\3\2\2\2\u010c\u010d")
        buf.write("\3\2\2\2\u010d%\3\2\2\2\u010e\u010c\3\2\2\2\u010f\u011a")
        buf.write("\7<\2\2\u0110\u0111\5$\23\2\u0111\u0112\7\36\2\2\u0112")
        buf.write("\u0113\7<\2\2\u0113\u011a\3\2\2\2\u0114\u0115\5$\23\2")
        buf.write("\u0115\u0116\7\27\2\2\u0116\u0117\5$\23\2\u0117\u0118")
        buf.write("\7\30\2\2\u0118\u011a\3\2\2\2\u0119\u010f\3\2\2\2\u0119")
        buf.write("\u0110\3\2\2\2\u0119\u0114\3\2\2\2\u011a\'\3\2\2\2\u011b")
        buf.write("\u011c\t\b\2\2\u011c)\3\2\2\2\u011d\u0122\t\t\2\2\u011e")
        buf.write("\u011f\7\27\2\2\u011f\u0120\5$\23\2\u0120\u0121\7\30\2")
        buf.write("\2\u0121\u0123\3\2\2\2\u0122\u011e\3\2\2\2\u0122\u0123")
        buf.write("\3\2\2\2\u0123+\3\2\2\2\u0124\u0130\7\33\2\2\u0125\u012d")
        buf.write("\5(\25\2\u0126\u0128\7\37\2\2\u0127\u0129\7=\2\2\u0128")
        buf.write("\u0127\3\2\2\2\u0128\u0129\3\2\2\2\u0129\u012a\3\2\2\2")
        buf.write("\u012a\u012c\5(\25\2\u012b\u0126\3\2\2\2\u012c\u012f\3")
        buf.write("\2\2\2\u012d\u012b\3\2\2\2\u012d\u012e\3\2\2\2\u012e\u0131")
        buf.write("\3\2\2\2\u012f\u012d\3\2\2\2\u0130\u0125\3\2\2\2\u0130")
        buf.write("\u0131\3\2\2\2\u0131\u0132\3\2\2\2\u0132\u0133\7\34\2")
        buf.write("\2\u0133-\3\2\2\2\u0134\u0137\7<\2\2\u0135\u0136\7\25")
        buf.write("\2\2\u0136\u0138\5$\23\2\u0137\u0135\3\2\2\2\u0137\u0138")
        buf.write("\3\2\2\2\u0138\u0139\3\2\2\2\u0139\u013a\7\37\2\2\u013a")
        buf.write("\u0141\5.\30\2\u013b\u013e\7<\2\2\u013c\u013d\7\25\2\2")
        buf.write("\u013d\u013f\5$\23\2\u013e\u013c\3\2\2\2\u013e\u013f\3")
        buf.write("\2\2\2\u013f\u0141\3\2\2\2\u0140\u0134\3\2\2\2\u0140\u013b")
        buf.write("\3\2\2\2\u0141/\3\2\2\2\u0142\u0145\7<\2\2\u0143\u0144")
        buf.write("\7\26\2\2\u0144\u0146\5$\23\2\u0145\u0143\3\2\2\2\u0145")
        buf.write("\u0146\3\2\2\2\u0146\u0147\3\2\2\2\u0147\u0148\7\37\2")
        buf.write("\2\u0148\u014f\5\60\31\2\u0149\u014c\7<\2\2\u014a\u014b")
        buf.write("\7\26\2\2\u014b\u014d\5$\23\2\u014c\u014a\3\2\2\2\u014c")
        buf.write("\u014d\3\2\2\2\u014d\u014f\3\2\2\2\u014e\u0142\3\2\2\2")
        buf.write("\u014e\u0149\3\2\2\2\u014f\61\3\2\2\2*\65=CJNQVX^gmu|")
        buf.write("~\u0085\u0088\u0098\u00a2\u00a9\u00b2\u00b9\u00bb\u00d1")
        buf.write("\u00dc\u00e7\u0100\u0103\u010a\u010c\u0119\u0122\u0128")
        buf.write("\u012d\u0130\u0137\u013e\u0140\u0145\u014c\u014e")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'+'", "'-'", 
                     "'*'", "'/'", "'\\'", "'%'", "'!='", "'=='", "'<'", 
                     "'>'", "'<='", "'>='", "'||'", "'&&'", "'!'", "'^'", 
                     "':='", "'='", "'['", "']'", "'('", "')'", "'{'", "'}'", 
                     "';'", "'.'", "','", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'boolean'", "'int'", "'float'", "'string'", 
                     "'void'", "'true'", "'false'", "'nil'", "'class'", 
                     "'new'", "'final'", "'static'", "'extends'", "'this'", 
                     "'break'", "'continue'", "'do'", "'else'", "'if'", 
                     "'then'", "'for'", "'to'", "'downto'", "'return'" ]

    symbolicNames = [ "<INVALID>", "BLOCK_COMMENT", "LINE_COMMENT", "ADD", 
                      "SUB", "MUL", "DIV", "DEV_INT", "MOD", "NOT_EQUAL", 
                      "EQUAL", "LT", "GT", "LTE", "GTE", "OR", "AND", "NOT", 
                      "CONCAT", "ASSIGN", "ASSIGN_ATT", "LQB", "RQR", "LB", 
                      "RB", "LP", "RP", "SEMI", "DOT", "CM", "INT_LIT", 
                      "FLOAT_LIT", "BOOL_LIT", "STR_LIT", "BOOLEAN", "INT", 
                      "FLOAT", "STRING", "VOID", "TRUE", "FALSE", "NIL", 
                      "CLASS", "NEW", "FINAL", "STATIC", "EXTENDS", "THIS", 
                      "BREAK", "CONTINUE", "DO", "ELSE", "IF", "THEN", "FOR", 
                      "TO", "DOWNTO", "RETURN", "ID", "WS", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_class_decl = 1
    RULE_member = 2
    RULE_attribute_decl = 3
    RULE_immutable = 4
    RULE_mutable = 5
    RULE_var_decl_att = 6
    RULE_var_decl = 7
    RULE_method_decl = 8
    RULE_params = 9
    RULE_for_stmt = 10
    RULE_assign_stmt = 11
    RULE_if_stmt = 12
    RULE_method_invocation = 13
    RULE_list_exp = 14
    RULE_block_stmt = 15
    RULE_stmt = 16
    RULE_exp = 17
    RULE_lhs = 18
    RULE_literal = 19
    RULE_bktype = 20
    RULE_array_lit = 21
    RULE_listID = 22
    RULE_ids_att = 23

    ruleNames =  [ "program", "class_decl", "member", "attribute_decl", 
                   "immutable", "mutable", "var_decl_att", "var_decl", "method_decl", 
                   "params", "for_stmt", "assign_stmt", "if_stmt", "method_invocation", 
                   "list_exp", "block_stmt", "stmt", "exp", "lhs", "literal", 
                   "bktype", "array_lit", "listID", "ids_att" ]

    EOF = Token.EOF
    BLOCK_COMMENT=1
    LINE_COMMENT=2
    ADD=3
    SUB=4
    MUL=5
    DIV=6
    DEV_INT=7
    MOD=8
    NOT_EQUAL=9
    EQUAL=10
    LT=11
    GT=12
    LTE=13
    GTE=14
    OR=15
    AND=16
    NOT=17
    CONCAT=18
    ASSIGN=19
    ASSIGN_ATT=20
    LQB=21
    RQR=22
    LB=23
    RB=24
    LP=25
    RP=26
    SEMI=27
    DOT=28
    CM=29
    INT_LIT=30
    FLOAT_LIT=31
    BOOL_LIT=32
    STR_LIT=33
    BOOLEAN=34
    INT=35
    FLOAT=36
    STRING=37
    VOID=38
    TRUE=39
    FALSE=40
    NIL=41
    CLASS=42
    NEW=43
    FINAL=44
    STATIC=45
    EXTENDS=46
    THIS=47
    BREAK=48
    CONTINUE=49
    DO=50
    ELSE=51
    IF=52
    THEN=53
    FOR=54
    TO=55
    DOWNTO=56
    RETURN=57
    ID=58
    WS=59
    ERROR_CHAR=60
    UNCLOSE_STRING=61
    ILLEGAL_ESCAPE=62

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BKOOLParser.EOF, 0)

        def class_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Class_declContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Class_declContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_program




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 48
                self.class_decl()
                self.state = 51 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKOOLParser.CLASS):
                    break

            self.state = 53
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(BKOOLParser.CLASS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def EXTENDS(self):
            return self.getToken(BKOOLParser.EXTENDS, 0)

        def member(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.MemberContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.MemberContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_class_decl




    def class_decl(self):

        localctx = BKOOLParser.Class_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(BKOOLParser.CLASS)
            self.state = 56
            self.match(BKOOLParser.ID)
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EXTENDS:
                self.state = 57
                self.match(BKOOLParser.EXTENDS)
                self.state = 58
                self.match(BKOOLParser.ID)


            self.state = 61
            self.match(BKOOLParser.LP)
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.VOID) | (1 << BKOOLParser.FINAL) | (1 << BKOOLParser.STATIC) | (1 << BKOOLParser.ID))) != 0):
                self.state = 62
                self.member()
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 68
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Attribute_declContext,0)


        def method_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Method_declContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_member




    def member(self):

        localctx = BKOOLParser.MemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_member)
        try:
            self.state = 72
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self.attribute_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 71
                self.method_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mutable(self):
            return self.getTypedRuleContext(BKOOLParser.MutableContext,0)


        def immutable(self):
            return self.getTypedRuleContext(BKOOLParser.ImmutableContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attribute_decl




    def attribute_decl(self):

        localctx = BKOOLParser.Attribute_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_attribute_decl)
        try:
            self.state = 76
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.mutable()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                self.immutable()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImmutableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl_att(self):
            return self.getTypedRuleContext(BKOOLParser.Var_decl_attContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_immutable




    def immutable(self):

        localctx = BKOOLParser.ImmutableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_immutable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.STATIC:
                    self.state = 78
                    self.match(BKOOLParser.STATIC)


                self.state = 81
                self.match(BKOOLParser.FINAL)
                pass

            elif la_ == 2:
                self.state = 82
                self.match(BKOOLParser.FINAL)
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.STATIC:
                    self.state = 83
                    self.match(BKOOLParser.STATIC)


                pass


            self.state = 88
            self.var_decl_att()
            self.state = 89
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MutableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl_att(self):
            return self.getTypedRuleContext(BKOOLParser.Var_decl_attContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_mutable




    def mutable(self):

        localctx = BKOOLParser.MutableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_mutable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 91
                self.match(BKOOLParser.STATIC)


            self.state = 94
            self.var_decl_att()
            self.state = 95
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decl_attContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bktype(self):
            return self.getTypedRuleContext(BKOOLParser.BktypeContext,0)


        def ids_att(self):
            return self.getTypedRuleContext(BKOOLParser.Ids_attContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_var_decl_att




    def var_decl_att(self):

        localctx = BKOOLParser.Var_decl_attContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_var_decl_att)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.bktype()
            self.state = 98
            self.ids_att()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bktype(self):
            return self.getTypedRuleContext(BKOOLParser.BktypeContext,0)


        def listID(self):
            return self.getTypedRuleContext(BKOOLParser.ListIDContext,0)


        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_var_decl




    def var_decl(self):

        localctx = BKOOLParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_var_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.FINAL:
                self.state = 100
                self.match(BKOOLParser.FINAL)


            self.state = 103
            self.bktype()
            self.state = 104
            self.listID()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bktype(self):
            return self.getTypedRuleContext(BKOOLParser.BktypeContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def params(self):
            return self.getTypedRuleContext(BKOOLParser.ParamsContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_method_decl




    def method_decl(self):

        localctx = BKOOLParser.Method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_method_decl)
        self._la = 0 # Token type
        try:
            self.state = 124
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.STATIC:
                    self.state = 106
                    self.match(BKOOLParser.STATIC)


                self.state = 109
                self.bktype()
                self.state = 110
                self.match(BKOOLParser.ID)
                self.state = 111
                self.match(BKOOLParser.LB)
                self.state = 112
                self.params()
                self.state = 113
                self.match(BKOOLParser.RB)
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.LP:
                    self.state = 114
                    self.block_stmt()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 117
                self.match(BKOOLParser.ID)
                self.state = 118
                self.match(BKOOLParser.LB)
                self.state = 119
                self.params()
                self.state = 120
                self.match(BKOOLParser.RB)
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.LP:
                    self.state = 121
                    self.block_stmt()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Var_declContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Var_declContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.SEMI)
            else:
                return self.getToken(BKOOLParser.SEMI, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_params




    def params(self):

        localctx = BKOOLParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.VOID) | (1 << BKOOLParser.FINAL) | (1 << BKOOLParser.ID))) != 0):
                self.state = 126
                self.var_decl()
                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKOOLParser.SEMI:
                    self.state = 127
                    self.match(BKOOLParser.SEMI)
                    self.state = 128
                    self.var_decl()
                    self.state = 133
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKOOLParser.FOR, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(BKOOLParser.ASSIGN, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExpContext,i)


        def DO(self):
            return self.getToken(BKOOLParser.DO, 0)

        def stmt(self):
            return self.getTypedRuleContext(BKOOLParser.StmtContext,0)


        def TO(self):
            return self.getToken(BKOOLParser.TO, 0)

        def DOWNTO(self):
            return self.getToken(BKOOLParser.DOWNTO, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_for_stmt




    def for_stmt(self):

        localctx = BKOOLParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_for_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(BKOOLParser.FOR)
            self.state = 137
            self.match(BKOOLParser.ID)
            self.state = 138
            self.match(BKOOLParser.ASSIGN)
            self.state = 139
            self.exp(0)
            self.state = 140
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TO or _la==BKOOLParser.DOWNTO):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 141
            self.exp(0)
            self.state = 142
            self.match(BKOOLParser.DO)
            self.state = 143
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def lhs(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.LhsContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.LhsContext,i)


        def ASSIGN(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ASSIGN)
            else:
                return self.getToken(BKOOLParser.ASSIGN, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_assign_stmt




    def assign_stmt(self):

        localctx = BKOOLParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 145
                    self.lhs()
                    self.state = 146
                    self.match(BKOOLParser.ASSIGN)

                else:
                    raise NoViableAltException(self)
                self.state = 150 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

            self.state = 152
            self.exp(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKOOLParser.IF, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def THEN(self):
            return self.getToken(BKOOLParser.THEN, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.StmtContext,i)


        def ELSE(self):
            return self.getToken(BKOOLParser.ELSE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_if_stmt




    def if_stmt(self):

        localctx = BKOOLParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(BKOOLParser.IF)
            self.state = 155
            self.exp(0)
            self.state = 156
            self.match(BKOOLParser.THEN)
            self.state = 157
            self.stmt()
            self.state = 160
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 158
                self.match(BKOOLParser.ELSE)
                self.state = 159
                self.stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_invocationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def list_exp(self):
            return self.getTypedRuleContext(BKOOLParser.List_expContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_method_invocation




    def method_invocation(self):

        localctx = BKOOLParser.Method_invocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_method_invocation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.exp(0)
            self.state = 163
            self.match(BKOOLParser.DOT)
            self.state = 164
            self.match(BKOOLParser.ID)
            self.state = 165
            self.match(BKOOLParser.LB)
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.INT_LIT) | (1 << BKOOLParser.FLOAT_LIT) | (1 << BKOOLParser.BOOL_LIT) | (1 << BKOOLParser.STR_LIT) | (1 << BKOOLParser.NEW) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.ID))) != 0):
                self.state = 166
                self.list_exp()


            self.state = 169
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def CM(self):
            return self.getToken(BKOOLParser.CM, 0)

        def list_exp(self):
            return self.getTypedRuleContext(BKOOLParser.List_expContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_list_exp




    def list_exp(self):

        localctx = BKOOLParser.List_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_list_exp)
        try:
            self.state = 176
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.exp(0)
                self.state = 172
                self.match(BKOOLParser.CM)
                self.state = 173
                self.list_exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.exp(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.StmtContext,i)


        def var_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Var_declContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Var_declContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.SEMI)
            else:
                return self.getToken(BKOOLParser.SEMI, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_block_stmt




    def block_stmt(self):

        localctx = BKOOLParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(BKOOLParser.LP)
            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.INT_LIT) | (1 << BKOOLParser.FLOAT_LIT) | (1 << BKOOLParser.BOOL_LIT) | (1 << BKOOLParser.STR_LIT) | (1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.VOID) | (1 << BKOOLParser.NEW) | (1 << BKOOLParser.FINAL) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.BREAK) | (1 << BKOOLParser.CONTINUE) | (1 << BKOOLParser.IF) | (1 << BKOOLParser.FOR) | (1 << BKOOLParser.RETURN) | (1 << BKOOLParser.ID))) != 0):
                self.state = 183
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                if la_ == 1:
                    self.state = 179
                    self.stmt()
                    pass

                elif la_ == 2:
                    self.state = 180
                    self.var_decl()
                    self.state = 181
                    self.match(BKOOLParser.SEMI)
                    pass


                self.state = 187
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 188
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Block_stmtContext,0)


        def assign_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Assign_stmtContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def if_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.For_stmtContext,0)


        def BREAK(self):
            return self.getToken(BKOOLParser.BREAK, 0)

        def CONTINUE(self):
            return self.getToken(BKOOLParser.CONTINUE, 0)

        def RETURN(self):
            return self.getToken(BKOOLParser.RETURN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def method_invocation(self):
            return self.getTypedRuleContext(BKOOLParser.Method_invocationContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmt




    def stmt(self):

        localctx = BKOOLParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_stmt)
        try:
            self.state = 207
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 190
                self.block_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 191
                self.assign_stmt()
                self.state = 192
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 194
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 195
                self.for_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 196
                self.match(BKOOLParser.BREAK)
                self.state = 197
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 198
                self.match(BKOOLParser.CONTINUE)
                self.state = 199
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 200
                self.match(BKOOLParser.RETURN)
                self.state = 201
                self.exp(0)
                self.state = 202
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 204
                self.method_invocation()
                self.state = 205
                self.match(BKOOLParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExpContext,i)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def NEW(self):
            return self.getToken(BKOOLParser.NEW, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def list_exp(self):
            return self.getTypedRuleContext(BKOOLParser.List_expContext,0)


        def ADD(self):
            return self.getToken(BKOOLParser.ADD, 0)

        def SUB(self):
            return self.getToken(BKOOLParser.SUB, 0)

        def NOT(self):
            return self.getToken(BKOOLParser.NOT, 0)

        def literal(self):
            return self.getTypedRuleContext(BKOOLParser.LiteralContext,0)


        def array_lit(self):
            return self.getTypedRuleContext(BKOOLParser.Array_litContext,0)


        def THIS(self):
            return self.getToken(BKOOLParser.THIS, 0)

        def CONCAT(self):
            return self.getToken(BKOOLParser.CONCAT, 0)

        def MUL(self):
            return self.getToken(BKOOLParser.MUL, 0)

        def DIV(self):
            return self.getToken(BKOOLParser.DIV, 0)

        def DEV_INT(self):
            return self.getToken(BKOOLParser.DEV_INT, 0)

        def MOD(self):
            return self.getToken(BKOOLParser.MOD, 0)

        def AND(self):
            return self.getToken(BKOOLParser.AND, 0)

        def OR(self):
            return self.getToken(BKOOLParser.OR, 0)

        def EQUAL(self):
            return self.getToken(BKOOLParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(BKOOLParser.NOT_EQUAL, 0)

        def LT(self):
            return self.getToken(BKOOLParser.LT, 0)

        def GT(self):
            return self.getToken(BKOOLParser.GT, 0)

        def LTE(self):
            return self.getToken(BKOOLParser.LTE, 0)

        def GTE(self):
            return self.getToken(BKOOLParser.GTE, 0)

        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def LQB(self):
            return self.getToken(BKOOLParser.LQB, 0)

        def RQR(self):
            return self.getToken(BKOOLParser.RQR, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp



    def exp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.ExpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_exp, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.LB]:
                self.state = 210
                self.match(BKOOLParser.LB)
                self.state = 211
                self.exp(0)
                self.state = 212
                self.match(BKOOLParser.RB)
                pass
            elif token in [BKOOLParser.NEW]:
                self.state = 214
                self.match(BKOOLParser.NEW)
                self.state = 215
                self.match(BKOOLParser.ID)
                self.state = 216
                self.match(BKOOLParser.LB)
                self.state = 218
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.INT_LIT) | (1 << BKOOLParser.FLOAT_LIT) | (1 << BKOOLParser.BOOL_LIT) | (1 << BKOOLParser.STR_LIT) | (1 << BKOOLParser.NEW) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.ID))) != 0):
                    self.state = 217
                    self.list_exp()


                self.state = 220
                self.match(BKOOLParser.RB)
                pass
            elif token in [BKOOLParser.ADD, BKOOLParser.SUB]:
                self.state = 221
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.ADD or _la==BKOOLParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 222
                self.exp(12)
                pass
            elif token in [BKOOLParser.NOT]:
                self.state = 223
                self.match(BKOOLParser.NOT)
                self.state = 224
                self.exp(11)
                pass
            elif token in [BKOOLParser.ID]:
                self.state = 225
                self.match(BKOOLParser.ID)
                pass
            elif token in [BKOOLParser.INT_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.BOOL_LIT, BKOOLParser.STR_LIT]:
                self.state = 226
                self.literal()
                pass
            elif token in [BKOOLParser.LP]:
                self.state = 227
                self.array_lit()
                pass
            elif token in [BKOOLParser.THIS]:
                self.state = 228
                self.match(BKOOLParser.THIS)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 266
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 264
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                    if la_ == 1:
                        localctx = BKOOLParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 231
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 232
                        self.match(BKOOLParser.CONCAT)
                        self.state = 233
                        self.exp(11)
                        pass

                    elif la_ == 2:
                        localctx = BKOOLParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 234
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 235
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.MUL) | (1 << BKOOLParser.DIV) | (1 << BKOOLParser.DEV_INT) | (1 << BKOOLParser.MOD))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 236
                        self.exp(10)
                        pass

                    elif la_ == 3:
                        localctx = BKOOLParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 237
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 238
                        _la = self._input.LA(1)
                        if not(_la==BKOOLParser.ADD or _la==BKOOLParser.SUB):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 239
                        self.exp(9)
                        pass

                    elif la_ == 4:
                        localctx = BKOOLParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 240
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 241
                        _la = self._input.LA(1)
                        if not(_la==BKOOLParser.OR or _la==BKOOLParser.AND):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 242
                        self.exp(8)
                        pass

                    elif la_ == 5:
                        localctx = BKOOLParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 243
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 244
                        _la = self._input.LA(1)
                        if not(_la==BKOOLParser.NOT_EQUAL or _la==BKOOLParser.EQUAL):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 245
                        self.exp(7)
                        pass

                    elif la_ == 6:
                        localctx = BKOOLParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 246
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 247
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.LT) | (1 << BKOOLParser.GT) | (1 << BKOOLParser.LTE) | (1 << BKOOLParser.GTE))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 248
                        self.exp(6)
                        pass

                    elif la_ == 7:
                        localctx = BKOOLParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 249
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 250
                        self.match(BKOOLParser.DOT)
                        self.state = 251
                        self.match(BKOOLParser.ID)
                        self.state = 257
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                        if la_ == 1:
                            self.state = 252
                            self.match(BKOOLParser.LB)
                            self.state = 254
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.INT_LIT) | (1 << BKOOLParser.FLOAT_LIT) | (1 << BKOOLParser.BOOL_LIT) | (1 << BKOOLParser.STR_LIT) | (1 << BKOOLParser.NEW) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.ID))) != 0):
                                self.state = 253
                                self.list_exp()


                            self.state = 256
                            self.match(BKOOLParser.RB)


                        pass

                    elif la_ == 8:
                        localctx = BKOOLParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 259
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 260
                        self.match(BKOOLParser.LQB)
                        self.state = 261
                        self.exp(0)
                        self.state = 262
                        self.match(BKOOLParser.RQR)
                        pass

             
                self.state = 268
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExpContext,i)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def LQB(self):
            return self.getToken(BKOOLParser.LQB, 0)

        def RQR(self):
            return self.getToken(BKOOLParser.RQR, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_lhs




    def lhs(self):

        localctx = BKOOLParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_lhs)
        try:
            self.state = 279
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 269
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 270
                self.exp(0)
                self.state = 271
                self.match(BKOOLParser.DOT)
                self.state = 272
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 274
                self.exp(0)
                self.state = 275
                self.match(BKOOLParser.LQB)
                self.state = 276
                self.exp(0)
                self.state = 277
                self.match(BKOOLParser.RQR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(BKOOLParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(BKOOLParser.FLOAT_LIT, 0)

        def STR_LIT(self):
            return self.getToken(BKOOLParser.STR_LIT, 0)

        def BOOL_LIT(self):
            return self.getToken(BKOOLParser.BOOL_LIT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_literal




    def literal(self):

        localctx = BKOOLParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.INT_LIT) | (1 << BKOOLParser.FLOAT_LIT) | (1 << BKOOLParser.BOOL_LIT) | (1 << BKOOLParser.STR_LIT))) != 0)):
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


    class BktypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(BKOOLParser.INT, 0)

        def VOID(self):
            return self.getToken(BKOOLParser.VOID, 0)

        def FLOAT(self):
            return self.getToken(BKOOLParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(BKOOLParser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(BKOOLParser.BOOLEAN, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LQB(self):
            return self.getToken(BKOOLParser.LQB, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def RQR(self):
            return self.getToken(BKOOLParser.RQR, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_bktype




    def bktype(self):

        localctx = BKOOLParser.BktypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_bktype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.VOID) | (1 << BKOOLParser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 288
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.LQB:
                self.state = 284
                self.match(BKOOLParser.LQB)
                self.state = 285
                self.exp(0)
                self.state = 286
                self.match(BKOOLParser.RQR)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.LiteralContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.LiteralContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.CM)
            else:
                return self.getToken(BKOOLParser.CM, i)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.WS)
            else:
                return self.getToken(BKOOLParser.WS, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_array_lit




    def array_lit(self):

        localctx = BKOOLParser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_array_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.match(BKOOLParser.LP)
            self.state = 302
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.INT_LIT) | (1 << BKOOLParser.FLOAT_LIT) | (1 << BKOOLParser.BOOL_LIT) | (1 << BKOOLParser.STR_LIT))) != 0):
                self.state = 291
                self.literal()
                self.state = 299
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKOOLParser.CM:
                    self.state = 292
                    self.match(BKOOLParser.CM)
                    self.state = 294
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==BKOOLParser.WS:
                        self.state = 293
                        self.match(BKOOLParser.WS)


                    self.state = 296
                    self.literal()
                    self.state = 301
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 304
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListIDContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def CM(self):
            return self.getToken(BKOOLParser.CM, 0)

        def listID(self):
            return self.getTypedRuleContext(BKOOLParser.ListIDContext,0)


        def ASSIGN(self):
            return self.getToken(BKOOLParser.ASSIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_listID




    def listID(self):

        localctx = BKOOLParser.ListIDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_listID)
        self._la = 0 # Token type
        try:
            self.state = 318
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 306
                self.match(BKOOLParser.ID)
                self.state = 309
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.ASSIGN:
                    self.state = 307
                    self.match(BKOOLParser.ASSIGN)
                    self.state = 308
                    self.exp(0)


                self.state = 311
                self.match(BKOOLParser.CM)
                self.state = 312
                self.listID()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 313
                self.match(BKOOLParser.ID)
                self.state = 316
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.ASSIGN:
                    self.state = 314
                    self.match(BKOOLParser.ASSIGN)
                    self.state = 315
                    self.exp(0)


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ids_attContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def CM(self):
            return self.getToken(BKOOLParser.CM, 0)

        def ids_att(self):
            return self.getTypedRuleContext(BKOOLParser.Ids_attContext,0)


        def ASSIGN_ATT(self):
            return self.getToken(BKOOLParser.ASSIGN_ATT, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_ids_att




    def ids_att(self):

        localctx = BKOOLParser.Ids_attContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_ids_att)
        self._la = 0 # Token type
        try:
            self.state = 332
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 320
                self.match(BKOOLParser.ID)
                self.state = 323
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.ASSIGN_ATT:
                    self.state = 321
                    self.match(BKOOLParser.ASSIGN_ATT)
                    self.state = 322
                    self.exp(0)


                self.state = 325
                self.match(BKOOLParser.CM)
                self.state = 326
                self.ids_att()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 327
                self.match(BKOOLParser.ID)
                self.state = 330
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.ASSIGN_ATT:
                    self.state = 328
                    self.match(BKOOLParser.ASSIGN_ATT)
                    self.state = 329
                    self.exp(0)


                pass


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
        self._predicates[17] = self.exp_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp_sempred(self, localctx:ExpContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 13)
         




