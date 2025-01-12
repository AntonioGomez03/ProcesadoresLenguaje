# Generated from gec_parser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .gec_parserParser import gec_parserParser
else:
    from gec_parserParser import gec_parserParser

# This class defines a complete generic visitor for a parse tree produced by gec_parserParser.

class gec_parserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by gec_parserParser#program.
    def visitProgram(self, ctx:gec_parserParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gec_parserParser#define_setup.
    def visitDefine_setup(self, ctx:gec_parserParser.Define_setupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gec_parserParser#define_world.
    def visitDefine_world(self, ctx:gec_parserParser.Define_worldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gec_parserParser#define_scene.
    def visitDefine_scene(self, ctx:gec_parserParser.Define_sceneContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gec_parserParser#statement.
    def visitStatement(self, ctx:gec_parserParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gec_parserParser#chunk_constructor.
    def visitChunk_constructor(self, ctx:gec_parserParser.Chunk_constructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gec_parserParser#gameobject_constructor.
    def visitGameobject_constructor(self, ctx:gec_parserParser.Gameobject_constructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gec_parserParser#define_list.
    def visitDefine_list(self, ctx:gec_parserParser.Define_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gec_parserParser#array.
    def visitArray(self, ctx:gec_parserParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gec_parserParser#append_statement.
    def visitAppend_statement(self, ctx:gec_parserParser.Append_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gec_parserParser#add_statement.
    def visitAdd_statement(self, ctx:gec_parserParser.Add_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gec_parserParser#for_loop_number.
    def visitFor_loop_number(self, ctx:gec_parserParser.For_loop_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gec_parserParser#for_loop_list.
    def visitFor_loop_list(self, ctx:gec_parserParser.For_loop_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gec_parserParser#assignment.
    def visitAssignment(self, ctx:gec_parserParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gec_parserParser#numeric_expression.
    def visitNumeric_expression(self, ctx:gec_parserParser.Numeric_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gec_parserParser#numeric_expression_aux.
    def visitNumeric_expression_aux(self, ctx:gec_parserParser.Numeric_expression_auxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gec_parserParser#string_expression.
    def visitString_expression(self, ctx:gec_parserParser.String_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gec_parserParser#string_expression_aux.
    def visitString_expression_aux(self, ctx:gec_parserParser.String_expression_auxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gec_parserParser#declaration.
    def visitDeclaration(self, ctx:gec_parserParser.DeclarationContext):
        return self.visitChildren(ctx)



del gec_parserParser