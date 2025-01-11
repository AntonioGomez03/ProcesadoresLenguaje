// Generated from /home/antonio/Documentos/Universidad/Cuarto/Procesadores de Lenguajes/ProcesadoresLenguaje/python/src/gec_parser.g4 by ANTLR 4.13.1

from parser.symbol_table import SymbolTable
from parser.gec_objects import GameObject, Chunk, Scene, World
import json

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

	public gec_parserParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public Define_worldContext define_world;
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
			self.on_programa_start()
			setState(35);
			define_setup();
			setState(36);
			((ProgramContext)_localctx).define_world = define_world();
			setState(37);
			match(EOF);

			print("world", ((ProgramContext)_localctx).define_world.world.get_scenes())
			self.on_programa_end(((ProgramContext)_localctx).define_world.world,"World.json")
			    
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
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 268564656L) != 0)) {
				{
				{
				setState(45);
				statement();
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
		public World world;
		public Define_sceneContext define_scene;
		public List<Define_sceneContext> scenes = new ArrayList<Define_sceneContext>();
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
			setState(53);
			match(DEFINE);
			setState(54);
			match(WORLD);
			setState(55);
			match(LPAREN);
			setState(56);
			_la = _input.LA(1);
			if ( !(_la==ID || _la==STRING_LITERAL) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}


			temp_name = self._input.LT(-1).text
			if temp_name.startswith('"') and temp_name.endswith('"'):
			    temp_name = temp_name[1:-1]
			else:
			    temp_name = self.symbol_table.get_value(temp_name)

			_localctx.world = World(temp_name)

			    
			setState(58);
			match(RPAREN);
			setState(59);
			match(LBRACE);
			setState(63);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==DEFINE) {
				{
				{
				setState(60);
				((Define_worldContext)_localctx).define_scene = define_scene();
				((Define_worldContext)_localctx).scenes.add(((Define_worldContext)_localctx).define_scene);
				}
				}
				setState(65);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(66);
			match(RBRACE);

			for scene in ((Define_worldContext)_localctx).scenes:
			    _localctx.world.add_scene(scene.scene)
			    
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
		public Scene scene;
		public StatementContext statement;
		public List<StatementContext> statements = new ArrayList<StatementContext>();
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
			setState(69);
			match(DEFINE);
			setState(70);
			match(SCENE);
			setState(71);
			match(LPAREN);
			setState(72);
			_la = _input.LA(1);
			if ( !(_la==ID || _la==STRING_LITERAL) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}


			temp_name = self._input.LT(-1).text
			if temp_name.startswith('"') and temp_name.endswith('"'):
			    temp_name = temp_name[1:-1]
			else:
			    temp_name = self.symbol_table.get_value(temp_name)

			    
			setState(74);
			match(COMMA);
			setState(75);
			_la = _input.LA(1);
			if ( !(_la==ID || _la==INT_LITERAL) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}


			temp_width_chunk = self._input.LT(-1).text  
			if temp_width_chunk.isdigit():
			    temp_width_chunk = int(temp_width_chunk)
			else:
			    temp_width_chunk = int(self.symbol_table.get_value(temp_width_chunk))

			    
			setState(77);
			match(COMMA);
			setState(78);
			_la = _input.LA(1);
			if ( !(_la==ID || _la==INT_LITERAL) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}


			temp_length_chunk = self._input.LT(-1).text
			if temp_length_chunk.isdigit():
			    temp_length_chunk = int(temp_length_chunk)
			else:
			    temp_length_chunk = int(self.symbol_table.get_value(temp_length_chunk))

			    
			setState(80);
			match(RPAREN);

			_localctx.scene = Scene(temp_name, temp_width_chunk, temp_length_chunk)
			    
			setState(82);
			match(LBRACE);
			setState(86);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 268564656L) != 0)) {
				{
				{
				setState(83);
				((Define_sceneContext)_localctx).statement = statement();
				((Define_sceneContext)_localctx).statements.add(((Define_sceneContext)_localctx).statement);
				}
				}
				setState(88);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			   
			for stmt in ((Define_sceneContext)_localctx).statements: 
			    if isinstance(stmt.value, Chunk): 
			        _localctx.scene.add_chunk(stmt.value)
			    
			setState(90);
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
		public any value;
		public Add_statementContext add_statement;
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
			setState(102);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(93);
				assignment();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(94);
				define_list();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(95);
				append_statement();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(96);
				for_loop_number();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(97);
				for_loop_list();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(98);
				declaration();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(99);
				((StatementContext)_localctx).add_statement = add_statement();

				_localctx.value = ((StatementContext)_localctx).add_statement.chunk
				    
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
		public Chunk chunk;
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
			setState(104);
			match(CHUNK);
			setState(105);
			match(LPAREN);
			setState(106);
			_la = _input.LA(1);
			if ( !(_la==ID || _la==INT_LITERAL) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}


			temp_pos_x = self._input.LT(-1).text
			if temp_pos_x.isdigit():
			    temp_pos_x = int(temp_pos_x)
			else:  
			    temp_pos_x = int(self.symbol_table.get_value(temp_pos_x))


			setState(108);
			match(COMMA);
			setState(109);
			_la = _input.LA(1);
			if ( !(_la==ID || _la==INT_LITERAL) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}

			    
			temp_pos_y = self._input.LT(-1).text
			if temp_pos_y.isdigit():
			    temp_pos_y = int(temp_pos_y)
			else:  
			    temp_pos_y = int(self.symbol_table.get_value(temp_pos_y))


			setState(111);
			match(COMMA);
			setState(112);
			_la = _input.LA(1);
			if ( !(_la==ID || _la==FLOAT_LITERAL) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}


			temp_scale = self._input.LT(-1).text
			if temp_scale.replace(".","",1).isdigit():
			    temp_scale = float(temp_scale)
			else:  
			    temp_scale = float(self.symbol_table.get_value(temp_scale))


			setState(114);
			match(COMMA);
			setState(115);
			_la = _input.LA(1);
			if ( !(_la==ID || _la==FLOAT_LITERAL) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}


			temp_height_multiplier = self._input.LT(-1).text
			if temp_height_multiplier.replace(".","",1).isdigit():
			    temp_height_multiplier = float(temp_height_multiplier)
			else:  
			    temp_height_multiplier = float(self.symbol_table.get_value(temp_height_multiplier))
			    

			setState(117);
			match(COMMA);
			setState(118);
			_la = _input.LA(1);
			if ( !(_la==ID || _la==STRING_LITERAL) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}


			temp_texture = self._input.LT(-1).text
			if temp_texture.startswith('"') and temp_texture.endswith('"'):
			    temp_texture = temp_texture[1:-1]
			else:
			    temp_texture = self.symbol_table.get_value(temp_texture)


			setState(120);
			match(COMMA);
			{
			setState(121);
			match(ID);
			}

			temp_game_objects = self._input.LT(-1).text
			temp_game_objects = self.symbol_table.get_value(temp_game_objects)


			setState(123);
			match(RPAREN);

			_localctx.chunk = Chunk(temp_pos_x, temp_pos_y, temp_scale, temp_height_multiplier, temp_texture, temp_game_objects)
			    
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
		public GameObject gameobject;
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
			setState(153);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(126);
				match(GAMEOBJECT);
				setState(127);
				match(LPAREN);
				setState(128);
				_la = _input.LA(1);
				if ( !(_la==ID || _la==STRING_LITERAL) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}


				temp_model = self._input.LT(-1).text
				if temp_model.startswith('"') and temp_model.endswith('"'):
				    temp_model = temp_model[1:-1]
				else:
				    temp_model = self.symbol_table.get_value(temp_model)


				setState(130);
				match(COMMA);
				setState(131);
				_la = _input.LA(1);
				if ( !(_la==ID || _la==INT_LITERAL) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}

				    
				temp_density = self._input.LT(-1).text
				if temp_density.isdigit():
				    temp_density = int(temp_density)
				else:  
				    temp_density = int(self.symbol_table.get_value(temp_density))
				    

				setState(133);
				match(COMMA);
				setState(134);
				_la = _input.LA(1);
				if ( !(_la==ID || _la==FLOAT_LITERAL) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}

				    
				temp_min_scale = self._input.LT(-1).text
				if temp_min_scale.replace(".","",1).isdigit():
				    temp_min_scale = float(temp_min_scale)
				else:  
				    temp_min_scale = float(self.symbol_table.get_value(temp_min_scale))
				    

				setState(136);
				match(COMMA);
				setState(137);
				_la = _input.LA(1);
				if ( !(_la==ID || _la==FLOAT_LITERAL) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}

				    
				temp_max_scale = self._input.LT(-1).text
				if temp_max_scale.replace(".","",1).isdigit():
				    temp_max_scale = float(temp_max_scale)
				else:  
				    temp_max_scale = float(self.symbol_table.get_value(temp_max_scale))
				    

				setState(139);
				match(RPAREN);

				_localctx.gameobject = GameObject(temp_model, temp_density, temp_min_scale, temp_max_scale)

				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(141);
				match(GAMEOBJECT);
				setState(142);
				match(LPAREN);
				setState(143);
				_la = _input.LA(1);
				if ( !(_la==ID || _la==STRING_LITERAL) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}

				    
				temp_model = self._input.LT(-1).text
				if temp_model.startswith('"') and temp_model.endswith('"'):
				    temp_model = temp_model[1:-1]
				else:
				    temp_model = self.symbol_table.get_value(temp_model)
				    

				setState(145);
				match(COMMA);
				setState(146);
				_la = _input.LA(1);
				if ( !(_la==ID || _la==INT_LITERAL) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}

				    
				temp_density = self._input.LT(-1).text
				if temp_density.isdigit():
				    temp_density = int(temp_density)
				else:  
				    temp_density = int(self.symbol_table.get_value(temp_density))
				    

				setState(148);
				match(COMMA);
				setState(149);
				_la = _input.LA(1);
				if ( !(_la==ID || _la==FLOAT_LITERAL) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}

				    
				temp_scale = self._input.LT(-1).text
				if temp_scale.replace(".","",1).isdigit():
				    temp_scale = float(temp_scale)
				else:  
				    temp_scale = float(self.symbol_table.get_value(temp_scale))
				    

				setState(151);
				match(RPAREN);

				_localctx.gameobject = GameObject(temp_model, temp_density, temp_scale)

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
		public Token ID;
		public ArrayContext array;
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
			setState(160);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LIST:
				{
				setState(155);
				match(LIST);
				setState(156);
				match(LT);
				setState(157);
				_la = _input.LA(1);
				if ( !(_la==CHUNK || _la==GAMEOBJECT) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(158);
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
			setState(162);
			((Define_listContext)_localctx).ID = match(ID);
			setState(163);
			match(ASSIGN);
			setState(164);
			((Define_listContext)_localctx).array = array();

			self.symbol_table.set_value((((Define_listContext)_localctx).ID!=null?((Define_listContext)_localctx).ID.getText():null), ((Define_listContext)_localctx).array.object_list, "LIST<" + (((Define_listContext)_localctx).ID!=null?((Define_listContext)_localctx).ID.getText():null) + ">", "Contexto")

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
		public any object_list;
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
			setState(197);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(167);
				match(LSQUARE);
				setState(176);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case ID:
					{
					setState(168);
					match(ID);
					_localctx.object_list = [self.symbol_table.get_value(self._input.LT(-1).text)]
					}
					break;
				case CHUNK:
					{
					setState(170);
					chunk_constructor();
					_localctx.object_list = [chunk_constructor.chunk]
					}
					break;
				case GAMEOBJECT:
					{
					setState(173);
					gameobject_constructor();
					_localctx.object_list = [gameobject_constructor.gameobject]
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(191);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(178);
					match(COMMA);
					setState(187);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case ID:
						{
						setState(179);
						match(ID);
						_localctx.object_list.append(self.symbol_table.get_value(self._input.LT(-1).text))
						}
						break;
					case CHUNK:
						{
						setState(181);
						chunk_constructor();
						_localctx.object_list.append(chunk_constructor.chunk)
						}
						break;
					case GAMEOBJECT:
						{
						setState(184);
						gameobject_constructor();
						_localctx.object_list.append(gameobject_constructor.gameobject)
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					}
					}
					setState(193);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(194);
				match(RSQUARE);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(195);
				match(LSQUARE);
				setState(196);
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
			setState(199);
			match(APPEND);
			setState(200);
			match(ID);
			object_list_id = self._input.LT(-1).text
			setState(205);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				{
				setState(202);
				match(ID);
				}
				break;
			case GAMEOBJECT:
				{
				setState(203);
				gameobject_constructor();
				}
				break;
			case CHUNK:
				{
				setState(204);
				chunk_constructor();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			 
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
		public Chunk chunk;
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
			enterOuterAlt(_localctx, 1);
			{
			setState(213);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				{
				setState(209);
				match(ADD);
				setState(210);
				match(ID);
				}
				break;
			case 2:
				{
				setState(211);
				match(ADD);
				setState(212);
				chunk_constructor();
				}
				break;
			}


			temp_chunk = self._input.LT(-1).text
			if isinstance(temp_chunk, Chunk):
			    temp_chunk = temp_chunk
			else:
			    temp_chunk = self.symbol_table.get_value(temp_chunk)
			_localctx.chunk = temp_chunk

			    
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
		public StatementContext statement;
		public List<StatementContext> statements = new ArrayList<StatementContext>();
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
			setState(217);
			match(FOR);
			setState(218);
			match(ID);
			id = self._input.LT(-1).text
			setState(220);
			match(FROM);
			setState(221);
			match(INT_LITERAL);
			start = int(self._input.LT(-1).text)
			setState(223);
			match(TO);
			setState(224);
			match(INT_LITERAL);
			end = int(self._input.LT(-1).text) 

			print("FOR", id, start, end)
			for i in range(start, end + 1):
			    self.symbol_table.set_value(id, i, "INT", "Contexto")
			    for stmt in ((For_loop_numberContext)_localctx).statements:
			        pass
			    
			setState(227);
			match(LBRACE);
			setState(231);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 268564656L) != 0)) {
				{
				{
				setState(228);
				((For_loop_numberContext)_localctx).statement = statement();
				((For_loop_numberContext)_localctx).statements.add(((For_loop_numberContext)_localctx).statement);
				}
				}
				setState(233);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(234);
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
		public StatementContext statement;
		public List<StatementContext> statements = new ArrayList<StatementContext>();
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
			setState(236);
			match(FOR);
			setState(237);
			match(ID);
			id = self._input.LT(-1).text
			setState(239);
			match(IN);
			setState(240);
			match(ID);
			list_id = self._input.LT(-1).text
			setState(242);
			match(LBRACE);
			setState(246);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 268564656L) != 0)) {
				{
				{
				setState(243);
				((For_loop_listContext)_localctx).statement = statement();
				((For_loop_listContext)_localctx).statements.add(((For_loop_listContext)_localctx).statement);
				}
				}
				setState(248);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(249);
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
		public ExpressionContext expression;
		public Chunk_constructorContext chunk_constructor;
		public Gameobject_constructorContext gameobject_constructor;
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
			setState(283);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(255);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case INT:
					{
					setState(251);
					match(INT);
					}
					break;
				case STRING:
					{
					setState(252);
					match(STRING);
					}
					break;
				case FLOAT:
					{
					setState(253);
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
				setState(257);
				match(ID);
				id = self._input.LT(-1).text 
				setState(259);
				match(ASSIGN);
				setState(260);
				((AssignmentContext)_localctx).expression = expression();

				self.symbol_table.set_value(id, ((AssignmentContext)_localctx).expression.value, "INT", "Contexto")
				    
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(265);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case CHUNK:
					{
					setState(263);
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
				setState(267);
				match(ID);
				id = self._input.LT(-1).text 
				setState(269);
				match(ASSIGN);
				setState(270);
				((AssignmentContext)_localctx).chunk_constructor = chunk_constructor();

				self.symbol_table.set_value(id, ((AssignmentContext)_localctx).chunk_constructor.chunk, "CHUNK", "Contexto")
				    
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(275);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case GAMEOBJECT:
					{
					setState(273);
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
				setState(277);
				match(ID);
				id = self._input.LT(-1).text 
				setState(279);
				match(ASSIGN);
				setState(280);
				((AssignmentContext)_localctx).gameobject_constructor = gameobject_constructor();
				 
				self.symbol_table.set_value(id, ((AssignmentContext)_localctx).gameobject_constructor.gameobject, "GAMEOBJECT", "Contexto")
				    
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
		public any value;
		public Expression_auxContext e1;
		public Token op;
		public Expression_auxContext e2;
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
			setState(285);
			((ExpressionContext)_localctx).e1 = expression_aux();

			values = [((ExpressionContext)_localctx).e1.value]
			operators = []
			        
			setState(293);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==OP_ARIT) {
				{
				{
				setState(287);
				((ExpressionContext)_localctx).op = match(OP_ARIT);
				setState(288);
				((ExpressionContext)_localctx).e2 = expression_aux();

				values.append(((ExpressionContext)_localctx).e2.value)
				operators.append((((ExpressionContext)_localctx).op!=null?((ExpressionContext)_localctx).op.getText():null))
				        
				}
				}
				setState(295);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}

			_localctx.value = self.eval_expression(values, operators)
			    
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
		public any value;
		public ExpressionContext expression;
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
			setState(311);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case STRING_LITERAL:
				enterOuterAlt(_localctx, 1);
				{
				setState(298);
				match(STRING_LITERAL);
				 
				_localctx.value = self._input.LT(-1).text
				    
				}
				break;
			case INT_LITERAL:
				enterOuterAlt(_localctx, 2);
				{
				setState(300);
				match(INT_LITERAL);

				_localctx.value = int(self._input.LT(-1).text)
				    
				}
				break;
			case FLOAT_LITERAL:
				enterOuterAlt(_localctx, 3);
				{
				setState(302);
				match(FLOAT_LITERAL);

				_localctx.value = float(self._input.LT(-1).text)
				    
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 4);
				{
				setState(304);
				match(ID);

				_localctx.value = self._input.LT(-1).text
				    
				}
				break;
			case LPAREN:
				enterOuterAlt(_localctx, 5);
				{
				setState(306);
				match(LPAREN);
				setState(307);
				((Expression_auxContext)_localctx).expression = expression();
				setState(308);
				match(RPAREN);

				_localctx.value = ((Expression_auxContext)_localctx).expression.value
				    
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
			setState(328);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
				{
				setState(313);
				match(INT);
				type = self._input.LT(-1).text
				}
				break;
			case STRING:
				{
				setState(315);
				match(STRING);
				type = self._input.LT(-1).text
				}
				break;
			case FLOAT:
				{
				setState(317);
				match(FLOAT);
				type = self._input.LT(-1).text
				}
				break;
			case CHUNK:
				{
				setState(319);
				match(CHUNK);
				type = self._input.LT(-1).text
				}
				break;
			case GAMEOBJECT:
				{
				setState(321);
				match(GAMEOBJECT);
				type = self._input.LT(-1).text
				}
				break;
			case LIST:
				{
				setState(323);
				match(LIST);
				setState(324);
				match(LT);
				setState(325);
				_la = _input.LA(1);
				if ( !(_la==CHUNK || _la==GAMEOBJECT) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(326);
				match(GT);
				type = "LIST<" + self._input.LT(-2).text + ">"
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(330);
			match(ID);
			id = self._input.LT(-1).text

			self.symbol_table.set_value(id, [], type, "Contexto")
			    
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
		"\u0004\u0001\"\u014f\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0005\u0001/\b\u0001\n\u0001\f\u00012\t\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0005\u0002>\b\u0002"+
		"\n\u0002\f\u0002A\t\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0005\u0003U\b\u0003\n\u0003\f\u0003X\t\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0003\u0004g\b\u0004\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0003\u0006\u009a\b\u0006"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0003\u0007"+
		"\u00a1\b\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0003\b\u00b1\b\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0003\b\u00bc\b\b\u0005\b\u00be\b\b\n\b\f\b\u00c1\t"+
		"\b\u0001\b\u0001\b\u0001\b\u0003\b\u00c6\b\b\u0001\t\u0001\t\u0001\t\u0001"+
		"\t\u0001\t\u0001\t\u0003\t\u00ce\b\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0003\n\u00d6\b\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0005\u000b\u00e6\b\u000b\n"+
		"\u000b\f\u000b\u00e9\t\u000b\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001"+
		"\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0005\f\u00f5\b\f\n\f\f\f\u00f8"+
		"\t\f\u0001\f\u0001\f\u0001\r\u0001\r\u0001\r\u0001\r\u0003\r\u0100\b\r"+
		"\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0003"+
		"\r\u010a\b\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001"+
		"\r\u0003\r\u0114\b\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0003"+
		"\r\u011c\b\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0005\u000e\u0124\b\u000e\n\u000e\f\u000e\u0127\t\u000e\u0001"+
		"\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001"+
		"\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001"+
		"\u000f\u0001\u000f\u0001\u000f\u0003\u000f\u0138\b\u000f\u0001\u0010\u0001"+
		"\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001"+
		"\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001"+
		"\u0010\u0001\u0010\u0003\u0010\u0149\b\u0010\u0001\u0010\u0001\u0010\u0001"+
		"\u0010\u0001\u0010\u0001\u0010\u0000\u0000\u0011\u0000\u0002\u0004\u0006"+
		"\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e \u0000\u0004"+
		"\u0002\u0000\u001c\u001c\u001f\u001f\u0001\u0000\u001c\u001d\u0002\u0000"+
		"\u001c\u001c\u001e\u001e\u0001\u0000\u000b\f\u0164\u0000\"\u0001\u0000"+
		"\u0000\u0000\u0002(\u0001\u0000\u0000\u0000\u00045\u0001\u0000\u0000\u0000"+
		"\u0006E\u0001\u0000\u0000\u0000\bf\u0001\u0000\u0000\u0000\nh\u0001\u0000"+
		"\u0000\u0000\f\u0099\u0001\u0000\u0000\u0000\u000e\u00a0\u0001\u0000\u0000"+
		"\u0000\u0010\u00c5\u0001\u0000\u0000\u0000\u0012\u00c7\u0001\u0000\u0000"+
		"\u0000\u0014\u00d5\u0001\u0000\u0000\u0000\u0016\u00d9\u0001\u0000\u0000"+
		"\u0000\u0018\u00ec\u0001\u0000\u0000\u0000\u001a\u011b\u0001\u0000\u0000"+
		"\u0000\u001c\u011d\u0001\u0000\u0000\u0000\u001e\u0137\u0001\u0000\u0000"+
		"\u0000 \u0148\u0001\u0000\u0000\u0000\"#\u0006\u0000\uffff\uffff\u0000"+
		"#$\u0003\u0002\u0001\u0000$%\u0003\u0004\u0002\u0000%&\u0005\u0000\u0000"+
		"\u0001&\'\u0006\u0000\uffff\uffff\u0000\'\u0001\u0001\u0000\u0000\u0000"+
		"()\u0005\u0001\u0000\u0000)*\u0005\u0002\u0000\u0000*+\u0005\u0011\u0000"+
		"\u0000+,\u0005\u0012\u0000\u0000,0\u0005\u0013\u0000\u0000-/\u0003\b\u0004"+
		"\u0000.-\u0001\u0000\u0000\u0000/2\u0001\u0000\u0000\u00000.\u0001\u0000"+
		"\u0000\u000001\u0001\u0000\u0000\u000013\u0001\u0000\u0000\u000020\u0001"+
		"\u0000\u0000\u000034\u0005\u0014\u0000\u00004\u0003\u0001\u0000\u0000"+
		"\u000056\u0005\u0001\u0000\u000067\u0005\u0003\u0000\u000078\u0005\u0011"+
		"\u0000\u000089\u0007\u0000\u0000\u00009:\u0006\u0002\uffff\uffff\u0000"+
		":;\u0005\u0012\u0000\u0000;?\u0005\u0013\u0000\u0000<>\u0003\u0006\u0003"+
		"\u0000=<\u0001\u0000\u0000\u0000>A\u0001\u0000\u0000\u0000?=\u0001\u0000"+
		"\u0000\u0000?@\u0001\u0000\u0000\u0000@B\u0001\u0000\u0000\u0000A?\u0001"+
		"\u0000\u0000\u0000BC\u0005\u0014\u0000\u0000CD\u0006\u0002\uffff\uffff"+
		"\u0000D\u0005\u0001\u0000\u0000\u0000EF\u0005\u0001\u0000\u0000FG\u0005"+
		"\u0006\u0000\u0000GH\u0005\u0011\u0000\u0000HI\u0007\u0000\u0000\u0000"+
		"IJ\u0006\u0003\uffff\uffff\u0000JK\u0005\u0017\u0000\u0000KL\u0007\u0001"+
		"\u0000\u0000LM\u0006\u0003\uffff\uffff\u0000MN\u0005\u0017\u0000\u0000"+
		"NO\u0007\u0001\u0000\u0000OP\u0006\u0003\uffff\uffff\u0000PQ\u0005\u0012"+
		"\u0000\u0000QR\u0006\u0003\uffff\uffff\u0000RV\u0005\u0013\u0000\u0000"+
		"SU\u0003\b\u0004\u0000TS\u0001\u0000\u0000\u0000UX\u0001\u0000\u0000\u0000"+
		"VT\u0001\u0000\u0000\u0000VW\u0001\u0000\u0000\u0000WY\u0001\u0000\u0000"+
		"\u0000XV\u0001\u0000\u0000\u0000YZ\u0006\u0003\uffff\uffff\u0000Z[\u0005"+
		"\u0014\u0000\u0000[\\\u0006\u0003\uffff\uffff\u0000\\\u0007\u0001\u0000"+
		"\u0000\u0000]g\u0003\u001a\r\u0000^g\u0003\u000e\u0007\u0000_g\u0003\u0012"+
		"\t\u0000`g\u0003\u0016\u000b\u0000ag\u0003\u0018\f\u0000bg\u0003 \u0010"+
		"\u0000cd\u0003\u0014\n\u0000de\u0006\u0004\uffff\uffff\u0000eg\u0001\u0000"+
		"\u0000\u0000f]\u0001\u0000\u0000\u0000f^\u0001\u0000\u0000\u0000f_\u0001"+
		"\u0000\u0000\u0000f`\u0001\u0000\u0000\u0000fa\u0001\u0000\u0000\u0000"+
		"fb\u0001\u0000\u0000\u0000fc\u0001\u0000\u0000\u0000g\t\u0001\u0000\u0000"+
		"\u0000hi\u0005\u000b\u0000\u0000ij\u0005\u0011\u0000\u0000jk\u0007\u0001"+
		"\u0000\u0000kl\u0006\u0005\uffff\uffff\u0000lm\u0005\u0017\u0000\u0000"+
		"mn\u0007\u0001\u0000\u0000no\u0006\u0005\uffff\uffff\u0000op\u0005\u0017"+
		"\u0000\u0000pq\u0007\u0002\u0000\u0000qr\u0006\u0005\uffff\uffff\u0000"+
		"rs\u0005\u0017\u0000\u0000st\u0007\u0002\u0000\u0000tu\u0006\u0005\uffff"+
		"\uffff\u0000uv\u0005\u0017\u0000\u0000vw\u0007\u0000\u0000\u0000wx\u0006"+
		"\u0005\uffff\uffff\u0000xy\u0005\u0017\u0000\u0000yz\u0005\u001c\u0000"+
		"\u0000z{\u0006\u0005\uffff\uffff\u0000{|\u0005\u0012\u0000\u0000|}\u0006"+
		"\u0005\uffff\uffff\u0000}\u000b\u0001\u0000\u0000\u0000~\u007f\u0005\f"+
		"\u0000\u0000\u007f\u0080\u0005\u0011\u0000\u0000\u0080\u0081\u0007\u0000"+
		"\u0000\u0000\u0081\u0082\u0006\u0006\uffff\uffff\u0000\u0082\u0083\u0005"+
		"\u0017\u0000\u0000\u0083\u0084\u0007\u0001\u0000\u0000\u0084\u0085\u0006"+
		"\u0006\uffff\uffff\u0000\u0085\u0086\u0005\u0017\u0000\u0000\u0086\u0087"+
		"\u0007\u0002\u0000\u0000\u0087\u0088\u0006\u0006\uffff\uffff\u0000\u0088"+
		"\u0089\u0005\u0017\u0000\u0000\u0089\u008a\u0007\u0002\u0000\u0000\u008a"+
		"\u008b\u0006\u0006\uffff\uffff\u0000\u008b\u008c\u0005\u0012\u0000\u0000"+
		"\u008c\u009a\u0006\u0006\uffff\uffff\u0000\u008d\u008e\u0005\f\u0000\u0000"+
		"\u008e\u008f\u0005\u0011\u0000\u0000\u008f\u0090\u0007\u0000\u0000\u0000"+
		"\u0090\u0091\u0006\u0006\uffff\uffff\u0000\u0091\u0092\u0005\u0017\u0000"+
		"\u0000\u0092\u0093\u0007\u0001\u0000\u0000\u0093\u0094\u0006\u0006\uffff"+
		"\uffff\u0000\u0094\u0095\u0005\u0017\u0000\u0000\u0095\u0096\u0007\u0002"+
		"\u0000\u0000\u0096\u0097\u0006\u0006\uffff\uffff\u0000\u0097\u0098\u0005"+
		"\u0012\u0000\u0000\u0098\u009a\u0006\u0006\uffff\uffff\u0000\u0099~\u0001"+
		"\u0000\u0000\u0000\u0099\u008d\u0001\u0000\u0000\u0000\u009a\r\u0001\u0000"+
		"\u0000\u0000\u009b\u009c\u0005\r\u0000\u0000\u009c\u009d\u0005\u0018\u0000"+
		"\u0000\u009d\u009e\u0007\u0003\u0000\u0000\u009e\u00a1\u0005\u0019\u0000"+
		"\u0000\u009f\u00a1\u0001\u0000\u0000\u0000\u00a0\u009b\u0001\u0000\u0000"+
		"\u0000\u00a0\u009f\u0001\u0000\u0000\u0000\u00a1\u00a2\u0001\u0000\u0000"+
		"\u0000\u00a2\u00a3\u0005\u001c\u0000\u0000\u00a3\u00a4\u0005\u001a\u0000"+
		"\u0000\u00a4\u00a5\u0003\u0010\b\u0000\u00a5\u00a6\u0006\u0007\uffff\uffff"+
		"\u0000\u00a6\u000f\u0001\u0000\u0000\u0000\u00a7\u00b0\u0005\u0015\u0000"+
		"\u0000\u00a8\u00a9\u0005\u001c\u0000\u0000\u00a9\u00b1\u0006\b\uffff\uffff"+
		"\u0000\u00aa\u00ab\u0003\n\u0005\u0000\u00ab\u00ac\u0006\b\uffff\uffff"+
		"\u0000\u00ac\u00b1\u0001\u0000\u0000\u0000\u00ad\u00ae\u0003\f\u0006\u0000"+
		"\u00ae\u00af\u0006\b\uffff\uffff\u0000\u00af\u00b1\u0001\u0000\u0000\u0000"+
		"\u00b0\u00a8\u0001\u0000\u0000\u0000\u00b0\u00aa\u0001\u0000\u0000\u0000"+
		"\u00b0\u00ad\u0001\u0000\u0000\u0000\u00b1\u00bf\u0001\u0000\u0000\u0000"+
		"\u00b2\u00bb\u0005\u0017\u0000\u0000\u00b3\u00b4\u0005\u001c\u0000\u0000"+
		"\u00b4\u00bc\u0006\b\uffff\uffff\u0000\u00b5\u00b6\u0003\n\u0005\u0000"+
		"\u00b6\u00b7\u0006\b\uffff\uffff\u0000\u00b7\u00bc\u0001\u0000\u0000\u0000"+
		"\u00b8\u00b9\u0003\f\u0006\u0000\u00b9\u00ba\u0006\b\uffff\uffff\u0000"+
		"\u00ba\u00bc\u0001\u0000\u0000\u0000\u00bb\u00b3\u0001\u0000\u0000\u0000"+
		"\u00bb\u00b5\u0001\u0000\u0000\u0000\u00bb\u00b8\u0001\u0000\u0000\u0000"+
		"\u00bc\u00be\u0001\u0000\u0000\u0000\u00bd\u00b2\u0001\u0000\u0000\u0000"+
		"\u00be\u00c1\u0001\u0000\u0000\u0000\u00bf\u00bd\u0001\u0000\u0000\u0000"+
		"\u00bf\u00c0\u0001\u0000\u0000\u0000\u00c0\u00c2\u0001\u0000\u0000\u0000"+
		"\u00c1\u00bf\u0001\u0000\u0000\u0000\u00c2\u00c6\u0005\u0016\u0000\u0000"+
		"\u00c3\u00c4\u0005\u0015\u0000\u0000\u00c4\u00c6\u0005\u0016\u0000\u0000"+
		"\u00c5\u00a7\u0001\u0000\u0000\u0000\u00c5\u00c3\u0001\u0000\u0000\u0000"+
		"\u00c6\u0011\u0001\u0000\u0000\u0000\u00c7\u00c8\u0005\u0005\u0000\u0000"+
		"\u00c8\u00c9\u0005\u001c\u0000\u0000\u00c9\u00cd\u0006\t\uffff\uffff\u0000"+
		"\u00ca\u00ce\u0005\u001c\u0000\u0000\u00cb\u00ce\u0003\f\u0006\u0000\u00cc"+
		"\u00ce\u0003\n\u0005\u0000\u00cd\u00ca\u0001\u0000\u0000\u0000\u00cd\u00cb"+
		"\u0001\u0000\u0000\u0000\u00cd\u00cc\u0001\u0000\u0000\u0000\u00ce\u00cf"+
		"\u0001\u0000\u0000\u0000\u00cf\u00d0\u0006\t\uffff\uffff\u0000\u00d0\u0013"+
		"\u0001\u0000\u0000\u0000\u00d1\u00d2\u0005\u0004\u0000\u0000\u00d2\u00d6"+
		"\u0005\u001c\u0000\u0000\u00d3\u00d4\u0005\u0004\u0000\u0000\u00d4\u00d6"+
		"\u0003\n\u0005\u0000\u00d5\u00d1\u0001\u0000\u0000\u0000\u00d5\u00d3\u0001"+
		"\u0000\u0000\u0000\u00d6\u00d7\u0001\u0000\u0000\u0000\u00d7\u00d8\u0006"+
		"\n\uffff\uffff\u0000\u00d8\u0015\u0001\u0000\u0000\u0000\u00d9\u00da\u0005"+
		"\u0007\u0000\u0000\u00da\u00db\u0005\u001c\u0000\u0000\u00db\u00dc\u0006"+
		"\u000b\uffff\uffff\u0000\u00dc\u00dd\u0005\b\u0000\u0000\u00dd\u00de\u0005"+
		"\u001d\u0000\u0000\u00de\u00df\u0006\u000b\uffff\uffff\u0000\u00df\u00e0"+
		"\u0005\t\u0000\u0000\u00e0\u00e1\u0005\u001d\u0000\u0000\u00e1\u00e2\u0006"+
		"\u000b\uffff\uffff\u0000\u00e2\u00e3\u0006\u000b\uffff\uffff\u0000\u00e3"+
		"\u00e7\u0005\u0013\u0000\u0000\u00e4\u00e6\u0003\b\u0004\u0000\u00e5\u00e4"+
		"\u0001\u0000\u0000\u0000\u00e6\u00e9\u0001\u0000\u0000\u0000\u00e7\u00e5"+
		"\u0001\u0000\u0000\u0000\u00e7\u00e8\u0001\u0000\u0000\u0000\u00e8\u00ea"+
		"\u0001\u0000\u0000\u0000\u00e9\u00e7\u0001\u0000\u0000\u0000\u00ea\u00eb"+
		"\u0005\u0014\u0000\u0000\u00eb\u0017\u0001\u0000\u0000\u0000\u00ec\u00ed"+
		"\u0005\u0007\u0000\u0000\u00ed\u00ee\u0005\u001c\u0000\u0000\u00ee\u00ef"+
		"\u0006\f\uffff\uffff\u0000\u00ef\u00f0\u0005\n\u0000\u0000\u00f0\u00f1"+
		"\u0005\u001c\u0000\u0000\u00f1\u00f2\u0006\f\uffff\uffff\u0000\u00f2\u00f6"+
		"\u0005\u0013\u0000\u0000\u00f3\u00f5\u0003\b\u0004\u0000\u00f4\u00f3\u0001"+
		"\u0000\u0000\u0000\u00f5\u00f8\u0001\u0000\u0000\u0000\u00f6\u00f4\u0001"+
		"\u0000\u0000\u0000\u00f6\u00f7\u0001\u0000\u0000\u0000\u00f7\u00f9\u0001"+
		"\u0000\u0000\u0000\u00f8\u00f6\u0001\u0000\u0000\u0000\u00f9\u00fa\u0005"+
		"\u0014\u0000\u0000\u00fa\u0019\u0001\u0000\u0000\u0000\u00fb\u0100\u0005"+
		"\u000e\u0000\u0000\u00fc\u0100\u0005\u0010\u0000\u0000\u00fd\u0100\u0005"+
		"\u000f\u0000\u0000\u00fe\u0100\u0001\u0000\u0000\u0000\u00ff\u00fb\u0001"+
		"\u0000\u0000\u0000\u00ff\u00fc\u0001\u0000\u0000\u0000\u00ff\u00fd\u0001"+
		"\u0000\u0000\u0000\u00ff\u00fe\u0001\u0000\u0000\u0000\u0100\u0101\u0001"+
		"\u0000\u0000\u0000\u0101\u0102\u0005\u001c\u0000\u0000\u0102\u0103\u0006"+
		"\r\uffff\uffff\u0000\u0103\u0104\u0005\u001a\u0000\u0000\u0104\u0105\u0003"+
		"\u001c\u000e\u0000\u0105\u0106\u0006\r\uffff\uffff\u0000\u0106\u011c\u0001"+
		"\u0000\u0000\u0000\u0107\u010a\u0005\u000b\u0000\u0000\u0108\u010a\u0001"+
		"\u0000\u0000\u0000\u0109\u0107\u0001\u0000\u0000\u0000\u0109\u0108\u0001"+
		"\u0000\u0000\u0000\u010a\u010b\u0001\u0000\u0000\u0000\u010b\u010c\u0005"+
		"\u001c\u0000\u0000\u010c\u010d\u0006\r\uffff\uffff\u0000\u010d\u010e\u0005"+
		"\u001a\u0000\u0000\u010e\u010f\u0003\n\u0005\u0000\u010f\u0110\u0006\r"+
		"\uffff\uffff\u0000\u0110\u011c\u0001\u0000\u0000\u0000\u0111\u0114\u0005"+
		"\f\u0000\u0000\u0112\u0114\u0001\u0000\u0000\u0000\u0113\u0111\u0001\u0000"+
		"\u0000\u0000\u0113\u0112\u0001\u0000\u0000\u0000\u0114\u0115\u0001\u0000"+
		"\u0000\u0000\u0115\u0116\u0005\u001c\u0000\u0000\u0116\u0117\u0006\r\uffff"+
		"\uffff\u0000\u0117\u0118\u0005\u001a\u0000\u0000\u0118\u0119\u0003\f\u0006"+
		"\u0000\u0119\u011a\u0006\r\uffff\uffff\u0000\u011a\u011c\u0001\u0000\u0000"+
		"\u0000\u011b\u00ff\u0001\u0000\u0000\u0000\u011b\u0109\u0001\u0000\u0000"+
		"\u0000\u011b\u0113\u0001\u0000\u0000\u0000\u011c\u001b\u0001\u0000\u0000"+
		"\u0000\u011d\u011e\u0003\u001e\u000f\u0000\u011e\u0125\u0006\u000e\uffff"+
		"\uffff\u0000\u011f\u0120\u0005\u001b\u0000\u0000\u0120\u0121\u0003\u001e"+
		"\u000f\u0000\u0121\u0122\u0006\u000e\uffff\uffff\u0000\u0122\u0124\u0001"+
		"\u0000\u0000\u0000\u0123\u011f\u0001\u0000\u0000\u0000\u0124\u0127\u0001"+
		"\u0000\u0000\u0000\u0125\u0123\u0001\u0000\u0000\u0000\u0125\u0126\u0001"+
		"\u0000\u0000\u0000\u0126\u0128\u0001\u0000\u0000\u0000\u0127\u0125\u0001"+
		"\u0000\u0000\u0000\u0128\u0129\u0006\u000e\uffff\uffff\u0000\u0129\u001d"+
		"\u0001\u0000\u0000\u0000\u012a\u012b\u0005\u001f\u0000\u0000\u012b\u0138"+
		"\u0006\u000f\uffff\uffff\u0000\u012c\u012d\u0005\u001d\u0000\u0000\u012d"+
		"\u0138\u0006\u000f\uffff\uffff\u0000\u012e\u012f\u0005\u001e\u0000\u0000"+
		"\u012f\u0138\u0006\u000f\uffff\uffff\u0000\u0130\u0131\u0005\u001c\u0000"+
		"\u0000\u0131\u0138\u0006\u000f\uffff\uffff\u0000\u0132\u0133\u0005\u0011"+
		"\u0000\u0000\u0133\u0134\u0003\u001c\u000e\u0000\u0134\u0135\u0005\u0012"+
		"\u0000\u0000\u0135\u0136\u0006\u000f\uffff\uffff\u0000\u0136\u0138\u0001"+
		"\u0000\u0000\u0000\u0137\u012a\u0001\u0000\u0000\u0000\u0137\u012c\u0001"+
		"\u0000\u0000\u0000\u0137\u012e\u0001\u0000\u0000\u0000\u0137\u0130\u0001"+
		"\u0000\u0000\u0000\u0137\u0132\u0001\u0000\u0000\u0000\u0138\u001f\u0001"+
		"\u0000\u0000\u0000\u0139\u013a\u0005\u000e\u0000\u0000\u013a\u0149\u0006"+
		"\u0010\uffff\uffff\u0000\u013b\u013c\u0005\u0010\u0000\u0000\u013c\u0149"+
		"\u0006\u0010\uffff\uffff\u0000\u013d\u013e\u0005\u000f\u0000\u0000\u013e"+
		"\u0149\u0006\u0010\uffff\uffff\u0000\u013f\u0140\u0005\u000b\u0000\u0000"+
		"\u0140\u0149\u0006\u0010\uffff\uffff\u0000\u0141\u0142\u0005\f\u0000\u0000"+
		"\u0142\u0149\u0006\u0010\uffff\uffff\u0000\u0143\u0144\u0005\r\u0000\u0000"+
		"\u0144\u0145\u0005\u0018\u0000\u0000\u0145\u0146\u0007\u0003\u0000\u0000"+
		"\u0146\u0147\u0005\u0019\u0000\u0000\u0147\u0149\u0006\u0010\uffff\uffff"+
		"\u0000\u0148\u0139\u0001\u0000\u0000\u0000\u0148\u013b\u0001\u0000\u0000"+
		"\u0000\u0148\u013d\u0001\u0000\u0000\u0000\u0148\u013f\u0001\u0000\u0000"+
		"\u0000\u0148\u0141\u0001\u0000\u0000\u0000\u0148\u0143\u0001\u0000\u0000"+
		"\u0000\u0149\u014a\u0001\u0000\u0000\u0000\u014a\u014b\u0005\u001c\u0000"+
		"\u0000\u014b\u014c\u0006\u0010\uffff\uffff\u0000\u014c\u014d\u0006\u0010"+
		"\uffff\uffff\u0000\u014d!\u0001\u0000\u0000\u0000\u00150?Vf\u0099\u00a0"+
		"\u00b0\u00bb\u00bf\u00c5\u00cd\u00d5\u00e7\u00f6\u00ff\u0109\u0113\u011b"+
		"\u0125\u0137\u0148";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}