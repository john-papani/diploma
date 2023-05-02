# Generated from DebateGrammar.g4 by ANTLR 4.12.0
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
        4,1,42,175,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,1,0,3,0,50,8,0,1,0,3,0,53,8,0,
        1,0,3,0,56,8,0,1,0,3,0,59,8,0,1,0,3,0,62,8,0,1,0,3,0,65,8,0,1,0,
        1,0,1,1,1,1,1,2,3,2,72,8,2,1,2,1,2,1,3,3,3,77,8,3,1,3,3,3,80,8,3,
        1,3,3,3,83,8,3,1,3,3,3,86,8,3,1,3,3,3,89,8,3,1,3,1,3,1,4,1,4,4,4,
        95,8,4,11,4,12,4,96,1,5,1,5,4,5,101,8,5,11,5,12,5,102,1,6,1,6,1,
        7,1,7,1,8,1,8,1,8,1,9,4,9,113,8,9,11,9,12,9,114,1,10,1,10,1,10,1,
        11,4,11,121,8,11,11,11,12,11,122,1,12,1,12,4,12,127,8,12,11,12,12,
        12,128,1,13,1,13,1,13,1,14,4,14,135,8,14,11,14,12,14,136,1,15,1,
        15,1,15,1,16,3,16,143,8,16,1,16,1,16,3,16,147,8,16,1,16,3,16,150,
        8,16,1,16,3,16,153,8,16,1,16,3,16,156,8,16,1,16,1,16,1,17,1,17,1,
        18,1,18,1,19,1,19,1,20,1,20,1,21,1,21,1,21,1,22,1,22,1,23,1,23,1,
        23,0,0,24,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,
        40,42,44,46,0,1,1,0,4,5,173,0,49,1,0,0,0,2,68,1,0,0,0,4,71,1,0,0,
        0,6,76,1,0,0,0,8,92,1,0,0,0,10,98,1,0,0,0,12,104,1,0,0,0,14,106,
        1,0,0,0,16,108,1,0,0,0,18,112,1,0,0,0,20,116,1,0,0,0,22,120,1,0,
        0,0,24,124,1,0,0,0,26,130,1,0,0,0,28,134,1,0,0,0,30,138,1,0,0,0,
        32,142,1,0,0,0,34,159,1,0,0,0,36,161,1,0,0,0,38,163,1,0,0,0,40,165,
        1,0,0,0,42,167,1,0,0,0,44,170,1,0,0,0,46,172,1,0,0,0,48,50,3,2,1,
        0,49,48,1,0,0,0,49,50,1,0,0,0,50,52,1,0,0,0,51,53,3,4,2,0,52,51,
        1,0,0,0,52,53,1,0,0,0,53,55,1,0,0,0,54,56,3,8,4,0,55,54,1,0,0,0,
        55,56,1,0,0,0,56,58,1,0,0,0,57,59,3,16,8,0,58,57,1,0,0,0,58,59,1,
        0,0,0,59,61,1,0,0,0,60,62,3,20,10,0,61,60,1,0,0,0,61,62,1,0,0,0,
        62,64,1,0,0,0,63,65,3,24,12,0,64,63,1,0,0,0,64,65,1,0,0,0,65,66,
        1,0,0,0,66,67,3,30,15,0,67,1,1,0,0,0,68,69,5,9,0,0,69,3,1,0,0,0,
        70,72,5,1,0,0,71,70,1,0,0,0,71,72,1,0,0,0,72,73,1,0,0,0,73,74,3,
        6,3,0,74,5,1,0,0,0,75,77,3,36,18,0,76,75,1,0,0,0,76,77,1,0,0,0,77,
        79,1,0,0,0,78,80,3,38,19,0,79,78,1,0,0,0,79,80,1,0,0,0,80,82,1,0,
        0,0,81,83,3,40,20,0,82,81,1,0,0,0,82,83,1,0,0,0,83,85,1,0,0,0,84,
        86,3,42,21,0,85,84,1,0,0,0,85,86,1,0,0,0,86,88,1,0,0,0,87,89,3,44,
        22,0,88,87,1,0,0,0,88,89,1,0,0,0,89,90,1,0,0,0,90,91,3,46,23,0,91,
        7,1,0,0,0,92,94,5,2,0,0,93,95,3,10,5,0,94,93,1,0,0,0,95,96,1,0,0,
        0,96,94,1,0,0,0,96,97,1,0,0,0,97,9,1,0,0,0,98,100,5,7,0,0,99,101,
        3,12,6,0,100,99,1,0,0,0,101,102,1,0,0,0,102,100,1,0,0,0,102,103,
        1,0,0,0,103,11,1,0,0,0,104,105,3,14,7,0,105,13,1,0,0,0,106,107,5,
        8,0,0,107,15,1,0,0,0,108,109,5,3,0,0,109,110,3,18,9,0,110,17,1,0,
        0,0,111,113,5,13,0,0,112,111,1,0,0,0,113,114,1,0,0,0,114,112,1,0,
        0,0,114,115,1,0,0,0,115,19,1,0,0,0,116,117,7,0,0,0,117,118,3,22,
        11,0,118,21,1,0,0,0,119,121,5,13,0,0,120,119,1,0,0,0,121,122,1,0,
        0,0,122,120,1,0,0,0,122,123,1,0,0,0,123,23,1,0,0,0,124,126,5,6,0,
        0,125,127,3,26,13,0,126,125,1,0,0,0,127,128,1,0,0,0,128,126,1,0,
        0,0,128,129,1,0,0,0,129,25,1,0,0,0,130,131,5,10,0,0,131,132,3,28,
        14,0,132,27,1,0,0,0,133,135,5,13,0,0,134,133,1,0,0,0,135,136,1,0,
        0,0,136,134,1,0,0,0,136,137,1,0,0,0,137,29,1,0,0,0,138,139,5,14,
        0,0,139,140,3,32,16,0,140,31,1,0,0,0,141,143,3,34,17,0,142,141,1,
        0,0,0,142,143,1,0,0,0,143,144,1,0,0,0,144,146,3,36,18,0,145,147,
        3,38,19,0,146,145,1,0,0,0,146,147,1,0,0,0,147,149,1,0,0,0,148,150,
        3,40,20,0,149,148,1,0,0,0,149,150,1,0,0,0,150,152,1,0,0,0,151,153,
        3,42,21,0,152,151,1,0,0,0,152,153,1,0,0,0,153,155,1,0,0,0,154,156,
        3,44,22,0,155,154,1,0,0,0,155,156,1,0,0,0,156,157,1,0,0,0,157,158,
        3,46,23,0,158,33,1,0,0,0,159,160,5,16,0,0,160,35,1,0,0,0,161,162,
        5,15,0,0,162,37,1,0,0,0,163,164,5,17,0,0,164,39,1,0,0,0,165,166,
        5,19,0,0,166,41,1,0,0,0,167,168,5,21,0,0,168,169,5,22,0,0,169,43,
        1,0,0,0,170,171,5,18,0,0,171,45,1,0,0,0,172,173,5,23,0,0,173,47,
        1,0,0,0,23,49,52,55,58,61,64,71,76,79,82,85,88,96,102,114,122,128,
        136,142,146,149,152,155
    ]

class DebateGrammarParser ( Parser ):

    grammarFileName = "DebateGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\\u03A0\\u0399\\u039D\\u0391\\u039A\\u0391\\u03A3 \\u03A0\\u0395\\u03A1\\u0399\\u0395\\u03A7\\u039F\\u039C\\u0395\\u039D\\u03A9\\u039D'", 
                     "'\\u0398\\u0395\\u039C\\u0391\\u03A4\\u0391'", "'\\u03A0\\u03A1\\u039F\\u0395\\u0394\\u03A1\\u039F\\u03A3'", 
                     "'\\u03A0\\u03A1\\u039F\\u0395\\u0394\\u03A1\\u0395\\u03A5\\u03A9\\u039D'", 
                     "'\\u03A0\\u03A1\\u039F\\u0395\\u0394\\u03A1\\u0395\\u03A5\\u039F\\u039D\\u03A4\\u0395\\u03A3'", 
                     "'\\u039F\\u039C\\u0399\\u039B\\u0397\\u03A4\\u0395\\u03A3'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "<INVALID>", "<INVALID>", "'.'", "','", "'\\u0027'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "SUBJECT_BASIC_CATEGORY", 
                      "SUBJECT_NUMBER", "SIMIOSI", "SPEAKER_CATEG_DETAIL", 
                      "EPI", "PAREMVASEIS", "NAME", "PRAKTIKA_BOULIS", "PERIODOS", 
                      "ANATH_BOULI", "DIMOKRATIA", "SUNDEDRIASI", "SUNODOS", 
                      "SUNODOS_NUM", "TMIMA_DIAKOPIS", "THEROS", "DATE", 
                      "NUMBER", "NUMBER_WITH_DOT", "LEFT_PARENTHESIS", "RIGHT_PARENTHESIS", 
                      "PAGE", "WORD", "DOT", "COMMA", "TONE", "BIG_GREEK_LETTER", 
                      "SMALL_GREEK_LETTER", "BIG_LETTER", "ROMAN_NUMERAL", 
                      "ROMAN_NUMERAL_SMALL", "ANY_TEXT", "ANY_TEXT_SPACE", 
                      "ANY_TEXT_COMMA", "ANY_TEXT_C", "WS" ]

    RULE_start = 0
    RULE_simiosi = 1
    RULE_table_of_contents = 2
    RULE_periexomena = 3
    RULE_subjects = 4
    RULE_subjects_category = 5
    RULE_subject = 6
    RULE_subject_name_ = 7
    RULE_proedros = 8
    RULE_proedros_list = 9
    RULE_proedreuontes = 10
    RULE_proedreuontes_list = 11
    RULE_speakers = 12
    RULE_speaker_detail = 13
    RULE_speakers_list = 14
    RULE_parliament_proceedings = 15
    RULE_parliament_detail = 16
    RULE_anatheoritiki_bouli = 17
    RULE_period_detail = 18
    RULE_dimokratia = 19
    RULE_sunodos = 20
    RULE_ergasies = 21
    RULE_sunedriasi = 22
    RULE_date = 23

    ruleNames =  [ "start", "simiosi", "table_of_contents", "periexomena", 
                   "subjects", "subjects_category", "subject", "subject_name_", 
                   "proedros", "proedros_list", "proedreuontes", "proedreuontes_list", 
                   "speakers", "speaker_detail", "speakers_list", "parliament_proceedings", 
                   "parliament_detail", "anatheoritiki_bouli", "period_detail", 
                   "dimokratia", "sunodos", "ergasies", "sunedriasi", "date" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    SUBJECT_BASIC_CATEGORY=7
    SUBJECT_NUMBER=8
    SIMIOSI=9
    SPEAKER_CATEG_DETAIL=10
    EPI=11
    PAREMVASEIS=12
    NAME=13
    PRAKTIKA_BOULIS=14
    PERIODOS=15
    ANATH_BOULI=16
    DIMOKRATIA=17
    SUNDEDRIASI=18
    SUNODOS=19
    SUNODOS_NUM=20
    TMIMA_DIAKOPIS=21
    THEROS=22
    DATE=23
    NUMBER=24
    NUMBER_WITH_DOT=25
    LEFT_PARENTHESIS=26
    RIGHT_PARENTHESIS=27
    PAGE=28
    WORD=29
    DOT=30
    COMMA=31
    TONE=32
    BIG_GREEK_LETTER=33
    SMALL_GREEK_LETTER=34
    BIG_LETTER=35
    ROMAN_NUMERAL=36
    ROMAN_NUMERAL_SMALL=37
    ANY_TEXT=38
    ANY_TEXT_SPACE=39
    ANY_TEXT_COMMA=40
    ANY_TEXT_C=41
    WS=42

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parliament_proceedings(self):
            return self.getTypedRuleContext(DebateGrammarParser.Parliament_proceedingsContext,0)


        def simiosi(self):
            return self.getTypedRuleContext(DebateGrammarParser.SimiosiContext,0)


        def table_of_contents(self):
            return self.getTypedRuleContext(DebateGrammarParser.Table_of_contentsContext,0)


        def subjects(self):
            return self.getTypedRuleContext(DebateGrammarParser.SubjectsContext,0)


        def proedros(self):
            return self.getTypedRuleContext(DebateGrammarParser.ProedrosContext,0)


        def proedreuontes(self):
            return self.getTypedRuleContext(DebateGrammarParser.ProedreuontesContext,0)


        def speakers(self):
            return self.getTypedRuleContext(DebateGrammarParser.SpeakersContext,0)


        def getRuleIndex(self):
            return DebateGrammarParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = DebateGrammarParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 48
                self.simiosi()


            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 11436034) != 0):
                self.state = 51
                self.table_of_contents()


            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 54
                self.subjects()


            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 57
                self.proedros()


            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4 or _la==5:
                self.state = 60
                self.proedreuontes()


            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 63
                self.speakers()


            self.state = 66
            self.parliament_proceedings()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SimiosiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SIMIOSI(self):
            return self.getToken(DebateGrammarParser.SIMIOSI, 0)

        def getRuleIndex(self):
            return DebateGrammarParser.RULE_simiosi

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimiosi" ):
                listener.enterSimiosi(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimiosi" ):
                listener.exitSimiosi(self)




    def simiosi(self):

        localctx = DebateGrammarParser.SimiosiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_simiosi)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(DebateGrammarParser.SIMIOSI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Table_of_contentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def periexomena(self):
            return self.getTypedRuleContext(DebateGrammarParser.PeriexomenaContext,0)


        def getRuleIndex(self):
            return DebateGrammarParser.RULE_table_of_contents

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTable_of_contents" ):
                listener.enterTable_of_contents(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTable_of_contents" ):
                listener.exitTable_of_contents(self)




    def table_of_contents(self):

        localctx = DebateGrammarParser.Table_of_contentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_table_of_contents)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 70
                self.match(DebateGrammarParser.T__0)


            self.state = 73
            self.periexomena()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PeriexomenaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def date(self):
            return self.getTypedRuleContext(DebateGrammarParser.DateContext,0)


        def period_detail(self):
            return self.getTypedRuleContext(DebateGrammarParser.Period_detailContext,0)


        def dimokratia(self):
            return self.getTypedRuleContext(DebateGrammarParser.DimokratiaContext,0)


        def sunodos(self):
            return self.getTypedRuleContext(DebateGrammarParser.SunodosContext,0)


        def ergasies(self):
            return self.getTypedRuleContext(DebateGrammarParser.ErgasiesContext,0)


        def sunedriasi(self):
            return self.getTypedRuleContext(DebateGrammarParser.SunedriasiContext,0)


        def getRuleIndex(self):
            return DebateGrammarParser.RULE_periexomena

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeriexomena" ):
                listener.enterPeriexomena(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeriexomena" ):
                listener.exitPeriexomena(self)




    def periexomena(self):

        localctx = DebateGrammarParser.PeriexomenaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_periexomena)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 75
                self.period_detail()


            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 78
                self.dimokratia()


            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 81
                self.sunodos()


            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 84
                self.ergasies()


            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 87
                self.sunedriasi()


            self.state = 90
            self.date()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubjectsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subjects_category(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DebateGrammarParser.Subjects_categoryContext)
            else:
                return self.getTypedRuleContext(DebateGrammarParser.Subjects_categoryContext,i)


        def getRuleIndex(self):
            return DebateGrammarParser.RULE_subjects

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubjects" ):
                listener.enterSubjects(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubjects" ):
                listener.exitSubjects(self)




    def subjects(self):

        localctx = DebateGrammarParser.SubjectsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_subjects)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(DebateGrammarParser.T__1)
            self.state = 94 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 93
                self.subjects_category()
                self.state = 96 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==7):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Subjects_categoryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUBJECT_BASIC_CATEGORY(self):
            return self.getToken(DebateGrammarParser.SUBJECT_BASIC_CATEGORY, 0)

        def subject(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DebateGrammarParser.SubjectContext)
            else:
                return self.getTypedRuleContext(DebateGrammarParser.SubjectContext,i)


        def getRuleIndex(self):
            return DebateGrammarParser.RULE_subjects_category

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubjects_category" ):
                listener.enterSubjects_category(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubjects_category" ):
                listener.exitSubjects_category(self)




    def subjects_category(self):

        localctx = DebateGrammarParser.Subjects_categoryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_subjects_category)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(DebateGrammarParser.SUBJECT_BASIC_CATEGORY)
            self.state = 100 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 99
                self.subject()
                self.state = 102 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==8):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubjectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subject_name_(self):
            return self.getTypedRuleContext(DebateGrammarParser.Subject_name_Context,0)


        def getRuleIndex(self):
            return DebateGrammarParser.RULE_subject

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubject" ):
                listener.enterSubject(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubject" ):
                listener.exitSubject(self)




    def subject(self):

        localctx = DebateGrammarParser.SubjectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_subject)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.subject_name_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Subject_name_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUBJECT_NUMBER(self):
            return self.getToken(DebateGrammarParser.SUBJECT_NUMBER, 0)

        def getRuleIndex(self):
            return DebateGrammarParser.RULE_subject_name_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubject_name_" ):
                listener.enterSubject_name_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubject_name_" ):
                listener.exitSubject_name_(self)




    def subject_name_(self):

        localctx = DebateGrammarParser.Subject_name_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_subject_name_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(DebateGrammarParser.SUBJECT_NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProedrosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def proedros_list(self):
            return self.getTypedRuleContext(DebateGrammarParser.Proedros_listContext,0)


        def getRuleIndex(self):
            return DebateGrammarParser.RULE_proedros

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProedros" ):
                listener.enterProedros(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProedros" ):
                listener.exitProedros(self)




    def proedros(self):

        localctx = DebateGrammarParser.ProedrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_proedros)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(DebateGrammarParser.T__2)
            self.state = 109
            self.proedros_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Proedros_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(DebateGrammarParser.NAME)
            else:
                return self.getToken(DebateGrammarParser.NAME, i)

        def getRuleIndex(self):
            return DebateGrammarParser.RULE_proedros_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProedros_list" ):
                listener.enterProedros_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProedros_list" ):
                listener.exitProedros_list(self)




    def proedros_list(self):

        localctx = DebateGrammarParser.Proedros_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_proedros_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 111
                self.match(DebateGrammarParser.NAME)
                self.state = 114 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==13):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProedreuontesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def proedreuontes_list(self):
            return self.getTypedRuleContext(DebateGrammarParser.Proedreuontes_listContext,0)


        def getRuleIndex(self):
            return DebateGrammarParser.RULE_proedreuontes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProedreuontes" ):
                listener.enterProedreuontes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProedreuontes" ):
                listener.exitProedreuontes(self)




    def proedreuontes(self):

        localctx = DebateGrammarParser.ProedreuontesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_proedreuontes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            _la = self._input.LA(1)
            if not(_la==4 or _la==5):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 117
            self.proedreuontes_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Proedreuontes_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(DebateGrammarParser.NAME)
            else:
                return self.getToken(DebateGrammarParser.NAME, i)

        def getRuleIndex(self):
            return DebateGrammarParser.RULE_proedreuontes_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProedreuontes_list" ):
                listener.enterProedreuontes_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProedreuontes_list" ):
                listener.exitProedreuontes_list(self)




    def proedreuontes_list(self):

        localctx = DebateGrammarParser.Proedreuontes_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_proedreuontes_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 119
                self.match(DebateGrammarParser.NAME)
                self.state = 122 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==13):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SpeakersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def speaker_detail(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DebateGrammarParser.Speaker_detailContext)
            else:
                return self.getTypedRuleContext(DebateGrammarParser.Speaker_detailContext,i)


        def getRuleIndex(self):
            return DebateGrammarParser.RULE_speakers

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpeakers" ):
                listener.enterSpeakers(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpeakers" ):
                listener.exitSpeakers(self)




    def speakers(self):

        localctx = DebateGrammarParser.SpeakersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_speakers)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(DebateGrammarParser.T__5)
            self.state = 126 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 125
                self.speaker_detail()
                self.state = 128 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==10):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Speaker_detailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SPEAKER_CATEG_DETAIL(self):
            return self.getToken(DebateGrammarParser.SPEAKER_CATEG_DETAIL, 0)

        def speakers_list(self):
            return self.getTypedRuleContext(DebateGrammarParser.Speakers_listContext,0)


        def getRuleIndex(self):
            return DebateGrammarParser.RULE_speaker_detail

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpeaker_detail" ):
                listener.enterSpeaker_detail(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpeaker_detail" ):
                listener.exitSpeaker_detail(self)




    def speaker_detail(self):

        localctx = DebateGrammarParser.Speaker_detailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_speaker_detail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(DebateGrammarParser.SPEAKER_CATEG_DETAIL)
            self.state = 131
            self.speakers_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Speakers_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(DebateGrammarParser.NAME)
            else:
                return self.getToken(DebateGrammarParser.NAME, i)

        def getRuleIndex(self):
            return DebateGrammarParser.RULE_speakers_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpeakers_list" ):
                listener.enterSpeakers_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpeakers_list" ):
                listener.exitSpeakers_list(self)




    def speakers_list(self):

        localctx = DebateGrammarParser.Speakers_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_speakers_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 133
                self.match(DebateGrammarParser.NAME)
                self.state = 136 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==13):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parliament_proceedingsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRAKTIKA_BOULIS(self):
            return self.getToken(DebateGrammarParser.PRAKTIKA_BOULIS, 0)

        def parliament_detail(self):
            return self.getTypedRuleContext(DebateGrammarParser.Parliament_detailContext,0)


        def getRuleIndex(self):
            return DebateGrammarParser.RULE_parliament_proceedings

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParliament_proceedings" ):
                listener.enterParliament_proceedings(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParliament_proceedings" ):
                listener.exitParliament_proceedings(self)




    def parliament_proceedings(self):

        localctx = DebateGrammarParser.Parliament_proceedingsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_parliament_proceedings)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(DebateGrammarParser.PRAKTIKA_BOULIS)
            self.state = 139
            self.parliament_detail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parliament_detailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def period_detail(self):
            return self.getTypedRuleContext(DebateGrammarParser.Period_detailContext,0)


        def date(self):
            return self.getTypedRuleContext(DebateGrammarParser.DateContext,0)


        def anatheoritiki_bouli(self):
            return self.getTypedRuleContext(DebateGrammarParser.Anatheoritiki_bouliContext,0)


        def dimokratia(self):
            return self.getTypedRuleContext(DebateGrammarParser.DimokratiaContext,0)


        def sunodos(self):
            return self.getTypedRuleContext(DebateGrammarParser.SunodosContext,0)


        def ergasies(self):
            return self.getTypedRuleContext(DebateGrammarParser.ErgasiesContext,0)


        def sunedriasi(self):
            return self.getTypedRuleContext(DebateGrammarParser.SunedriasiContext,0)


        def getRuleIndex(self):
            return DebateGrammarParser.RULE_parliament_detail

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParliament_detail" ):
                listener.enterParliament_detail(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParliament_detail" ):
                listener.exitParliament_detail(self)




    def parliament_detail(self):

        localctx = DebateGrammarParser.Parliament_detailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_parliament_detail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 141
                self.anatheoritiki_bouli()


            self.state = 144
            self.period_detail()
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 145
                self.dimokratia()


            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 148
                self.sunodos()


            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 151
                self.ergasies()


            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 154
                self.sunedriasi()


            self.state = 157
            self.date()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Anatheoritiki_bouliContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ANATH_BOULI(self):
            return self.getToken(DebateGrammarParser.ANATH_BOULI, 0)

        def getRuleIndex(self):
            return DebateGrammarParser.RULE_anatheoritiki_bouli

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnatheoritiki_bouli" ):
                listener.enterAnatheoritiki_bouli(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnatheoritiki_bouli" ):
                listener.exitAnatheoritiki_bouli(self)




    def anatheoritiki_bouli(self):

        localctx = DebateGrammarParser.Anatheoritiki_bouliContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_anatheoritiki_bouli)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(DebateGrammarParser.ANATH_BOULI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Period_detailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PERIODOS(self):
            return self.getToken(DebateGrammarParser.PERIODOS, 0)

        def getRuleIndex(self):
            return DebateGrammarParser.RULE_period_detail

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeriod_detail" ):
                listener.enterPeriod_detail(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeriod_detail" ):
                listener.exitPeriod_detail(self)




    def period_detail(self):

        localctx = DebateGrammarParser.Period_detailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_period_detail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(DebateGrammarParser.PERIODOS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimokratiaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIMOKRATIA(self):
            return self.getToken(DebateGrammarParser.DIMOKRATIA, 0)

        def getRuleIndex(self):
            return DebateGrammarParser.RULE_dimokratia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDimokratia" ):
                listener.enterDimokratia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDimokratia" ):
                listener.exitDimokratia(self)




    def dimokratia(self):

        localctx = DebateGrammarParser.DimokratiaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_dimokratia)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(DebateGrammarParser.DIMOKRATIA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SunodosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUNODOS(self):
            return self.getToken(DebateGrammarParser.SUNODOS, 0)

        def getRuleIndex(self):
            return DebateGrammarParser.RULE_sunodos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSunodos" ):
                listener.enterSunodos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSunodos" ):
                listener.exitSunodos(self)




    def sunodos(self):

        localctx = DebateGrammarParser.SunodosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_sunodos)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(DebateGrammarParser.SUNODOS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ErgasiesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TMIMA_DIAKOPIS(self):
            return self.getToken(DebateGrammarParser.TMIMA_DIAKOPIS, 0)

        def THEROS(self):
            return self.getToken(DebateGrammarParser.THEROS, 0)

        def getRuleIndex(self):
            return DebateGrammarParser.RULE_ergasies

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterErgasies" ):
                listener.enterErgasies(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitErgasies" ):
                listener.exitErgasies(self)




    def ergasies(self):

        localctx = DebateGrammarParser.ErgasiesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_ergasies)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(DebateGrammarParser.TMIMA_DIAKOPIS)
            self.state = 168
            self.match(DebateGrammarParser.THEROS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SunedriasiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUNDEDRIASI(self):
            return self.getToken(DebateGrammarParser.SUNDEDRIASI, 0)

        def getRuleIndex(self):
            return DebateGrammarParser.RULE_sunedriasi

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSunedriasi" ):
                listener.enterSunedriasi(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSunedriasi" ):
                listener.exitSunedriasi(self)




    def sunedriasi(self):

        localctx = DebateGrammarParser.SunedriasiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_sunedriasi)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(DebateGrammarParser.SUNDEDRIASI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DATE(self):
            return self.getToken(DebateGrammarParser.DATE, 0)

        def getRuleIndex(self):
            return DebateGrammarParser.RULE_date

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDate" ):
                listener.enterDate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDate" ):
                listener.exitDate(self)




    def date(self):

        localctx = DebateGrammarParser.DateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_date)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(DebateGrammarParser.DATE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





