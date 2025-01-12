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
        4,1,34,264,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,1,0,1,0,1,
        0,1,1,1,1,1,1,1,1,1,1,1,1,5,1,49,8,1,10,1,12,1,52,9,1,1,1,1,1,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,63,8,2,10,2,12,2,66,9,2,1,2,1,2,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,81,8,3,10,3,12,3,84,
        9,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,95,8,4,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,
        6,132,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,3,
        8,147,8,8,1,8,1,8,1,8,1,8,3,8,153,8,8,5,8,155,8,8,10,8,12,8,158,
        9,8,1,8,1,8,1,8,3,8,163,8,8,1,9,1,9,1,9,1,9,1,9,3,9,170,8,9,1,10,
        1,10,1,10,1,10,3,10,176,8,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,5,11,186,8,11,10,11,12,11,189,9,11,1,11,1,11,1,12,1,12,1,12,
        1,12,1,12,1,12,5,12,199,8,12,10,12,12,12,202,9,12,1,12,1,12,1,13,
        1,13,1,13,1,13,3,13,210,8,13,1,13,1,13,1,13,1,13,1,13,3,13,217,8,
        13,1,13,1,13,1,13,1,13,1,13,3,13,224,8,13,1,13,1,13,1,13,3,13,229,
        8,13,1,14,1,14,1,14,5,14,234,8,14,10,14,12,14,237,9,14,1,15,1,15,
        1,15,1,15,1,15,1,15,3,15,245,8,15,1,16,1,16,1,17,1,17,1,18,1,18,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,260,8,18,1,18,1,18,1,18,
        0,0,19,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,0,4,2,
        0,28,28,31,31,1,0,28,29,1,0,11,12,1,0,28,30,280,0,38,1,0,0,0,2,42,
        1,0,0,0,4,55,1,0,0,0,6,69,1,0,0,0,8,94,1,0,0,0,10,96,1,0,0,0,12,
        131,1,0,0,0,14,133,1,0,0,0,16,162,1,0,0,0,18,164,1,0,0,0,20,175,
        1,0,0,0,22,177,1,0,0,0,24,192,1,0,0,0,26,228,1,0,0,0,28,230,1,0,
        0,0,30,244,1,0,0,0,32,246,1,0,0,0,34,248,1,0,0,0,36,259,1,0,0,0,
        38,39,3,2,1,0,39,40,3,4,2,0,40,41,5,0,0,1,41,1,1,0,0,0,42,43,5,1,
        0,0,43,44,5,2,0,0,44,45,5,17,0,0,45,46,5,18,0,0,46,50,5,19,0,0,47,
        49,3,8,4,0,48,47,1,0,0,0,49,52,1,0,0,0,50,48,1,0,0,0,50,51,1,0,0,
        0,51,53,1,0,0,0,52,50,1,0,0,0,53,54,5,20,0,0,54,3,1,0,0,0,55,56,
        5,1,0,0,56,57,5,3,0,0,57,58,5,17,0,0,58,59,7,0,0,0,59,60,5,18,0,
        0,60,64,5,19,0,0,61,63,3,6,3,0,62,61,1,0,0,0,63,66,1,0,0,0,64,62,
        1,0,0,0,64,65,1,0,0,0,65,67,1,0,0,0,66,64,1,0,0,0,67,68,5,20,0,0,
        68,5,1,0,0,0,69,70,5,1,0,0,70,71,5,6,0,0,71,72,5,17,0,0,72,73,7,
        0,0,0,73,74,5,23,0,0,74,75,7,1,0,0,75,76,5,23,0,0,76,77,7,1,0,0,
        77,78,5,18,0,0,78,82,5,19,0,0,79,81,3,8,4,0,80,79,1,0,0,0,81,84,
        1,0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,85,1,0,0,0,84,82,1,0,0,0,
        85,86,5,20,0,0,86,7,1,0,0,0,87,95,3,26,13,0,88,95,3,14,7,0,89,95,
        3,18,9,0,90,95,3,22,11,0,91,95,3,24,12,0,92,95,3,36,18,0,93,95,3,
        20,10,0,94,87,1,0,0,0,94,88,1,0,0,0,94,89,1,0,0,0,94,90,1,0,0,0,
        94,91,1,0,0,0,94,92,1,0,0,0,94,93,1,0,0,0,95,9,1,0,0,0,96,97,5,11,
        0,0,97,98,5,17,0,0,98,99,3,28,14,0,99,100,5,23,0,0,100,101,3,28,
        14,0,101,102,5,23,0,0,102,103,3,28,14,0,103,104,5,23,0,0,104,105,
        3,28,14,0,105,106,5,23,0,0,106,107,3,28,14,0,107,108,5,23,0,0,108,
        109,5,28,0,0,109,110,5,18,0,0,110,11,1,0,0,0,111,112,5,12,0,0,112,
        113,5,17,0,0,113,114,3,28,14,0,114,115,5,23,0,0,115,116,3,28,14,
        0,116,117,5,23,0,0,117,118,3,28,14,0,118,119,5,23,0,0,119,120,3,
        28,14,0,120,121,5,18,0,0,121,132,1,0,0,0,122,123,5,12,0,0,123,124,
        5,17,0,0,124,125,3,28,14,0,125,126,5,23,0,0,126,127,3,28,14,0,127,
        128,5,23,0,0,128,129,3,28,14,0,129,130,5,18,0,0,130,132,1,0,0,0,
        131,111,1,0,0,0,131,122,1,0,0,0,132,13,1,0,0,0,133,134,5,13,0,0,
        134,135,5,24,0,0,135,136,7,2,0,0,136,137,5,25,0,0,137,138,1,0,0,
        0,138,139,5,28,0,0,139,140,5,26,0,0,140,141,3,16,8,0,141,15,1,0,
        0,0,142,146,5,21,0,0,143,147,5,28,0,0,144,147,3,10,5,0,145,147,3,
        12,6,0,146,143,1,0,0,0,146,144,1,0,0,0,146,145,1,0,0,0,147,156,1,
        0,0,0,148,152,5,23,0,0,149,153,5,28,0,0,150,153,3,10,5,0,151,153,
        3,12,6,0,152,149,1,0,0,0,152,150,1,0,0,0,152,151,1,0,0,0,153,155,
        1,0,0,0,154,148,1,0,0,0,155,158,1,0,0,0,156,154,1,0,0,0,156,157,
        1,0,0,0,157,159,1,0,0,0,158,156,1,0,0,0,159,163,5,22,0,0,160,161,
        5,21,0,0,161,163,5,22,0,0,162,142,1,0,0,0,162,160,1,0,0,0,163,17,
        1,0,0,0,164,165,5,5,0,0,165,169,5,28,0,0,166,170,5,28,0,0,167,170,
        3,12,6,0,168,170,3,10,5,0,169,166,1,0,0,0,169,167,1,0,0,0,169,168,
        1,0,0,0,170,19,1,0,0,0,171,172,5,4,0,0,172,176,5,28,0,0,173,174,
        5,4,0,0,174,176,3,10,5,0,175,171,1,0,0,0,175,173,1,0,0,0,176,21,
        1,0,0,0,177,178,5,7,0,0,178,179,5,28,0,0,179,180,5,8,0,0,180,181,
        5,29,0,0,181,182,5,9,0,0,182,183,5,29,0,0,183,187,5,19,0,0,184,186,
        3,8,4,0,185,184,1,0,0,0,186,189,1,0,0,0,187,185,1,0,0,0,187,188,
        1,0,0,0,188,190,1,0,0,0,189,187,1,0,0,0,190,191,5,20,0,0,191,23,
        1,0,0,0,192,193,5,7,0,0,193,194,5,28,0,0,194,195,5,10,0,0,195,196,
        5,28,0,0,196,200,5,19,0,0,197,199,3,8,4,0,198,197,1,0,0,0,199,202,
        1,0,0,0,200,198,1,0,0,0,200,201,1,0,0,0,201,203,1,0,0,0,202,200,
        1,0,0,0,203,204,5,20,0,0,204,25,1,0,0,0,205,210,5,14,0,0,206,210,
        5,16,0,0,207,210,5,15,0,0,208,210,1,0,0,0,209,205,1,0,0,0,209,206,
        1,0,0,0,209,207,1,0,0,0,209,208,1,0,0,0,210,211,1,0,0,0,211,212,
        5,28,0,0,212,213,5,26,0,0,213,229,3,28,14,0,214,217,5,11,0,0,215,
        217,1,0,0,0,216,214,1,0,0,0,216,215,1,0,0,0,217,218,1,0,0,0,218,
        219,5,28,0,0,219,220,5,26,0,0,220,229,3,10,5,0,221,224,5,12,0,0,
        222,224,1,0,0,0,223,221,1,0,0,0,223,222,1,0,0,0,224,225,1,0,0,0,
        225,226,5,28,0,0,226,227,5,26,0,0,227,229,3,12,6,0,228,209,1,0,0,
        0,228,216,1,0,0,0,228,223,1,0,0,0,229,27,1,0,0,0,230,235,3,30,15,
        0,231,232,5,27,0,0,232,234,3,30,15,0,233,231,1,0,0,0,234,237,1,0,
        0,0,235,233,1,0,0,0,235,236,1,0,0,0,236,29,1,0,0,0,237,235,1,0,0,
        0,238,245,3,32,16,0,239,245,3,34,17,0,240,241,5,17,0,0,241,242,3,
        28,14,0,242,243,5,18,0,0,243,245,1,0,0,0,244,238,1,0,0,0,244,239,
        1,0,0,0,244,240,1,0,0,0,245,31,1,0,0,0,246,247,7,3,0,0,247,33,1,
        0,0,0,248,249,7,0,0,0,249,35,1,0,0,0,250,260,5,14,0,0,251,260,5,
        16,0,0,252,260,5,15,0,0,253,260,5,11,0,0,254,260,5,12,0,0,255,256,
        5,13,0,0,256,257,5,24,0,0,257,258,7,2,0,0,258,260,5,25,0,0,259,250,
        1,0,0,0,259,251,1,0,0,0,259,252,1,0,0,0,259,253,1,0,0,0,259,254,
        1,0,0,0,259,255,1,0,0,0,260,261,1,0,0,0,261,262,5,28,0,0,262,37,
        1,0,0,0,20,50,64,82,94,131,146,152,156,162,169,175,187,200,209,216,
        223,228,235,244,259
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
    RULE_numeric_expression = 16
    RULE_string_expression = 17
    RULE_declaration = 18

    ruleNames =  [ "program", "define_setup", "define_world", "define_scene", 
                   "statement", "chunk_constructor", "gameobject_constructor", 
                   "define_list", "array", "append_statement", "add_statement", 
                   "for_loop_number", "for_loop_list", "assignment", "expression", 
                   "expression_aux", "numeric_expression", "string_expression", 
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
            self.state = 55
            self.match(gec_parserParser.DEFINE)
            self.state = 56
            self.match(gec_parserParser.WORLD)
            self.state = 57
            self.match(gec_parserParser.LPAREN)
            self.state = 58
            _la = self._input.LA(1)
            if not(_la==28 or _la==31):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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
            self.state = 69
            self.match(gec_parserParser.DEFINE)
            self.state = 70
            self.match(gec_parserParser.SCENE)
            self.state = 71
            self.match(gec_parserParser.LPAREN)
            self.state = 72
            _la = self._input.LA(1)
            if not(_la==28 or _la==31):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 73
            self.match(gec_parserParser.COMMA)
            self.state = 74
            _la = self._input.LA(1)
            if not(_la==28 or _la==29):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 75
            self.match(gec_parserParser.COMMA)
            self.state = 76
            _la = self._input.LA(1)
            if not(_la==28 or _la==29):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gec_parserParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(gec_parserParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(gec_parserParser.COMMA)
            else:
                return self.getToken(gec_parserParser.COMMA, i)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(gec_parserParser.CHUNK)
            self.state = 97
            self.match(gec_parserParser.LPAREN)
            self.state = 98
            self.expression()
            self.state = 99
            self.match(gec_parserParser.COMMA)
            self.state = 100
            self.expression()
            self.state = 101
            self.match(gec_parserParser.COMMA)
            self.state = 102
            self.expression()
            self.state = 103
            self.match(gec_parserParser.COMMA)
            self.state = 104
            self.expression()
            self.state = 105
            self.match(gec_parserParser.COMMA)
            self.state = 106
            self.expression()
            self.state = 107
            self.match(gec_parserParser.COMMA)
            self.state = 108
            self.match(gec_parserParser.ID)
            self.state = 109
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

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gec_parserParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(gec_parserParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(gec_parserParser.COMMA)
            else:
                return self.getToken(gec_parserParser.COMMA, i)

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
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 111
                self.match(gec_parserParser.GAMEOBJECT)
                self.state = 112
                self.match(gec_parserParser.LPAREN)
                self.state = 113
                self.expression()
                self.state = 114
                self.match(gec_parserParser.COMMA)
                self.state = 115
                self.expression()
                self.state = 116
                self.match(gec_parserParser.COMMA)
                self.state = 117
                self.expression()
                self.state = 118
                self.match(gec_parserParser.COMMA)
                self.state = 119
                self.expression()
                self.state = 120
                self.match(gec_parserParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 122
                self.match(gec_parserParser.GAMEOBJECT)
                self.state = 123
                self.match(gec_parserParser.LPAREN)
                self.state = 124
                self.expression()
                self.state = 125
                self.match(gec_parserParser.COMMA)
                self.state = 126
                self.expression()
                self.state = 127
                self.match(gec_parserParser.COMMA)
                self.state = 128
                self.expression()
                self.state = 129
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
            self.state = 133
            self.match(gec_parserParser.LIST)
            self.state = 134
            self.match(gec_parserParser.LT)
            self.state = 135
            _la = self._input.LA(1)
            if not(_la==11 or _la==12):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 136
            self.match(gec_parserParser.GT)
            self.state = 138
            self.match(gec_parserParser.ID)
            self.state = 139
            self.match(gec_parserParser.ASSIGN)
            self.state = 140
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
            self.state = 162
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.match(gec_parserParser.LSQUARE)
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

                self.state = 156
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==23:
                    self.state = 148
                    self.match(gec_parserParser.COMMA)
                    self.state = 152
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [28]:
                        self.state = 149
                        self.match(gec_parserParser.ID)
                        pass
                    elif token in [11]:
                        self.state = 150
                        self.chunk_constructor()
                        pass
                    elif token in [12]:
                        self.state = 151
                        self.gameobject_constructor()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 158
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 159
                self.match(gec_parserParser.RSQUARE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
                self.match(gec_parserParser.LSQUARE)
                self.state = 161
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
            self.state = 164
            self.match(gec_parserParser.APPEND)
            self.state = 165
            self.match(gec_parserParser.ID)
            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.state = 166
                self.match(gec_parserParser.ID)
                pass
            elif token in [12]:
                self.state = 167
                self.gameobject_constructor()
                pass
            elif token in [11]:
                self.state = 168
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
            self.state = 175
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.match(gec_parserParser.ADD)
                self.state = 172
                self.match(gec_parserParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
                self.match(gec_parserParser.ADD)
                self.state = 174
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
            self.state = 177
            self.match(gec_parserParser.FOR)
            self.state = 178
            self.match(gec_parserParser.ID)
            self.state = 179
            self.match(gec_parserParser.FROM)
            self.state = 180
            self.match(gec_parserParser.INT_LITERAL)
            self.state = 181
            self.match(gec_parserParser.TO)
            self.state = 182
            self.match(gec_parserParser.INT_LITERAL)
            self.state = 183
            self.match(gec_parserParser.LBRACE)
            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 268564656) != 0):
                self.state = 184
                self.statement()
                self.state = 189
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 190
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
            self.state = 192
            self.match(gec_parserParser.FOR)
            self.state = 193
            self.match(gec_parserParser.ID)
            self.state = 194
            self.match(gec_parserParser.IN)
            self.state = 195
            self.match(gec_parserParser.ID)
            self.state = 196
            self.match(gec_parserParser.LBRACE)
            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 268564656) != 0):
                self.state = 197
                self.statement()
                self.state = 202
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 203
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
            self.state = 228
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 209
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [14]:
                    self.state = 205
                    self.match(gec_parserParser.INT)
                    pass
                elif token in [16]:
                    self.state = 206
                    self.match(gec_parserParser.STRING)
                    pass
                elif token in [15]:
                    self.state = 207
                    self.match(gec_parserParser.FLOAT)
                    pass
                elif token in [28]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 211
                self.match(gec_parserParser.ID)
                self.state = 212
                self.match(gec_parserParser.ASSIGN)
                self.state = 213
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 216
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [11]:
                    self.state = 214
                    self.match(gec_parserParser.CHUNK)
                    pass
                elif token in [28]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 218
                self.match(gec_parserParser.ID)
                self.state = 219
                self.match(gec_parserParser.ASSIGN)
                self.state = 220
                self.chunk_constructor()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 223
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [12]:
                    self.state = 221
                    self.match(gec_parserParser.GAMEOBJECT)
                    pass
                elif token in [28]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 225
                self.match(gec_parserParser.ID)
                self.state = 226
                self.match(gec_parserParser.ASSIGN)
                self.state = 227
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
            self.state = 230
            self.expression_aux()
            self.state = 235
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27:
                self.state = 231
                self.match(gec_parserParser.OP_ARIT)
                self.state = 232
                self.expression_aux()
                self.state = 237
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

        def numeric_expression(self):
            return self.getTypedRuleContext(gec_parserParser.Numeric_expressionContext,0)


        def string_expression(self):
            return self.getTypedRuleContext(gec_parserParser.String_expressionContext,0)


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
            self.state = 244
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.numeric_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 239
                self.string_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 240
                self.match(gec_parserParser.LPAREN)
                self.state = 241
                self.expression()
                self.state = 242
                self.match(gec_parserParser.RPAREN)
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

        def INT_LITERAL(self):
            return self.getToken(gec_parserParser.INT_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(gec_parserParser.FLOAT_LITERAL, 0)

        def ID(self):
            return self.getToken(gec_parserParser.ID, 0)

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
        self.enterRule(localctx, 32, self.RULE_numeric_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1879048192) != 0)):
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


    class String_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_LITERAL(self):
            return self.getToken(gec_parserParser.STRING_LITERAL, 0)

        def ID(self):
            return self.getToken(gec_parserParser.ID, 0)

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
        self.enterRule(localctx, 34, self.RULE_string_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            _la = self._input.LA(1)
            if not(_la==28 or _la==31):
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
            self.state = 259
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.state = 250
                self.match(gec_parserParser.INT)
                pass
            elif token in [16]:
                self.state = 251
                self.match(gec_parserParser.STRING)
                pass
            elif token in [15]:
                self.state = 252
                self.match(gec_parserParser.FLOAT)
                pass
            elif token in [11]:
                self.state = 253
                self.match(gec_parserParser.CHUNK)
                pass
            elif token in [12]:
                self.state = 254
                self.match(gec_parserParser.GAMEOBJECT)
                pass
            elif token in [13]:
                self.state = 255
                self.match(gec_parserParser.LIST)
                self.state = 256
                self.match(gec_parserParser.LT)
                self.state = 257
                _la = self._input.LA(1)
                if not(_la==11 or _la==12):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 258
                self.match(gec_parserParser.GT)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 261
            self.match(gec_parserParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





