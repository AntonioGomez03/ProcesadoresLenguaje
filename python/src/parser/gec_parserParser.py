# Generated from gec_parser.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,34,288,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,1,0,1,0,1,
        0,1,1,1,1,1,1,1,1,1,1,1,1,5,1,49,8,1,10,1,12,1,52,9,1,1,1,1,1,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,63,8,2,10,2,12,2,66,9,2,1,2,1,2,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,81,8,3,10,3,12,3,84,
        9,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,95,8,4,1,5,1,5,1,5,5,
        5,100,8,5,10,5,12,5,103,9,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,137,8,6,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,1,7,1,8,1,8,1,8,1,8,3,8,152,8,8,1,8,1,8,1,8,1,8,3,8,158,
        8,8,5,8,160,8,8,10,8,12,8,163,9,8,1,8,1,8,1,8,3,8,168,8,8,1,9,1,
        9,1,9,1,9,1,9,3,9,175,8,9,1,10,1,10,1,10,1,10,3,10,181,8,10,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,5,11,191,8,11,10,11,12,11,194,
        9,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,5,12,204,8,12,10,12,
        12,12,207,9,12,1,12,1,12,1,13,1,13,1,13,3,13,214,8,13,1,13,1,13,
        1,13,1,13,1,13,3,13,221,8,13,1,13,1,13,1,13,1,13,1,13,3,13,228,8,
        13,1,13,1,13,1,13,1,13,1,13,3,13,235,8,13,1,13,1,13,1,13,3,13,240,
        8,13,1,14,1,14,1,14,5,14,245,8,14,10,14,12,14,248,9,14,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,3,15,257,8,15,1,16,1,16,1,16,5,16,262,8,
        16,10,16,12,16,265,9,16,1,17,1,17,1,17,1,17,1,17,1,17,3,17,273,8,
        17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,284,8,18,1,
        18,1,18,1,18,0,0,19,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,
        34,36,0,1,1,0,11,12,310,0,38,1,0,0,0,2,42,1,0,0,0,4,55,1,0,0,0,6,
        69,1,0,0,0,8,94,1,0,0,0,10,96,1,0,0,0,12,136,1,0,0,0,14,138,1,0,
        0,0,16,167,1,0,0,0,18,169,1,0,0,0,20,180,1,0,0,0,22,182,1,0,0,0,
        24,197,1,0,0,0,26,239,1,0,0,0,28,241,1,0,0,0,30,256,1,0,0,0,32,258,
        1,0,0,0,34,272,1,0,0,0,36,283,1,0,0,0,38,39,3,2,1,0,39,40,3,4,2,
        0,40,41,5,0,0,1,41,1,1,0,0,0,42,43,5,1,0,0,43,44,5,2,0,0,44,45,5,
        17,0,0,45,46,5,18,0,0,46,50,5,19,0,0,47,49,3,8,4,0,48,47,1,0,0,0,
        49,52,1,0,0,0,50,48,1,0,0,0,50,51,1,0,0,0,51,53,1,0,0,0,52,50,1,
        0,0,0,53,54,5,20,0,0,54,3,1,0,0,0,55,56,5,1,0,0,56,57,5,3,0,0,57,
        58,5,17,0,0,58,59,3,32,16,0,59,60,5,18,0,0,60,64,5,19,0,0,61,63,
        3,6,3,0,62,61,1,0,0,0,63,66,1,0,0,0,64,62,1,0,0,0,64,65,1,0,0,0,
        65,67,1,0,0,0,66,64,1,0,0,0,67,68,5,20,0,0,68,5,1,0,0,0,69,70,5,
        1,0,0,70,71,5,6,0,0,71,72,5,17,0,0,72,73,3,32,16,0,73,74,5,23,0,
        0,74,75,3,28,14,0,75,76,5,23,0,0,76,77,3,28,14,0,77,78,5,18,0,0,
        78,82,5,19,0,0,79,81,3,8,4,0,80,79,1,0,0,0,81,84,1,0,0,0,82,80,1,
        0,0,0,82,83,1,0,0,0,83,85,1,0,0,0,84,82,1,0,0,0,85,86,5,20,0,0,86,
        7,1,0,0,0,87,95,3,26,13,0,88,95,3,14,7,0,89,95,3,18,9,0,90,95,3,
        22,11,0,91,95,3,24,12,0,92,95,3,36,18,0,93,95,3,20,10,0,94,87,1,
        0,0,0,94,88,1,0,0,0,94,89,1,0,0,0,94,90,1,0,0,0,94,91,1,0,0,0,94,
        92,1,0,0,0,94,93,1,0,0,0,95,9,1,0,0,0,96,97,5,11,0,0,97,101,5,17,
        0,0,98,100,3,28,14,0,99,98,1,0,0,0,100,103,1,0,0,0,101,99,1,0,0,
        0,101,102,1,0,0,0,102,104,1,0,0,0,103,101,1,0,0,0,104,105,5,23,0,
        0,105,106,3,28,14,0,106,107,5,23,0,0,107,108,3,28,14,0,108,109,5,
        23,0,0,109,110,3,28,14,0,110,111,5,23,0,0,111,112,3,32,16,0,112,
        113,5,23,0,0,113,114,5,28,0,0,114,115,5,18,0,0,115,11,1,0,0,0,116,
        117,5,12,0,0,117,118,5,17,0,0,118,119,3,32,16,0,119,120,5,23,0,0,
        120,121,3,28,14,0,121,122,5,23,0,0,122,123,3,28,14,0,123,124,5,23,
        0,0,124,125,3,28,14,0,125,126,5,18,0,0,126,137,1,0,0,0,127,128,5,
        12,0,0,128,129,5,17,0,0,129,130,3,32,16,0,130,131,5,23,0,0,131,132,
        3,28,14,0,132,133,5,23,0,0,133,134,3,28,14,0,134,135,5,18,0,0,135,
        137,1,0,0,0,136,116,1,0,0,0,136,127,1,0,0,0,137,13,1,0,0,0,138,139,
        5,13,0,0,139,140,5,24,0,0,140,141,7,0,0,0,141,142,5,25,0,0,142,143,
        1,0,0,0,143,144,5,28,0,0,144,145,5,26,0,0,145,146,3,16,8,0,146,15,
        1,0,0,0,147,151,5,21,0,0,148,152,5,28,0,0,149,152,3,10,5,0,150,152,
        3,12,6,0,151,148,1,0,0,0,151,149,1,0,0,0,151,150,1,0,0,0,152,161,
        1,0,0,0,153,157,5,23,0,0,154,158,5,28,0,0,155,158,3,10,5,0,156,158,
        3,12,6,0,157,154,1,0,0,0,157,155,1,0,0,0,157,156,1,0,0,0,158,160,
        1,0,0,0,159,153,1,0,0,0,160,163,1,0,0,0,161,159,1,0,0,0,161,162,
        1,0,0,0,162,164,1,0,0,0,163,161,1,0,0,0,164,168,5,22,0,0,165,166,
        5,21,0,0,166,168,5,22,0,0,167,147,1,0,0,0,167,165,1,0,0,0,168,17,
        1,0,0,0,169,170,5,5,0,0,170,174,5,28,0,0,171,175,5,28,0,0,172,175,
        3,12,6,0,173,175,3,10,5,0,174,171,1,0,0,0,174,172,1,0,0,0,174,173,
        1,0,0,0,175,19,1,0,0,0,176,177,5,4,0,0,177,181,5,28,0,0,178,179,
        5,4,0,0,179,181,3,10,5,0,180,176,1,0,0,0,180,178,1,0,0,0,181,21,
        1,0,0,0,182,183,5,7,0,0,183,184,5,28,0,0,184,185,5,8,0,0,185,186,
        5,29,0,0,186,187,5,9,0,0,187,188,5,29,0,0,188,192,5,19,0,0,189,191,
        3,8,4,0,190,189,1,0,0,0,191,194,1,0,0,0,192,190,1,0,0,0,192,193,
        1,0,0,0,193,195,1,0,0,0,194,192,1,0,0,0,195,196,5,20,0,0,196,23,
        1,0,0,0,197,198,5,7,0,0,198,199,5,28,0,0,199,200,5,10,0,0,200,201,
        5,28,0,0,201,205,5,19,0,0,202,204,3,8,4,0,203,202,1,0,0,0,204,207,
        1,0,0,0,205,203,1,0,0,0,205,206,1,0,0,0,206,208,1,0,0,0,207,205,
        1,0,0,0,208,209,5,20,0,0,209,25,1,0,0,0,210,214,5,14,0,0,211,214,
        5,15,0,0,212,214,1,0,0,0,213,210,1,0,0,0,213,211,1,0,0,0,213,212,
        1,0,0,0,214,215,1,0,0,0,215,216,5,28,0,0,216,217,5,26,0,0,217,240,
        3,28,14,0,218,221,5,16,0,0,219,221,1,0,0,0,220,218,1,0,0,0,220,219,
        1,0,0,0,221,222,1,0,0,0,222,223,5,28,0,0,223,224,5,26,0,0,224,240,
        3,32,16,0,225,228,5,11,0,0,226,228,1,0,0,0,227,225,1,0,0,0,227,226,
        1,0,0,0,228,229,1,0,0,0,229,230,5,28,0,0,230,231,5,26,0,0,231,240,
        3,10,5,0,232,235,5,12,0,0,233,235,1,0,0,0,234,232,1,0,0,0,234,233,
        1,0,0,0,235,236,1,0,0,0,236,237,5,28,0,0,237,238,5,26,0,0,238,240,
        3,12,6,0,239,213,1,0,0,0,239,220,1,0,0,0,239,227,1,0,0,0,239,234,
        1,0,0,0,240,27,1,0,0,0,241,246,3,30,15,0,242,243,5,27,0,0,243,245,
        3,30,15,0,244,242,1,0,0,0,245,248,1,0,0,0,246,244,1,0,0,0,246,247,
        1,0,0,0,247,29,1,0,0,0,248,246,1,0,0,0,249,257,5,29,0,0,250,257,
        5,30,0,0,251,257,5,28,0,0,252,253,5,17,0,0,253,254,3,28,14,0,254,
        255,5,18,0,0,255,257,1,0,0,0,256,249,1,0,0,0,256,250,1,0,0,0,256,
        251,1,0,0,0,256,252,1,0,0,0,257,31,1,0,0,0,258,263,3,34,17,0,259,
        260,5,27,0,0,260,262,3,34,17,0,261,259,1,0,0,0,262,265,1,0,0,0,263,
        261,1,0,0,0,263,264,1,0,0,0,264,33,1,0,0,0,265,263,1,0,0,0,266,273,
        5,31,0,0,267,273,5,28,0,0,268,269,5,17,0,0,269,270,3,32,16,0,270,
        271,5,18,0,0,271,273,1,0,0,0,272,266,1,0,0,0,272,267,1,0,0,0,272,
        268,1,0,0,0,273,35,1,0,0,0,274,284,5,14,0,0,275,284,5,16,0,0,276,
        284,5,15,0,0,277,284,5,11,0,0,278,284,5,12,0,0,279,280,5,13,0,0,
        280,281,5,24,0,0,281,282,7,0,0,0,282,284,5,25,0,0,283,274,1,0,0,
        0,283,275,1,0,0,0,283,276,1,0,0,0,283,277,1,0,0,0,283,278,1,0,0,
        0,283,279,1,0,0,0,284,285,1,0,0,0,285,286,5,28,0,0,286,37,1,0,0,
        0,24,50,64,82,94,101,136,151,157,161,167,174,180,192,205,213,220,
        227,234,239,246,256,263,272,283
    ]

class gec_parserParser ( Parser ):

    grammarFileName = "gec_parser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'DEFINE'", "'SETUP'", "'WORLD'", "'ADD'", 
                     "'APPEND'", "'SCENE'", "'FOR'", "'FROM'", "'TO'", "'IN'", 
                     "'CHUNK'", "'GAMEOBJECT'", "'LIST'", "'INT'", "'FLOAT'", 
                     "'STRING'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "','", "'<'", "'>'", "'='" ]

    symbolicNames = [ "<INVALID>", "DEFINE", "SETUP", "WORLD", "ADD", "APPEND", 
                      "SCENE", "FOR", "FROM", "TO", "IN", "CHUNK", "GAMEOBJECT", 
                      "LIST", "INT", "FLOAT", "STRING", "LPAREN", "RPAREN", 
                      "LBRACE", "RBRACE", "LSQUARE", "RSQUARE", "COMMA", 
                      "LT", "GT", "ASSIGN", "OP_ARIT", "ID", "INT_LITERAL", 
                      "FLOAT_LITERAL", "STRING_LITERAL", "COMMENT", "BLOCK_COMMENT", 
                      "WS" ]

    RULE_program = 0
    RULE_define_setup = 1
    RULE_define_world = 2
    RULE_define_scene = 3
    RULE_statement = 4
    RULE_chunk_constructor = 5
    RULE_gameobject_constructor = 6
    RULE_define_list = 7
    RULE_array = 8
    RULE_append_statement = 9
    RULE_add_statement = 10
    RULE_for_loop_number = 11
    RULE_for_loop_list = 12
    RULE_assignment = 13
    RULE_numeric_expression = 14
    RULE_numeric_expression_aux = 15
    RULE_string_expression = 16
    RULE_string_expression_aux = 17
    RULE_declaration = 18

    ruleNames =  [ "program", "define_setup", "define_world", "define_scene", 
                   "statement", "chunk_constructor", "gameobject_constructor", 
                   "define_list", "array", "append_statement", "add_statement", 
                   "for_loop_number", "for_loop_list", "assignment", "numeric_expression", 
                   "numeric_expression_aux", "string_expression", "string_expression_aux", 
                   "declaration" ]

    EOF = Token.EOF
    DEFINE=1
    SETUP=2
    WORLD=3
    ADD=4
    APPEND=5
    SCENE=6
    FOR=7
    FROM=8
    TO=9
    IN=10
    CHUNK=11
    GAMEOBJECT=12
    LIST=13
    INT=14
    FLOAT=15
    STRING=16
    LPAREN=17
    RPAREN=18
    LBRACE=19
    RBRACE=20
    LSQUARE=21
    RSQUARE=22
    COMMA=23
    LT=24
    GT=25
    ASSIGN=26
    OP_ARIT=27
    ID=28
    INT_LITERAL=29
    FLOAT_LITERAL=30
    STRING_LITERAL=31
    COMMENT=32
    BLOCK_COMMENT=33
    WS=34

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def define_setup(self):
            return self.getTypedRuleContext(gec_parserParser.Define_setupContext,0)


        def define_world(self):
            return self.getTypedRuleContext(gec_parserParser.Define_worldContext,0)


        def EOF(self):
            return self.getToken(gec_parserParser.EOF, 0)

        def getRuleIndex(self):
            return gec_parserParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = gec_parserParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.define_setup()
            self.state = 39
            self.define_world()
            self.state = 40
            self.match(gec_parserParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Define_setupContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFINE(self):
            return self.getToken(gec_parserParser.DEFINE, 0)

        def SETUP(self):
            return self.getToken(gec_parserParser.SETUP, 0)

        def LPAREN(self):
            return self.getToken(gec_parserParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(gec_parserParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(gec_parserParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(gec_parserParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gec_parserParser.StatementContext)
            else:
                return self.getTypedRuleContext(gec_parserParser.StatementContext,i)


        def getRuleIndex(self):
            return gec_parserParser.RULE_define_setup

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefine_setup" ):
                listener.enterDefine_setup(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefine_setup" ):
                listener.exitDefine_setup(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefine_setup" ):
                return visitor.visitDefine_setup(self)
            else:
                return visitor.visitChildren(self)




    def define_setup(self):

        localctx = gec_parserParser.Define_setupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_define_setup)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(gec_parserParser.DEFINE)
            self.state = 43
            self.match(gec_parserParser.SETUP)
            self.state = 44
            self.match(gec_parserParser.LPAREN)
            self.state = 45
            self.match(gec_parserParser.RPAREN)
            self.state = 46
            self.match(gec_parserParser.LBRACE)
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 268564656) != 0):
                self.state = 47
                self.statement()
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 53
            self.match(gec_parserParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Define_worldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFINE(self):
            return self.getToken(gec_parserParser.DEFINE, 0)

        def WORLD(self):
            return self.getToken(gec_parserParser.WORLD, 0)

        def LPAREN(self):
            return self.getToken(gec_parserParser.LPAREN, 0)

        def string_expression(self):
            return self.getTypedRuleContext(gec_parserParser.String_expressionContext,0)


        def RPAREN(self):
            return self.getToken(gec_parserParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(gec_parserParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(gec_parserParser.RBRACE, 0)

        def define_scene(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gec_parserParser.Define_sceneContext)
            else:
                return self.getTypedRuleContext(gec_parserParser.Define_sceneContext,i)


        def getRuleIndex(self):
            return gec_parserParser.RULE_define_world

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefine_world" ):
                listener.enterDefine_world(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefine_world" ):
                listener.exitDefine_world(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefine_world" ):
                return visitor.visitDefine_world(self)
            else:
                return visitor.visitChildren(self)




    def define_world(self):

        localctx = gec_parserParser.Define_worldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_define_world)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(gec_parserParser.DEFINE)
            self.state = 56
            self.match(gec_parserParser.WORLD)
            self.state = 57
            self.match(gec_parserParser.LPAREN)
            self.state = 58
            self.string_expression()
            self.state = 59
            self.match(gec_parserParser.RPAREN)
            self.state = 60
            self.match(gec_parserParser.LBRACE)
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 61
                self.define_scene()
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 67
            self.match(gec_parserParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Define_sceneContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFINE(self):
            return self.getToken(gec_parserParser.DEFINE, 0)

        def SCENE(self):
            return self.getToken(gec_parserParser.SCENE, 0)

        def LPAREN(self):
            return self.getToken(gec_parserParser.LPAREN, 0)

        def string_expression(self):
            return self.getTypedRuleContext(gec_parserParser.String_expressionContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(gec_parserParser.COMMA)
            else:
                return self.getToken(gec_parserParser.COMMA, i)

        def numeric_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gec_parserParser.Numeric_expressionContext)
            else:
                return self.getTypedRuleContext(gec_parserParser.Numeric_expressionContext,i)


        def RPAREN(self):
            return self.getToken(gec_parserParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(gec_parserParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(gec_parserParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gec_parserParser.StatementContext)
            else:
                return self.getTypedRuleContext(gec_parserParser.StatementContext,i)


        def getRuleIndex(self):
            return gec_parserParser.RULE_define_scene

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefine_scene" ):
                listener.enterDefine_scene(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefine_scene" ):
                listener.exitDefine_scene(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefine_scene" ):
                return visitor.visitDefine_scene(self)
            else:
                return visitor.visitChildren(self)




    def define_scene(self):

        localctx = gec_parserParser.Define_sceneContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_define_scene)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(gec_parserParser.DEFINE)
            self.state = 70
            self.match(gec_parserParser.SCENE)
            self.state = 71
            self.match(gec_parserParser.LPAREN)
            self.state = 72
            self.string_expression()
            self.state = 73
            self.match(gec_parserParser.COMMA)
            self.state = 74
            self.numeric_expression()
            self.state = 75
            self.match(gec_parserParser.COMMA)
            self.state = 76
            self.numeric_expression()
            self.state = 77
            self.match(gec_parserParser.RPAREN)
            self.state = 78
            self.match(gec_parserParser.LBRACE)
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 268564656) != 0):
                self.state = 79
                self.statement()
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 85
            self.match(gec_parserParser.RBRACE)
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

        def assignment(self):
            return self.getTypedRuleContext(gec_parserParser.AssignmentContext,0)


        def define_list(self):
            return self.getTypedRuleContext(gec_parserParser.Define_listContext,0)


        def append_statement(self):
            return self.getTypedRuleContext(gec_parserParser.Append_statementContext,0)


        def for_loop_number(self):
            return self.getTypedRuleContext(gec_parserParser.For_loop_numberContext,0)


        def for_loop_list(self):
            return self.getTypedRuleContext(gec_parserParser.For_loop_listContext,0)


        def declaration(self):
            return self.getTypedRuleContext(gec_parserParser.DeclarationContext,0)


        def add_statement(self):
            return self.getTypedRuleContext(gec_parserParser.Add_statementContext,0)


        def getRuleIndex(self):
            return gec_parserParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = gec_parserParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_statement)
        try:
            self.state = 94
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 88
                self.define_list()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 89
                self.append_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 90
                self.for_loop_number()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 91
                self.for_loop_list()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 92
                self.declaration()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 93
                self.add_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Chunk_constructorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHUNK(self):
            return self.getToken(gec_parserParser.CHUNK, 0)

        def LPAREN(self):
            return self.getToken(gec_parserParser.LPAREN, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(gec_parserParser.COMMA)
            else:
                return self.getToken(gec_parserParser.COMMA, i)

        def numeric_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gec_parserParser.Numeric_expressionContext)
            else:
                return self.getTypedRuleContext(gec_parserParser.Numeric_expressionContext,i)


        def string_expression(self):
            return self.getTypedRuleContext(gec_parserParser.String_expressionContext,0)


        def ID(self):
            return self.getToken(gec_parserParser.ID, 0)

        def RPAREN(self):
            return self.getToken(gec_parserParser.RPAREN, 0)

        def getRuleIndex(self):
            return gec_parserParser.RULE_chunk_constructor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChunk_constructor" ):
                listener.enterChunk_constructor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChunk_constructor" ):
                listener.exitChunk_constructor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChunk_constructor" ):
                return visitor.visitChunk_constructor(self)
            else:
                return visitor.visitChildren(self)




    def chunk_constructor(self):

        localctx = gec_parserParser.Chunk_constructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_chunk_constructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(gec_parserParser.CHUNK)
            self.state = 97
            self.match(gec_parserParser.LPAREN)
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1879179264) != 0):
                self.state = 98
                self.numeric_expression()
                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 104
            self.match(gec_parserParser.COMMA)
            self.state = 105
            self.numeric_expression()
            self.state = 106
            self.match(gec_parserParser.COMMA)
            self.state = 107
            self.numeric_expression()
            self.state = 108
            self.match(gec_parserParser.COMMA)
            self.state = 109
            self.numeric_expression()
            self.state = 110
            self.match(gec_parserParser.COMMA)
            self.state = 111
            self.string_expression()
            self.state = 112
            self.match(gec_parserParser.COMMA)
            self.state = 113
            self.match(gec_parserParser.ID)
            self.state = 114
            self.match(gec_parserParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Gameobject_constructorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GAMEOBJECT(self):
            return self.getToken(gec_parserParser.GAMEOBJECT, 0)

        def LPAREN(self):
            return self.getToken(gec_parserParser.LPAREN, 0)

        def string_expression(self):
            return self.getTypedRuleContext(gec_parserParser.String_expressionContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(gec_parserParser.COMMA)
            else:
                return self.getToken(gec_parserParser.COMMA, i)

        def numeric_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gec_parserParser.Numeric_expressionContext)
            else:
                return self.getTypedRuleContext(gec_parserParser.Numeric_expressionContext,i)


        def RPAREN(self):
            return self.getToken(gec_parserParser.RPAREN, 0)

        def getRuleIndex(self):
            return gec_parserParser.RULE_gameobject_constructor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGameobject_constructor" ):
                listener.enterGameobject_constructor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGameobject_constructor" ):
                listener.exitGameobject_constructor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGameobject_constructor" ):
                return visitor.visitGameobject_constructor(self)
            else:
                return visitor.visitChildren(self)




    def gameobject_constructor(self):

        localctx = gec_parserParser.Gameobject_constructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_gameobject_constructor)
        try:
            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 116
                self.match(gec_parserParser.GAMEOBJECT)
                self.state = 117
                self.match(gec_parserParser.LPAREN)
                self.state = 118
                self.string_expression()
                self.state = 119
                self.match(gec_parserParser.COMMA)
                self.state = 120
                self.numeric_expression()
                self.state = 121
                self.match(gec_parserParser.COMMA)
                self.state = 122
                self.numeric_expression()
                self.state = 123
                self.match(gec_parserParser.COMMA)
                self.state = 124
                self.numeric_expression()
                self.state = 125
                self.match(gec_parserParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
                self.match(gec_parserParser.GAMEOBJECT)
                self.state = 128
                self.match(gec_parserParser.LPAREN)
                self.state = 129
                self.string_expression()
                self.state = 130
                self.match(gec_parserParser.COMMA)
                self.state = 131
                self.numeric_expression()
                self.state = 132
                self.match(gec_parserParser.COMMA)
                self.state = 133
                self.numeric_expression()
                self.state = 134
                self.match(gec_parserParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Define_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(gec_parserParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(gec_parserParser.ASSIGN, 0)

        def array(self):
            return self.getTypedRuleContext(gec_parserParser.ArrayContext,0)


        def LIST(self):
            return self.getToken(gec_parserParser.LIST, 0)

        def LT(self):
            return self.getToken(gec_parserParser.LT, 0)

        def GT(self):
            return self.getToken(gec_parserParser.GT, 0)

        def CHUNK(self):
            return self.getToken(gec_parserParser.CHUNK, 0)

        def GAMEOBJECT(self):
            return self.getToken(gec_parserParser.GAMEOBJECT, 0)

        def getRuleIndex(self):
            return gec_parserParser.RULE_define_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefine_list" ):
                listener.enterDefine_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefine_list" ):
                listener.exitDefine_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefine_list" ):
                return visitor.visitDefine_list(self)
            else:
                return visitor.visitChildren(self)




    def define_list(self):

        localctx = gec_parserParser.Define_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_define_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(gec_parserParser.LIST)
            self.state = 139
            self.match(gec_parserParser.LT)
            self.state = 140
            _la = self._input.LA(1)
            if not(_la==11 or _la==12):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 141
            self.match(gec_parserParser.GT)
            self.state = 143
            self.match(gec_parserParser.ID)
            self.state = 144
            self.match(gec_parserParser.ASSIGN)
            self.state = 145
            self.array()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSQUARE(self):
            return self.getToken(gec_parserParser.LSQUARE, 0)

        def RSQUARE(self):
            return self.getToken(gec_parserParser.RSQUARE, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(gec_parserParser.ID)
            else:
                return self.getToken(gec_parserParser.ID, i)

        def chunk_constructor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gec_parserParser.Chunk_constructorContext)
            else:
                return self.getTypedRuleContext(gec_parserParser.Chunk_constructorContext,i)


        def gameobject_constructor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gec_parserParser.Gameobject_constructorContext)
            else:
                return self.getTypedRuleContext(gec_parserParser.Gameobject_constructorContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(gec_parserParser.COMMA)
            else:
                return self.getToken(gec_parserParser.COMMA, i)

        def getRuleIndex(self):
            return gec_parserParser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = gec_parserParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.state = 167
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.match(gec_parserParser.LSQUARE)
                self.state = 151
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [28]:
                    self.state = 148
                    self.match(gec_parserParser.ID)
                    pass
                elif token in [11]:
                    self.state = 149
                    self.chunk_constructor()
                    pass
                elif token in [12]:
                    self.state = 150
                    self.gameobject_constructor()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==23:
                    self.state = 153
                    self.match(gec_parserParser.COMMA)
                    self.state = 157
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [28]:
                        self.state = 154
                        self.match(gec_parserParser.ID)
                        pass
                    elif token in [11]:
                        self.state = 155
                        self.chunk_constructor()
                        pass
                    elif token in [12]:
                        self.state = 156
                        self.gameobject_constructor()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 163
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 164
                self.match(gec_parserParser.RSQUARE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 165
                self.match(gec_parserParser.LSQUARE)
                self.state = 166
                self.match(gec_parserParser.RSQUARE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Append_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def APPEND(self):
            return self.getToken(gec_parserParser.APPEND, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(gec_parserParser.ID)
            else:
                return self.getToken(gec_parserParser.ID, i)

        def gameobject_constructor(self):
            return self.getTypedRuleContext(gec_parserParser.Gameobject_constructorContext,0)


        def chunk_constructor(self):
            return self.getTypedRuleContext(gec_parserParser.Chunk_constructorContext,0)


        def getRuleIndex(self):
            return gec_parserParser.RULE_append_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAppend_statement" ):
                listener.enterAppend_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAppend_statement" ):
                listener.exitAppend_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAppend_statement" ):
                return visitor.visitAppend_statement(self)
            else:
                return visitor.visitChildren(self)




    def append_statement(self):

        localctx = gec_parserParser.Append_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_append_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(gec_parserParser.APPEND)
            self.state = 170
            self.match(gec_parserParser.ID)
            self.state = 174
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.state = 171
                self.match(gec_parserParser.ID)
                pass
            elif token in [12]:
                self.state = 172
                self.gameobject_constructor()
                pass
            elif token in [11]:
                self.state = 173
                self.chunk_constructor()
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


    class Add_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(gec_parserParser.ADD, 0)

        def ID(self):
            return self.getToken(gec_parserParser.ID, 0)

        def chunk_constructor(self):
            return self.getTypedRuleContext(gec_parserParser.Chunk_constructorContext,0)


        def getRuleIndex(self):
            return gec_parserParser.RULE_add_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd_statement" ):
                listener.enterAdd_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd_statement" ):
                listener.exitAdd_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd_statement" ):
                return visitor.visitAdd_statement(self)
            else:
                return visitor.visitChildren(self)




    def add_statement(self):

        localctx = gec_parserParser.Add_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_add_statement)
        try:
            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 176
                self.match(gec_parserParser.ADD)
                self.state = 177
                self.match(gec_parserParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self.match(gec_parserParser.ADD)
                self.state = 179
                self.chunk_constructor()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_loop_numberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(gec_parserParser.FOR, 0)

        def ID(self):
            return self.getToken(gec_parserParser.ID, 0)

        def FROM(self):
            return self.getToken(gec_parserParser.FROM, 0)

        def INT_LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(gec_parserParser.INT_LITERAL)
            else:
                return self.getToken(gec_parserParser.INT_LITERAL, i)

        def TO(self):
            return self.getToken(gec_parserParser.TO, 0)

        def LBRACE(self):
            return self.getToken(gec_parserParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(gec_parserParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gec_parserParser.StatementContext)
            else:
                return self.getTypedRuleContext(gec_parserParser.StatementContext,i)


        def getRuleIndex(self):
            return gec_parserParser.RULE_for_loop_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_loop_number" ):
                listener.enterFor_loop_number(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_loop_number" ):
                listener.exitFor_loop_number(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_loop_number" ):
                return visitor.visitFor_loop_number(self)
            else:
                return visitor.visitChildren(self)




    def for_loop_number(self):

        localctx = gec_parserParser.For_loop_numberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_for_loop_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(gec_parserParser.FOR)
            self.state = 183
            self.match(gec_parserParser.ID)
            self.state = 184
            self.match(gec_parserParser.FROM)
            self.state = 185
            self.match(gec_parserParser.INT_LITERAL)
            self.state = 186
            self.match(gec_parserParser.TO)
            self.state = 187
            self.match(gec_parserParser.INT_LITERAL)
            self.state = 188
            self.match(gec_parserParser.LBRACE)
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 268564656) != 0):
                self.state = 189
                self.statement()
                self.state = 194
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 195
            self.match(gec_parserParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_loop_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(gec_parserParser.FOR, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(gec_parserParser.ID)
            else:
                return self.getToken(gec_parserParser.ID, i)

        def IN(self):
            return self.getToken(gec_parserParser.IN, 0)

        def LBRACE(self):
            return self.getToken(gec_parserParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(gec_parserParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gec_parserParser.StatementContext)
            else:
                return self.getTypedRuleContext(gec_parserParser.StatementContext,i)


        def getRuleIndex(self):
            return gec_parserParser.RULE_for_loop_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_loop_list" ):
                listener.enterFor_loop_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_loop_list" ):
                listener.exitFor_loop_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_loop_list" ):
                return visitor.visitFor_loop_list(self)
            else:
                return visitor.visitChildren(self)




    def for_loop_list(self):

        localctx = gec_parserParser.For_loop_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_for_loop_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(gec_parserParser.FOR)
            self.state = 198
            self.match(gec_parserParser.ID)
            self.state = 199
            self.match(gec_parserParser.IN)
            self.state = 200
            self.match(gec_parserParser.ID)
            self.state = 201
            self.match(gec_parserParser.LBRACE)
            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 268564656) != 0):
                self.state = 202
                self.statement()
                self.state = 207
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 208
            self.match(gec_parserParser.RBRACE)
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

        def ID(self):
            return self.getToken(gec_parserParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(gec_parserParser.ASSIGN, 0)

        def numeric_expression(self):
            return self.getTypedRuleContext(gec_parserParser.Numeric_expressionContext,0)


        def INT(self):
            return self.getToken(gec_parserParser.INT, 0)

        def FLOAT(self):
            return self.getToken(gec_parserParser.FLOAT, 0)

        def string_expression(self):
            return self.getTypedRuleContext(gec_parserParser.String_expressionContext,0)


        def STRING(self):
            return self.getToken(gec_parserParser.STRING, 0)

        def chunk_constructor(self):
            return self.getTypedRuleContext(gec_parserParser.Chunk_constructorContext,0)


        def CHUNK(self):
            return self.getToken(gec_parserParser.CHUNK, 0)

        def gameobject_constructor(self):
            return self.getTypedRuleContext(gec_parserParser.Gameobject_constructorContext,0)


        def GAMEOBJECT(self):
            return self.getToken(gec_parserParser.GAMEOBJECT, 0)

        def getRuleIndex(self):
            return gec_parserParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = gec_parserParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_assignment)
        try:
            self.state = 239
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [14]:
                    self.state = 210
                    self.match(gec_parserParser.INT)
                    pass
                elif token in [15]:
                    self.state = 211
                    self.match(gec_parserParser.FLOAT)
                    pass
                elif token in [28]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 215
                self.match(gec_parserParser.ID)
                self.state = 216
                self.match(gec_parserParser.ASSIGN)
                self.state = 217
                self.numeric_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [16]:
                    self.state = 218
                    self.match(gec_parserParser.STRING)
                    pass
                elif token in [28]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 222
                self.match(gec_parserParser.ID)
                self.state = 223
                self.match(gec_parserParser.ASSIGN)
                self.state = 224
                self.string_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 227
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [11]:
                    self.state = 225
                    self.match(gec_parserParser.CHUNK)
                    pass
                elif token in [28]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 229
                self.match(gec_parserParser.ID)
                self.state = 230
                self.match(gec_parserParser.ASSIGN)
                self.state = 231
                self.chunk_constructor()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 234
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [12]:
                    self.state = 232
                    self.match(gec_parserParser.GAMEOBJECT)
                    pass
                elif token in [28]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 236
                self.match(gec_parserParser.ID)
                self.state = 237
                self.match(gec_parserParser.ASSIGN)
                self.state = 238
                self.gameobject_constructor()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Numeric_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numeric_expression_aux(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gec_parserParser.Numeric_expression_auxContext)
            else:
                return self.getTypedRuleContext(gec_parserParser.Numeric_expression_auxContext,i)


        def OP_ARIT(self, i:int=None):
            if i is None:
                return self.getTokens(gec_parserParser.OP_ARIT)
            else:
                return self.getToken(gec_parserParser.OP_ARIT, i)

        def getRuleIndex(self):
            return gec_parserParser.RULE_numeric_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumeric_expression" ):
                listener.enterNumeric_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumeric_expression" ):
                listener.exitNumeric_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumeric_expression" ):
                return visitor.visitNumeric_expression(self)
            else:
                return visitor.visitChildren(self)




    def numeric_expression(self):

        localctx = gec_parserParser.Numeric_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_numeric_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.numeric_expression_aux()
            self.state = 246
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27:
                self.state = 242
                self.match(gec_parserParser.OP_ARIT)
                self.state = 243
                self.numeric_expression_aux()
                self.state = 248
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Numeric_expression_auxContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LITERAL(self):
            return self.getToken(gec_parserParser.INT_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(gec_parserParser.FLOAT_LITERAL, 0)

        def ID(self):
            return self.getToken(gec_parserParser.ID, 0)

        def LPAREN(self):
            return self.getToken(gec_parserParser.LPAREN, 0)

        def numeric_expression(self):
            return self.getTypedRuleContext(gec_parserParser.Numeric_expressionContext,0)


        def RPAREN(self):
            return self.getToken(gec_parserParser.RPAREN, 0)

        def getRuleIndex(self):
            return gec_parserParser.RULE_numeric_expression_aux

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumeric_expression_aux" ):
                listener.enterNumeric_expression_aux(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumeric_expression_aux" ):
                listener.exitNumeric_expression_aux(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumeric_expression_aux" ):
                return visitor.visitNumeric_expression_aux(self)
            else:
                return visitor.visitChildren(self)




    def numeric_expression_aux(self):

        localctx = gec_parserParser.Numeric_expression_auxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_numeric_expression_aux)
        try:
            self.state = 256
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29]:
                self.enterOuterAlt(localctx, 1)
                self.state = 249
                self.match(gec_parserParser.INT_LITERAL)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
                self.match(gec_parserParser.FLOAT_LITERAL)
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 3)
                self.state = 251
                self.match(gec_parserParser.ID)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 4)
                self.state = 252
                self.match(gec_parserParser.LPAREN)
                self.state = 253
                self.numeric_expression()
                self.state = 254
                self.match(gec_parserParser.RPAREN)
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


    class String_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string_expression_aux(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gec_parserParser.String_expression_auxContext)
            else:
                return self.getTypedRuleContext(gec_parserParser.String_expression_auxContext,i)


        def OP_ARIT(self, i:int=None):
            if i is None:
                return self.getTokens(gec_parserParser.OP_ARIT)
            else:
                return self.getToken(gec_parserParser.OP_ARIT, i)

        def getRuleIndex(self):
            return gec_parserParser.RULE_string_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString_expression" ):
                listener.enterString_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString_expression" ):
                listener.exitString_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_expression" ):
                return visitor.visitString_expression(self)
            else:
                return visitor.visitChildren(self)




    def string_expression(self):

        localctx = gec_parserParser.String_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_string_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.string_expression_aux()
            self.state = 263
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27:
                self.state = 259
                self.match(gec_parserParser.OP_ARIT)
                self.state = 260
                self.string_expression_aux()
                self.state = 265
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_expression_auxContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_LITERAL(self):
            return self.getToken(gec_parserParser.STRING_LITERAL, 0)

        def ID(self):
            return self.getToken(gec_parserParser.ID, 0)

        def LPAREN(self):
            return self.getToken(gec_parserParser.LPAREN, 0)

        def string_expression(self):
            return self.getTypedRuleContext(gec_parserParser.String_expressionContext,0)


        def RPAREN(self):
            return self.getToken(gec_parserParser.RPAREN, 0)

        def getRuleIndex(self):
            return gec_parserParser.RULE_string_expression_aux

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString_expression_aux" ):
                listener.enterString_expression_aux(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString_expression_aux" ):
                listener.exitString_expression_aux(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_expression_aux" ):
                return visitor.visitString_expression_aux(self)
            else:
                return visitor.visitChildren(self)




    def string_expression_aux(self):

        localctx = gec_parserParser.String_expression_auxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_string_expression_aux)
        try:
            self.state = 272
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 266
                self.match(gec_parserParser.STRING_LITERAL)
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 267
                self.match(gec_parserParser.ID)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 3)
                self.state = 268
                self.match(gec_parserParser.LPAREN)
                self.state = 269
                self.string_expression()
                self.state = 270
                self.match(gec_parserParser.RPAREN)
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


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(gec_parserParser.ID, 0)

        def INT(self):
            return self.getToken(gec_parserParser.INT, 0)

        def STRING(self):
            return self.getToken(gec_parserParser.STRING, 0)

        def FLOAT(self):
            return self.getToken(gec_parserParser.FLOAT, 0)

        def CHUNK(self):
            return self.getToken(gec_parserParser.CHUNK, 0)

        def GAMEOBJECT(self):
            return self.getToken(gec_parserParser.GAMEOBJECT, 0)

        def LIST(self):
            return self.getToken(gec_parserParser.LIST, 0)

        def LT(self):
            return self.getToken(gec_parserParser.LT, 0)

        def GT(self):
            return self.getToken(gec_parserParser.GT, 0)

        def getRuleIndex(self):
            return gec_parserParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = gec_parserParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.state = 274
                self.match(gec_parserParser.INT)
                pass
            elif token in [16]:
                self.state = 275
                self.match(gec_parserParser.STRING)
                pass
            elif token in [15]:
                self.state = 276
                self.match(gec_parserParser.FLOAT)
                pass
            elif token in [11]:
                self.state = 277
                self.match(gec_parserParser.CHUNK)
                pass
            elif token in [12]:
                self.state = 278
                self.match(gec_parserParser.GAMEOBJECT)
                pass
            elif token in [13]:
                self.state = 279
                self.match(gec_parserParser.LIST)
                self.state = 280
                self.match(gec_parserParser.LT)
                self.state = 281
                _la = self._input.LA(1)
                if not(_la==11 or _la==12):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 282
                self.match(gec_parserParser.GT)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 285
            self.match(gec_parserParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





