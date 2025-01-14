# Generated from gec_parser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .gec_parserParser import gec_parserParser
else:
    from gec_parserParser import gec_parserParser

# This class defines a complete listener for a parse tree produced by gec_parserParser.
class gec_parserListener(ParseTreeListener):

    # Enter a parse tree produced by gec_parserParser#program.
    def enterProgram(self, ctx:gec_parserParser.ProgramContext):
        pass

    # Exit a parse tree produced by gec_parserParser#program.
    def exitProgram(self, ctx:gec_parserParser.ProgramContext):
        pass


    # Enter a parse tree produced by gec_parserParser#define_setup.
    def enterDefine_setup(self, ctx:gec_parserParser.Define_setupContext):
        pass

    # Exit a parse tree produced by gec_parserParser#define_setup.
    def exitDefine_setup(self, ctx:gec_parserParser.Define_setupContext):
        pass


    # Enter a parse tree produced by gec_parserParser#define_world.
    def enterDefine_world(self, ctx:gec_parserParser.Define_worldContext):
        pass

    # Exit a parse tree produced by gec_parserParser#define_world.
    def exitDefine_world(self, ctx:gec_parserParser.Define_worldContext):
        pass


    # Enter a parse tree produced by gec_parserParser#define_scene.
    def enterDefine_scene(self, ctx:gec_parserParser.Define_sceneContext):
        pass

    # Exit a parse tree produced by gec_parserParser#define_scene.
    def exitDefine_scene(self, ctx:gec_parserParser.Define_sceneContext):
        pass


    # Enter a parse tree produced by gec_parserParser#statement.
    def enterStatement(self, ctx:gec_parserParser.StatementContext):
        pass

    # Exit a parse tree produced by gec_parserParser#statement.
    def exitStatement(self, ctx:gec_parserParser.StatementContext):
        pass


    # Enter a parse tree produced by gec_parserParser#chunk_constructor.
    def enterChunk_constructor(self, ctx:gec_parserParser.Chunk_constructorContext):
        pass

    # Exit a parse tree produced by gec_parserParser#chunk_constructor.
    def exitChunk_constructor(self, ctx:gec_parserParser.Chunk_constructorContext):
        pass


    # Enter a parse tree produced by gec_parserParser#gameobject_constructor.
    def enterGameobject_constructor(self, ctx:gec_parserParser.Gameobject_constructorContext):
        pass

    # Exit a parse tree produced by gec_parserParser#gameobject_constructor.
    def exitGameobject_constructor(self, ctx:gec_parserParser.Gameobject_constructorContext):
        pass


    # Enter a parse tree produced by gec_parserParser#define_list.
    def enterDefine_list(self, ctx:gec_parserParser.Define_listContext):
        pass

    # Exit a parse tree produced by gec_parserParser#define_list.
    def exitDefine_list(self, ctx:gec_parserParser.Define_listContext):
        pass


    # Enter a parse tree produced by gec_parserParser#array.
    def enterArray(self, ctx:gec_parserParser.ArrayContext):
        pass

    # Exit a parse tree produced by gec_parserParser#array.
    def exitArray(self, ctx:gec_parserParser.ArrayContext):
        pass


    # Enter a parse tree produced by gec_parserParser#append_statement.
    def enterAppend_statement(self, ctx:gec_parserParser.Append_statementContext):
        pass

    # Exit a parse tree produced by gec_parserParser#append_statement.
    def exitAppend_statement(self, ctx:gec_parserParser.Append_statementContext):
        pass


    # Enter a parse tree produced by gec_parserParser#add_statement.
    def enterAdd_statement(self, ctx:gec_parserParser.Add_statementContext):
        pass

    # Exit a parse tree produced by gec_parserParser#add_statement.
    def exitAdd_statement(self, ctx:gec_parserParser.Add_statementContext):
        pass


    # Enter a parse tree produced by gec_parserParser#for_loop_number.
    def enterFor_loop_number(self, ctx:gec_parserParser.For_loop_numberContext):
        pass

    # Exit a parse tree produced by gec_parserParser#for_loop_number.
    def exitFor_loop_number(self, ctx:gec_parserParser.For_loop_numberContext):
        pass


    # Enter a parse tree produced by gec_parserParser#for_loop_list.
    def enterFor_loop_list(self, ctx:gec_parserParser.For_loop_listContext):
        pass

    # Exit a parse tree produced by gec_parserParser#for_loop_list.
    def exitFor_loop_list(self, ctx:gec_parserParser.For_loop_listContext):
        pass


    # Enter a parse tree produced by gec_parserParser#assignment.
    def enterAssignment(self, ctx:gec_parserParser.AssignmentContext):
        pass

    # Exit a parse tree produced by gec_parserParser#assignment.
    def exitAssignment(self, ctx:gec_parserParser.AssignmentContext):
        pass


    # Enter a parse tree produced by gec_parserParser#numeric_expression.
    def enterNumeric_expression(self, ctx:gec_parserParser.Numeric_expressionContext):
        pass

    # Exit a parse tree produced by gec_parserParser#numeric_expression.
    def exitNumeric_expression(self, ctx:gec_parserParser.Numeric_expressionContext):
        pass


    # Enter a parse tree produced by gec_parserParser#numeric_expression_aux.
    def enterNumeric_expression_aux(self, ctx:gec_parserParser.Numeric_expression_auxContext):
        pass

    # Exit a parse tree produced by gec_parserParser#numeric_expression_aux.
    def exitNumeric_expression_aux(self, ctx:gec_parserParser.Numeric_expression_auxContext):
        pass


    # Enter a parse tree produced by gec_parserParser#string_expression.
    def enterString_expression(self, ctx:gec_parserParser.String_expressionContext):
        pass

    # Exit a parse tree produced by gec_parserParser#string_expression.
    def exitString_expression(self, ctx:gec_parserParser.String_expressionContext):
        pass


    # Enter a parse tree produced by gec_parserParser#string_expression_aux.
    def enterString_expression_aux(self, ctx:gec_parserParser.String_expression_auxContext):
        pass

    # Exit a parse tree produced by gec_parserParser#string_expression_aux.
    def exitString_expression_aux(self, ctx:gec_parserParser.String_expression_auxContext):
        pass


    # Enter a parse tree produced by gec_parserParser#declaration.
    def enterDeclaration(self, ctx:gec_parserParser.DeclarationContext):
        pass

    # Exit a parse tree produced by gec_parserParser#declaration.
    def exitDeclaration(self, ctx:gec_parserParser.DeclarationContext):
        pass



del gec_parserParser