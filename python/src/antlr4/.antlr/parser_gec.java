// Generated from /home/antonio/Documentos/Universidad/Cuarto/Procesadores de Lenguajes/ProcesadoresLenguaje/python/src/antlr4/parser_gec.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class parser_gec extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		DEFINE=1, SETUP=2, WORLD=3, ADD=4, APPEND=5, SCENE=6, FOR=7, FROM=8, TO=9, 
		IN=10, DESCRIPTOR=11, LIST=12, INT=13, FLOAT=14, STRING=15, LPAREN=16, 
		RPAREN=17, LBRACE=18, RBRACE=19, LSQUARE=20, RSQUARE=21, COMMA=22, LT=23, 
		GT=24, ASSIGN=25, OP_ARIT=26, ID=27, INT_LITERAL=28, FLOAT_LITERAL=29, 
		STRING_LITERAL=30, COMMENT=31, WS=32;
	public static final int
		RULE_program = 0, RULE_define_setup = 1, RULE_define_world = 2, RULE_define_scene = 3, 
		RULE_parameters = 4, RULE_expression = 5, RULE_expression_aux = 6, RULE_descriptor_constructor = 7, 
		RULE_setup_statement = 8, RULE_statement = 9, RULE_assignment = 10, RULE_declaration = 11, 
		RULE_data_type = 12, RULE_list_type = 13, RULE_append_statement = 14, 
		RULE_for_loop_setup = 15, RULE_for_loop_world = 16, RULE_add_statement = 17;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "define_setup", "define_world", "define_scene", "parameters", 
			"expression", "expression_aux", "descriptor_constructor", "setup_statement", 
			"statement", "assignment", "declaration", "data_type", "list_type", "append_statement", 
			"for_loop_setup", "for_loop_world", "add_statement"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'DEFINE'", "'SETUP'", "'WORLD'", "'ADD'", "'APPEND'", "'SCENE'", 
			"'FOR'", "'FROM'", "'TO'", "'IN'", null, "'LIST'", "'INT'", "'FLOAT'", 
			"'STRING'", "'('", "')'", "'{'", "'}'", "'['", "']'", "','", "'<'", "'>'", 
			"'='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "DEFINE", "SETUP", "WORLD", "ADD", "APPEND", "SCENE", "FOR", "FROM", 
			"TO", "IN", "DESCRIPTOR", "LIST", "INT", "FLOAT", "STRING", "LPAREN", 
			"RPAREN", "LBRACE", "RBRACE", "LSQUARE", "RSQUARE", "COMMA", "LT", "GT", 
			"ASSIGN", "OP_ARIT", "ID", "INT_LITERAL", "FLOAT_LITERAL", "STRING_LITERAL", 
			"COMMENT", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "parser_gec.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public parser_gec(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public Define_setupContext define_setup() {
			return getRuleContext(Define_setupContext.class,0);
		}
		public Define_worldContext define_world() {
			return getRuleContext(Define_worldContext.class,0);
		}
		public TerminalNode EOF() { return getToken(parser_gec.EOF, 0); }
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(36);
			define_setup();
			setState(37);
			define_world();
			setState(38);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Define_setupContext extends ParserRuleContext {
		public TerminalNode DEFINE() { return getToken(parser_gec.DEFINE, 0); }
		public TerminalNode SETUP() { return getToken(parser_gec.SETUP, 0); }
		public TerminalNode LPAREN() { return getToken(parser_gec.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(parser_gec.RPAREN, 0); }
		public TerminalNode LBRACE() { return getToken(parser_gec.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(parser_gec.RBRACE, 0); }
		public List<Setup_statementContext> setup_statement() {
			return getRuleContexts(Setup_statementContext.class);
		}
		public Setup_statementContext setup_statement(int i) {
			return getRuleContext(Setup_statementContext.class,i);
		}
		public Define_setupContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_define_setup; }
	}

	public final Define_setupContext define_setup() throws RecognitionException {
		Define_setupContext _localctx = new Define_setupContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_define_setup);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(40);
			match(DEFINE);
			setState(41);
			match(SETUP);
			setState(42);
			match(LPAREN);
			setState(43);
			match(RPAREN);
			setState(44);
			match(LBRACE);
			setState(48);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 134281376L) != 0)) {
				{
				{
				setState(45);
				setup_statement();
				}
				}
				setState(50);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(51);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Define_worldContext extends ParserRuleContext {
		public TerminalNode DEFINE() { return getToken(parser_gec.DEFINE, 0); }
		public TerminalNode WORLD() { return getToken(parser_gec.WORLD, 0); }
		public TerminalNode LPAREN() { return getToken(parser_gec.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(parser_gec.RPAREN, 0); }
		public TerminalNode LBRACE() { return getToken(parser_gec.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(parser_gec.RBRACE, 0); }
		public List<Define_sceneContext> define_scene() {
			return getRuleContexts(Define_sceneContext.class);
		}
		public Define_sceneContext define_scene(int i) {
			return getRuleContext(Define_sceneContext.class,i);
		}
		public Define_worldContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_define_world; }
	}

	public final Define_worldContext define_world() throws RecognitionException {
		Define_worldContext _localctx = new Define_worldContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_define_world);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(53);
			match(DEFINE);
			setState(54);
			match(WORLD);
			setState(55);
			match(LPAREN);
			setState(56);
			expression();
			setState(57);
			match(RPAREN);
			setState(58);
			match(LBRACE);
			setState(60); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(59);
				define_scene();
				}
				}
				setState(62); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==DEFINE );
			setState(64);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Define_sceneContext extends ParserRuleContext {
		public TerminalNode DEFINE() { return getToken(parser_gec.DEFINE, 0); }
		public TerminalNode SCENE() { return getToken(parser_gec.SCENE, 0); }
		public TerminalNode LPAREN() { return getToken(parser_gec.LPAREN, 0); }
		public ParametersContext parameters() {
			return getRuleContext(ParametersContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(parser_gec.RPAREN, 0); }
		public TerminalNode LBRACE() { return getToken(parser_gec.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(parser_gec.RBRACE, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public Define_sceneContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_define_scene; }
	}

	public final Define_sceneContext define_scene() throws RecognitionException {
		Define_sceneContext _localctx = new Define_sceneContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_define_scene);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(66);
			match(DEFINE);
			setState(67);
			match(SCENE);
			setState(68);
			match(LPAREN);
			setState(69);
			parameters();
			setState(70);
			match(RPAREN);
			setState(71);
			match(LBRACE);
			setState(75);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 134281392L) != 0)) {
				{
				{
				setState(72);
				statement();
				}
				}
				setState(77);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(78);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParametersContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(parser_gec.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(parser_gec.COMMA, i);
		}
		public ParametersContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameters; }
	}

	public final ParametersContext parameters() throws RecognitionException {
		ParametersContext _localctx = new ParametersContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_parameters);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(80);
			expression();
			setState(85);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(81);
				match(COMMA);
				setState(82);
				expression();
				}
				}
				setState(87);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpressionContext extends ParserRuleContext {
		public List<Expression_auxContext> expression_aux() {
			return getRuleContexts(Expression_auxContext.class);
		}
		public Expression_auxContext expression_aux(int i) {
			return getRuleContext(Expression_auxContext.class,i);
		}
		public List<TerminalNode> OP_ARIT() { return getTokens(parser_gec.OP_ARIT); }
		public TerminalNode OP_ARIT(int i) {
			return getToken(parser_gec.OP_ARIT, i);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_expression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(88);
			expression_aux();
			setState(93);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==OP_ARIT) {
				{
				{
				setState(89);
				match(OP_ARIT);
				setState(90);
				expression_aux();
				}
				}
				setState(95);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expression_auxContext extends ParserRuleContext {
		public TerminalNode STRING_LITERAL() { return getToken(parser_gec.STRING_LITERAL, 0); }
		public TerminalNode INT_LITERAL() { return getToken(parser_gec.INT_LITERAL, 0); }
		public TerminalNode FLOAT_LITERAL() { return getToken(parser_gec.FLOAT_LITERAL, 0); }
		public TerminalNode ID() { return getToken(parser_gec.ID, 0); }
		public TerminalNode LPAREN() { return getToken(parser_gec.LPAREN, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode RPAREN() { return getToken(parser_gec.RPAREN, 0); }
		public TerminalNode LSQUARE() { return getToken(parser_gec.LSQUARE, 0); }
		public TerminalNode RSQUARE() { return getToken(parser_gec.RSQUARE, 0); }
		public List<TerminalNode> COMMA() { return getTokens(parser_gec.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(parser_gec.COMMA, i);
		}
		public Descriptor_constructorContext descriptor_constructor() {
			return getRuleContext(Descriptor_constructorContext.class,0);
		}
		public Expression_auxContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression_aux; }
	}

	public final Expression_auxContext expression_aux() throws RecognitionException {
		Expression_auxContext _localctx = new Expression_auxContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_expression_aux);
		int _la;
		try {
			setState(116);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case STRING_LITERAL:
				enterOuterAlt(_localctx, 1);
				{
				setState(96);
				match(STRING_LITERAL);
				}
				break;
			case INT_LITERAL:
				enterOuterAlt(_localctx, 2);
				{
				setState(97);
				match(INT_LITERAL);
				}
				break;
			case FLOAT_LITERAL:
				enterOuterAlt(_localctx, 3);
				{
				setState(98);
				match(FLOAT_LITERAL);
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 4);
				{
				setState(99);
				match(ID);
				}
				break;
			case LPAREN:
				enterOuterAlt(_localctx, 5);
				{
				setState(100);
				match(LPAREN);
				setState(101);
				expression();
				setState(102);
				match(RPAREN);
				}
				break;
			case LSQUARE:
				enterOuterAlt(_localctx, 6);
				{
				setState(104);
				match(LSQUARE);
				setState(105);
				expression();
				setState(110);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(106);
					match(COMMA);
					setState(107);
					expression();
					}
					}
					setState(112);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(113);
				match(RSQUARE);
				}
				break;
			case DESCRIPTOR:
				enterOuterAlt(_localctx, 7);
				{
				setState(115);
				descriptor_constructor();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Descriptor_constructorContext extends ParserRuleContext {
		public TerminalNode DESCRIPTOR() { return getToken(parser_gec.DESCRIPTOR, 0); }
		public TerminalNode LPAREN() { return getToken(parser_gec.LPAREN, 0); }
		public ParametersContext parameters() {
			return getRuleContext(ParametersContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(parser_gec.RPAREN, 0); }
		public Descriptor_constructorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_descriptor_constructor; }
	}

	public final Descriptor_constructorContext descriptor_constructor() throws RecognitionException {
		Descriptor_constructorContext _localctx = new Descriptor_constructorContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_descriptor_constructor);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(118);
			match(DESCRIPTOR);
			setState(119);
			match(LPAREN);
			setState(120);
			parameters();
			setState(121);
			match(RPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Setup_statementContext extends ParserRuleContext {
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public DeclarationContext declaration() {
			return getRuleContext(DeclarationContext.class,0);
		}
		public Append_statementContext append_statement() {
			return getRuleContext(Append_statementContext.class,0);
		}
		public For_loop_setupContext for_loop_setup() {
			return getRuleContext(For_loop_setupContext.class,0);
		}
		public Setup_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_setup_statement; }
	}

	public final Setup_statementContext setup_statement() throws RecognitionException {
		Setup_statementContext _localctx = new Setup_statementContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_setup_statement);
		try {
			setState(127);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(123);
				assignment();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(124);
				declaration();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(125);
				append_statement();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(126);
				for_loop_setup();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public Setup_statementContext setup_statement() {
			return getRuleContext(Setup_statementContext.class,0);
		}
		public Add_statementContext add_statement() {
			return getRuleContext(Add_statementContext.class,0);
		}
		public For_loop_worldContext for_loop_world() {
			return getRuleContext(For_loop_worldContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_statement);
		try {
			setState(132);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(129);
				setup_statement();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(130);
				add_statement();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(131);
				for_loop_world();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignmentContext extends ParserRuleContext {
		public Data_typeContext data_type() {
			return getRuleContext(Data_typeContext.class,0);
		}
		public TerminalNode ID() { return getToken(parser_gec.ID, 0); }
		public TerminalNode ASSIGN() { return getToken(parser_gec.ASSIGN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_assignment);
		try {
			setState(142);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case DESCRIPTOR:
			case LIST:
			case INT:
			case FLOAT:
			case STRING:
				enterOuterAlt(_localctx, 1);
				{
				setState(134);
				data_type();
				setState(135);
				match(ID);
				setState(136);
				match(ASSIGN);
				setState(137);
				expression();
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(139);
				match(ID);
				setState(140);
				match(ASSIGN);
				setState(141);
				expression();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclarationContext extends ParserRuleContext {
		public Data_typeContext data_type() {
			return getRuleContext(Data_typeContext.class,0);
		}
		public TerminalNode ID() { return getToken(parser_gec.ID, 0); }
		public DeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaration; }
	}

	public final DeclarationContext declaration() throws RecognitionException {
		DeclarationContext _localctx = new DeclarationContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_declaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(144);
			data_type();
			setState(145);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Data_typeContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(parser_gec.INT, 0); }
		public TerminalNode FLOAT() { return getToken(parser_gec.FLOAT, 0); }
		public TerminalNode STRING() { return getToken(parser_gec.STRING, 0); }
		public TerminalNode DESCRIPTOR() { return getToken(parser_gec.DESCRIPTOR, 0); }
		public List_typeContext list_type() {
			return getRuleContext(List_typeContext.class,0);
		}
		public Data_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_data_type; }
	}

	public final Data_typeContext data_type() throws RecognitionException {
		Data_typeContext _localctx = new Data_typeContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_data_type);
		try {
			setState(152);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
				enterOuterAlt(_localctx, 1);
				{
				setState(147);
				match(INT);
				}
				break;
			case FLOAT:
				enterOuterAlt(_localctx, 2);
				{
				setState(148);
				match(FLOAT);
				}
				break;
			case STRING:
				enterOuterAlt(_localctx, 3);
				{
				setState(149);
				match(STRING);
				}
				break;
			case DESCRIPTOR:
				enterOuterAlt(_localctx, 4);
				{
				setState(150);
				match(DESCRIPTOR);
				}
				break;
			case LIST:
				enterOuterAlt(_localctx, 5);
				{
				setState(151);
				list_type();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class List_typeContext extends ParserRuleContext {
		public TerminalNode LIST() { return getToken(parser_gec.LIST, 0); }
		public TerminalNode LT() { return getToken(parser_gec.LT, 0); }
		public TerminalNode DESCRIPTOR() { return getToken(parser_gec.DESCRIPTOR, 0); }
		public TerminalNode GT() { return getToken(parser_gec.GT, 0); }
		public List_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_list_type; }
	}

	public final List_typeContext list_type() throws RecognitionException {
		List_typeContext _localctx = new List_typeContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_list_type);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(154);
			match(LIST);
			setState(155);
			match(LT);
			setState(156);
			match(DESCRIPTOR);
			setState(157);
			match(GT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Append_statementContext extends ParserRuleContext {
		public TerminalNode APPEND() { return getToken(parser_gec.APPEND, 0); }
		public List<TerminalNode> ID() { return getTokens(parser_gec.ID); }
		public TerminalNode ID(int i) {
			return getToken(parser_gec.ID, i);
		}
		public Descriptor_constructorContext descriptor_constructor() {
			return getRuleContext(Descriptor_constructorContext.class,0);
		}
		public Append_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_append_statement; }
	}

	public final Append_statementContext append_statement() throws RecognitionException {
		Append_statementContext _localctx = new Append_statementContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_append_statement);
		try {
			setState(165);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(159);
				match(APPEND);
				setState(160);
				match(ID);
				setState(161);
				match(ID);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(162);
				match(APPEND);
				setState(163);
				match(ID);
				setState(164);
				descriptor_constructor();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class For_loop_setupContext extends ParserRuleContext {
		public TerminalNode FOR() { return getToken(parser_gec.FOR, 0); }
		public List<TerminalNode> ID() { return getTokens(parser_gec.ID); }
		public TerminalNode ID(int i) {
			return getToken(parser_gec.ID, i);
		}
		public TerminalNode FROM() { return getToken(parser_gec.FROM, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode TO() { return getToken(parser_gec.TO, 0); }
		public TerminalNode LBRACE() { return getToken(parser_gec.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(parser_gec.RBRACE, 0); }
		public List<Setup_statementContext> setup_statement() {
			return getRuleContexts(Setup_statementContext.class);
		}
		public Setup_statementContext setup_statement(int i) {
			return getRuleContext(Setup_statementContext.class,i);
		}
		public TerminalNode IN() { return getToken(parser_gec.IN, 0); }
		public For_loop_setupContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_for_loop_setup; }
	}

	public final For_loop_setupContext for_loop_setup() throws RecognitionException {
		For_loop_setupContext _localctx = new For_loop_setupContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_for_loop_setup);
		int _la;
		try {
			setState(194);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(167);
				match(FOR);
				setState(168);
				match(ID);
				setState(169);
				match(FROM);
				setState(170);
				expression();
				setState(171);
				match(TO);
				setState(172);
				expression();
				setState(173);
				match(LBRACE);
				setState(177);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 134281376L) != 0)) {
					{
					{
					setState(174);
					setup_statement();
					}
					}
					setState(179);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(180);
				match(RBRACE);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(182);
				match(FOR);
				setState(183);
				match(ID);
				setState(184);
				match(IN);
				setState(185);
				match(ID);
				setState(186);
				match(LBRACE);
				setState(190);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 134281376L) != 0)) {
					{
					{
					setState(187);
					setup_statement();
					}
					}
					setState(192);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(193);
				match(RBRACE);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class For_loop_worldContext extends ParserRuleContext {
		public TerminalNode FOR() { return getToken(parser_gec.FOR, 0); }
		public List<TerminalNode> ID() { return getTokens(parser_gec.ID); }
		public TerminalNode ID(int i) {
			return getToken(parser_gec.ID, i);
		}
		public TerminalNode FROM() { return getToken(parser_gec.FROM, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode TO() { return getToken(parser_gec.TO, 0); }
		public TerminalNode LBRACE() { return getToken(parser_gec.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(parser_gec.RBRACE, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public TerminalNode IN() { return getToken(parser_gec.IN, 0); }
		public For_loop_worldContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_for_loop_world; }
	}

	public final For_loop_worldContext for_loop_world() throws RecognitionException {
		For_loop_worldContext _localctx = new For_loop_worldContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_for_loop_world);
		int _la;
		try {
			setState(223);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(196);
				match(FOR);
				setState(197);
				match(ID);
				setState(198);
				match(FROM);
				setState(199);
				expression();
				setState(200);
				match(TO);
				setState(201);
				expression();
				setState(202);
				match(LBRACE);
				setState(206);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 134281392L) != 0)) {
					{
					{
					setState(203);
					statement();
					}
					}
					setState(208);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(209);
				match(RBRACE);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(211);
				match(FOR);
				setState(212);
				match(ID);
				setState(213);
				match(IN);
				setState(214);
				match(ID);
				setState(215);
				match(LBRACE);
				setState(219);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 134281392L) != 0)) {
					{
					{
					setState(216);
					statement();
					}
					}
					setState(221);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(222);
				match(RBRACE);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Add_statementContext extends ParserRuleContext {
		public TerminalNode ADD() { return getToken(parser_gec.ADD, 0); }
		public TerminalNode ID() { return getToken(parser_gec.ID, 0); }
		public Add_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_add_statement; }
	}

	public final Add_statementContext add_statement() throws RecognitionException {
		Add_statementContext _localctx = new Add_statementContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_add_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(225);
			match(ADD);
			setState(226);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001 \u00e5\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0005\u0001/\b\u0001\n\u0001\f\u00012\t\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0004\u0002=\b\u0002\u000b\u0002"+
		"\f\u0002>\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0005\u0003J\b\u0003"+
		"\n\u0003\f\u0003M\t\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0005\u0004T\b\u0004\n\u0004\f\u0004W\t\u0004\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0005\u0005\\\b\u0005\n\u0005\f\u0005_\t\u0005"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0005\u0006m\b\u0006\n\u0006\f\u0006p\t\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0003\u0006u\b\u0006\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0003\b\u0080"+
		"\b\b\u0001\t\u0001\t\u0001\t\u0003\t\u0085\b\t\u0001\n\u0001\n\u0001\n"+
		"\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0003\n\u008f\b\n\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0003"+
		"\f\u0099\b\f\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\u000e\u0001"+
		"\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0003\u000e\u00a6"+
		"\b\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001"+
		"\u000f\u0001\u000f\u0001\u000f\u0005\u000f\u00b0\b\u000f\n\u000f\f\u000f"+
		"\u00b3\t\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0005\u000f\u00bd\b\u000f\n\u000f"+
		"\f\u000f\u00c0\t\u000f\u0001\u000f\u0003\u000f\u00c3\b\u000f\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0005\u0010\u00cd\b\u0010\n\u0010\f\u0010\u00d0\t\u0010\u0001"+
		"\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001"+
		"\u0010\u0001\u0010\u0005\u0010\u00da\b\u0010\n\u0010\f\u0010\u00dd\t\u0010"+
		"\u0001\u0010\u0003\u0010\u00e0\b\u0010\u0001\u0011\u0001\u0011\u0001\u0011"+
		"\u0001\u0011\u0000\u0000\u0012\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010"+
		"\u0012\u0014\u0016\u0018\u001a\u001c\u001e \"\u0000\u0000\u00ef\u0000"+
		"$\u0001\u0000\u0000\u0000\u0002(\u0001\u0000\u0000\u0000\u00045\u0001"+
		"\u0000\u0000\u0000\u0006B\u0001\u0000\u0000\u0000\bP\u0001\u0000\u0000"+
		"\u0000\nX\u0001\u0000\u0000\u0000\ft\u0001\u0000\u0000\u0000\u000ev\u0001"+
		"\u0000\u0000\u0000\u0010\u007f\u0001\u0000\u0000\u0000\u0012\u0084\u0001"+
		"\u0000\u0000\u0000\u0014\u008e\u0001\u0000\u0000\u0000\u0016\u0090\u0001"+
		"\u0000\u0000\u0000\u0018\u0098\u0001\u0000\u0000\u0000\u001a\u009a\u0001"+
		"\u0000\u0000\u0000\u001c\u00a5\u0001\u0000\u0000\u0000\u001e\u00c2\u0001"+
		"\u0000\u0000\u0000 \u00df\u0001\u0000\u0000\u0000\"\u00e1\u0001\u0000"+
		"\u0000\u0000$%\u0003\u0002\u0001\u0000%&\u0003\u0004\u0002\u0000&\'\u0005"+
		"\u0000\u0000\u0001\'\u0001\u0001\u0000\u0000\u0000()\u0005\u0001\u0000"+
		"\u0000)*\u0005\u0002\u0000\u0000*+\u0005\u0010\u0000\u0000+,\u0005\u0011"+
		"\u0000\u0000,0\u0005\u0012\u0000\u0000-/\u0003\u0010\b\u0000.-\u0001\u0000"+
		"\u0000\u0000/2\u0001\u0000\u0000\u00000.\u0001\u0000\u0000\u000001\u0001"+
		"\u0000\u0000\u000013\u0001\u0000\u0000\u000020\u0001\u0000\u0000\u0000"+
		"34\u0005\u0013\u0000\u00004\u0003\u0001\u0000\u0000\u000056\u0005\u0001"+
		"\u0000\u000067\u0005\u0003\u0000\u000078\u0005\u0010\u0000\u000089\u0003"+
		"\n\u0005\u00009:\u0005\u0011\u0000\u0000:<\u0005\u0012\u0000\u0000;=\u0003"+
		"\u0006\u0003\u0000<;\u0001\u0000\u0000\u0000=>\u0001\u0000\u0000\u0000"+
		"><\u0001\u0000\u0000\u0000>?\u0001\u0000\u0000\u0000?@\u0001\u0000\u0000"+
		"\u0000@A\u0005\u0013\u0000\u0000A\u0005\u0001\u0000\u0000\u0000BC\u0005"+
		"\u0001\u0000\u0000CD\u0005\u0006\u0000\u0000DE\u0005\u0010\u0000\u0000"+
		"EF\u0003\b\u0004\u0000FG\u0005\u0011\u0000\u0000GK\u0005\u0012\u0000\u0000"+
		"HJ\u0003\u0012\t\u0000IH\u0001\u0000\u0000\u0000JM\u0001\u0000\u0000\u0000"+
		"KI\u0001\u0000\u0000\u0000KL\u0001\u0000\u0000\u0000LN\u0001\u0000\u0000"+
		"\u0000MK\u0001\u0000\u0000\u0000NO\u0005\u0013\u0000\u0000O\u0007\u0001"+
		"\u0000\u0000\u0000PU\u0003\n\u0005\u0000QR\u0005\u0016\u0000\u0000RT\u0003"+
		"\n\u0005\u0000SQ\u0001\u0000\u0000\u0000TW\u0001\u0000\u0000\u0000US\u0001"+
		"\u0000\u0000\u0000UV\u0001\u0000\u0000\u0000V\t\u0001\u0000\u0000\u0000"+
		"WU\u0001\u0000\u0000\u0000X]\u0003\f\u0006\u0000YZ\u0005\u001a\u0000\u0000"+
		"Z\\\u0003\f\u0006\u0000[Y\u0001\u0000\u0000\u0000\\_\u0001\u0000\u0000"+
		"\u0000][\u0001\u0000\u0000\u0000]^\u0001\u0000\u0000\u0000^\u000b\u0001"+
		"\u0000\u0000\u0000_]\u0001\u0000\u0000\u0000`u\u0005\u001e\u0000\u0000"+
		"au\u0005\u001c\u0000\u0000bu\u0005\u001d\u0000\u0000cu\u0005\u001b\u0000"+
		"\u0000de\u0005\u0010\u0000\u0000ef\u0003\n\u0005\u0000fg\u0005\u0011\u0000"+
		"\u0000gu\u0001\u0000\u0000\u0000hi\u0005\u0014\u0000\u0000in\u0003\n\u0005"+
		"\u0000jk\u0005\u0016\u0000\u0000km\u0003\n\u0005\u0000lj\u0001\u0000\u0000"+
		"\u0000mp\u0001\u0000\u0000\u0000nl\u0001\u0000\u0000\u0000no\u0001\u0000"+
		"\u0000\u0000oq\u0001\u0000\u0000\u0000pn\u0001\u0000\u0000\u0000qr\u0005"+
		"\u0015\u0000\u0000ru\u0001\u0000\u0000\u0000su\u0003\u000e\u0007\u0000"+
		"t`\u0001\u0000\u0000\u0000ta\u0001\u0000\u0000\u0000tb\u0001\u0000\u0000"+
		"\u0000tc\u0001\u0000\u0000\u0000td\u0001\u0000\u0000\u0000th\u0001\u0000"+
		"\u0000\u0000ts\u0001\u0000\u0000\u0000u\r\u0001\u0000\u0000\u0000vw\u0005"+
		"\u000b\u0000\u0000wx\u0005\u0010\u0000\u0000xy\u0003\b\u0004\u0000yz\u0005"+
		"\u0011\u0000\u0000z\u000f\u0001\u0000\u0000\u0000{\u0080\u0003\u0014\n"+
		"\u0000|\u0080\u0003\u0016\u000b\u0000}\u0080\u0003\u001c\u000e\u0000~"+
		"\u0080\u0003\u001e\u000f\u0000\u007f{\u0001\u0000\u0000\u0000\u007f|\u0001"+
		"\u0000\u0000\u0000\u007f}\u0001\u0000\u0000\u0000\u007f~\u0001\u0000\u0000"+
		"\u0000\u0080\u0011\u0001\u0000\u0000\u0000\u0081\u0085\u0003\u0010\b\u0000"+
		"\u0082\u0085\u0003\"\u0011\u0000\u0083\u0085\u0003 \u0010\u0000\u0084"+
		"\u0081\u0001\u0000\u0000\u0000\u0084\u0082\u0001\u0000\u0000\u0000\u0084"+
		"\u0083\u0001\u0000\u0000\u0000\u0085\u0013\u0001\u0000\u0000\u0000\u0086"+
		"\u0087\u0003\u0018\f\u0000\u0087\u0088\u0005\u001b\u0000\u0000\u0088\u0089"+
		"\u0005\u0019\u0000\u0000\u0089\u008a\u0003\n\u0005\u0000\u008a\u008f\u0001"+
		"\u0000\u0000\u0000\u008b\u008c\u0005\u001b\u0000\u0000\u008c\u008d\u0005"+
		"\u0019\u0000\u0000\u008d\u008f\u0003\n\u0005\u0000\u008e\u0086\u0001\u0000"+
		"\u0000\u0000\u008e\u008b\u0001\u0000\u0000\u0000\u008f\u0015\u0001\u0000"+
		"\u0000\u0000\u0090\u0091\u0003\u0018\f\u0000\u0091\u0092\u0005\u001b\u0000"+
		"\u0000\u0092\u0017\u0001\u0000\u0000\u0000\u0093\u0099\u0005\r\u0000\u0000"+
		"\u0094\u0099\u0005\u000e\u0000\u0000\u0095\u0099\u0005\u000f\u0000\u0000"+
		"\u0096\u0099\u0005\u000b\u0000\u0000\u0097\u0099\u0003\u001a\r\u0000\u0098"+
		"\u0093\u0001\u0000\u0000\u0000\u0098\u0094\u0001\u0000\u0000\u0000\u0098"+
		"\u0095\u0001\u0000\u0000\u0000\u0098\u0096\u0001\u0000\u0000\u0000\u0098"+
		"\u0097\u0001\u0000\u0000\u0000\u0099\u0019\u0001\u0000\u0000\u0000\u009a"+
		"\u009b\u0005\f\u0000\u0000\u009b\u009c\u0005\u0017\u0000\u0000\u009c\u009d"+
		"\u0005\u000b\u0000\u0000\u009d\u009e\u0005\u0018\u0000\u0000\u009e\u001b"+
		"\u0001\u0000\u0000\u0000\u009f\u00a0\u0005\u0005\u0000\u0000\u00a0\u00a1"+
		"\u0005\u001b\u0000\u0000\u00a1\u00a6\u0005\u001b\u0000\u0000\u00a2\u00a3"+
		"\u0005\u0005\u0000\u0000\u00a3\u00a4\u0005\u001b\u0000\u0000\u00a4\u00a6"+
		"\u0003\u000e\u0007\u0000\u00a5\u009f\u0001\u0000\u0000\u0000\u00a5\u00a2"+
		"\u0001\u0000\u0000\u0000\u00a6\u001d\u0001\u0000\u0000\u0000\u00a7\u00a8"+
		"\u0005\u0007\u0000\u0000\u00a8\u00a9\u0005\u001b\u0000\u0000\u00a9\u00aa"+
		"\u0005\b\u0000\u0000\u00aa\u00ab\u0003\n\u0005\u0000\u00ab\u00ac\u0005"+
		"\t\u0000\u0000\u00ac\u00ad\u0003\n\u0005\u0000\u00ad\u00b1\u0005\u0012"+
		"\u0000\u0000\u00ae\u00b0\u0003\u0010\b\u0000\u00af\u00ae\u0001\u0000\u0000"+
		"\u0000\u00b0\u00b3\u0001\u0000\u0000\u0000\u00b1\u00af\u0001\u0000\u0000"+
		"\u0000\u00b1\u00b2\u0001\u0000\u0000\u0000\u00b2\u00b4\u0001\u0000\u0000"+
		"\u0000\u00b3\u00b1\u0001\u0000\u0000\u0000\u00b4\u00b5\u0005\u0013\u0000"+
		"\u0000\u00b5\u00c3\u0001\u0000\u0000\u0000\u00b6\u00b7\u0005\u0007\u0000"+
		"\u0000\u00b7\u00b8\u0005\u001b\u0000\u0000\u00b8\u00b9\u0005\n\u0000\u0000"+
		"\u00b9\u00ba\u0005\u001b\u0000\u0000\u00ba\u00be\u0005\u0012\u0000\u0000"+
		"\u00bb\u00bd\u0003\u0010\b\u0000\u00bc\u00bb\u0001\u0000\u0000\u0000\u00bd"+
		"\u00c0\u0001\u0000\u0000\u0000\u00be\u00bc\u0001\u0000\u0000\u0000\u00be"+
		"\u00bf\u0001\u0000\u0000\u0000\u00bf\u00c1\u0001\u0000\u0000\u0000\u00c0"+
		"\u00be\u0001\u0000\u0000\u0000\u00c1\u00c3\u0005\u0013\u0000\u0000\u00c2"+
		"\u00a7\u0001\u0000\u0000\u0000\u00c2\u00b6\u0001\u0000\u0000\u0000\u00c3"+
		"\u001f\u0001\u0000\u0000\u0000\u00c4\u00c5\u0005\u0007\u0000\u0000\u00c5"+
		"\u00c6\u0005\u001b\u0000\u0000\u00c6\u00c7\u0005\b\u0000\u0000\u00c7\u00c8"+
		"\u0003\n\u0005\u0000\u00c8\u00c9\u0005\t\u0000\u0000\u00c9\u00ca\u0003"+
		"\n\u0005\u0000\u00ca\u00ce\u0005\u0012\u0000\u0000\u00cb\u00cd\u0003\u0012"+
		"\t\u0000\u00cc\u00cb\u0001\u0000\u0000\u0000\u00cd\u00d0\u0001\u0000\u0000"+
		"\u0000\u00ce\u00cc\u0001\u0000\u0000\u0000\u00ce\u00cf\u0001\u0000\u0000"+
		"\u0000\u00cf\u00d1\u0001\u0000\u0000\u0000\u00d0\u00ce\u0001\u0000\u0000"+
		"\u0000\u00d1\u00d2\u0005\u0013\u0000\u0000\u00d2\u00e0\u0001\u0000\u0000"+
		"\u0000\u00d3\u00d4\u0005\u0007\u0000\u0000\u00d4\u00d5\u0005\u001b\u0000"+
		"\u0000\u00d5\u00d6\u0005\n\u0000\u0000\u00d6\u00d7\u0005\u001b\u0000\u0000"+
		"\u00d7\u00db\u0005\u0012\u0000\u0000\u00d8\u00da\u0003\u0012\t\u0000\u00d9"+
		"\u00d8\u0001\u0000\u0000\u0000\u00da\u00dd\u0001\u0000\u0000\u0000\u00db"+
		"\u00d9\u0001\u0000\u0000\u0000\u00db\u00dc\u0001\u0000\u0000\u0000\u00dc"+
		"\u00de\u0001\u0000\u0000\u0000\u00dd\u00db\u0001\u0000\u0000\u0000\u00de"+
		"\u00e0\u0005\u0013\u0000\u0000\u00df\u00c4\u0001\u0000\u0000\u0000\u00df"+
		"\u00d3\u0001\u0000\u0000\u0000\u00e0!\u0001\u0000\u0000\u0000\u00e1\u00e2"+
		"\u0005\u0004\u0000\u0000\u00e2\u00e3\u0005\u001b\u0000\u0000\u00e3#\u0001"+
		"\u0000\u0000\u0000\u00120>KU]nt\u007f\u0084\u008e\u0098\u00a5\u00b1\u00be"+
		"\u00c2\u00ce\u00db\u00df";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}