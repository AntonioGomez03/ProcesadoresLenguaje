// Generated from /home/antonio/Documentos/Universidad/Cuarto/Procesadores de Lenguajes/ProcesadoresLenguaje/python/src/antlr4/lexer_gec.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class lexer_gec extends Lexer {
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
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"DEFINE", "SETUP", "WORLD", "ADD", "APPEND", "SCENE", "FOR", "FROM", 
			"TO", "IN", "DESCRIPTOR", "LIST", "INT", "FLOAT", "STRING", "LPAREN", 
			"RPAREN", "LBRACE", "RBRACE", "LSQUARE", "RSQUARE", "COMMA", "LT", "GT", 
			"ASSIGN", "OP_ARIT", "ID", "INT_LITERAL", "FLOAT_LITERAL", "STRING_LITERAL", 
			"COMMENT", "WS"
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


	public lexer_gec(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "lexer_gec.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	@Override
	public void action(RuleContext _localctx, int ruleIndex, int actionIndex) {
		switch (ruleIndex) {
		case 0:
			DEFINE_action((RuleContext)_localctx, actionIndex);
			break;
		case 1:
			SETUP_action((RuleContext)_localctx, actionIndex);
			break;
		case 2:
			WORLD_action((RuleContext)_localctx, actionIndex);
			break;
		case 3:
			ADD_action((RuleContext)_localctx, actionIndex);
			break;
		case 4:
			APPEND_action((RuleContext)_localctx, actionIndex);
			break;
		case 5:
			SCENE_action((RuleContext)_localctx, actionIndex);
			break;
		case 6:
			FOR_action((RuleContext)_localctx, actionIndex);
			break;
		case 7:
			FROM_action((RuleContext)_localctx, actionIndex);
			break;
		case 8:
			TO_action((RuleContext)_localctx, actionIndex);
			break;
		case 9:
			IN_action((RuleContext)_localctx, actionIndex);
			break;
		case 10:
			DESCRIPTOR_action((RuleContext)_localctx, actionIndex);
			break;
		case 11:
			LIST_action((RuleContext)_localctx, actionIndex);
			break;
		case 12:
			INT_action((RuleContext)_localctx, actionIndex);
			break;
		case 13:
			FLOAT_action((RuleContext)_localctx, actionIndex);
			break;
		case 14:
			STRING_action((RuleContext)_localctx, actionIndex);
			break;
		case 15:
			LPAREN_action((RuleContext)_localctx, actionIndex);
			break;
		case 16:
			RPAREN_action((RuleContext)_localctx, actionIndex);
			break;
		case 17:
			LBRACE_action((RuleContext)_localctx, actionIndex);
			break;
		case 18:
			RBRACE_action((RuleContext)_localctx, actionIndex);
			break;
		case 19:
			LSQUARE_action((RuleContext)_localctx, actionIndex);
			break;
		case 20:
			RSQUARE_action((RuleContext)_localctx, actionIndex);
			break;
		case 21:
			COMMA_action((RuleContext)_localctx, actionIndex);
			break;
		case 22:
			LT_action((RuleContext)_localctx, actionIndex);
			break;
		case 23:
			GT_action((RuleContext)_localctx, actionIndex);
			break;
		case 24:
			ASSIGN_action((RuleContext)_localctx, actionIndex);
			break;
		case 25:
			OP_ARIT_action((RuleContext)_localctx, actionIndex);
			break;
		case 26:
			ID_action((RuleContext)_localctx, actionIndex);
			break;
		case 27:
			INT_LITERAL_action((RuleContext)_localctx, actionIndex);
			break;
		case 28:
			FLOAT_LITERAL_action((RuleContext)_localctx, actionIndex);
			break;
		case 29:
			STRING_LITERAL_action((RuleContext)_localctx, actionIndex);
			break;
		}
	}
	private void DEFINE_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 0:
			print("DEFINE")
			break;
		}
	}
	private void SETUP_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 1:
			print("SETUP")
			break;
		}
	}
	private void WORLD_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 2:
			print("WORLD")
			break;
		}
	}
	private void ADD_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 3:
			print("ADD")
			break;
		}
	}
	private void APPEND_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 4:
			print("APPEND")
			break;
		}
	}
	private void SCENE_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 5:
			print("SCENE")
			break;
		}
	}
	private void FOR_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 6:
			print("FOR")
			break;
		}
	}
	private void FROM_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 7:
			print("FROM")
			break;
		}
	}
	private void TO_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 8:
			print("TO")
			break;
		}
	}
	private void IN_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 9:
			print("IN")
			break;
		}
	}
	private void DESCRIPTOR_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 10:
			print("DESCRIPTOR")
			break;
		}
	}
	private void LIST_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 11:
			print("LIST")
			break;
		}
	}
	private void INT_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 12:
			print("INT")
			break;
		}
	}
	private void FLOAT_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 13:
			print("FLOAT")
			break;
		}
	}
	private void STRING_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 14:
			print("STRING")
			break;
		}
	}
	private void LPAREN_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 15:
			print("LPAREN")
			break;
		}
	}
	private void RPAREN_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 16:
			print("RPAREN")
			break;
		}
	}
	private void LBRACE_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 17:
			print("LBRACE")
			break;
		}
	}
	private void RBRACE_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 18:
			print("RBRACE")
			break;
		}
	}
	private void LSQUARE_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 19:
			print("LSQUARE")
			break;
		}
	}
	private void RSQUARE_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 20:
			print("RSQUARE")
			break;
		}
	}
	private void COMMA_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 21:
			print("COMMA")
			break;
		}
	}
	private void LT_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 22:
			print("LT")
			break;
		}
	}
	private void GT_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 23:
			print("GT")
			break;
		}
	}
	private void ASSIGN_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 24:
			print("ASSIGN")
			break;
		}
	}
	private void OP_ARIT_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 25:
			print("OP_ARIT")
			break;
		}
	}
	private void ID_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 26:
			print("ID")
			break;
		}
	}
	private void INT_LITERAL_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 27:
			print("INT_LITERAL")
			break;
		}
	}
	private void FLOAT_LITERAL_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 28:
			print("FLOAT_LITERAL")
			break;
		}
	}
	private void STRING_LITERAL_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 29:
			print("STRING_LITERAL")
			break;
		}
	}

	public static final String _serializedATN =
		"\u0004\u0000 \u0115\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002"+
		"\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002"+
		"\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002"+
		"\u0015\u0007\u0015\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002"+
		"\u0018\u0007\u0018\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002"+
		"\u001b\u0007\u001b\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002"+
		"\u001e\u0007\u001e\u0002\u001f\u0007\u001f\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b"+
		"\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0003\n\u009a"+
		"\b\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001"+
		"\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\u000e"+
		"\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0012"+
		"\u0001\u0012\u0001\u0012\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0014"+
		"\u0001\u0014\u0001\u0014\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0016"+
		"\u0001\u0016\u0001\u0016\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0018"+
		"\u0001\u0018\u0001\u0018\u0001\u0019\u0001\u0019\u0001\u0019\u0003\u0019"+
		"\u00db\b\u0019\u0001\u001a\u0001\u001a\u0005\u001a\u00df\b\u001a\n\u001a"+
		"\f\u001a\u00e2\t\u001a\u0001\u001a\u0001\u001a\u0001\u001b\u0004\u001b"+
		"\u00e7\b\u001b\u000b\u001b\f\u001b\u00e8\u0001\u001b\u0001\u001b\u0001"+
		"\u001c\u0004\u001c\u00ee\b\u001c\u000b\u001c\f\u001c\u00ef\u0001\u001c"+
		"\u0001\u001c\u0004\u001c\u00f4\b\u001c\u000b\u001c\f\u001c\u00f5\u0001"+
		"\u001c\u0001\u001c\u0001\u001d\u0001\u001d\u0005\u001d\u00fc\b\u001d\n"+
		"\u001d\f\u001d\u00ff\t\u001d\u0001\u001d\u0001\u001d\u0001\u001d\u0001"+
		"\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0005\u001e\u0108\b\u001e\n"+
		"\u001e\f\u001e\u010b\t\u001e\u0001\u001e\u0001\u001e\u0001\u001f\u0004"+
		"\u001f\u0110\b\u001f\u000b\u001f\f\u001f\u0111\u0001\u001f\u0001\u001f"+
		"\u0000\u0000 \u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005"+
		"\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019"+
		"\r\u001b\u000e\u001d\u000f\u001f\u0010!\u0011#\u0012%\u0013\'\u0014)\u0015"+
		"+\u0016-\u0017/\u00181\u00193\u001a5\u001b7\u001c9\u001d;\u001e=\u001f"+
		"? \u0001\u0000\u0007\u0002\u0000*+--\u0002\u0000AZaz\u0004\u000009AZ_"+
		"_az\u0001\u000009\u0001\u0000\"\"\u0002\u0000\n\n\r\r\u0003\u0000\t\n"+
		"\r\r  \u011d\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000"+
		"\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000"+
		"\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000"+
		"\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000"+
		"\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000"+
		"\u0000\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000"+
		"\u0000\u0019\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000\u0000\u0000"+
		"\u0000\u001d\u0001\u0000\u0000\u0000\u0000\u001f\u0001\u0000\u0000\u0000"+
		"\u0000!\u0001\u0000\u0000\u0000\u0000#\u0001\u0000\u0000\u0000\u0000%"+
		"\u0001\u0000\u0000\u0000\u0000\'\u0001\u0000\u0000\u0000\u0000)\u0001"+
		"\u0000\u0000\u0000\u0000+\u0001\u0000\u0000\u0000\u0000-\u0001\u0000\u0000"+
		"\u0000\u0000/\u0001\u0000\u0000\u0000\u00001\u0001\u0000\u0000\u0000\u0000"+
		"3\u0001\u0000\u0000\u0000\u00005\u0001\u0000\u0000\u0000\u00007\u0001"+
		"\u0000\u0000\u0000\u00009\u0001\u0000\u0000\u0000\u0000;\u0001\u0000\u0000"+
		"\u0000\u0000=\u0001\u0000\u0000\u0000\u0000?\u0001\u0000\u0000\u0000\u0001"+
		"A\u0001\u0000\u0000\u0000\u0003J\u0001\u0000\u0000\u0000\u0005R\u0001"+
		"\u0000\u0000\u0000\u0007Z\u0001\u0000\u0000\u0000\t`\u0001\u0000\u0000"+
		"\u0000\u000bi\u0001\u0000\u0000\u0000\rq\u0001\u0000\u0000\u0000\u000f"+
		"w\u0001\u0000\u0000\u0000\u0011~\u0001\u0000\u0000\u0000\u0013\u0083\u0001"+
		"\u0000\u0000\u0000\u0015\u0099\u0001\u0000\u0000\u0000\u0017\u009b\u0001"+
		"\u0000\u0000\u0000\u0019\u00a2\u0001\u0000\u0000\u0000\u001b\u00a8\u0001"+
		"\u0000\u0000\u0000\u001d\u00b0\u0001\u0000\u0000\u0000\u001f\u00b9\u0001"+
		"\u0000\u0000\u0000!\u00bc\u0001\u0000\u0000\u0000#\u00bf\u0001\u0000\u0000"+
		"\u0000%\u00c2\u0001\u0000\u0000\u0000\'\u00c5\u0001\u0000\u0000\u0000"+
		")\u00c8\u0001\u0000\u0000\u0000+\u00cb\u0001\u0000\u0000\u0000-\u00ce"+
		"\u0001\u0000\u0000\u0000/\u00d1\u0001\u0000\u0000\u00001\u00d4\u0001\u0000"+
		"\u0000\u00003\u00da\u0001\u0000\u0000\u00005\u00dc\u0001\u0000\u0000\u0000"+
		"7\u00e6\u0001\u0000\u0000\u00009\u00ed\u0001\u0000\u0000\u0000;\u00f9"+
		"\u0001\u0000\u0000\u0000=\u0103\u0001\u0000\u0000\u0000?\u010f\u0001\u0000"+
		"\u0000\u0000AB\u0005D\u0000\u0000BC\u0005E\u0000\u0000CD\u0005F\u0000"+
		"\u0000DE\u0005I\u0000\u0000EF\u0005N\u0000\u0000FG\u0005E\u0000\u0000"+
		"GH\u0001\u0000\u0000\u0000HI\u0006\u0000\u0000\u0000I\u0002\u0001\u0000"+
		"\u0000\u0000JK\u0005S\u0000\u0000KL\u0005E\u0000\u0000LM\u0005T\u0000"+
		"\u0000MN\u0005U\u0000\u0000NO\u0005P\u0000\u0000OP\u0001\u0000\u0000\u0000"+
		"PQ\u0006\u0001\u0001\u0000Q\u0004\u0001\u0000\u0000\u0000RS\u0005W\u0000"+
		"\u0000ST\u0005O\u0000\u0000TU\u0005R\u0000\u0000UV\u0005L\u0000\u0000"+
		"VW\u0005D\u0000\u0000WX\u0001\u0000\u0000\u0000XY\u0006\u0002\u0002\u0000"+
		"Y\u0006\u0001\u0000\u0000\u0000Z[\u0005A\u0000\u0000[\\\u0005D\u0000\u0000"+
		"\\]\u0005D\u0000\u0000]^\u0001\u0000\u0000\u0000^_\u0006\u0003\u0003\u0000"+
		"_\b\u0001\u0000\u0000\u0000`a\u0005A\u0000\u0000ab\u0005P\u0000\u0000"+
		"bc\u0005P\u0000\u0000cd\u0005E\u0000\u0000de\u0005N\u0000\u0000ef\u0005"+
		"D\u0000\u0000fg\u0001\u0000\u0000\u0000gh\u0006\u0004\u0004\u0000h\n\u0001"+
		"\u0000\u0000\u0000ij\u0005S\u0000\u0000jk\u0005C\u0000\u0000kl\u0005E"+
		"\u0000\u0000lm\u0005N\u0000\u0000mn\u0005E\u0000\u0000no\u0001\u0000\u0000"+
		"\u0000op\u0006\u0005\u0005\u0000p\f\u0001\u0000\u0000\u0000qr\u0005F\u0000"+
		"\u0000rs\u0005O\u0000\u0000st\u0005R\u0000\u0000tu\u0001\u0000\u0000\u0000"+
		"uv\u0006\u0006\u0006\u0000v\u000e\u0001\u0000\u0000\u0000wx\u0005F\u0000"+
		"\u0000xy\u0005R\u0000\u0000yz\u0005O\u0000\u0000z{\u0005M\u0000\u0000"+
		"{|\u0001\u0000\u0000\u0000|}\u0006\u0007\u0007\u0000}\u0010\u0001\u0000"+
		"\u0000\u0000~\u007f\u0005T\u0000\u0000\u007f\u0080\u0005O\u0000\u0000"+
		"\u0080\u0081\u0001\u0000\u0000\u0000\u0081\u0082\u0006\b\b\u0000\u0082"+
		"\u0012\u0001\u0000\u0000\u0000\u0083\u0084\u0005I\u0000\u0000\u0084\u0085"+
		"\u0005N\u0000\u0000\u0085\u0086\u0001\u0000\u0000\u0000\u0086\u0087\u0006"+
		"\t\t\u0000\u0087\u0014\u0001\u0000\u0000\u0000\u0088\u0089\u0005G\u0000"+
		"\u0000\u0089\u008a\u0005A\u0000\u0000\u008a\u008b\u0005M\u0000\u0000\u008b"+
		"\u008c\u0005E\u0000\u0000\u008c\u008d\u0005O\u0000\u0000\u008d\u008e\u0005"+
		"B\u0000\u0000\u008e\u008f\u0005J\u0000\u0000\u008f\u0090\u0005E\u0000"+
		"\u0000\u0090\u0091\u0005C\u0000\u0000\u0091\u009a\u0005T\u0000\u0000\u0092"+
		"\u0093\u0005C\u0000\u0000\u0093\u0094\u0005H\u0000\u0000\u0094\u0095\u0005"+
		"U\u0000\u0000\u0095\u0096\u0005N\u0000\u0000\u0096\u0097\u0005K\u0000"+
		"\u0000\u0097\u0098\u0001\u0000\u0000\u0000\u0098\u009a\u0006\n\n\u0000"+
		"\u0099\u0088\u0001\u0000\u0000\u0000\u0099\u0092\u0001\u0000\u0000\u0000"+
		"\u009a\u0016\u0001\u0000\u0000\u0000\u009b\u009c\u0005L\u0000\u0000\u009c"+
		"\u009d\u0005I\u0000\u0000\u009d\u009e\u0005S\u0000\u0000\u009e\u009f\u0005"+
		"T\u0000\u0000\u009f\u00a0\u0001\u0000\u0000\u0000\u00a0\u00a1\u0006\u000b"+
		"\u000b\u0000\u00a1\u0018\u0001\u0000\u0000\u0000\u00a2\u00a3\u0005I\u0000"+
		"\u0000\u00a3\u00a4\u0005N\u0000\u0000\u00a4\u00a5\u0005T\u0000\u0000\u00a5"+
		"\u00a6\u0001\u0000\u0000\u0000\u00a6\u00a7\u0006\f\f\u0000\u00a7\u001a"+
		"\u0001\u0000\u0000\u0000\u00a8\u00a9\u0005F\u0000\u0000\u00a9\u00aa\u0005"+
		"L\u0000\u0000\u00aa\u00ab\u0005O\u0000\u0000\u00ab\u00ac\u0005A\u0000"+
		"\u0000\u00ac\u00ad\u0005T\u0000\u0000\u00ad\u00ae\u0001\u0000\u0000\u0000"+
		"\u00ae\u00af\u0006\r\r\u0000\u00af\u001c\u0001\u0000\u0000\u0000\u00b0"+
		"\u00b1\u0005S\u0000\u0000\u00b1\u00b2\u0005T\u0000\u0000\u00b2\u00b3\u0005"+
		"R\u0000\u0000\u00b3\u00b4\u0005I\u0000\u0000\u00b4\u00b5\u0005N\u0000"+
		"\u0000\u00b5\u00b6\u0005G\u0000\u0000\u00b6\u00b7\u0001\u0000\u0000\u0000"+
		"\u00b7\u00b8\u0006\u000e\u000e\u0000\u00b8\u001e\u0001\u0000\u0000\u0000"+
		"\u00b9\u00ba\u0005(\u0000\u0000\u00ba\u00bb\u0006\u000f\u000f\u0000\u00bb"+
		" \u0001\u0000\u0000\u0000\u00bc\u00bd\u0005)\u0000\u0000\u00bd\u00be\u0006"+
		"\u0010\u0010\u0000\u00be\"\u0001\u0000\u0000\u0000\u00bf\u00c0\u0005{"+
		"\u0000\u0000\u00c0\u00c1\u0006\u0011\u0011\u0000\u00c1$\u0001\u0000\u0000"+
		"\u0000\u00c2\u00c3\u0005}\u0000\u0000\u00c3\u00c4\u0006\u0012\u0012\u0000"+
		"\u00c4&\u0001\u0000\u0000\u0000\u00c5\u00c6\u0005[\u0000\u0000\u00c6\u00c7"+
		"\u0006\u0013\u0013\u0000\u00c7(\u0001\u0000\u0000\u0000\u00c8\u00c9\u0005"+
		"]\u0000\u0000\u00c9\u00ca\u0006\u0014\u0014\u0000\u00ca*\u0001\u0000\u0000"+
		"\u0000\u00cb\u00cc\u0005,\u0000\u0000\u00cc\u00cd\u0006\u0015\u0015\u0000"+
		"\u00cd,\u0001\u0000\u0000\u0000\u00ce\u00cf\u0005<\u0000\u0000\u00cf\u00d0"+
		"\u0006\u0016\u0016\u0000\u00d0.\u0001\u0000\u0000\u0000\u00d1\u00d2\u0005"+
		">\u0000\u0000\u00d2\u00d3\u0006\u0017\u0017\u0000\u00d30\u0001\u0000\u0000"+
		"\u0000\u00d4\u00d5\u0005=\u0000\u0000\u00d5\u00d6\u0006\u0018\u0018\u0000"+
		"\u00d62\u0001\u0000\u0000\u0000\u00d7\u00db\u0007\u0000\u0000\u0000\u00d8"+
		"\u00d9\u0005/\u0000\u0000\u00d9\u00db\u0006\u0019\u0019\u0000\u00da\u00d7"+
		"\u0001\u0000\u0000\u0000\u00da\u00d8\u0001\u0000\u0000\u0000\u00db4\u0001"+
		"\u0000\u0000\u0000\u00dc\u00e0\u0007\u0001\u0000\u0000\u00dd\u00df\u0007"+
		"\u0002\u0000\u0000\u00de\u00dd\u0001\u0000\u0000\u0000\u00df\u00e2\u0001"+
		"\u0000\u0000\u0000\u00e0\u00de\u0001\u0000\u0000\u0000\u00e0\u00e1\u0001"+
		"\u0000\u0000\u0000\u00e1\u00e3\u0001\u0000\u0000\u0000\u00e2\u00e0\u0001"+
		"\u0000\u0000\u0000\u00e3\u00e4\u0006\u001a\u001a\u0000\u00e46\u0001\u0000"+
		"\u0000\u0000\u00e5\u00e7\u0007\u0003\u0000\u0000\u00e6\u00e5\u0001\u0000"+
		"\u0000\u0000\u00e7\u00e8\u0001\u0000\u0000\u0000\u00e8\u00e6\u0001\u0000"+
		"\u0000\u0000\u00e8\u00e9\u0001\u0000\u0000\u0000\u00e9\u00ea\u0001\u0000"+
		"\u0000\u0000\u00ea\u00eb\u0006\u001b\u001b\u0000\u00eb8\u0001\u0000\u0000"+
		"\u0000\u00ec\u00ee\u0007\u0003\u0000\u0000\u00ed\u00ec\u0001\u0000\u0000"+
		"\u0000\u00ee\u00ef\u0001\u0000\u0000\u0000\u00ef\u00ed\u0001\u0000\u0000"+
		"\u0000\u00ef\u00f0\u0001\u0000\u0000\u0000\u00f0\u00f1\u0001\u0000\u0000"+
		"\u0000\u00f1\u00f3\u0005.\u0000\u0000\u00f2\u00f4\u0007\u0003\u0000\u0000"+
		"\u00f3\u00f2\u0001\u0000\u0000\u0000\u00f4\u00f5\u0001\u0000\u0000\u0000"+
		"\u00f5\u00f3\u0001\u0000\u0000\u0000\u00f5\u00f6\u0001\u0000\u0000\u0000"+
		"\u00f6\u00f7\u0001\u0000\u0000\u0000\u00f7\u00f8\u0006\u001c\u001c\u0000"+
		"\u00f8:\u0001\u0000\u0000\u0000\u00f9\u00fd\u0005\"\u0000\u0000\u00fa"+
		"\u00fc\b\u0004\u0000\u0000\u00fb\u00fa\u0001\u0000\u0000\u0000\u00fc\u00ff"+
		"\u0001\u0000\u0000\u0000\u00fd\u00fb\u0001\u0000\u0000\u0000\u00fd\u00fe"+
		"\u0001\u0000\u0000\u0000\u00fe\u0100\u0001\u0000\u0000\u0000\u00ff\u00fd"+
		"\u0001\u0000\u0000\u0000\u0100\u0101\u0005\"\u0000\u0000\u0101\u0102\u0006"+
		"\u001d\u001d\u0000\u0102<\u0001\u0000\u0000\u0000\u0103\u0104\u0005/\u0000"+
		"\u0000\u0104\u0105\u0005/\u0000\u0000\u0105\u0109\u0001\u0000\u0000\u0000"+
		"\u0106\u0108\b\u0005\u0000\u0000\u0107\u0106\u0001\u0000\u0000\u0000\u0108"+
		"\u010b\u0001\u0000\u0000\u0000\u0109\u0107\u0001\u0000\u0000\u0000\u0109"+
		"\u010a\u0001\u0000\u0000\u0000\u010a\u010c\u0001\u0000\u0000\u0000\u010b"+
		"\u0109\u0001\u0000\u0000\u0000\u010c\u010d\u0006\u001e\u001e\u0000\u010d"+
		">\u0001\u0000\u0000\u0000\u010e\u0110\u0007\u0006\u0000\u0000\u010f\u010e"+
		"\u0001\u0000\u0000\u0000\u0110\u0111\u0001\u0000\u0000\u0000\u0111\u010f"+
		"\u0001\u0000\u0000\u0000\u0111\u0112\u0001\u0000\u0000\u0000\u0112\u0113"+
		"\u0001\u0000\u0000\u0000\u0113\u0114\u0006\u001f\u001e\u0000\u0114@\u0001"+
		"\u0000\u0000\u0000\n\u0000\u0099\u00da\u00e0\u00e8\u00ef\u00f5\u00fd\u0109"+
		"\u0111\u001f\u0001\u0000\u0000\u0001\u0001\u0001\u0001\u0002\u0002\u0001"+
		"\u0003\u0003\u0001\u0004\u0004\u0001\u0005\u0005\u0001\u0006\u0006\u0001"+
		"\u0007\u0007\u0001\b\b\u0001\t\t\u0001\n\n\u0001\u000b\u000b\u0001\f\f"+
		"\u0001\r\r\u0001\u000e\u000e\u0001\u000f\u000f\u0001\u0010\u0010\u0001"+
		"\u0011\u0011\u0001\u0012\u0012\u0001\u0013\u0013\u0001\u0014\u0014\u0001"+
		"\u0015\u0015\u0001\u0016\u0016\u0001\u0017\u0017\u0001\u0018\u0018\u0001"+
		"\u0019\u0019\u0001\u001a\u001a\u0001\u001b\u001b\u0001\u001c\u001c\u0001"+
		"\u001d\u001d\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}