// Generated from /home/alex/ProcesadoresLenguaje/python/src/antlr4/gec_parser.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class gec_parserParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		DEFINE=1, SETUP=2, WORLD=3, ADD=4, APPEND=5, SCENE=6, FOR=7, FROM=8, TO=9, 
		IN=10, CHUNK=11, GAMEOBJECT=12, LIST=13, INT=14, FLOAT=15, STRING=16, 
		LPAREN=17, RPAREN=18, LBRACE=19, RBRACE=20, LSQUARE=21, RSQUARE=22, COMMA=23, 
		LT=24, GT=25, ASSIGN=26, OP_ARIT=27, ID=28, INT_LITERAL=29, FLOAT_LITERAL=30, 
		STRING_LITERAL=31, COMMENT=32, BLOCK_COMMENT=33, WS=34;
	public static final int
		RULE_program = 0, RULE_define_setup = 1, RULE_define_world = 2, RULE_define_scene = 3, 
		RULE_statement = 4, RULE_chunk_constructor = 5, RULE_gameobject_constructor = 6, 
		RULE_define_list = 7, RULE_array = 8, RULE_append_statement = 9, RULE_add_statement = 10, 
		RULE_for_loop_number = 11, RULE_for_loop_list = 12, RULE_assignment = 13, 
		RULE_expression = 14, RULE_expression_aux = 15, RULE_declaration = 16;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "define_setup", "define_world", "define_scene", "statement", 
			"chunk_constructor", "gameobject_constructor", "define_list", "array", 
			"append_statement", "add_statement", "for_loop_number", "for_loop_list", 
			"assignment", "expression", "expression_aux", "declaration"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'DEFINE'", "'SETUP'", "'WORLD'", "'ADD'", "'APPEND'", "'SCENE'", 
			"'FOR'", "'FROM'", "'TO'", "'IN'", "'CHUNK'", "'GAMEOBJECT'", "'LIST'", 
			"'INT'", "'FLOAT'", "'STRING'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
			"','", "'<'", "'>'", "'='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "DEFINE", "SETUP", "WORLD", "ADD", "APPEND", "SCENE", "FOR", "FROM", 
			"TO", "IN", "CHUNK", "GAMEOBJECT", "LIST", "INT", "FLOAT", "STRING", 
			"LPAREN", "RPAREN", "LBRACE", "RBRACE", "LSQUARE", "RSQUARE", "COMMA", 
			"LT", "GT", "ASSIGN", "OP_ARIT", "ID", "INT_LITERAL", "FLOAT_LITERAL", 
			"STRING_LITERAL", "COMMENT", "BLOCK_COMMENT", "WS"
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
	public String getGrammarFileName() { return "gec_parser.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public gec_parserParser(TokenStream input) {
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
		public TerminalNode EOF() { return getToken(gec_parserParser.EOF, 0); }
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
			setState(34);
			define_setup();
			setState(35);
			define_world();
			setState(36);
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
		public TerminalNode DEFINE() { return getToken(gec_parserParser.DEFINE, 0); }
		public TerminalNode SETUP() { return getToken(gec_parserParser.SETUP, 0); }
		public TerminalNode LPAREN() { return getToken(gec_parserParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(gec_parserParser.RPAREN, 0); }
		public TerminalNode LBRACE() { return getToken(gec_parserParser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(gec_parserParser.RBRACE, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
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
			setState(38);
			match(DEFINE);
			setState(39);
			match(SETUP);
			setState(40);
			match(LPAREN);
			setState(41);
			match(RPAREN);
			setState(42);
			match(LBRACE);
			setState(46);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 268564656L) != 0)) {
				{
				{
				setState(43);
				statement();
				}
				}
				setState(48);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(49);
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
		public TerminalNode DEFINE() { return getToken(gec_parserParser.DEFINE, 0); }
		public TerminalNode WORLD() { return getToken(gec_parserParser.WORLD, 0); }
		public TerminalNode LPAREN() { return getToken(gec_parserParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(gec_parserParser.RPAREN, 0); }
		public TerminalNode LBRACE() { return getToken(gec_parserParser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(gec_parserParser.RBRACE, 0); }
		public TerminalNode STRING_LITERAL() { return getToken(gec_parserParser.STRING_LITERAL, 0); }
		public TerminalNode ID() { return getToken(gec_parserParser.ID, 0); }
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
			setState(51);
			match(DEFINE);
			setState(52);
			match(WORLD);
			setState(53);
			match(LPAREN);
			setState(54);
			_la = _input.LA(1);
			if ( !(_la==ID || _la==STRING_LITERAL) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(55);
			match(RPAREN);
			setState(56);
			match(LBRACE);
			setState(60);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==DEFINE) {
				{
				{
				setState(57);
				define_scene();
				}
				}
				setState(62);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(63);
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
		public TerminalNode DEFINE() { return getToken(gec_parserParser.DEFINE, 0); }
		public TerminalNode SCENE() { return getToken(gec_parserParser.SCENE, 0); }
		public TerminalNode LPAREN() { return getToken(gec_parserParser.LPAREN, 0); }
		public List<TerminalNode> COMMA() { return getTokens(gec_parserParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(gec_parserParser.COMMA, i);
		}
		public TerminalNode RPAREN() { return getToken(gec_parserParser.RPAREN, 0); }
		public TerminalNode LBRACE() { return getToken(gec_parserParser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(gec_parserParser.RBRACE, 0); }
		public TerminalNode STRING_LITERAL() { return getToken(gec_parserParser.STRING_LITERAL, 0); }
		public List<TerminalNode> ID() { return getTokens(gec_parserParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(gec_parserParser.ID, i);
		}
		public List<TerminalNode> INT_LITERAL() { return getTokens(gec_parserParser.INT_LITERAL); }
		public TerminalNode INT_LITERAL(int i) {
			return getToken(gec_parserParser.INT_LITERAL, i);
		}
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
			setState(65);
			match(DEFINE);
			setState(66);
			match(SCENE);
			setState(67);
			match(LPAREN);
			setState(68);
			_la = _input.LA(1);
			if ( !(_la==ID || _la==STRING_LITERAL) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(69);
			match(COMMA);
			setState(70);
			_la = _input.LA(1);
			if ( !(_la==ID || _la==INT_LITERAL) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(71);
			match(COMMA);
			setState(72);
			_la = _input.LA(1);
			if ( !(_la==ID || _la==INT_LITERAL) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(73);
			match(RPAREN);
			setState(74);
			match(LBRACE);
			setState(78);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 268564656L) != 0)) {
				{
				{
				setState(75);
				statement();
				}
				}
				setState(80);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(81);
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
	public static class StatementContext extends ParserRuleContext {
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public Define_listContext define_list() {
			return getRuleContext(Define_listContext.class,0);
		}
		public Append_statementContext append_statement() {
			return getRuleContext(Append_statementContext.class,0);
		}
		public For_loop_numberContext for_loop_number() {
			return getRuleContext(For_loop_numberContext.class,0);
		}
		public For_loop_listContext for_loop_list() {
			return getRuleContext(For_loop_listContext.class,0);
		}
		public DeclarationContext declaration() {
			return getRuleContext(DeclarationContext.class,0);
		}
		public Add_statementContext add_statement() {
			return getRuleContext(Add_statementContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_statement);
		try {
			setState(90);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(83);
				assignment();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(84);
				define_list();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(85);
				append_statement();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(86);
				for_loop_number();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(87);
				for_loop_list();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(88);
				declaration();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(89);
				add_statement();
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
	public static class Chunk_constructorContext extends ParserRuleContext {
		public TerminalNode CHUNK() { return getToken(gec_parserParser.CHUNK, 0); }
		public TerminalNode LPAREN() { return getToken(gec_parserParser.LPAREN, 0); }
		public List<TerminalNode> COMMA() { return getTokens(gec_parserParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(gec_parserParser.COMMA, i);
		}
		public TerminalNode RPAREN() { return getToken(gec_parserParser.RPAREN, 0); }
		public List<TerminalNode> ID() { return getTokens(gec_parserParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(gec_parserParser.ID, i);
		}
		public List<TerminalNode> INT_LITERAL() { return getTokens(gec_parserParser.INT_LITERAL); }
		public TerminalNode INT_LITERAL(int i) {
			return getToken(gec_parserParser.INT_LITERAL, i);
		}
		public List<TerminalNode> FLOAT_LITERAL() { return getTokens(gec_parserParser.FLOAT_LITERAL); }
		public TerminalNode FLOAT_LITERAL(int i) {
			return getToken(gec_parserParser.FLOAT_LITERAL, i);
		}
		public TerminalNode STRING_LITERAL() { return getToken(gec_parserParser.STRING_LITERAL, 0); }
		public ArrayContext array() {
			return getRuleContext(ArrayContext.class,0);
		}
		public Chunk_constructorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_chunk_constructor; }
	}

	public final Chunk_constructorContext chunk_constructor() throws RecognitionException {
		Chunk_constructorContext _localctx = new Chunk_constructorContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_chunk_constructor);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(92);
			match(CHUNK);
			setState(93);
			match(LPAREN);
			setState(94);
			_la = _input.LA(1);
			if ( !(_la==ID || _la==INT_LITERAL) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(95);
			match(COMMA);
			setState(96);
			_la = _input.LA(1);
			if ( !(_la==ID || _la==INT_LITERAL) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(97);
			match(COMMA);
			setState(98);
			_la = _input.LA(1);
			if ( !(_la==ID || _la==FLOAT_LITERAL) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(99);
			match(COMMA);
			setState(100);
			_la = _input.LA(1);
			if ( !(_la==ID || _la==FLOAT_LITERAL) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(101);
			match(COMMA);
			setState(102);
			_la = _input.LA(1);
			if ( !(_la==ID || _la==STRING_LITERAL) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(103);
			match(COMMA);
			setState(106);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				{
				setState(104);
				match(ID);
				}
				break;
			case LSQUARE:
				{
				setState(105);
				array();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(108);
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
	public static class Gameobject_constructorContext extends ParserRuleContext {
		public TerminalNode GAMEOBJECT() { return getToken(gec_parserParser.GAMEOBJECT, 0); }
		public TerminalNode LPAREN() { return getToken(gec_parserParser.LPAREN, 0); }
		public List<TerminalNode> COMMA() { return getTokens(gec_parserParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(gec_parserParser.COMMA, i);
		}
		public TerminalNode RPAREN() { return getToken(gec_parserParser.RPAREN, 0); }
		public List<TerminalNode> ID() { return getTokens(gec_parserParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(gec_parserParser.ID, i);
		}
		public TerminalNode STRING_LITERAL() { return getToken(gec_parserParser.STRING_LITERAL, 0); }
		public TerminalNode INT_LITERAL() { return getToken(gec_parserParser.INT_LITERAL, 0); }
		public List<TerminalNode> FLOAT_LITERAL() { return getTokens(gec_parserParser.FLOAT_LITERAL); }
		public TerminalNode FLOAT_LITERAL(int i) {
			return getToken(gec_parserParser.FLOAT_LITERAL, i);
		}
		public Gameobject_constructorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_gameobject_constructor; }
	}

	public final Gameobject_constructorContext gameobject_constructor() throws RecognitionException {
		Gameobject_constructorContext _localctx = new Gameobject_constructorContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_gameobject_constructor);
		int _la;
		try {
			setState(128);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(110);
				match(GAMEOBJECT);
				setState(111);
				match(LPAREN);
				setState(112);
				_la = _input.LA(1);
				if ( !(_la==ID || _la==STRING_LITERAL) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(113);
				match(COMMA);
				setState(114);
				_la = _input.LA(1);
				if ( !(_la==ID || _la==INT_LITERAL) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(115);
				match(COMMA);
				setState(116);
				_la = _input.LA(1);
				if ( !(_la==ID || _la==FLOAT_LITERAL) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(117);
				match(COMMA);
				setState(118);
				_la = _input.LA(1);
				if ( !(_la==ID || _la==FLOAT_LITERAL) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(119);
				match(RPAREN);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(120);
				match(GAMEOBJECT);
				setState(121);
				match(LPAREN);
				setState(122);
				_la = _input.LA(1);
				if ( !(_la==ID || _la==STRING_LITERAL) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(123);
				match(COMMA);
				setState(124);
				_la = _input.LA(1);
				if ( !(_la==ID || _la==INT_LITERAL) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(125);
				match(COMMA);
				setState(126);
				_la = _input.LA(1);
				if ( !(_la==ID || _la==FLOAT_LITERAL) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(127);
				match(RPAREN);
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
	public static class Define_listContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(gec_parserParser.ID, 0); }
		public TerminalNode ASSIGN() { return getToken(gec_parserParser.ASSIGN, 0); }
		public ArrayContext array() {
			return getRuleContext(ArrayContext.class,0);
		}
		public TerminalNode LIST() { return getToken(gec_parserParser.LIST, 0); }
		public TerminalNode LT() { return getToken(gec_parserParser.LT, 0); }
		public TerminalNode GT() { return getToken(gec_parserParser.GT, 0); }
		public TerminalNode CHUNK() { return getToken(gec_parserParser.CHUNK, 0); }
		public TerminalNode GAMEOBJECT() { return getToken(gec_parserParser.GAMEOBJECT, 0); }
		public Define_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_define_list; }
	}

	public final Define_listContext define_list() throws RecognitionException {
		Define_listContext _localctx = new Define_listContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_define_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(135);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LIST:
				{
				setState(130);
				match(LIST);
				setState(131);
				match(LT);
				setState(132);
				_la = _input.LA(1);
				if ( !(_la==CHUNK || _la==GAMEOBJECT) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(133);
				match(GT);
				}
				break;
			case ID:
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(137);
			match(ID);
			setState(138);
			match(ASSIGN);
			setState(139);
			array();
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
	public static class ArrayContext extends ParserRuleContext {
		public TerminalNode LSQUARE() { return getToken(gec_parserParser.LSQUARE, 0); }
		public TerminalNode RSQUARE() { return getToken(gec_parserParser.RSQUARE, 0); }
		public List<TerminalNode> ID() { return getTokens(gec_parserParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(gec_parserParser.ID, i);
		}
		public List<Chunk_constructorContext> chunk_constructor() {
			return getRuleContexts(Chunk_constructorContext.class);
		}
		public Chunk_constructorContext chunk_constructor(int i) {
			return getRuleContext(Chunk_constructorContext.class,i);
		}
		public List<Gameobject_constructorContext> gameobject_constructor() {
			return getRuleContexts(Gameobject_constructorContext.class);
		}
		public Gameobject_constructorContext gameobject_constructor(int i) {
			return getRuleContext(Gameobject_constructorContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(gec_parserParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(gec_parserParser.COMMA, i);
		}
		public ArrayContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array; }
	}

	public final ArrayContext array() throws RecognitionException {
		ArrayContext _localctx = new ArrayContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_array);
		int _la;
		try {
			setState(161);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(141);
				match(LSQUARE);
				setState(145);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case ID:
					{
					setState(142);
					match(ID);
					}
					break;
				case CHUNK:
					{
					setState(143);
					chunk_constructor();
					}
					break;
				case GAMEOBJECT:
					{
					setState(144);
					gameobject_constructor();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(155);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(147);
					match(COMMA);
					setState(151);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case ID:
						{
						setState(148);
						match(ID);
						}
						break;
					case CHUNK:
						{
						setState(149);
						chunk_constructor();
						}
						break;
					case GAMEOBJECT:
						{
						setState(150);
						gameobject_constructor();
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					}
					}
					setState(157);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(158);
				match(RSQUARE);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(159);
				match(LSQUARE);
				setState(160);
				match(RSQUARE);
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
	public static class Append_statementContext extends ParserRuleContext {
		public TerminalNode APPEND() { return getToken(gec_parserParser.APPEND, 0); }
		public List<TerminalNode> ID() { return getTokens(gec_parserParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(gec_parserParser.ID, i);
		}
		public Gameobject_constructorContext gameobject_constructor() {
			return getRuleContext(Gameobject_constructorContext.class,0);
		}
		public Chunk_constructorContext chunk_constructor() {
			return getRuleContext(Chunk_constructorContext.class,0);
		}
		public Append_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_append_statement; }
	}

	public final Append_statementContext append_statement() throws RecognitionException {
		Append_statementContext _localctx = new Append_statementContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_append_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(163);
			match(APPEND);
			setState(164);
			match(ID);
			setState(168);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				{
				setState(165);
				match(ID);
				}
				break;
			case GAMEOBJECT:
				{
				setState(166);
				gameobject_constructor();
				}
				break;
			case CHUNK:
				{
				setState(167);
				chunk_constructor();
				}
				break;
			default:
				throw new NoViableAltException(this);
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
	public static class Add_statementContext extends ParserRuleContext {
		public TerminalNode ADD() { return getToken(gec_parserParser.ADD, 0); }
		public TerminalNode ID() { return getToken(gec_parserParser.ID, 0); }
		public Chunk_constructorContext chunk_constructor() {
			return getRuleContext(Chunk_constructorContext.class,0);
		}
		public Add_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_add_statement; }
	}

	public final Add_statementContext add_statement() throws RecognitionException {
		Add_statementContext _localctx = new Add_statementContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_add_statement);
		try {
			setState(174);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,12,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(170);
				match(ADD);
				setState(171);
				match(ID);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(172);
				match(ADD);
				setState(173);
				chunk_constructor();
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
	public static class For_loop_numberContext extends ParserRuleContext {
		public TerminalNode FOR() { return getToken(gec_parserParser.FOR, 0); }
		public TerminalNode ID() { return getToken(gec_parserParser.ID, 0); }
		public TerminalNode FROM() { return getToken(gec_parserParser.FROM, 0); }
		public List<TerminalNode> INT_LITERAL() { return getTokens(gec_parserParser.INT_LITERAL); }
		public TerminalNode INT_LITERAL(int i) {
			return getToken(gec_parserParser.INT_LITERAL, i);
		}
		public TerminalNode TO() { return getToken(gec_parserParser.TO, 0); }
		public TerminalNode LBRACE() { return getToken(gec_parserParser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(gec_parserParser.RBRACE, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public For_loop_numberContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_for_loop_number; }
	}

	public final For_loop_numberContext for_loop_number() throws RecognitionException {
		For_loop_numberContext _localctx = new For_loop_numberContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_for_loop_number);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(176);
			match(FOR);
			setState(177);
			match(ID);
			setState(178);
			match(FROM);
			setState(179);
			match(INT_LITERAL);
			setState(180);
			match(TO);
			setState(181);
			match(INT_LITERAL);
			setState(182);
			match(LBRACE);
			setState(186);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 268564656L) != 0)) {
				{
				{
				setState(183);
				statement();
				}
				}
				setState(188);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(189);
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
	public static class For_loop_listContext extends ParserRuleContext {
		public TerminalNode FOR() { return getToken(gec_parserParser.FOR, 0); }
		public List<TerminalNode> ID() { return getTokens(gec_parserParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(gec_parserParser.ID, i);
		}
		public TerminalNode IN() { return getToken(gec_parserParser.IN, 0); }
		public TerminalNode LBRACE() { return getToken(gec_parserParser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(gec_parserParser.RBRACE, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public For_loop_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_for_loop_list; }
	}

	public final For_loop_listContext for_loop_list() throws RecognitionException {
		For_loop_listContext _localctx = new For_loop_listContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_for_loop_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(191);
			match(FOR);
			setState(192);
			match(ID);
			setState(193);
			match(IN);
			setState(194);
			match(ID);
			setState(195);
			match(LBRACE);
			setState(199);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 268564656L) != 0)) {
				{
				{
				setState(196);
				statement();
				}
				}
				setState(201);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(202);
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
	public static class AssignmentContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(gec_parserParser.ID, 0); }
		public TerminalNode ASSIGN() { return getToken(gec_parserParser.ASSIGN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode INT() { return getToken(gec_parserParser.INT, 0); }
		public TerminalNode STRING() { return getToken(gec_parserParser.STRING, 0); }
		public TerminalNode FLOAT() { return getToken(gec_parserParser.FLOAT, 0); }
		public Chunk_constructorContext chunk_constructor() {
			return getRuleContext(Chunk_constructorContext.class,0);
		}
		public TerminalNode CHUNK() { return getToken(gec_parserParser.CHUNK, 0); }
		public Gameobject_constructorContext gameobject_constructor() {
			return getRuleContext(Gameobject_constructorContext.class,0);
		}
		public TerminalNode GAMEOBJECT() { return getToken(gec_parserParser.GAMEOBJECT, 0); }
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_assignment);
		try {
			setState(227);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(208);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case INT:
					{
					setState(204);
					match(INT);
					}
					break;
				case STRING:
					{
					setState(205);
					match(STRING);
					}
					break;
				case FLOAT:
					{
					setState(206);
					match(FLOAT);
					}
					break;
				case ID:
					{
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(210);
				match(ID);
				setState(211);
				match(ASSIGN);
				setState(212);
				expression();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(215);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case CHUNK:
					{
					setState(213);
					match(CHUNK);
					}
					break;
				case ID:
					{
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(217);
				match(ID);
				setState(218);
				match(ASSIGN);
				setState(219);
				chunk_constructor();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(222);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case GAMEOBJECT:
					{
					setState(220);
					match(GAMEOBJECT);
					}
					break;
				case ID:
					{
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(224);
				match(ID);
				setState(225);
				match(ASSIGN);
				setState(226);
				gameobject_constructor();
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
	public static class ExpressionContext extends ParserRuleContext {
		public List<Expression_auxContext> expression_aux() {
			return getRuleContexts(Expression_auxContext.class);
		}
		public Expression_auxContext expression_aux(int i) {
			return getRuleContext(Expression_auxContext.class,i);
		}
		public List<TerminalNode> OP_ARIT() { return getTokens(gec_parserParser.OP_ARIT); }
		public TerminalNode OP_ARIT(int i) {
			return getToken(gec_parserParser.OP_ARIT, i);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_expression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(229);
			expression_aux();
			setState(234);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==OP_ARIT) {
				{
				{
				setState(230);
				match(OP_ARIT);
				setState(231);
				expression_aux();
				}
				}
				setState(236);
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
		public TerminalNode STRING_LITERAL() { return getToken(gec_parserParser.STRING_LITERAL, 0); }
		public TerminalNode INT_LITERAL() { return getToken(gec_parserParser.INT_LITERAL, 0); }
		public TerminalNode FLOAT_LITERAL() { return getToken(gec_parserParser.FLOAT_LITERAL, 0); }
		public TerminalNode ID() { return getToken(gec_parserParser.ID, 0); }
		public TerminalNode LPAREN() { return getToken(gec_parserParser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(gec_parserParser.RPAREN, 0); }
		public Expression_auxContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression_aux; }
	}

	public final Expression_auxContext expression_aux() throws RecognitionException {
		Expression_auxContext _localctx = new Expression_auxContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_expression_aux);
		try {
			setState(245);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case STRING_LITERAL:
				enterOuterAlt(_localctx, 1);
				{
				setState(237);
				match(STRING_LITERAL);
				}
				break;
			case INT_LITERAL:
				enterOuterAlt(_localctx, 2);
				{
				setState(238);
				match(INT_LITERAL);
				}
				break;
			case FLOAT_LITERAL:
				enterOuterAlt(_localctx, 3);
				{
				setState(239);
				match(FLOAT_LITERAL);
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 4);
				{
				setState(240);
				match(ID);
				}
				break;
			case LPAREN:
				enterOuterAlt(_localctx, 5);
				{
				setState(241);
				match(LPAREN);
				setState(242);
				expression();
				setState(243);
				match(RPAREN);
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
		public TerminalNode ID() { return getToken(gec_parserParser.ID, 0); }
		public TerminalNode INT() { return getToken(gec_parserParser.INT, 0); }
		public TerminalNode STRING() { return getToken(gec_parserParser.STRING, 0); }
		public TerminalNode FLOAT() { return getToken(gec_parserParser.FLOAT, 0); }
		public TerminalNode CHUNK() { return getToken(gec_parserParser.CHUNK, 0); }
		public TerminalNode GAMEOBJECT() { return getToken(gec_parserParser.GAMEOBJECT, 0); }
		public TerminalNode LIST() { return getToken(gec_parserParser.LIST, 0); }
		public TerminalNode LT() { return getToken(gec_parserParser.LT, 0); }
		public TerminalNode GT() { return getToken(gec_parserParser.GT, 0); }
		public DeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaration; }
	}

	public final DeclarationContext declaration() throws RecognitionException {
		DeclarationContext _localctx = new DeclarationContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_declaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(256);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
				{
				setState(247);
				match(INT);
				}
				break;
			case STRING:
				{
				setState(248);
				match(STRING);
				}
				break;
			case FLOAT:
				{
				setState(249);
				match(FLOAT);
				}
				break;
			case CHUNK:
				{
				setState(250);
				match(CHUNK);
				}
				break;
			case GAMEOBJECT:
				{
				setState(251);
				match(GAMEOBJECT);
				}
				break;
			case LIST:
				{
				setState(252);
				match(LIST);
				setState(253);
				match(LT);
				setState(254);
				_la = _input.LA(1);
				if ( !(_la==CHUNK || _la==GAMEOBJECT) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(255);
				match(GT);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(258);
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
		"\u0004\u0001\"\u0105\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0005\u0001-\b\u0001\n\u0001\f\u00010\t\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0005\u0002;\b\u0002\n\u0002\f\u0002>\t\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0005\u0003M\b\u0003\n\u0003\f\u0003P\t\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0003\u0004[\b\u0004\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0003\u0005"+
		"k\b\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0003\u0006\u0081\b\u0006\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0003\u0007\u0088\b\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0003\b\u0092\b\b\u0001\b\u0001\b\u0001\b\u0001\b\u0003\b\u0098"+
		"\b\b\u0005\b\u009a\b\b\n\b\f\b\u009d\t\b\u0001\b\u0001\b\u0001\b\u0003"+
		"\b\u00a2\b\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0003\t\u00a9\b\t"+
		"\u0001\n\u0001\n\u0001\n\u0001\n\u0003\n\u00af\b\n\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0005\u000b\u00b9\b\u000b\n\u000b\f\u000b\u00bc\t\u000b\u0001\u000b\u0001"+
		"\u000b\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0005\f\u00c6\b"+
		"\f\n\f\f\f\u00c9\t\f\u0001\f\u0001\f\u0001\r\u0001\r\u0001\r\u0001\r\u0003"+
		"\r\u00d1\b\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0003\r\u00d8\b\r"+
		"\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0003\r\u00df\b\r\u0001\r\u0001"+
		"\r\u0001\r\u0003\r\u00e4\b\r\u0001\u000e\u0001\u000e\u0001\u000e\u0005"+
		"\u000e\u00e9\b\u000e\n\u000e\f\u000e\u00ec\t\u000e\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0003\u000f\u00f6\b\u000f\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0003\u0010"+
		"\u0101\b\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0000\u0000\u0011\u0000"+
		"\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c"+
		"\u001e \u0000\u0004\u0002\u0000\u001c\u001c\u001f\u001f\u0001\u0000\u001c"+
		"\u001d\u0002\u0000\u001c\u001c\u001e\u001e\u0001\u0000\u000b\f\u011b\u0000"+
		"\"\u0001\u0000\u0000\u0000\u0002&\u0001\u0000\u0000\u0000\u00043\u0001"+
		"\u0000\u0000\u0000\u0006A\u0001\u0000\u0000\u0000\bZ\u0001\u0000\u0000"+
		"\u0000\n\\\u0001\u0000\u0000\u0000\f\u0080\u0001\u0000\u0000\u0000\u000e"+
		"\u0087\u0001\u0000\u0000\u0000\u0010\u00a1\u0001\u0000\u0000\u0000\u0012"+
		"\u00a3\u0001\u0000\u0000\u0000\u0014\u00ae\u0001\u0000\u0000\u0000\u0016"+
		"\u00b0\u0001\u0000\u0000\u0000\u0018\u00bf\u0001\u0000\u0000\u0000\u001a"+
		"\u00e3\u0001\u0000\u0000\u0000\u001c\u00e5\u0001\u0000\u0000\u0000\u001e"+
		"\u00f5\u0001\u0000\u0000\u0000 \u0100\u0001\u0000\u0000\u0000\"#\u0003"+
		"\u0002\u0001\u0000#$\u0003\u0004\u0002\u0000$%\u0005\u0000\u0000\u0001"+
		"%\u0001\u0001\u0000\u0000\u0000&\'\u0005\u0001\u0000\u0000\'(\u0005\u0002"+
		"\u0000\u0000()\u0005\u0011\u0000\u0000)*\u0005\u0012\u0000\u0000*.\u0005"+
		"\u0013\u0000\u0000+-\u0003\b\u0004\u0000,+\u0001\u0000\u0000\u0000-0\u0001"+
		"\u0000\u0000\u0000.,\u0001\u0000\u0000\u0000./\u0001\u0000\u0000\u0000"+
		"/1\u0001\u0000\u0000\u00000.\u0001\u0000\u0000\u000012\u0005\u0014\u0000"+
		"\u00002\u0003\u0001\u0000\u0000\u000034\u0005\u0001\u0000\u000045\u0005"+
		"\u0003\u0000\u000056\u0005\u0011\u0000\u000067\u0007\u0000\u0000\u0000"+
		"78\u0005\u0012\u0000\u00008<\u0005\u0013\u0000\u00009;\u0003\u0006\u0003"+
		"\u0000:9\u0001\u0000\u0000\u0000;>\u0001\u0000\u0000\u0000<:\u0001\u0000"+
		"\u0000\u0000<=\u0001\u0000\u0000\u0000=?\u0001\u0000\u0000\u0000><\u0001"+
		"\u0000\u0000\u0000?@\u0005\u0014\u0000\u0000@\u0005\u0001\u0000\u0000"+
		"\u0000AB\u0005\u0001\u0000\u0000BC\u0005\u0006\u0000\u0000CD\u0005\u0011"+
		"\u0000\u0000DE\u0007\u0000\u0000\u0000EF\u0005\u0017\u0000\u0000FG\u0007"+
		"\u0001\u0000\u0000GH\u0005\u0017\u0000\u0000HI\u0007\u0001\u0000\u0000"+
		"IJ\u0005\u0012\u0000\u0000JN\u0005\u0013\u0000\u0000KM\u0003\b\u0004\u0000"+
		"LK\u0001\u0000\u0000\u0000MP\u0001\u0000\u0000\u0000NL\u0001\u0000\u0000"+
		"\u0000NO\u0001\u0000\u0000\u0000OQ\u0001\u0000\u0000\u0000PN\u0001\u0000"+
		"\u0000\u0000QR\u0005\u0014\u0000\u0000R\u0007\u0001\u0000\u0000\u0000"+
		"S[\u0003\u001a\r\u0000T[\u0003\u000e\u0007\u0000U[\u0003\u0012\t\u0000"+
		"V[\u0003\u0016\u000b\u0000W[\u0003\u0018\f\u0000X[\u0003 \u0010\u0000"+
		"Y[\u0003\u0014\n\u0000ZS\u0001\u0000\u0000\u0000ZT\u0001\u0000\u0000\u0000"+
		"ZU\u0001\u0000\u0000\u0000ZV\u0001\u0000\u0000\u0000ZW\u0001\u0000\u0000"+
		"\u0000ZX\u0001\u0000\u0000\u0000ZY\u0001\u0000\u0000\u0000[\t\u0001\u0000"+
		"\u0000\u0000\\]\u0005\u000b\u0000\u0000]^\u0005\u0011\u0000\u0000^_\u0007"+
		"\u0001\u0000\u0000_`\u0005\u0017\u0000\u0000`a\u0007\u0001\u0000\u0000"+
		"ab\u0005\u0017\u0000\u0000bc\u0007\u0002\u0000\u0000cd\u0005\u0017\u0000"+
		"\u0000de\u0007\u0002\u0000\u0000ef\u0005\u0017\u0000\u0000fg\u0007\u0000"+
		"\u0000\u0000gj\u0005\u0017\u0000\u0000hk\u0005\u001c\u0000\u0000ik\u0003"+
		"\u0010\b\u0000jh\u0001\u0000\u0000\u0000ji\u0001\u0000\u0000\u0000kl\u0001"+
		"\u0000\u0000\u0000lm\u0005\u0012\u0000\u0000m\u000b\u0001\u0000\u0000"+
		"\u0000no\u0005\f\u0000\u0000op\u0005\u0011\u0000\u0000pq\u0007\u0000\u0000"+
		"\u0000qr\u0005\u0017\u0000\u0000rs\u0007\u0001\u0000\u0000st\u0005\u0017"+
		"\u0000\u0000tu\u0007\u0002\u0000\u0000uv\u0005\u0017\u0000\u0000vw\u0007"+
		"\u0002\u0000\u0000w\u0081\u0005\u0012\u0000\u0000xy\u0005\f\u0000\u0000"+
		"yz\u0005\u0011\u0000\u0000z{\u0007\u0000\u0000\u0000{|\u0005\u0017\u0000"+
		"\u0000|}\u0007\u0001\u0000\u0000}~\u0005\u0017\u0000\u0000~\u007f\u0007"+
		"\u0002\u0000\u0000\u007f\u0081\u0005\u0012\u0000\u0000\u0080n\u0001\u0000"+
		"\u0000\u0000\u0080x\u0001\u0000\u0000\u0000\u0081\r\u0001\u0000\u0000"+
		"\u0000\u0082\u0083\u0005\r\u0000\u0000\u0083\u0084\u0005\u0018\u0000\u0000"+
		"\u0084\u0085\u0007\u0003\u0000\u0000\u0085\u0088\u0005\u0019\u0000\u0000"+
		"\u0086\u0088\u0001\u0000\u0000\u0000\u0087\u0082\u0001\u0000\u0000\u0000"+
		"\u0087\u0086\u0001\u0000\u0000\u0000\u0088\u0089\u0001\u0000\u0000\u0000"+
		"\u0089\u008a\u0005\u001c\u0000\u0000\u008a\u008b\u0005\u001a\u0000\u0000"+
		"\u008b\u008c\u0003\u0010\b\u0000\u008c\u000f\u0001\u0000\u0000\u0000\u008d"+
		"\u0091\u0005\u0015\u0000\u0000\u008e\u0092\u0005\u001c\u0000\u0000\u008f"+
		"\u0092\u0003\n\u0005\u0000\u0090\u0092\u0003\f\u0006\u0000\u0091\u008e"+
		"\u0001\u0000\u0000\u0000\u0091\u008f\u0001\u0000\u0000\u0000\u0091\u0090"+
		"\u0001\u0000\u0000\u0000\u0092\u009b\u0001\u0000\u0000\u0000\u0093\u0097"+
		"\u0005\u0017\u0000\u0000\u0094\u0098\u0005\u001c\u0000\u0000\u0095\u0098"+
		"\u0003\n\u0005\u0000\u0096\u0098\u0003\f\u0006\u0000\u0097\u0094\u0001"+
		"\u0000\u0000\u0000\u0097\u0095\u0001\u0000\u0000\u0000\u0097\u0096\u0001"+
		"\u0000\u0000\u0000\u0098\u009a\u0001\u0000\u0000\u0000\u0099\u0093\u0001"+
		"\u0000\u0000\u0000\u009a\u009d\u0001\u0000\u0000\u0000\u009b\u0099\u0001"+
		"\u0000\u0000\u0000\u009b\u009c\u0001\u0000\u0000\u0000\u009c\u009e\u0001"+
		"\u0000\u0000\u0000\u009d\u009b\u0001\u0000\u0000\u0000\u009e\u00a2\u0005"+
		"\u0016\u0000\u0000\u009f\u00a0\u0005\u0015\u0000\u0000\u00a0\u00a2\u0005"+
		"\u0016\u0000\u0000\u00a1\u008d\u0001\u0000\u0000\u0000\u00a1\u009f\u0001"+
		"\u0000\u0000\u0000\u00a2\u0011\u0001\u0000\u0000\u0000\u00a3\u00a4\u0005"+
		"\u0005\u0000\u0000\u00a4\u00a8\u0005\u001c\u0000\u0000\u00a5\u00a9\u0005"+
		"\u001c\u0000\u0000\u00a6\u00a9\u0003\f\u0006\u0000\u00a7\u00a9\u0003\n"+
		"\u0005\u0000\u00a8\u00a5\u0001\u0000\u0000\u0000\u00a8\u00a6\u0001\u0000"+
		"\u0000\u0000\u00a8\u00a7\u0001\u0000\u0000\u0000\u00a9\u0013\u0001\u0000"+
		"\u0000\u0000\u00aa\u00ab\u0005\u0004\u0000\u0000\u00ab\u00af\u0005\u001c"+
		"\u0000\u0000\u00ac\u00ad\u0005\u0004\u0000\u0000\u00ad\u00af\u0003\n\u0005"+
		"\u0000\u00ae\u00aa\u0001\u0000\u0000\u0000\u00ae\u00ac\u0001\u0000\u0000"+
		"\u0000\u00af\u0015\u0001\u0000\u0000\u0000\u00b0\u00b1\u0005\u0007\u0000"+
		"\u0000\u00b1\u00b2\u0005\u001c\u0000\u0000\u00b2\u00b3\u0005\b\u0000\u0000"+
		"\u00b3\u00b4\u0005\u001d\u0000\u0000\u00b4\u00b5\u0005\t\u0000\u0000\u00b5"+
		"\u00b6\u0005\u001d\u0000\u0000\u00b6\u00ba\u0005\u0013\u0000\u0000\u00b7"+
		"\u00b9\u0003\b\u0004\u0000\u00b8\u00b7\u0001\u0000\u0000\u0000\u00b9\u00bc"+
		"\u0001\u0000\u0000\u0000\u00ba\u00b8\u0001\u0000\u0000\u0000\u00ba\u00bb"+
		"\u0001\u0000\u0000\u0000\u00bb\u00bd\u0001\u0000\u0000\u0000\u00bc\u00ba"+
		"\u0001\u0000\u0000\u0000\u00bd\u00be\u0005\u0014\u0000\u0000\u00be\u0017"+
		"\u0001\u0000\u0000\u0000\u00bf\u00c0\u0005\u0007\u0000\u0000\u00c0\u00c1"+
		"\u0005\u001c\u0000\u0000\u00c1\u00c2\u0005\n\u0000\u0000\u00c2\u00c3\u0005"+
		"\u001c\u0000\u0000\u00c3\u00c7\u0005\u0013\u0000\u0000\u00c4\u00c6\u0003"+
		"\b\u0004\u0000\u00c5\u00c4\u0001\u0000\u0000\u0000\u00c6\u00c9\u0001\u0000"+
		"\u0000\u0000\u00c7\u00c5\u0001\u0000\u0000\u0000\u00c7\u00c8\u0001\u0000"+
		"\u0000\u0000\u00c8\u00ca\u0001\u0000\u0000\u0000\u00c9\u00c7\u0001\u0000"+
		"\u0000\u0000\u00ca\u00cb\u0005\u0014\u0000\u0000\u00cb\u0019\u0001\u0000"+
		"\u0000\u0000\u00cc\u00d1\u0005\u000e\u0000\u0000\u00cd\u00d1\u0005\u0010"+
		"\u0000\u0000\u00ce\u00d1\u0005\u000f\u0000\u0000\u00cf\u00d1\u0001\u0000"+
		"\u0000\u0000\u00d0\u00cc\u0001\u0000\u0000\u0000\u00d0\u00cd\u0001\u0000"+
		"\u0000\u0000\u00d0\u00ce\u0001\u0000\u0000\u0000\u00d0\u00cf\u0001\u0000"+
		"\u0000\u0000\u00d1\u00d2\u0001\u0000\u0000\u0000\u00d2\u00d3\u0005\u001c"+
		"\u0000\u0000\u00d3\u00d4\u0005\u001a\u0000\u0000\u00d4\u00e4\u0003\u001c"+
		"\u000e\u0000\u00d5\u00d8\u0005\u000b\u0000\u0000\u00d6\u00d8\u0001\u0000"+
		"\u0000\u0000\u00d7\u00d5\u0001\u0000\u0000\u0000\u00d7\u00d6\u0001\u0000"+
		"\u0000\u0000\u00d8\u00d9\u0001\u0000\u0000\u0000\u00d9\u00da\u0005\u001c"+
		"\u0000\u0000\u00da\u00db\u0005\u001a\u0000\u0000\u00db\u00e4\u0003\n\u0005"+
		"\u0000\u00dc\u00df\u0005\f\u0000\u0000\u00dd\u00df\u0001\u0000\u0000\u0000"+
		"\u00de\u00dc\u0001\u0000\u0000\u0000\u00de\u00dd\u0001\u0000\u0000\u0000"+
		"\u00df\u00e0\u0001\u0000\u0000\u0000\u00e0\u00e1\u0005\u001c\u0000\u0000"+
		"\u00e1\u00e2\u0005\u001a\u0000\u0000\u00e2\u00e4\u0003\f\u0006\u0000\u00e3"+
		"\u00d0\u0001\u0000\u0000\u0000\u00e3\u00d7\u0001\u0000\u0000\u0000\u00e3"+
		"\u00de\u0001\u0000\u0000\u0000\u00e4\u001b\u0001\u0000\u0000\u0000\u00e5"+
		"\u00ea\u0003\u001e\u000f\u0000\u00e6\u00e7\u0005\u001b\u0000\u0000\u00e7"+
		"\u00e9\u0003\u001e\u000f\u0000\u00e8\u00e6\u0001\u0000\u0000\u0000\u00e9"+
		"\u00ec\u0001\u0000\u0000\u0000\u00ea\u00e8\u0001\u0000\u0000\u0000\u00ea"+
		"\u00eb\u0001\u0000\u0000\u0000\u00eb\u001d\u0001\u0000\u0000\u0000\u00ec"+
		"\u00ea\u0001\u0000\u0000\u0000\u00ed\u00f6\u0005\u001f\u0000\u0000\u00ee"+
		"\u00f6\u0005\u001d\u0000\u0000\u00ef\u00f6\u0005\u001e\u0000\u0000\u00f0"+
		"\u00f6\u0005\u001c\u0000\u0000\u00f1\u00f2\u0005\u0011\u0000\u0000\u00f2"+
		"\u00f3\u0003\u001c\u000e\u0000\u00f3\u00f4\u0005\u0012\u0000\u0000\u00f4"+
		"\u00f6\u0001\u0000\u0000\u0000\u00f5\u00ed\u0001\u0000\u0000\u0000\u00f5"+
		"\u00ee\u0001\u0000\u0000\u0000\u00f5\u00ef\u0001\u0000\u0000\u0000\u00f5"+
		"\u00f0\u0001\u0000\u0000\u0000\u00f5\u00f1\u0001\u0000\u0000\u0000\u00f6"+
		"\u001f\u0001\u0000\u0000\u0000\u00f7\u0101\u0005\u000e\u0000\u0000\u00f8"+
		"\u0101\u0005\u0010\u0000\u0000\u00f9\u0101\u0005\u000f\u0000\u0000\u00fa"+
		"\u0101\u0005\u000b\u0000\u0000\u00fb\u0101\u0005\f\u0000\u0000\u00fc\u00fd"+
		"\u0005\r\u0000\u0000\u00fd\u00fe\u0005\u0018\u0000\u0000\u00fe\u00ff\u0007"+
		"\u0003\u0000\u0000\u00ff\u0101\u0005\u0019\u0000\u0000\u0100\u00f7\u0001"+
		"\u0000\u0000\u0000\u0100\u00f8\u0001\u0000\u0000\u0000\u0100\u00f9\u0001"+
		"\u0000\u0000\u0000\u0100\u00fa\u0001\u0000\u0000\u0000\u0100\u00fb\u0001"+
		"\u0000\u0000\u0000\u0100\u00fc\u0001\u0000\u0000\u0000\u0101\u0102\u0001"+
		"\u0000\u0000\u0000\u0102\u0103\u0005\u001c\u0000\u0000\u0103!\u0001\u0000"+
		"\u0000\u0000\u0016.<NZj\u0080\u0087\u0091\u0097\u009b\u00a1\u00a8\u00ae"+
		"\u00ba\u00c7\u00d0\u00d7\u00de\u00e3\u00ea\u00f5\u0100";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}