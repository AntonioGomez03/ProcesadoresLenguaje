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
        4,1,34,256,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,
        1,1,1,5,1,45,8,1,10,1,12,1,48,9,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,5,2,59,8,2,10,2,12,2,62,9,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,5,3,77,8,3,10,3,12,3,80,9,3,1,3,1,3,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,3,4,91,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,126,8,6,1,7,1,7,1,7,1,7,
        1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,3,8,141,8,8,1,8,1,8,1,8,1,8,
        3,8,147,8,8,5,8,149,8,8,10,8,12,8,152,9,8,1,8,1,8,1,8,3,8,157,8,
        8,1,9,1,9,1,9,1,9,1,9,3,9,164,8,9,1,10,1,10,1,10,1,10,3,10,170,8,
        10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,5,11,180,8,11,10,11,12,
        11,183,9,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,5,12,193,8,12,
        10,12,12,12,196,9,12,1,12,1,12,1,13,1,13,1,13,1,13,3,13,204,8,13,
        1,13,1,13,1,13,1,13,1,13,3,13,211,8,13,1,13,1,13,1,13,1,13,1,13,
        3,13,218,8,13,1,13,1,13,1,13,3,13,223,8,13,1,14,1,14,1,14,5,14,228,
        8,14,10,14,12,14,231,9,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        3,15,241,8,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,
        252,8,16,1,16,1,16,1,16,0,0,17,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,28,30,32,0,4,2,0,28,28,31,31,1,0,28,29,2,0,28,28,30,30,1,0,11,
        12,276,0,34,1,0,0,0,2,38,1,0,0,0,4,51,1,0,0,0,6,65,1,0,0,0,8,90,
        1,0,0,0,10,92,1,0,0,0,12,125,1,0,0,0,14,127,1,0,0,0,16,156,1,0,0,
        0,18,158,1,0,0,0,20,169,1,0,0,0,22,171,1,0,0,0,24,186,1,0,0,0,26,
        222,1,0,0,0,28,224,1,0,0,0,30,240,1,0,0,0,32,251,1,0,0,0,34,35,3,
        2,1,0,35,36,3,4,2,0,36,37,5,0,0,1,37,1,1,0,0,0,38,39,5,1,0,0,39,
        40,5,2,0,0,40,41,5,17,0,0,41,42,5,18,0,0,42,46,5,19,0,0,43,45,3,
        8,4,0,44,43,1,0,0,0,45,48,1,0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,
        49,1,0,0,0,48,46,1,0,0,0,49,50,5,20,0,0,50,3,1,0,0,0,51,52,5,1,0,
        0,52,53,5,3,0,0,53,54,5,17,0,0,54,55,7,0,0,0,55,56,5,18,0,0,56,60,
        5,19,0,0,57,59,3,6,3,0,58,57,1,0,0,0,59,62,1,0,0,0,60,58,1,0,0,0,
        60,61,1,0,0,0,61,63,1,0,0,0,62,60,1,0,0,0,63,64,5,20,0,0,64,5,1,
        0,0,0,65,66,5,1,0,0,66,67,5,6,0,0,67,68,5,17,0,0,68,69,7,0,0,0,69,
        70,5,23,0,0,70,71,7,1,0,0,71,72,5,23,0,0,72,73,7,1,0,0,73,74,5,18,
        0,0,74,78,5,19,0,0,75,77,3,8,4,0,76,75,1,0,0,0,77,80,1,0,0,0,78,
        76,1,0,0,0,78,79,1,0,0,0,79,81,1,0,0,0,80,78,1,0,0,0,81,82,5,20,
        0,0,82,7,1,0,0,0,83,91,3,26,13,0,84,91,3,14,7,0,85,91,3,18,9,0,86,
        91,3,22,11,0,87,91,3,24,12,0,88,91,3,32,16,0,89,91,3,20,10,0,90,
        83,1,0,0,0,90,84,1,0,0,0,90,85,1,0,0,0,90,86,1,0,0,0,90,87,1,0,0,
        0,90,88,1,0,0,0,90,89,1,0,0,0,91,9,1,0,0,0,92,93,5,11,0,0,93,94,
        5,17,0,0,94,95,7,1,0,0,95,96,5,23,0,0,96,97,7,1,0,0,97,98,5,23,0,
        0,98,99,7,2,0,0,99,100,5,23,0,0,100,101,7,2,0,0,101,102,5,23,0,0,
        102,103,7,0,0,0,103,104,5,23,0,0,104,105,5,28,0,0,105,106,5,18,0,
        0,106,11,1,0,0,0,107,108,5,12,0,0,108,109,5,17,0,0,109,110,7,0,0,
        0,110,111,5,23,0,0,111,112,7,1,0,0,112,113,5,23,0,0,113,114,7,2,
        0,0,114,115,5,23,0,0,115,116,7,2,0,0,116,126,5,18,0,0,117,118,5,
        12,0,0,118,119,5,17,0,0,119,120,7,0,0,0,120,121,5,23,0,0,121,122,
        7,1,0,0,122,123,5,23,0,0,123,124,7,2,0,0,124,126,5,18,0,0,125,107,
        1,0,0,0,125,117,1,0,0,0,126,13,1,0,0,0,127,128,5,13,0,0,128,129,
        5,24,0,0,129,130,7,3,0,0,130,131,5,25,0,0,131,132,1,0,0,0,132,133,
        5,28,0,0,133,134,5,26,0,0,134,135,3,16,8,0,135,15,1,0,0,0,136,140,
        5,21,0,0,137,141,5,28,0,0,138,141,3,10,5,0,139,141,3,12,6,0,140,
        137,1,0,0,0,140,138,1,0,0,0,140,139,1,0,0,0,141,150,1,0,0,0,142,
        146,5,23,0,0,143,147,5,28,0,0,144,147,3,10,5,0,145,147,3,12,6,0,
        146,143,1,0,0,0,146,144,1,0,0,0,146,145,1,0,0,0,147,149,1,0,0,0,
        148,142,1,0,0,0,149,152,1,0,0,0,150,148,1,0,0,0,150,151,1,0,0,0,
        151,153,1,0,0,0,152,150,1,0,0,0,153,157,5,22,0,0,154,155,5,21,0,
        0,155,157,5,22,0,0,156,136,1,0,0,0,156,154,1,0,0,0,157,17,1,0,0,
        0,158,159,5,5,0,0,159,163,5,28,0,0,160,164,5,28,0,0,161,164,3,12,
        6,0,162,164,3,10,5,0,163,160,1,0,0,0,163,161,1,0,0,0,163,162,1,0,
        0,0,164,19,1,0,0,0,165,166,5,4,0,0,166,170,5,28,0,0,167,168,5,4,
        0,0,168,170,3,10,5,0,169,165,1,0,0,0,169,167,1,0,0,0,170,21,1,0,
        0,0,171,172,5,7,0,0,172,173,5,28,0,0,173,174,5,8,0,0,174,175,5,29,
        0,0,175,176,5,9,0,0,176,177,5,29,0,0,177,181,5,19,0,0,178,180,3,
        8,4,0,179,178,1,0,0,0,180,183,1,0,0,0,181,179,1,0,0,0,181,182,1,
        0,0,0,182,184,1,0,0,0,183,181,1,0,0,0,184,185,5,20,0,0,185,23,1,
        0,0,0,186,187,5,7,0,0,187,188,5,28,0,0,188,189,5,10,0,0,189,190,
        5,28,0,0,190,194,5,19,0,0,191,193,3,8,4,0,192,191,1,0,0,0,193,196,
        1,0,0,0,194,192,1,0,0,0,194,195,1,0,0,0,195,197,1,0,0,0,196,194,
        1,0,0,0,197,198,5,20,0,0,198,25,1,0,0,0,199,204,5,14,0,0,200,204,
        5,16,0,0,201,204,5,15,0,0,202,204,1,0,0,0,203,199,1,0,0,0,203,200,
        1,0,0,0,203,201,1,0,0,0,203,202,1,0,0,0,204,205,1,0,0,0,205,206,
        5,28,0,0,206,207,5,26,0,0,207,223,3,28,14,0,208,211,5,11,0,0,209,
        211,1,0,0,0,210,208,1,0,0,0,210,209,1,0,0,0,211,212,1,0,0,0,212,
        213,5,28,0,0,213,214,5,26,0,0,214,223,3,10,5,0,215,218,5,12,0,0,
        216,218,1,0,0,0,217,215,1,0,0,0,217,216,1,0,0,0,218,219,1,0,0,0,
        219,220,5,28,0,0,220,221,5,26,0,0,221,223,3,12,6,0,222,203,1,0,0,
        0,222,210,1,0,0,0,222,217,1,0,0,0,223,27,1,0,0,0,224,229,3,30,15,
        0,225,226,5,27,0,0,226,228,3,30,15,0,227,225,1,0,0,0,228,231,1,0,
        0,0,229,227,1,0,0,0,229,230,1,0,0,0,230,29,1,0,0,0,231,229,1,0,0,
        0,232,241,5,31,0,0,233,241,5,29,0,0,234,241,5,30,0,0,235,241,5,28,
        0,0,236,237,5,17,0,0,237,238,3,28,14,0,238,239,5,18,0,0,239,241,
        1,0,0,0,240,232,1,0,0,0,240,233,1,0,0,0,240,234,1,0,0,0,240,235,
        1,0,0,0,240,236,1,0,0,0,241,31,1,0,0,0,242,252,5,14,0,0,243,252,
        5,16,0,0,244,252,5,15,0,0,245,252,5,11,0,0,246,252,5,12,0,0,247,
        248,5,13,0,0,248,249,5,24,0,0,249,250,7,3,0,0,250,252,5,25,0,0,251,
        242,1,0,0,0,251,243,1,0,0,0,251,244,1,0,0,0,251,245,1,0,0,0,251,
        246,1,0,0,0,251,247,1,0,0,0,252,253,1,0,0,0,253,254,5,28,0,0,254,
        33,1,0,0,0,20,46,60,78,90,125,140,146,150,156,163,169,181,194,203,
        210,217,222,229,240,251
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
    RULE_expression = 14
    RULE_expression_aux = 15
    RULE_declaration = 16

    ruleNames =  [ "program", "define_setup", "define_world", "define_scene", 
                   "statement", "chunk_constructor", "gameobject_constructor", 
                   "define_list", "array", "append_statement", "add_statement", 
                   "for_loop_number", "for_loop_list", "assignment", "expression", 
                   "expression_aux", "declaration" ]

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
            self.state = 34
            self.define_setup()
            self.state = 35
            self.define_world()
            self.state = 36
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
            self.state = 38
            self.match(gec_parserParser.DEFINE)
            self.state = 39
            self.match(gec_parserParser.SETUP)
            self.state = 40
            self.match(gec_parserParser.LPAREN)
            self.state = 41
            self.match(gec_parserParser.RPAREN)
            self.state = 42
            self.match(gec_parserParser.LBRACE)
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 268564656) != 0):
                self.state = 43
                self.statement()
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 49
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

        def RPAREN(self):
            return self.getToken(gec_parserParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(gec_parserParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(gec_parserParser.RBRACE, 0)

        def STRING_LITERAL(self):
            return self.getToken(gec_parserParser.STRING_LITERAL, 0)

        def ID(self):
            return self.getToken(gec_parserParser.ID, 0)

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
            self.state = 51
            self.match(gec_parserParser.DEFINE)
            self.state = 52
            self.match(gec_parserParser.WORLD)
            self.state = 53
            self.match(gec_parserParser.LPAREN)
            self.state = 54
            _la = self._input.LA(1)
            if not(_la==28 or _la==31):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 55
            self.match(gec_parserParser.RPAREN)
            self.state = 56
            self.match(gec_parserParser.LBRACE)
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 57
                self.define_scene()
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 63
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

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(gec_parserParser.COMMA)
            else:
                return self.getToken(gec_parserParser.COMMA, i)

        def RPAREN(self):
            return self.getToken(gec_parserParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(gec_parserParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(gec_parserParser.RBRACE, 0)

        def STRING_LITERAL(self):
            return self.getToken(gec_parserParser.STRING_LITERAL, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(gec_parserParser.ID)
            else:
                return self.getToken(gec_parserParser.ID, i)

        def INT_LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(gec_parserParser.INT_LITERAL)
            else:
                return self.getToken(gec_parserParser.INT_LITERAL, i)

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
            self.state = 65
            self.match(gec_parserParser.DEFINE)
            self.state = 66
            self.match(gec_parserParser.SCENE)
            self.state = 67
            self.match(gec_parserParser.LPAREN)
            self.state = 68
            _la = self._input.LA(1)
            if not(_la==28 or _la==31):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 69
            self.match(gec_parserParser.COMMA)
            self.state = 70
            _la = self._input.LA(1)
            if not(_la==28 or _la==29):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 71
            self.match(gec_parserParser.COMMA)
            self.state = 72
            _la = self._input.LA(1)
            if not(_la==28 or _la==29):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 73
            self.match(gec_parserParser.RPAREN)
            self.state = 74
            self.match(gec_parserParser.LBRACE)
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 268564656) != 0):
                self.state = 75
                self.statement()
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 81
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
            self.state = 90
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 83
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 84
                self.define_list()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 85
                self.append_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 86
                self.for_loop_number()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 87
                self.for_loop_list()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 88
                self.declaration()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 89
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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(gec_parserParser.ID)
            else:
                return self.getToken(gec_parserParser.ID, i)

        def RPAREN(self):
            return self.getToken(gec_parserParser.RPAREN, 0)

        def INT_LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(gec_parserParser.INT_LITERAL)
            else:
                return self.getToken(gec_parserParser.INT_LITERAL, i)

        def FLOAT_LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(gec_parserParser.FLOAT_LITERAL)
            else:
                return self.getToken(gec_parserParser.FLOAT_LITERAL, i)

        def STRING_LITERAL(self):
            return self.getToken(gec_parserParser.STRING_LITERAL, 0)

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
            self.state = 92
            self.match(gec_parserParser.CHUNK)
            self.state = 93
            self.match(gec_parserParser.LPAREN)
            self.state = 94
            _la = self._input.LA(1)
            if not(_la==28 or _la==29):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 95
            self.match(gec_parserParser.COMMA)
            self.state = 96
            _la = self._input.LA(1)
            if not(_la==28 or _la==29):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 97
            self.match(gec_parserParser.COMMA)
            self.state = 98
            _la = self._input.LA(1)
            if not(_la==28 or _la==30):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 99
            self.match(gec_parserParser.COMMA)
            self.state = 100
            _la = self._input.LA(1)
            if not(_la==28 or _la==30):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 101
            self.match(gec_parserParser.COMMA)
            self.state = 102
            _la = self._input.LA(1)
            if not(_la==28 or _la==31):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 103
            self.match(gec_parserParser.COMMA)
            self.state = 104
            self.match(gec_parserParser.ID)
            self.state = 105
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

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(gec_parserParser.COMMA)
            else:
                return self.getToken(gec_parserParser.COMMA, i)

        def RPAREN(self):
            return self.getToken(gec_parserParser.RPAREN, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(gec_parserParser.ID)
            else:
                return self.getToken(gec_parserParser.ID, i)

        def STRING_LITERAL(self):
            return self.getToken(gec_parserParser.STRING_LITERAL, 0)

        def INT_LITERAL(self):
            return self.getToken(gec_parserParser.INT_LITERAL, 0)

        def FLOAT_LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(gec_parserParser.FLOAT_LITERAL)
            else:
                return self.getToken(gec_parserParser.FLOAT_LITERAL, i)

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
        self._la = 0 # Token type
        try:
            self.state = 125
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.match(gec_parserParser.GAMEOBJECT)
                self.state = 108
                self.match(gec_parserParser.LPAREN)
                self.state = 109
                _la = self._input.LA(1)
                if not(_la==28 or _la==31):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 110
                self.match(gec_parserParser.COMMA)
                self.state = 111
                _la = self._input.LA(1)
                if not(_la==28 or _la==29):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 112
                self.match(gec_parserParser.COMMA)
                self.state = 113
                _la = self._input.LA(1)
                if not(_la==28 or _la==30):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 114
                self.match(gec_parserParser.COMMA)
                self.state = 115
                _la = self._input.LA(1)
                if not(_la==28 or _la==30):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 116
                self.match(gec_parserParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 117
                self.match(gec_parserParser.GAMEOBJECT)
                self.state = 118
                self.match(gec_parserParser.LPAREN)
                self.state = 119
                _la = self._input.LA(1)
                if not(_la==28 or _la==31):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 120
                self.match(gec_parserParser.COMMA)
                self.state = 121
                _la = self._input.LA(1)
                if not(_la==28 or _la==29):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 122
                self.match(gec_parserParser.COMMA)
                self.state = 123
                _la = self._input.LA(1)
                if not(_la==28 or _la==30):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 124
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
            self.state = 127
            self.match(gec_parserParser.LIST)
            self.state = 128
            self.match(gec_parserParser.LT)
            self.state = 129
            _la = self._input.LA(1)
            if not(_la==11 or _la==12):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 130
            self.match(gec_parserParser.GT)
            self.state = 132
            self.match(gec_parserParser.ID)
            self.state = 133
            self.match(gec_parserParser.ASSIGN)
            self.state = 134
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
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.match(gec_parserParser.LSQUARE)
                self.state = 140
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [28]:
                    self.state = 137
                    self.match(gec_parserParser.ID)
                    pass
                elif token in [11]:
                    self.state = 138
                    self.chunk_constructor()
                    pass
                elif token in [12]:
                    self.state = 139
                    self.gameobject_constructor()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==23:
                    self.state = 142
                    self.match(gec_parserParser.COMMA)
                    self.state = 146
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [28]:
                        self.state = 143
                        self.match(gec_parserParser.ID)
                        pass
                    elif token in [11]:
                        self.state = 144
                        self.chunk_constructor()
                        pass
                    elif token in [12]:
                        self.state = 145
                        self.gameobject_constructor()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 152
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 153
                self.match(gec_parserParser.RSQUARE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 154
                self.match(gec_parserParser.LSQUARE)
                self.state = 155
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
            self.state = 158
            self.match(gec_parserParser.APPEND)
            self.state = 159
            self.match(gec_parserParser.ID)
            self.state = 163
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.state = 160
                self.match(gec_parserParser.ID)
                pass
            elif token in [12]:
                self.state = 161
                self.gameobject_constructor()
                pass
            elif token in [11]:
                self.state = 162
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
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self.match(gec_parserParser.ADD)
                self.state = 166
                self.match(gec_parserParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 167
                self.match(gec_parserParser.ADD)
                self.state = 168
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
            self.state = 171
            self.match(gec_parserParser.FOR)
            self.state = 172
            self.match(gec_parserParser.ID)
            self.state = 173
            self.match(gec_parserParser.FROM)
            self.state = 174
            self.match(gec_parserParser.INT_LITERAL)
            self.state = 175
            self.match(gec_parserParser.TO)
            self.state = 176
            self.match(gec_parserParser.INT_LITERAL)
            self.state = 177
            self.match(gec_parserParser.LBRACE)
            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 268564656) != 0):
                self.state = 178
                self.statement()
                self.state = 183
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 184
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
            self.state = 186
            self.match(gec_parserParser.FOR)
            self.state = 187
            self.match(gec_parserParser.ID)
            self.state = 188
            self.match(gec_parserParser.IN)
            self.state = 189
            self.match(gec_parserParser.ID)
            self.state = 190
            self.match(gec_parserParser.LBRACE)
            self.state = 194
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 268564656) != 0):
                self.state = 191
                self.statement()
                self.state = 196
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 197
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

        def expression(self):
            return self.getTypedRuleContext(gec_parserParser.ExpressionContext,0)


        def INT(self):
            return self.getToken(gec_parserParser.INT, 0)

        def STRING(self):
            return self.getToken(gec_parserParser.STRING, 0)

        def FLOAT(self):
            return self.getToken(gec_parserParser.FLOAT, 0)

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
            self.state = 222
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 203
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [14]:
                    self.state = 199
                    self.match(gec_parserParser.INT)
                    pass
                elif token in [16]:
                    self.state = 200
                    self.match(gec_parserParser.STRING)
                    pass
                elif token in [15]:
                    self.state = 201
                    self.match(gec_parserParser.FLOAT)
                    pass
                elif token in [28]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 205
                self.match(gec_parserParser.ID)
                self.state = 206
                self.match(gec_parserParser.ASSIGN)
                self.state = 207
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 210
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [11]:
                    self.state = 208
                    self.match(gec_parserParser.CHUNK)
                    pass
                elif token in [28]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 212
                self.match(gec_parserParser.ID)
                self.state = 213
                self.match(gec_parserParser.ASSIGN)
                self.state = 214
                self.chunk_constructor()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 217
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [12]:
                    self.state = 215
                    self.match(gec_parserParser.GAMEOBJECT)
                    pass
                elif token in [28]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 219
                self.match(gec_parserParser.ID)
                self.state = 220
                self.match(gec_parserParser.ASSIGN)
                self.state = 221
                self.gameobject_constructor()
                pass


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

        def expression_aux(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gec_parserParser.Expression_auxContext)
            else:
                return self.getTypedRuleContext(gec_parserParser.Expression_auxContext,i)


        def OP_ARIT(self, i:int=None):
            if i is None:
                return self.getTokens(gec_parserParser.OP_ARIT)
            else:
                return self.getToken(gec_parserParser.OP_ARIT, i)

        def getRuleIndex(self):
            return gec_parserParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = gec_parserParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.expression_aux()
            self.state = 229
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27:
                self.state = 225
                self.match(gec_parserParser.OP_ARIT)
                self.state = 226
                self.expression_aux()
                self.state = 231
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_auxContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_LITERAL(self):
            return self.getToken(gec_parserParser.STRING_LITERAL, 0)

        def INT_LITERAL(self):
            return self.getToken(gec_parserParser.INT_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(gec_parserParser.FLOAT_LITERAL, 0)

        def ID(self):
            return self.getToken(gec_parserParser.ID, 0)

        def LPAREN(self):
            return self.getToken(gec_parserParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(gec_parserParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(gec_parserParser.RPAREN, 0)

        def getRuleIndex(self):
            return gec_parserParser.RULE_expression_aux

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression_aux" ):
                listener.enterExpression_aux(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression_aux" ):
                listener.exitExpression_aux(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_aux" ):
                return visitor.visitExpression_aux(self)
            else:
                return visitor.visitChildren(self)




    def expression_aux(self):

        localctx = gec_parserParser.Expression_auxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expression_aux)
        try:
            self.state = 240
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.match(gec_parserParser.STRING_LITERAL)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
                self.match(gec_parserParser.INT_LITERAL)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 3)
                self.state = 234
                self.match(gec_parserParser.FLOAT_LITERAL)
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 4)
                self.state = 235
                self.match(gec_parserParser.ID)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 5)
                self.state = 236
                self.match(gec_parserParser.LPAREN)
                self.state = 237
                self.expression()
                self.state = 238
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
        self.enterRule(localctx, 32, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.state = 242
                self.match(gec_parserParser.INT)
                pass
            elif token in [16]:
                self.state = 243
                self.match(gec_parserParser.STRING)
                pass
            elif token in [15]:
                self.state = 244
                self.match(gec_parserParser.FLOAT)
                pass
            elif token in [11]:
                self.state = 245
                self.match(gec_parserParser.CHUNK)
                pass
            elif token in [12]:
                self.state = 246
                self.match(gec_parserParser.GAMEOBJECT)
                pass
            elif token in [13]:
                self.state = 247
                self.match(gec_parserParser.LIST)
                self.state = 248
                self.match(gec_parserParser.LT)
                self.state = 249
                _la = self._input.LA(1)
                if not(_la==11 or _la==12):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 250
                self.match(gec_parserParser.GT)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 253
            self.match(gec_parserParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





