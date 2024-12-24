// Generated from /home/alex/ProcesadoresLenguaje/python/src/antlr4/gec_parser.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link gec_parserParser}.
 */
public interface gec_parserListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link gec_parserParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(gec_parserParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link gec_parserParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(gec_parserParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link gec_parserParser#define_setup}.
	 * @param ctx the parse tree
	 */
	void enterDefine_setup(gec_parserParser.Define_setupContext ctx);
	/**
	 * Exit a parse tree produced by {@link gec_parserParser#define_setup}.
	 * @param ctx the parse tree
	 */
	void exitDefine_setup(gec_parserParser.Define_setupContext ctx);
	/**
	 * Enter a parse tree produced by {@link gec_parserParser#define_world}.
	 * @param ctx the parse tree
	 */
	void enterDefine_world(gec_parserParser.Define_worldContext ctx);
	/**
	 * Exit a parse tree produced by {@link gec_parserParser#define_world}.
	 * @param ctx the parse tree
	 */
	void exitDefine_world(gec_parserParser.Define_worldContext ctx);
	/**
	 * Enter a parse tree produced by {@link gec_parserParser#define_scene}.
	 * @param ctx the parse tree
	 */
	void enterDefine_scene(gec_parserParser.Define_sceneContext ctx);
	/**
	 * Exit a parse tree produced by {@link gec_parserParser#define_scene}.
	 * @param ctx the parse tree
	 */
	void exitDefine_scene(gec_parserParser.Define_sceneContext ctx);
	/**
	 * Enter a parse tree produced by {@link gec_parserParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(gec_parserParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link gec_parserParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(gec_parserParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link gec_parserParser#chunk_constructor}.
	 * @param ctx the parse tree
	 */
	void enterChunk_constructor(gec_parserParser.Chunk_constructorContext ctx);
	/**
	 * Exit a parse tree produced by {@link gec_parserParser#chunk_constructor}.
	 * @param ctx the parse tree
	 */
	void exitChunk_constructor(gec_parserParser.Chunk_constructorContext ctx);
	/**
	 * Enter a parse tree produced by {@link gec_parserParser#gameobject_constructor}.
	 * @param ctx the parse tree
	 */
	void enterGameobject_constructor(gec_parserParser.Gameobject_constructorContext ctx);
	/**
	 * Exit a parse tree produced by {@link gec_parserParser#gameobject_constructor}.
	 * @param ctx the parse tree
	 */
	void exitGameobject_constructor(gec_parserParser.Gameobject_constructorContext ctx);
	/**
	 * Enter a parse tree produced by {@link gec_parserParser#define_list}.
	 * @param ctx the parse tree
	 */
	void enterDefine_list(gec_parserParser.Define_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link gec_parserParser#define_list}.
	 * @param ctx the parse tree
	 */
	void exitDefine_list(gec_parserParser.Define_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link gec_parserParser#array}.
	 * @param ctx the parse tree
	 */
	void enterArray(gec_parserParser.ArrayContext ctx);
	/**
	 * Exit a parse tree produced by {@link gec_parserParser#array}.
	 * @param ctx the parse tree
	 */
	void exitArray(gec_parserParser.ArrayContext ctx);
	/**
	 * Enter a parse tree produced by {@link gec_parserParser#append_statement}.
	 * @param ctx the parse tree
	 */
	void enterAppend_statement(gec_parserParser.Append_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link gec_parserParser#append_statement}.
	 * @param ctx the parse tree
	 */
	void exitAppend_statement(gec_parserParser.Append_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link gec_parserParser#add_statement}.
	 * @param ctx the parse tree
	 */
	void enterAdd_statement(gec_parserParser.Add_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link gec_parserParser#add_statement}.
	 * @param ctx the parse tree
	 */
	void exitAdd_statement(gec_parserParser.Add_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link gec_parserParser#for_loop_number}.
	 * @param ctx the parse tree
	 */
	void enterFor_loop_number(gec_parserParser.For_loop_numberContext ctx);
	/**
	 * Exit a parse tree produced by {@link gec_parserParser#for_loop_number}.
	 * @param ctx the parse tree
	 */
	void exitFor_loop_number(gec_parserParser.For_loop_numberContext ctx);
	/**
	 * Enter a parse tree produced by {@link gec_parserParser#for_loop_list}.
	 * @param ctx the parse tree
	 */
	void enterFor_loop_list(gec_parserParser.For_loop_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link gec_parserParser#for_loop_list}.
	 * @param ctx the parse tree
	 */
	void exitFor_loop_list(gec_parserParser.For_loop_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link gec_parserParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(gec_parserParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link gec_parserParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(gec_parserParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link gec_parserParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(gec_parserParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link gec_parserParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(gec_parserParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link gec_parserParser#expression_aux}.
	 * @param ctx the parse tree
	 */
	void enterExpression_aux(gec_parserParser.Expression_auxContext ctx);
	/**
	 * Exit a parse tree produced by {@link gec_parserParser#expression_aux}.
	 * @param ctx the parse tree
	 */
	void exitExpression_aux(gec_parserParser.Expression_auxContext ctx);
	/**
	 * Enter a parse tree produced by {@link gec_parserParser#declaration}.
	 * @param ctx the parse tree
	 */
	void enterDeclaration(gec_parserParser.DeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link gec_parserParser#declaration}.
	 * @param ctx the parse tree
	 */
	void exitDeclaration(gec_parserParser.DeclarationContext ctx);
}