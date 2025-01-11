# Generated from gec_parser.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


from parser.symbol_table import SymbolTable
from parser.gec_objects import GameObject, Chunk, Scene, World
import json

def serializedATN():
    return [
        4,1,34,335,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,
        1,1,1,1,1,1,1,5,1,47,8,1,10,1,12,1,50,9,1,1,1,1,1,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,5,2,62,8,2,10,2,12,2,65,9,2,1,2,1,2,1,2,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,85,8,3,
        10,3,12,3,88,9,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,3,4,103,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,3,6,154,8,6,1,7,1,7,1,7,1,7,1,7,3,7,161,8,7,
        1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,177,
        8,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,188,8,8,5,8,190,8,8,
        10,8,12,8,193,9,8,1,8,1,8,1,8,3,8,198,8,8,1,9,1,9,1,9,1,9,1,9,1,
        9,3,9,206,8,9,1,9,1,9,1,10,1,10,1,10,1,10,3,10,214,8,10,1,10,1,10,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,5,11,
        230,8,11,10,11,12,11,233,9,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,5,12,245,8,12,10,12,12,12,248,9,12,1,12,1,12,1,13,
        1,13,1,13,1,13,3,13,256,8,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,3,13,266,8,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,
        276,8,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,284,8,13,1,14,1,14,1,
        14,1,14,1,14,1,14,5,14,292,8,14,10,14,12,14,295,9,14,1,14,1,14,1,
        15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,3,
        15,312,8,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,
        16,1,16,1,16,1,16,1,16,3,16,329,8,16,1,16,1,16,1,16,1,16,1,16,0,
        0,17,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,0,4,2,0,28,28,
        31,31,1,0,28,29,2,0,28,28,30,30,1,0,11,12,356,0,34,1,0,0,0,2,40,
        1,0,0,0,4,53,1,0,0,0,6,69,1,0,0,0,8,102,1,0,0,0,10,104,1,0,0,0,12,
        153,1,0,0,0,14,160,1,0,0,0,16,197,1,0,0,0,18,199,1,0,0,0,20,213,
        1,0,0,0,22,217,1,0,0,0,24,236,1,0,0,0,26,283,1,0,0,0,28,285,1,0,
        0,0,30,311,1,0,0,0,32,328,1,0,0,0,34,35,6,0,-1,0,35,36,3,2,1,0,36,
        37,3,4,2,0,37,38,5,0,0,1,38,39,6,0,-1,0,39,1,1,0,0,0,40,41,5,1,0,
        0,41,42,5,2,0,0,42,43,5,17,0,0,43,44,5,18,0,0,44,48,5,19,0,0,45,
        47,3,8,4,0,46,45,1,0,0,0,47,50,1,0,0,0,48,46,1,0,0,0,48,49,1,0,0,
        0,49,51,1,0,0,0,50,48,1,0,0,0,51,52,5,20,0,0,52,3,1,0,0,0,53,54,
        5,1,0,0,54,55,5,3,0,0,55,56,5,17,0,0,56,57,7,0,0,0,57,58,6,2,-1,
        0,58,59,5,18,0,0,59,63,5,19,0,0,60,62,3,6,3,0,61,60,1,0,0,0,62,65,
        1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,66,1,0,0,0,65,63,1,0,0,0,
        66,67,5,20,0,0,67,68,6,2,-1,0,68,5,1,0,0,0,69,70,5,1,0,0,70,71,5,
        6,0,0,71,72,5,17,0,0,72,73,7,0,0,0,73,74,6,3,-1,0,74,75,5,23,0,0,
        75,76,7,1,0,0,76,77,6,3,-1,0,77,78,5,23,0,0,78,79,7,1,0,0,79,80,
        6,3,-1,0,80,81,5,18,0,0,81,82,6,3,-1,0,82,86,5,19,0,0,83,85,3,8,
        4,0,84,83,1,0,0,0,85,88,1,0,0,0,86,84,1,0,0,0,86,87,1,0,0,0,87,89,
        1,0,0,0,88,86,1,0,0,0,89,90,6,3,-1,0,90,91,5,20,0,0,91,92,6,3,-1,
        0,92,7,1,0,0,0,93,103,3,26,13,0,94,103,3,14,7,0,95,103,3,18,9,0,
        96,103,3,22,11,0,97,103,3,24,12,0,98,103,3,32,16,0,99,100,3,20,10,
        0,100,101,6,4,-1,0,101,103,1,0,0,0,102,93,1,0,0,0,102,94,1,0,0,0,
        102,95,1,0,0,0,102,96,1,0,0,0,102,97,1,0,0,0,102,98,1,0,0,0,102,
        99,1,0,0,0,103,9,1,0,0,0,104,105,5,11,0,0,105,106,5,17,0,0,106,107,
        7,1,0,0,107,108,6,5,-1,0,108,109,5,23,0,0,109,110,7,1,0,0,110,111,
        6,5,-1,0,111,112,5,23,0,0,112,113,7,2,0,0,113,114,6,5,-1,0,114,115,
        5,23,0,0,115,116,7,2,0,0,116,117,6,5,-1,0,117,118,5,23,0,0,118,119,
        7,0,0,0,119,120,6,5,-1,0,120,121,5,23,0,0,121,122,5,28,0,0,122,123,
        6,5,-1,0,123,124,5,18,0,0,124,125,6,5,-1,0,125,11,1,0,0,0,126,127,
        5,12,0,0,127,128,5,17,0,0,128,129,7,0,0,0,129,130,6,6,-1,0,130,131,
        5,23,0,0,131,132,7,1,0,0,132,133,6,6,-1,0,133,134,5,23,0,0,134,135,
        7,2,0,0,135,136,6,6,-1,0,136,137,5,23,0,0,137,138,7,2,0,0,138,139,
        6,6,-1,0,139,140,5,18,0,0,140,154,6,6,-1,0,141,142,5,12,0,0,142,
        143,5,17,0,0,143,144,7,0,0,0,144,145,6,6,-1,0,145,146,5,23,0,0,146,
        147,7,1,0,0,147,148,6,6,-1,0,148,149,5,23,0,0,149,150,7,2,0,0,150,
        151,6,6,-1,0,151,152,5,18,0,0,152,154,6,6,-1,0,153,126,1,0,0,0,153,
        141,1,0,0,0,154,13,1,0,0,0,155,156,5,13,0,0,156,157,5,24,0,0,157,
        158,7,3,0,0,158,161,5,25,0,0,159,161,1,0,0,0,160,155,1,0,0,0,160,
        159,1,0,0,0,161,162,1,0,0,0,162,163,5,28,0,0,163,164,5,26,0,0,164,
        165,3,16,8,0,165,166,6,7,-1,0,166,15,1,0,0,0,167,176,5,21,0,0,168,
        169,5,28,0,0,169,177,6,8,-1,0,170,171,3,10,5,0,171,172,6,8,-1,0,
        172,177,1,0,0,0,173,174,3,12,6,0,174,175,6,8,-1,0,175,177,1,0,0,
        0,176,168,1,0,0,0,176,170,1,0,0,0,176,173,1,0,0,0,177,191,1,0,0,
        0,178,187,5,23,0,0,179,180,5,28,0,0,180,188,6,8,-1,0,181,182,3,10,
        5,0,182,183,6,8,-1,0,183,188,1,0,0,0,184,185,3,12,6,0,185,186,6,
        8,-1,0,186,188,1,0,0,0,187,179,1,0,0,0,187,181,1,0,0,0,187,184,1,
        0,0,0,188,190,1,0,0,0,189,178,1,0,0,0,190,193,1,0,0,0,191,189,1,
        0,0,0,191,192,1,0,0,0,192,194,1,0,0,0,193,191,1,0,0,0,194,198,5,
        22,0,0,195,196,5,21,0,0,196,198,5,22,0,0,197,167,1,0,0,0,197,195,
        1,0,0,0,198,17,1,0,0,0,199,200,5,5,0,0,200,201,5,28,0,0,201,205,
        6,9,-1,0,202,206,5,28,0,0,203,206,3,12,6,0,204,206,3,10,5,0,205,
        202,1,0,0,0,205,203,1,0,0,0,205,204,1,0,0,0,206,207,1,0,0,0,207,
        208,6,9,-1,0,208,19,1,0,0,0,209,210,5,4,0,0,210,214,5,28,0,0,211,
        212,5,4,0,0,212,214,3,10,5,0,213,209,1,0,0,0,213,211,1,0,0,0,214,
        215,1,0,0,0,215,216,6,10,-1,0,216,21,1,0,0,0,217,218,5,7,0,0,218,
        219,5,28,0,0,219,220,6,11,-1,0,220,221,5,8,0,0,221,222,5,29,0,0,
        222,223,6,11,-1,0,223,224,5,9,0,0,224,225,5,29,0,0,225,226,6,11,
        -1,0,226,227,6,11,-1,0,227,231,5,19,0,0,228,230,3,8,4,0,229,228,
        1,0,0,0,230,233,1,0,0,0,231,229,1,0,0,0,231,232,1,0,0,0,232,234,
        1,0,0,0,233,231,1,0,0,0,234,235,5,20,0,0,235,23,1,0,0,0,236,237,
        5,7,0,0,237,238,5,28,0,0,238,239,6,12,-1,0,239,240,5,10,0,0,240,
        241,5,28,0,0,241,242,6,12,-1,0,242,246,5,19,0,0,243,245,3,8,4,0,
        244,243,1,0,0,0,245,248,1,0,0,0,246,244,1,0,0,0,246,247,1,0,0,0,
        247,249,1,0,0,0,248,246,1,0,0,0,249,250,5,20,0,0,250,25,1,0,0,0,
        251,256,5,14,0,0,252,256,5,16,0,0,253,256,5,15,0,0,254,256,1,0,0,
        0,255,251,1,0,0,0,255,252,1,0,0,0,255,253,1,0,0,0,255,254,1,0,0,
        0,256,257,1,0,0,0,257,258,5,28,0,0,258,259,6,13,-1,0,259,260,5,26,
        0,0,260,261,3,28,14,0,261,262,6,13,-1,0,262,284,1,0,0,0,263,266,
        5,11,0,0,264,266,1,0,0,0,265,263,1,0,0,0,265,264,1,0,0,0,266,267,
        1,0,0,0,267,268,5,28,0,0,268,269,6,13,-1,0,269,270,5,26,0,0,270,
        271,3,10,5,0,271,272,6,13,-1,0,272,284,1,0,0,0,273,276,5,12,0,0,
        274,276,1,0,0,0,275,273,1,0,0,0,275,274,1,0,0,0,276,277,1,0,0,0,
        277,278,5,28,0,0,278,279,6,13,-1,0,279,280,5,26,0,0,280,281,3,12,
        6,0,281,282,6,13,-1,0,282,284,1,0,0,0,283,255,1,0,0,0,283,265,1,
        0,0,0,283,275,1,0,0,0,284,27,1,0,0,0,285,286,3,30,15,0,286,293,6,
        14,-1,0,287,288,5,27,0,0,288,289,3,30,15,0,289,290,6,14,-1,0,290,
        292,1,0,0,0,291,287,1,0,0,0,292,295,1,0,0,0,293,291,1,0,0,0,293,
        294,1,0,0,0,294,296,1,0,0,0,295,293,1,0,0,0,296,297,6,14,-1,0,297,
        29,1,0,0,0,298,299,5,31,0,0,299,312,6,15,-1,0,300,301,5,29,0,0,301,
        312,6,15,-1,0,302,303,5,30,0,0,303,312,6,15,-1,0,304,305,5,28,0,
        0,305,312,6,15,-1,0,306,307,5,17,0,0,307,308,3,28,14,0,308,309,5,
        18,0,0,309,310,6,15,-1,0,310,312,1,0,0,0,311,298,1,0,0,0,311,300,
        1,0,0,0,311,302,1,0,0,0,311,304,1,0,0,0,311,306,1,0,0,0,312,31,1,
        0,0,0,313,314,5,14,0,0,314,329,6,16,-1,0,315,316,5,16,0,0,316,329,
        6,16,-1,0,317,318,5,15,0,0,318,329,6,16,-1,0,319,320,5,11,0,0,320,
        329,6,16,-1,0,321,322,5,12,0,0,322,329,6,16,-1,0,323,324,5,13,0,
        0,324,325,5,24,0,0,325,326,7,3,0,0,326,327,5,25,0,0,327,329,6,16,
        -1,0,328,313,1,0,0,0,328,315,1,0,0,0,328,317,1,0,0,0,328,319,1,0,
        0,0,328,321,1,0,0,0,328,323,1,0,0,0,329,330,1,0,0,0,330,331,5,28,
        0,0,331,332,6,16,-1,0,332,333,6,16,-1,0,333,33,1,0,0,0,21,48,63,
        86,102,153,160,176,187,191,197,205,213,231,246,255,265,275,283,293,
        311,328
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



    def on_programa_start(self):
        self.symbol_table = SymbolTable()

    def on_programa_end(self, world, path):
    	print("Fin del programa\n")
    	print(self.symbol_table)
    	# Crear un json con las escenas
    	print(world.get_scenes())
    	world_json = world.to_dict()
    	with open(path, 'w') as file:
    		json.dump(world_json, file, indent=4)


    def eval_expression(self,values,operators=None):
        result = values[0]
        for i,op in enumerate(operators):
            result = self._eval_single_expression([result,values[i+1]],op)
        return result
            
    def _eval_single_expression(self,values, operator):
        match operator:
            case '+' :
                return values[0] + values[1]
            case '-' :
                return values[0] - values[1]
            case '*' :
                return values[0] * values[1]
            case '*' :
                return values[0] / values[1]
            case _:
                raise ValueError("Operador no existe")

    def is_add_statement(self, statement):
        return statement.text == "add"

    def get_type(self,object):
        if isinstance(object, int):
            return "INT"
        elif isinstance(object, float):
            return "FLOAT"
        elif isinstance(object, str):
            return "STRING"
        elif isinstance(object, Chunk):
            return "CHUNK"
        elif isinstance(object, GameObject):
            return "GAMEOBJECT"
        elif isinstance(object, Scene):
            return "SCENE"
        elif isinstance(object, World):
            return "WORLD"
        else:
            return "UNKNOWN"



    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._define_world = None # Define_worldContext

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




    def program(self):

        localctx = gec_parserParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.on_programa_start()
            self.state = 35
            self.define_setup()
            self.state = 36
            localctx._define_world = self.define_world()
            self.state = 37
            self.match(gec_parserParser.EOF)

            print("world", localctx._define_world.world.get_scenes())
            self.on_programa_end(localctx._define_world.world,"World.json")
                
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




    def define_setup(self):

        localctx = gec_parserParser.Define_setupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_define_setup)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(gec_parserParser.DEFINE)
            self.state = 41
            self.match(gec_parserParser.SETUP)
            self.state = 42
            self.match(gec_parserParser.LPAREN)
            self.state = 43
            self.match(gec_parserParser.RPAREN)
            self.state = 44
            self.match(gec_parserParser.LBRACE)
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 268564656) != 0):
                self.state = 45
                self.statement()
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 51
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
            self.world = None
            self._define_scene = None # Define_sceneContext
            self.scenes = list() # of Define_sceneContexts

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




    def define_world(self):

        localctx = gec_parserParser.Define_worldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_define_world)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(gec_parserParser.DEFINE)
            self.state = 54
            self.match(gec_parserParser.WORLD)
            self.state = 55
            self.match(gec_parserParser.LPAREN)
            self.state = 56
            _la = self._input.LA(1)
            if not(_la==28 or _la==31):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()


            temp_name = self._input.LT(-1).text
            if temp_name.startswith('"') and temp_name.endswith('"'):
                temp_name = temp_name[1:-1]
            else:
                temp_name = self.symbol_table.get_value(temp_name)

            localctx.world = World(temp_name)

                
            self.state = 58
            self.match(gec_parserParser.RPAREN)
            self.state = 59
            self.match(gec_parserParser.LBRACE)
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 60
                localctx._define_scene = self.define_scene()
                localctx.scenes.append(localctx._define_scene)
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 66
            self.match(gec_parserParser.RBRACE)

            for scene in localctx.scenes:
                localctx.world.add_scene(scene.scene)
                
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
            self.scene = None
            self._statement = None # StatementContext
            self.statements = list() # of StatementContexts

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


            temp_name = self._input.LT(-1).text
            if temp_name.startswith('"') and temp_name.endswith('"'):
                temp_name = temp_name[1:-1]
            else:
                temp_name = self.symbol_table.get_value(temp_name)

                
            self.state = 74
            self.match(gec_parserParser.COMMA)
            self.state = 75
            _la = self._input.LA(1)
            if not(_la==28 or _la==29):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()


            temp_width_chunk = self._input.LT(-1).text  
            if temp_width_chunk.isdigit():
                temp_width_chunk = int(temp_width_chunk)
            else:
                temp_width_chunk = int(self.symbol_table.get_value(temp_width_chunk))

                
            self.state = 77
            self.match(gec_parserParser.COMMA)
            self.state = 78
            _la = self._input.LA(1)
            if not(_la==28 or _la==29):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()


            temp_length_chunk = self._input.LT(-1).text
            if temp_length_chunk.isdigit():
                temp_length_chunk = int(temp_length_chunk)
            else:
                temp_length_chunk = int(self.symbol_table.get_value(temp_length_chunk))

                
            self.state = 80
            self.match(gec_parserParser.RPAREN)

            localctx.scene = Scene(temp_name, temp_width_chunk, temp_length_chunk)
                
            self.state = 82
            self.match(gec_parserParser.LBRACE)
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 268564656) != 0):
                self.state = 83
                localctx._statement = self.statement()
                localctx.statements.append(localctx._statement)
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)

               
            for stmt in localctx.statements: 
                if isinstance(stmt.value, Chunk): 
                    localctx.scene.add_chunk(stmt.value)
                
            self.state = 90
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
            self.value = None
            self._add_statement = None # Add_statementContext

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




    def statement(self):

        localctx = gec_parserParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_statement)
        try:
            self.state = 102
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 94
                self.define_list()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 95
                self.append_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 96
                self.for_loop_number()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 97
                self.for_loop_list()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 98
                self.declaration()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 99
                localctx._add_statement = self.add_statement()

                localctx.value = localctx._add_statement.chunk
                    
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
            self.chunk = None

        def CHUNK(self):
            return self.getToken(gec_parserParser.CHUNK, 0)

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




    def chunk_constructor(self):

        localctx = gec_parserParser.Chunk_constructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_chunk_constructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(gec_parserParser.CHUNK)
            self.state = 105
            self.match(gec_parserParser.LPAREN)
            self.state = 106
            _la = self._input.LA(1)
            if not(_la==28 or _la==29):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()


            temp_pos_x = self._input.LT(-1).text
            if temp_pos_x.isdigit():
                temp_pos_x = int(temp_pos_x)
            else:  
                temp_pos_x = int(self.symbol_table.get_value(temp_pos_x))


            self.state = 108
            self.match(gec_parserParser.COMMA)
            self.state = 109
            _la = self._input.LA(1)
            if not(_la==28 or _la==29):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()

                
            temp_pos_y = self._input.LT(-1).text
            if temp_pos_y.isdigit():
                temp_pos_y = int(temp_pos_y)
            else:  
                temp_pos_y = int(self.symbol_table.get_value(temp_pos_y))


            self.state = 111
            self.match(gec_parserParser.COMMA)
            self.state = 112
            _la = self._input.LA(1)
            if not(_la==28 or _la==30):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()


            temp_scale = self._input.LT(-1).text
            if temp_scale.replace(".","",1).isdigit():
                temp_scale = float(temp_scale)
            else:  
                temp_scale = float(self.symbol_table.get_value(temp_scale))


            self.state = 114
            self.match(gec_parserParser.COMMA)
            self.state = 115
            _la = self._input.LA(1)
            if not(_la==28 or _la==30):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()


            temp_height_multiplier = self._input.LT(-1).text
            if temp_height_multiplier.replace(".","",1).isdigit():
                temp_height_multiplier = float(temp_height_multiplier)
            else:  
                temp_height_multiplier = float(self.symbol_table.get_value(temp_height_multiplier))
                

            self.state = 117
            self.match(gec_parserParser.COMMA)
            self.state = 118
            _la = self._input.LA(1)
            if not(_la==28 or _la==31):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()


            temp_texture = self._input.LT(-1).text
            if temp_texture.startswith('"') and temp_texture.endswith('"'):
                temp_texture = temp_texture[1:-1]
            else:
                temp_texture = self.symbol_table.get_value(temp_texture)


            self.state = 120
            self.match(gec_parserParser.COMMA)

            self.state = 121
            self.match(gec_parserParser.ID)

            temp_game_objects = self._input.LT(-1).text
            temp_game_objects = self.symbol_table.get_value(temp_game_objects)


            self.state = 123
            self.match(gec_parserParser.RPAREN)

            localctx.chunk = Chunk(temp_pos_x, temp_pos_y, temp_scale, temp_height_multiplier, temp_texture, temp_game_objects)
                
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
            self.gameobject = None

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




    def gameobject_constructor(self):

        localctx = gec_parserParser.Gameobject_constructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_gameobject_constructor)
        self._la = 0 # Token type
        try:
            self.state = 153
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                self.match(gec_parserParser.GAMEOBJECT)
                self.state = 127
                self.match(gec_parserParser.LPAREN)
                self.state = 128
                _la = self._input.LA(1)
                if not(_la==28 or _la==31):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


                temp_model = self._input.LT(-1).text
                if temp_model.startswith('"') and temp_model.endswith('"'):
                    temp_model = temp_model[1:-1]
                else:
                    temp_model = self.symbol_table.get_value(temp_model)


                self.state = 130
                self.match(gec_parserParser.COMMA)
                self.state = 131
                _la = self._input.LA(1)
                if not(_la==28 or _la==29):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()

                    
                temp_density = self._input.LT(-1).text
                if temp_density.isdigit():
                    temp_density = int(temp_density)
                else:  
                    temp_density = int(self.symbol_table.get_value(temp_density))
                    

                self.state = 133
                self.match(gec_parserParser.COMMA)
                self.state = 134
                _la = self._input.LA(1)
                if not(_la==28 or _la==30):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()

                    
                temp_min_scale = self._input.LT(-1).text
                if temp_min_scale.replace(".","",1).isdigit():
                    temp_min_scale = float(temp_min_scale)
                else:  
                    temp_min_scale = float(self.symbol_table.get_value(temp_min_scale))
                    

                self.state = 136
                self.match(gec_parserParser.COMMA)
                self.state = 137
                _la = self._input.LA(1)
                if not(_la==28 or _la==30):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()

                    
                temp_max_scale = self._input.LT(-1).text
                if temp_max_scale.replace(".","",1).isdigit():
                    temp_max_scale = float(temp_max_scale)
                else:  
                    temp_max_scale = float(self.symbol_table.get_value(temp_max_scale))
                    

                self.state = 139
                self.match(gec_parserParser.RPAREN)

                localctx.gameobject = GameObject(temp_model, temp_density, temp_min_scale, temp_max_scale)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
                self.match(gec_parserParser.GAMEOBJECT)
                self.state = 142
                self.match(gec_parserParser.LPAREN)
                self.state = 143
                _la = self._input.LA(1)
                if not(_la==28 or _la==31):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()

                    
                temp_model = self._input.LT(-1).text
                if temp_model.startswith('"') and temp_model.endswith('"'):
                    temp_model = temp_model[1:-1]
                else:
                    temp_model = self.symbol_table.get_value(temp_model)
                    

                self.state = 145
                self.match(gec_parserParser.COMMA)
                self.state = 146
                _la = self._input.LA(1)
                if not(_la==28 or _la==29):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()

                    
                temp_density = self._input.LT(-1).text
                if temp_density.isdigit():
                    temp_density = int(temp_density)
                else:  
                    temp_density = int(self.symbol_table.get_value(temp_density))
                    

                self.state = 148
                self.match(gec_parserParser.COMMA)
                self.state = 149
                _la = self._input.LA(1)
                if not(_la==28 or _la==30):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()

                    
                temp_scale = self._input.LT(-1).text
                if temp_scale.replace(".","",1).isdigit():
                    temp_scale = float(temp_scale)
                else:  
                    temp_scale = float(self.symbol_table.get_value(temp_scale))
                    

                self.state = 151
                self.match(gec_parserParser.RPAREN)

                localctx.gameobject = GameObject(temp_model, temp_density, temp_scale)

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
            self._ID = None # Token
            self._array = None # ArrayContext

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




    def define_list(self):

        localctx = gec_parserParser.Define_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_define_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.state = 155
                self.match(gec_parserParser.LIST)
                self.state = 156
                self.match(gec_parserParser.LT)
                self.state = 157
                _la = self._input.LA(1)
                if not(_la==11 or _la==12):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 158
                self.match(gec_parserParser.GT)
                pass
            elif token in [28]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 162
            localctx._ID = self.match(gec_parserParser.ID)
            self.state = 163
            self.match(gec_parserParser.ASSIGN)
            self.state = 164
            localctx._array = self.array()

            self.symbol_table.set_value((None if localctx._ID is None else localctx._ID.text), localctx._array.object_list, "LIST<" + (None if localctx._ID is None else localctx._ID.text) + ">", "Contexto")

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
            self.object_list = None

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




    def array(self):

        localctx = gec_parserParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.state = 197
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.match(gec_parserParser.LSQUARE)
                self.state = 176
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [28]:
                    self.state = 168
                    self.match(gec_parserParser.ID)
                    localctx.object_list = [self.symbol_table.get_value(self._input.LT(-1).text)]
                    pass
                elif token in [11]:
                    self.state = 170
                    self.chunk_constructor()
                    localctx.object_list = [chunk_constructor.chunk]
                    pass
                elif token in [12]:
                    self.state = 173
                    self.gameobject_constructor()
                    localctx.object_list = [gameobject_constructor.gameobject]
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 191
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==23:
                    self.state = 178
                    self.match(gec_parserParser.COMMA)
                    self.state = 187
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [28]:
                        self.state = 179
                        self.match(gec_parserParser.ID)
                        localctx.object_list.append(self.symbol_table.get_value(self._input.LT(-1).text))
                        pass
                    elif token in [11]:
                        self.state = 181
                        self.chunk_constructor()
                        localctx.object_list.append(chunk_constructor.chunk)
                        pass
                    elif token in [12]:
                        self.state = 184
                        self.gameobject_constructor()
                        localctx.object_list.append(gameobject_constructor.gameobject)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 193
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 194
                self.match(gec_parserParser.RSQUARE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 195
                self.match(gec_parserParser.LSQUARE)
                self.state = 196
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




    def append_statement(self):

        localctx = gec_parserParser.Append_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_append_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(gec_parserParser.APPEND)
            self.state = 200
            self.match(gec_parserParser.ID)
            object_list_id = self._input.LT(-1).text
            self.state = 205
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.state = 202
                self.match(gec_parserParser.ID)
                pass
            elif token in [12]:
                self.state = 203
                self.gameobject_constructor()
                pass
            elif token in [11]:
                self.state = 204
                self.chunk_constructor()
                pass
            else:
                raise NoViableAltException(self)

             
            print("object_list_id", object_list_id)
            temp_object = self._input.LT(-1).text
            if isinstance(temp_object, Chunk):
                temp_object = temp_object
            elif isinstance(temp_object, GameObject):
                temp_object = temp_object
            else:
                temp_object = self.symbol_table.get_value(temp_object)
            object_list = self.symbol_table.get_value(object_list_id)
            object_list.append(temp_object)
            self.symbol_table.set_value(object_list_id, object_list, "LIST<" + self.get_type(temp_object) + ">", "Contexto")

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
            self.chunk = None

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




    def add_statement(self):

        localctx = gec_parserParser.Add_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_add_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 209
                self.match(gec_parserParser.ADD)
                self.state = 210
                self.match(gec_parserParser.ID)
                pass

            elif la_ == 2:
                self.state = 211
                self.match(gec_parserParser.ADD)
                self.state = 212
                self.chunk_constructor()
                pass




            temp_chunk = self._input.LT(-1).text
            if isinstance(temp_chunk, Chunk):
                temp_chunk = temp_chunk
            else:
                temp_chunk = self.symbol_table.get_value(temp_chunk)
            localctx.chunk = temp_chunk

                
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
            self._statement = None # StatementContext
            self.statements = list() # of StatementContexts

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




    def for_loop_number(self):

        localctx = gec_parserParser.For_loop_numberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_for_loop_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(gec_parserParser.FOR)
            self.state = 218
            self.match(gec_parserParser.ID)
            id = self._input.LT(-1).text
            self.state = 220
            self.match(gec_parserParser.FROM)
            self.state = 221
            self.match(gec_parserParser.INT_LITERAL)
            start = int(self._input.LT(-1).text)
            self.state = 223
            self.match(gec_parserParser.TO)
            self.state = 224
            self.match(gec_parserParser.INT_LITERAL)
            end = int(self._input.LT(-1).text) 

            print("FOR", id, start, end)
            for i in range(start, end + 1):
                self.symbol_table.set_value(id, i, "INT", "Contexto")
                for stmt in localctx.statements:
                    pass
                
            self.state = 227
            self.match(gec_parserParser.LBRACE)
            self.state = 231
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 268564656) != 0):
                self.state = 228
                localctx._statement = self.statement()
                localctx.statements.append(localctx._statement)
                self.state = 233
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 234
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
            self._statement = None # StatementContext
            self.statements = list() # of StatementContexts

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




    def for_loop_list(self):

        localctx = gec_parserParser.For_loop_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_for_loop_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.match(gec_parserParser.FOR)
            self.state = 237
            self.match(gec_parserParser.ID)
            id = self._input.LT(-1).text
            self.state = 239
            self.match(gec_parserParser.IN)
            self.state = 240
            self.match(gec_parserParser.ID)
            list_id = self._input.LT(-1).text
            self.state = 242
            self.match(gec_parserParser.LBRACE)
            self.state = 246
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 268564656) != 0):
                self.state = 243
                localctx._statement = self.statement()
                localctx.statements.append(localctx._statement)
                self.state = 248
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 249
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
            self._expression = None # ExpressionContext
            self._chunk_constructor = None # Chunk_constructorContext
            self._gameobject_constructor = None # Gameobject_constructorContext

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




    def assignment(self):

        localctx = gec_parserParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_assignment)
        try:
            self.state = 283
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 255
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [14]:
                    self.state = 251
                    self.match(gec_parserParser.INT)
                    pass
                elif token in [16]:
                    self.state = 252
                    self.match(gec_parserParser.STRING)
                    pass
                elif token in [15]:
                    self.state = 253
                    self.match(gec_parserParser.FLOAT)
                    pass
                elif token in [28]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 257
                self.match(gec_parserParser.ID)
                id = self._input.LT(-1).text 
                self.state = 259
                self.match(gec_parserParser.ASSIGN)
                self.state = 260
                localctx._expression = self.expression()

                self.symbol_table.set_value(id, localctx._expression.value, "INT", "Contexto")
                    
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 265
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [11]:
                    self.state = 263
                    self.match(gec_parserParser.CHUNK)
                    pass
                elif token in [28]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 267
                self.match(gec_parserParser.ID)
                id = self._input.LT(-1).text 
                self.state = 269
                self.match(gec_parserParser.ASSIGN)
                self.state = 270
                localctx._chunk_constructor = self.chunk_constructor()

                self.symbol_table.set_value(id, localctx._chunk_constructor.chunk, "CHUNK", "Contexto")
                    
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 275
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [12]:
                    self.state = 273
                    self.match(gec_parserParser.GAMEOBJECT)
                    pass
                elif token in [28]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 277
                self.match(gec_parserParser.ID)
                id = self._input.LT(-1).text 
                self.state = 279
                self.match(gec_parserParser.ASSIGN)
                self.state = 280
                localctx._gameobject_constructor = self.gameobject_constructor()
                 
                self.symbol_table.set_value(id, localctx._gameobject_constructor.gameobject, "GAMEOBJECT", "Contexto")
                    
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
            self.value = None
            self.e1 = None # Expression_auxContext
            self.op = None # Token
            self.e2 = None # Expression_auxContext

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




    def expression(self):

        localctx = gec_parserParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            localctx.e1 = self.expression_aux()

            values = [localctx.e1.value]
            operators = []
                    
            self.state = 293
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27:
                self.state = 287
                localctx.op = self.match(gec_parserParser.OP_ARIT)
                self.state = 288
                localctx.e2 = self.expression_aux()

                values.append(localctx.e2.value)
                operators.append((None if localctx.op is None else localctx.op.text))
                        
                self.state = 295
                self._errHandler.sync(self)
                _la = self._input.LA(1)


            localctx.value = self.eval_expression(values, operators)
                
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
            self.value = None
            self._expression = None # ExpressionContext

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




    def expression_aux(self):

        localctx = gec_parserParser.Expression_auxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expression_aux)
        try:
            self.state = 311
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 298
                self.match(gec_parserParser.STRING_LITERAL)
                 
                localctx.value = self._input.LT(-1).text
                    
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 300
                self.match(gec_parserParser.INT_LITERAL)

                localctx.value = int(self._input.LT(-1).text)
                    
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 3)
                self.state = 302
                self.match(gec_parserParser.FLOAT_LITERAL)

                localctx.value = float(self._input.LT(-1).text)
                    
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 4)
                self.state = 304
                self.match(gec_parserParser.ID)

                localctx.value = self._input.LT(-1).text
                    
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 5)
                self.state = 306
                self.match(gec_parserParser.LPAREN)
                self.state = 307
                localctx._expression = self.expression()
                self.state = 308
                self.match(gec_parserParser.RPAREN)

                localctx.value = localctx._expression.value
                    
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




    def declaration(self):

        localctx = gec_parserParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.state = 313
                self.match(gec_parserParser.INT)
                type = self._input.LT(-1).text
                pass
            elif token in [16]:
                self.state = 315
                self.match(gec_parserParser.STRING)
                type = self._input.LT(-1).text
                pass
            elif token in [15]:
                self.state = 317
                self.match(gec_parserParser.FLOAT)
                type = self._input.LT(-1).text
                pass
            elif token in [11]:
                self.state = 319
                self.match(gec_parserParser.CHUNK)
                type = self._input.LT(-1).text
                pass
            elif token in [12]:
                self.state = 321
                self.match(gec_parserParser.GAMEOBJECT)
                type = self._input.LT(-1).text
                pass
            elif token in [13]:
                self.state = 323
                self.match(gec_parserParser.LIST)
                self.state = 324
                self.match(gec_parserParser.LT)
                self.state = 325
                _la = self._input.LA(1)
                if not(_la==11 or _la==12):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 326
                self.match(gec_parserParser.GT)
                type = "LIST<" + self._input.LT(-2).text + ">"
                pass
            else:
                raise NoViableAltException(self)

            self.state = 330
            self.match(gec_parserParser.ID)
            id = self._input.LT(-1).text

            self.symbol_table.set_value(id, [], type, "Contexto")
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





