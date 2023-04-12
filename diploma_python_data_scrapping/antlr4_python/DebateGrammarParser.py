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
        4,1,43,181,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,1,0,3,0,54,
        8,0,1,0,3,0,57,8,0,1,0,3,0,60,8,0,1,0,3,0,63,8,0,1,0,1,0,3,0,67,
        8,0,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,3,3,3,77,8,3,1,3,3,3,80,8,3,1,
        3,3,3,83,8,3,1,3,3,3,86,8,3,1,3,1,3,1,3,1,4,1,4,4,4,93,8,4,11,4,
        12,4,94,1,5,1,5,4,5,99,8,5,11,5,12,5,100,1,6,1,6,1,6,5,6,106,8,6,
        10,6,12,6,109,9,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,10,3,10,120,
        8,10,1,11,4,11,123,8,11,11,11,12,11,124,1,12,1,12,4,12,129,8,12,
        11,12,12,12,130,1,13,1,13,1,13,1,14,4,14,137,8,14,11,14,12,14,138,
        1,15,1,15,1,15,1,16,3,16,145,8,16,1,16,1,16,1,16,1,16,3,16,151,8,
        16,1,16,3,16,154,8,16,1,16,1,16,1,16,1,17,1,17,1,18,1,18,1,19,1,
        19,1,20,1,20,1,21,1,21,1,21,1,22,1,22,1,23,1,23,1,24,1,24,1,25,4,
        25,177,8,25,11,25,12,25,178,1,25,0,0,26,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,0,2,2,0,8,8,39,39,
        2,0,9,9,39,39,175,0,53,1,0,0,0,2,70,1,0,0,0,4,72,1,0,0,0,6,76,1,
        0,0,0,8,90,1,0,0,0,10,96,1,0,0,0,12,102,1,0,0,0,14,110,1,0,0,0,16,
        112,1,0,0,0,18,114,1,0,0,0,20,119,1,0,0,0,22,122,1,0,0,0,24,126,
        1,0,0,0,26,132,1,0,0,0,28,136,1,0,0,0,30,140,1,0,0,0,32,144,1,0,
        0,0,34,158,1,0,0,0,36,160,1,0,0,0,38,162,1,0,0,0,40,164,1,0,0,0,
        42,166,1,0,0,0,44,169,1,0,0,0,46,171,1,0,0,0,48,173,1,0,0,0,50,176,
        1,0,0,0,52,54,3,2,1,0,53,52,1,0,0,0,53,54,1,0,0,0,54,56,1,0,0,0,
        55,57,3,4,2,0,56,55,1,0,0,0,56,57,1,0,0,0,57,59,1,0,0,0,58,60,3,
        8,4,0,59,58,1,0,0,0,59,60,1,0,0,0,60,62,1,0,0,0,61,63,3,20,10,0,
        62,61,1,0,0,0,62,63,1,0,0,0,63,64,1,0,0,0,64,66,3,24,12,0,65,67,
        3,30,15,0,66,65,1,0,0,0,66,67,1,0,0,0,67,68,1,0,0,0,68,69,3,50,25,
        0,69,1,1,0,0,0,70,71,5,6,0,0,71,3,1,0,0,0,72,73,5,1,0,0,73,74,3,
        6,3,0,74,5,1,0,0,0,75,77,3,36,18,0,76,75,1,0,0,0,76,77,1,0,0,0,77,
        79,1,0,0,0,78,80,3,38,19,0,79,78,1,0,0,0,79,80,1,0,0,0,80,82,1,0,
        0,0,81,83,3,40,20,0,82,81,1,0,0,0,82,83,1,0,0,0,83,85,1,0,0,0,84,
        86,3,42,21,0,85,84,1,0,0,0,85,86,1,0,0,0,86,87,1,0,0,0,87,88,3,44,
        22,0,88,89,3,46,23,0,89,7,1,0,0,0,90,92,5,2,0,0,91,93,3,10,5,0,92,
        91,1,0,0,0,93,94,1,0,0,0,94,92,1,0,0,0,94,95,1,0,0,0,95,9,1,0,0,
        0,96,98,5,7,0,0,97,99,3,12,6,0,98,97,1,0,0,0,99,100,1,0,0,0,100,
        98,1,0,0,0,100,101,1,0,0,0,101,11,1,0,0,0,102,107,3,14,7,0,103,106,
        3,16,8,0,104,106,3,18,9,0,105,103,1,0,0,0,105,104,1,0,0,0,106,109,
        1,0,0,0,107,105,1,0,0,0,107,108,1,0,0,0,108,13,1,0,0,0,109,107,1,
        0,0,0,110,111,7,0,0,0,111,15,1,0,0,0,112,113,7,1,0,0,113,17,1,0,
        0,0,114,115,5,10,0,0,115,19,1,0,0,0,116,120,5,3,0,0,117,118,5,4,
        0,0,118,120,3,22,11,0,119,116,1,0,0,0,119,117,1,0,0,0,120,21,1,0,
        0,0,121,123,5,14,0,0,122,121,1,0,0,0,123,124,1,0,0,0,124,122,1,0,
        0,0,124,125,1,0,0,0,125,23,1,0,0,0,126,128,5,5,0,0,127,129,3,26,
        13,0,128,127,1,0,0,0,129,130,1,0,0,0,130,128,1,0,0,0,130,131,1,0,
        0,0,131,25,1,0,0,0,132,133,5,11,0,0,133,134,3,28,14,0,134,27,1,0,
        0,0,135,137,5,14,0,0,136,135,1,0,0,0,137,138,1,0,0,0,138,136,1,0,
        0,0,138,139,1,0,0,0,139,29,1,0,0,0,140,141,5,15,0,0,141,142,3,32,
        16,0,142,31,1,0,0,0,143,145,3,34,17,0,144,143,1,0,0,0,144,145,1,
        0,0,0,145,146,1,0,0,0,146,147,3,36,18,0,147,148,3,38,19,0,148,150,
        3,40,20,0,149,151,3,42,21,0,150,149,1,0,0,0,150,151,1,0,0,0,151,
        153,1,0,0,0,152,154,3,44,22,0,153,152,1,0,0,0,153,154,1,0,0,0,154,
        155,1,0,0,0,155,156,3,46,23,0,156,157,3,48,24,0,157,33,1,0,0,0,158,
        159,5,16,0,0,159,35,1,0,0,0,160,161,5,17,0,0,161,37,1,0,0,0,162,
        163,5,18,0,0,163,39,1,0,0,0,164,165,5,19,0,0,165,41,1,0,0,0,166,
        167,5,21,0,0,167,168,5,22,0,0,168,43,1,0,0,0,169,170,5,23,0,0,170,
        45,1,0,0,0,171,172,5,39,0,0,172,47,1,0,0,0,173,174,5,24,0,0,174,
        49,1,0,0,0,175,177,5,39,0,0,176,175,1,0,0,0,177,178,1,0,0,0,178,
        176,1,0,0,0,178,179,1,0,0,0,179,51,1,0,0,0,21,53,56,59,62,66,76,
        79,82,85,94,100,105,107,119,124,130,138,144,150,153,178
    ]

class DebateGrammarParser ( Parser ):

    grammarFileName = "DebateGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\\u03A0\\u0399\\u039D\\u0391\\u039A\\u0391\\u03A3 \\u03A0\\u0395\\u03A1\\u0399\\u0395\\u03A7\\u039F\\u039C\\u0395\\u039D\\u03A9\\u039D'", 
                     "'\\u0398\\u0395\\u039C\\u0391\\u03A4\\u0391'", "'\\u03A0\\u03A1\\u039F\\u0395\\u0394\\u03A1\\u0395\\u03A5\\u03A9\\u039D'", 
                     "'\\u03A0\\u03A1\\u039F\\u0395\\u0394\\u03A1\\u0395\\u03A5\\u039F\\u039D\\u03A4\\u0395\\u03A3'", 
                     "'\\u039F\\u039C\\u0399\\u039B\\u0397\\u03A4\\u0395\\u03A3'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'('", "')'", "<INVALID>", "<INVALID>", 
                     "'.'", "','", "'\\u0027'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "SIMIOISI", "SUBJECT_MAIN_LIST", 
                      "SUBJECT_NUMBER", "SUBJECT_GREEK_LETTER", "SUBJECT_ROMAN_LETTER", 
                      "SPEAKER_CATEG_DETAIL", "EPI", "PAREMVASEIS", "NAME", 
                      "PRAKTIKA_BOULIS", "ANAT", "PERIODOS", "DIMOKRATIA", 
                      "SUNODOS", "SUNODOS_NUM", "TMIMA_DIAKOPIS", "THEROS", 
                      "SUNDEDRIASI", "PREAMBLE", "NUMBER", "NUMBER_WITH_DOT", 
                      "LEFT_PARENTHESIS", "RIGHT_PARENTHESIS", "PAGE", "WORD", 
                      "DOT", "COMMA", "TONE", "BIG_GREEK_LETTER", "SMALL_GREEK_LETTER", 
                      "BIG_LETTER", "ROMAN_NUMERAL", "ROMAN_NUMERAL_SMALL", 
                      "ANY_TEXT", "ANY_TEXT_WITH_SPACE", "ANY_TEXT_COMMA", 
                      "ANY_TEXT_C", "WS" ]

    RULE_start = 0
    RULE_simiosi = 1
    RULE_table_of_contents = 2
    RULE_periexomena = 3
    RULE_subjects = 4
    RULE_subjects_category = 5
    RULE_subject = 6
    RULE_subject_name_ = 7
    RULE_subject_main_list_details_greek = 8
    RULE_subject_main_list_details_roman = 9
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
    RULE_preamble = 24
    RULE_main_text = 25

    ruleNames =  [ "start", "simiosi", "table_of_contents", "periexomena", 
                   "subjects", "subjects_category", "subject", "subject_name_", 
                   "subject_main_list_details_greek", "subject_main_list_details_roman", 
                   "proedreuontes", "proedreuontes_list", "speakers", "speaker_detail", 
                   "speakers_list", "parliament_proceedings", "parliament_detail", 
                   "anatheoritiki_bouli", "period_detail", "dimokratia", 
                   "sunodos", "ergasies", "sunedriasi", "date", "preamble", 
                   "main_text" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    SIMIOISI=6
    SUBJECT_MAIN_LIST=7
    SUBJECT_NUMBER=8
    SUBJECT_GREEK_LETTER=9
    SUBJECT_ROMAN_LETTER=10
    SPEAKER_CATEG_DETAIL=11
    EPI=12
    PAREMVASEIS=13
    NAME=14
    PRAKTIKA_BOULIS=15
    ANAT=16
    PERIODOS=17
    DIMOKRATIA=18
    SUNODOS=19
    SUNODOS_NUM=20
    TMIMA_DIAKOPIS=21
    THEROS=22
    SUNDEDRIASI=23
    PREAMBLE=24
    NUMBER=25
    NUMBER_WITH_DOT=26
    LEFT_PARENTHESIS=27
    RIGHT_PARENTHESIS=28
    PAGE=29
    WORD=30
    DOT=31
    COMMA=32
    TONE=33
    BIG_GREEK_LETTER=34
    SMALL_GREEK_LETTER=35
    BIG_LETTER=36
    ROMAN_NUMERAL=37
    ROMAN_NUMERAL_SMALL=38
    ANY_TEXT=39
    ANY_TEXT_WITH_SPACE=40
    ANY_TEXT_COMMA=41
    ANY_TEXT_C=42
    WS=43

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

        def speakers(self):
            return self.getTypedRuleContext(DebateGrammarParser.SpeakersContext,0)


        def main_text(self):
            return self.getTypedRuleContext(DebateGrammarParser.Main_textContext,0)


        def simiosi(self):
            return self.getTypedRuleContext(DebateGrammarParser.SimiosiContext,0)


        def table_of_contents(self):
            return self.getTypedRuleContext(DebateGrammarParser.Table_of_contentsContext,0)


        def subjects(self):
            return self.getTypedRuleContext(DebateGrammarParser.SubjectsContext,0)


        def proedreuontes(self):
            return self.getTypedRuleContext(DebateGrammarParser.ProedreuontesContext,0)


        def parliament_proceedings(self):
            return self.getTypedRuleContext(DebateGrammarParser.Parliament_proceedingsContext,0)


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
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 52
                self.simiosi()


            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 55
                self.table_of_contents()


            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 58
                self.subjects()


            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3 or _la==4:
                self.state = 61
                self.proedreuontes()


            self.state = 64
            self.speakers()
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 65
                self.parliament_proceedings()


            self.state = 68
            self.main_text()
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

        def SIMIOISI(self):
            return self.getToken(DebateGrammarParser.SIMIOISI, 0)

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
            self.state = 70
            self.match(DebateGrammarParser.SIMIOISI)
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
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

        def sunedriasi(self):
            return self.getTypedRuleContext(DebateGrammarParser.SunedriasiContext,0)


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
            if _la==17:
                self.state = 75
                self.period_detail()


            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
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


            self.state = 87
            self.sunedriasi()
            self.state = 88
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
            self.state = 90
            self.match(DebateGrammarParser.T__1)
            self.state = 92 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 91
                self.subjects_category()
                self.state = 94 
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

        def SUBJECT_MAIN_LIST(self):
            return self.getToken(DebateGrammarParser.SUBJECT_MAIN_LIST, 0)

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
            self.state = 96
            self.match(DebateGrammarParser.SUBJECT_MAIN_LIST)
            self.state = 98 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 97
                self.subject()
                self.state = 100 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==8 or _la==39):
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


        def subject_main_list_details_greek(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DebateGrammarParser.Subject_main_list_details_greekContext)
            else:
                return self.getTypedRuleContext(DebateGrammarParser.Subject_main_list_details_greekContext,i)


        def subject_main_list_details_roman(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DebateGrammarParser.Subject_main_list_details_romanContext)
            else:
                return self.getTypedRuleContext(DebateGrammarParser.Subject_main_list_details_romanContext,i)


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
            self.state = 102
            self.subject_name_()
            self.state = 107
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 105
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [9, 39]:
                        self.state = 103
                        self.subject_main_list_details_greek()
                        pass
                    elif token in [10]:
                        self.state = 104
                        self.subject_main_list_details_roman()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 109
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

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

        def ANY_TEXT(self):
            return self.getToken(DebateGrammarParser.ANY_TEXT, 0)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            _la = self._input.LA(1)
            if not(_la==8 or _la==39):
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


    class Subject_main_list_details_greekContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUBJECT_GREEK_LETTER(self):
            return self.getToken(DebateGrammarParser.SUBJECT_GREEK_LETTER, 0)

        def ANY_TEXT(self):
            return self.getToken(DebateGrammarParser.ANY_TEXT, 0)

        def getRuleIndex(self):
            return DebateGrammarParser.RULE_subject_main_list_details_greek

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubject_main_list_details_greek" ):
                listener.enterSubject_main_list_details_greek(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubject_main_list_details_greek" ):
                listener.exitSubject_main_list_details_greek(self)




    def subject_main_list_details_greek(self):

        localctx = DebateGrammarParser.Subject_main_list_details_greekContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_subject_main_list_details_greek)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            _la = self._input.LA(1)
            if not(_la==9 or _la==39):
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


    class Subject_main_list_details_romanContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUBJECT_ROMAN_LETTER(self):
            return self.getToken(DebateGrammarParser.SUBJECT_ROMAN_LETTER, 0)

        def getRuleIndex(self):
            return DebateGrammarParser.RULE_subject_main_list_details_roman

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubject_main_list_details_roman" ):
                listener.enterSubject_main_list_details_roman(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubject_main_list_details_roman" ):
                listener.exitSubject_main_list_details_roman(self)




    def subject_main_list_details_roman(self):

        localctx = DebateGrammarParser.Subject_main_list_details_romanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_subject_main_list_details_roman)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(DebateGrammarParser.SUBJECT_ROMAN_LETTER)
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
        try:
            self.state = 119
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 116
                self.match(DebateGrammarParser.T__2)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 117
                self.match(DebateGrammarParser.T__3)
                self.state = 118
                self.proedreuontes_list()
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
            self.state = 122 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 121
                self.match(DebateGrammarParser.NAME)
                self.state = 124 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==14):
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
            self.state = 126
            self.match(DebateGrammarParser.T__4)
            self.state = 128 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 127
                self.speaker_detail()
                self.state = 130 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==11):
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
            self.state = 132
            self.match(DebateGrammarParser.SPEAKER_CATEG_DETAIL)
            self.state = 133
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
            self.state = 136 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 135
                self.match(DebateGrammarParser.NAME)
                self.state = 138 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==14):
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
            self.state = 140
            self.match(DebateGrammarParser.PRAKTIKA_BOULIS)
            self.state = 141
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


        def dimokratia(self):
            return self.getTypedRuleContext(DebateGrammarParser.DimokratiaContext,0)


        def sunodos(self):
            return self.getTypedRuleContext(DebateGrammarParser.SunodosContext,0)


        def date(self):
            return self.getTypedRuleContext(DebateGrammarParser.DateContext,0)


        def preamble(self):
            return self.getTypedRuleContext(DebateGrammarParser.PreambleContext,0)


        def anatheoritiki_bouli(self):
            return self.getTypedRuleContext(DebateGrammarParser.Anatheoritiki_bouliContext,0)


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
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 143
                self.anatheoritiki_bouli()


            self.state = 146
            self.period_detail()
            self.state = 147
            self.dimokratia()
            self.state = 148
            self.sunodos()
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 149
                self.ergasies()


            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 152
                self.sunedriasi()


            self.state = 155
            self.date()
            self.state = 156
            self.preamble()
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

        def ANAT(self):
            return self.getToken(DebateGrammarParser.ANAT, 0)

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
            self.state = 158
            self.match(DebateGrammarParser.ANAT)
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
            self.state = 160
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
            self.state = 162
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
            self.state = 164
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
            self.state = 166
            self.match(DebateGrammarParser.TMIMA_DIAKOPIS)
            self.state = 167
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
            self.state = 169
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

        def ANY_TEXT(self):
            return self.getToken(DebateGrammarParser.ANY_TEXT, 0)

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
            self.state = 171
            self.match(DebateGrammarParser.ANY_TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PreambleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PREAMBLE(self):
            return self.getToken(DebateGrammarParser.PREAMBLE, 0)

        def getRuleIndex(self):
            return DebateGrammarParser.RULE_preamble

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreamble" ):
                listener.enterPreamble(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreamble" ):
                listener.exitPreamble(self)




    def preamble(self):

        localctx = DebateGrammarParser.PreambleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_preamble)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(DebateGrammarParser.PREAMBLE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Main_textContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ANY_TEXT(self, i:int=None):
            if i is None:
                return self.getTokens(DebateGrammarParser.ANY_TEXT)
            else:
                return self.getToken(DebateGrammarParser.ANY_TEXT, i)

        def getRuleIndex(self):
            return DebateGrammarParser.RULE_main_text

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMain_text" ):
                listener.enterMain_text(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMain_text" ):
                listener.exitMain_text(self)




    def main_text(self):

        localctx = DebateGrammarParser.Main_textContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_main_text)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 175
                self.match(DebateGrammarParser.ANY_TEXT)
                self.state = 178 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==39):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





