# Generated from DebateGrammarParser.g4 by ANTLR 4.12.0
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
        4,1,42,166,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,1,0,3,0,46,8,0,1,0,3,0,49,8,0,1,0,3,0,52,8,0,1,0,
        3,0,55,8,0,1,0,5,0,58,8,0,10,0,12,0,61,9,0,1,0,3,0,64,8,0,1,0,3,
        0,67,8,0,1,1,1,1,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,4,3,81,
        8,3,11,3,12,3,82,1,4,1,4,4,4,87,8,4,11,4,12,4,88,1,5,3,5,92,8,5,
        1,5,4,5,95,8,5,11,5,12,5,96,1,6,1,6,1,7,1,7,1,8,1,8,4,8,105,8,8,
        11,8,12,8,106,1,9,1,9,1,10,1,10,4,10,113,8,10,11,10,12,10,114,1,
        11,3,11,118,8,11,1,11,4,11,121,8,11,11,11,12,11,122,1,12,1,12,1,
        13,1,13,1,13,1,14,3,14,131,8,14,1,14,3,14,134,8,14,1,14,3,14,137,
        8,14,1,14,3,14,140,8,14,1,14,3,14,143,8,14,1,14,3,14,146,8,14,1,
        14,1,14,1,15,1,15,1,16,1,16,1,17,1,17,1,18,1,18,1,19,1,19,3,19,160,
        8,19,1,20,1,20,1,21,1,21,1,21,0,0,22,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,32,34,36,38,40,42,0,0,172,0,45,1,0,0,0,2,68,1,0,0,
        0,4,70,1,0,0,0,6,80,1,0,0,0,8,84,1,0,0,0,10,91,1,0,0,0,12,98,1,0,
        0,0,14,100,1,0,0,0,16,102,1,0,0,0,18,108,1,0,0,0,20,110,1,0,0,0,
        22,117,1,0,0,0,24,124,1,0,0,0,26,126,1,0,0,0,28,130,1,0,0,0,30,149,
        1,0,0,0,32,151,1,0,0,0,34,153,1,0,0,0,36,155,1,0,0,0,38,157,1,0,
        0,0,40,161,1,0,0,0,42,163,1,0,0,0,44,46,3,4,2,0,45,44,1,0,0,0,45,
        46,1,0,0,0,46,48,1,0,0,0,47,49,3,2,1,0,48,47,1,0,0,0,48,49,1,0,0,
        0,49,51,1,0,0,0,50,52,3,6,3,0,51,50,1,0,0,0,51,52,1,0,0,0,52,54,
        1,0,0,0,53,55,3,8,4,0,54,53,1,0,0,0,54,55,1,0,0,0,55,59,1,0,0,0,
        56,58,3,16,8,0,57,56,1,0,0,0,58,61,1,0,0,0,59,57,1,0,0,0,59,60,1,
        0,0,0,60,63,1,0,0,0,61,59,1,0,0,0,62,64,3,20,10,0,63,62,1,0,0,0,
        63,64,1,0,0,0,64,66,1,0,0,0,65,67,3,26,13,0,66,65,1,0,0,0,66,67,
        1,0,0,0,67,1,1,0,0,0,68,69,5,2,0,0,69,3,1,0,0,0,70,71,3,40,20,0,
        71,5,1,0,0,0,72,81,5,3,0,0,73,81,3,30,15,0,74,81,3,32,16,0,75,81,
        3,34,17,0,76,81,3,36,18,0,77,81,3,40,20,0,78,81,3,38,19,0,79,81,
        3,42,21,0,80,72,1,0,0,0,80,73,1,0,0,0,80,74,1,0,0,0,80,75,1,0,0,
        0,80,76,1,0,0,0,80,77,1,0,0,0,80,78,1,0,0,0,80,79,1,0,0,0,81,82,
        1,0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,7,1,0,0,0,84,86,5,4,0,0,85,
        87,3,10,5,0,86,85,1,0,0,0,87,88,1,0,0,0,88,86,1,0,0,0,88,89,1,0,
        0,0,89,9,1,0,0,0,90,92,3,12,6,0,91,90,1,0,0,0,91,92,1,0,0,0,92,94,
        1,0,0,0,93,95,3,14,7,0,94,93,1,0,0,0,95,96,1,0,0,0,96,94,1,0,0,0,
        96,97,1,0,0,0,97,11,1,0,0,0,98,99,5,41,0,0,99,13,1,0,0,0,100,101,
        5,42,0,0,101,15,1,0,0,0,102,104,5,6,0,0,103,105,3,18,9,0,104,103,
        1,0,0,0,105,106,1,0,0,0,106,104,1,0,0,0,106,107,1,0,0,0,107,17,1,
        0,0,0,108,109,5,19,0,0,109,19,1,0,0,0,110,112,5,5,0,0,111,113,3,
        22,11,0,112,111,1,0,0,0,113,114,1,0,0,0,114,112,1,0,0,0,114,115,
        1,0,0,0,115,21,1,0,0,0,116,118,5,7,0,0,117,116,1,0,0,0,117,118,1,
        0,0,0,118,120,1,0,0,0,119,121,3,24,12,0,120,119,1,0,0,0,121,122,
        1,0,0,0,122,120,1,0,0,0,122,123,1,0,0,0,123,23,1,0,0,0,124,125,5,
        19,0,0,125,25,1,0,0,0,126,127,5,10,0,0,127,128,3,28,14,0,128,27,
        1,0,0,0,129,131,3,30,15,0,130,129,1,0,0,0,130,131,1,0,0,0,131,133,
        1,0,0,0,132,134,3,32,16,0,133,132,1,0,0,0,133,134,1,0,0,0,134,136,
        1,0,0,0,135,137,3,34,17,0,136,135,1,0,0,0,136,137,1,0,0,0,137,139,
        1,0,0,0,138,140,3,36,18,0,139,138,1,0,0,0,139,140,1,0,0,0,140,142,
        1,0,0,0,141,143,3,38,19,0,142,141,1,0,0,0,142,143,1,0,0,0,143,145,
        1,0,0,0,144,146,3,40,20,0,145,144,1,0,0,0,145,146,1,0,0,0,146,147,
        1,0,0,0,147,148,3,42,21,0,148,29,1,0,0,0,149,150,5,12,0,0,150,31,
        1,0,0,0,151,152,5,11,0,0,152,33,1,0,0,0,153,154,5,13,0,0,154,35,
        1,0,0,0,155,156,5,15,0,0,156,37,1,0,0,0,157,159,5,17,0,0,158,160,
        5,18,0,0,159,158,1,0,0,0,159,160,1,0,0,0,160,39,1,0,0,0,161,162,
        5,14,0,0,162,41,1,0,0,0,163,164,5,20,0,0,164,43,1,0,0,0,23,45,48,
        51,54,59,63,66,80,82,88,91,96,106,114,117,122,130,133,136,139,142,
        145,159
    ]

class DebateGrammarParser ( Parser ):

    grammarFileName = "DebateGrammarParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "<INVALID>", "<INVALID>", "'.'", "','", "'\\u0027'" ]

    symbolicNames = [ "<INVALID>", "WS", "SIMIOSI", "PINAKAS_PERIEXOMENON", 
                      "THEMATA_SPACES", "OMILITES", "PROEDREUONTES", "SPEAKER_CATEG_DETAIL", 
                      "EPI", "PAREMVASEIS", "PRAKTIKA_BOULIS", "PERIODOS", 
                      "ANATH_BOULI", "DIMOKRATIA", "SUNDEDRIASI", "SUNODOS", 
                      "SUNODOS_NUM", "TMIMA_DIAKOPIS", "THEROS", "NAME", 
                      "DATE", "NUMBER", "NUMBER_WITH_DOT", "LEFT_PARENTHESIS", 
                      "RIGHT_PARENTHESIS", "PAGE", "WORD", "DOT", "COMMA", 
                      "TONE", "BIG_LETTER", "SMALL_GREEK_LETTER", "ROMAN_NUMERAL", 
                      "ROMAN_NUMERAL_SMALL", "ANY_TEXT_DOT", "ANY_TEXT", 
                      "ANY_TEXT_SPACE", "ANY_TEXT_COMMA", "ANY_TEXT_C", 
                      "DASH", "WS1", "SUBJECT_BASIC_CATEGORY", "SUBJECT_" ]

    RULE_start = 0
    RULE_simiosi = 1
    RULE_header = 2
    RULE_table_of_contents = 3
    RULE_subjects = 4
    RULE_sectionContent = 5
    RULE_sbcategory = 6
    RULE_subject = 7
    RULE_proedreuontes = 8
    RULE_proedreuontes_name = 9
    RULE_speakers = 10
    RULE_speaker_detail = 11
    RULE_speakers_name = 12
    RULE_parliament_proceedings = 13
    RULE_parliament_detail = 14
    RULE_anatheoritiki_bouli = 15
    RULE_period_detail = 16
    RULE_dimokratia = 17
    RULE_sunodos = 18
    RULE_ergasies = 19
    RULE_sunedriasi = 20
    RULE_date = 21

    ruleNames =  [ "start", "simiosi", "header", "table_of_contents", "subjects", 
                   "sectionContent", "sbcategory", "subject", "proedreuontes", 
                   "proedreuontes_name", "speakers", "speaker_detail", "speakers_name", 
                   "parliament_proceedings", "parliament_detail", "anatheoritiki_bouli", 
                   "period_detail", "dimokratia", "sunodos", "ergasies", 
                   "sunedriasi", "date" ]

    EOF = Token.EOF
    WS=1
    SIMIOSI=2
    PINAKAS_PERIEXOMENON=3
    THEMATA_SPACES=4
    OMILITES=5
    PROEDREUONTES=6
    SPEAKER_CATEG_DETAIL=7
    EPI=8
    PAREMVASEIS=9
    PRAKTIKA_BOULIS=10
    PERIODOS=11
    ANATH_BOULI=12
    DIMOKRATIA=13
    SUNDEDRIASI=14
    SUNODOS=15
    SUNODOS_NUM=16
    TMIMA_DIAKOPIS=17
    THEROS=18
    NAME=19
    DATE=20
    NUMBER=21
    NUMBER_WITH_DOT=22
    LEFT_PARENTHESIS=23
    RIGHT_PARENTHESIS=24
    PAGE=25
    WORD=26
    DOT=27
    COMMA=28
    TONE=29
    BIG_LETTER=30
    SMALL_GREEK_LETTER=31
    ROMAN_NUMERAL=32
    ROMAN_NUMERAL_SMALL=33
    ANY_TEXT_DOT=34
    ANY_TEXT=35
    ANY_TEXT_SPACE=36
    ANY_TEXT_COMMA=37
    ANY_TEXT_C=38
    DASH=39
    WS1=40
    SUBJECT_BASIC_CATEGORY=41
    SUBJECT_=42

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

        def header(self):
            return self.getTypedRuleContext(DebateGrammarParser.HeaderContext,0)


        def simiosi(self):
            return self.getTypedRuleContext(DebateGrammarParser.SimiosiContext,0)


        def table_of_contents(self):
            return self.getTypedRuleContext(DebateGrammarParser.Table_of_contentsContext,0)


        def subjects(self):
            return self.getTypedRuleContext(DebateGrammarParser.SubjectsContext,0)


        def proedreuontes(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DebateGrammarParser.ProedreuontesContext)
            else:
                return self.getTypedRuleContext(DebateGrammarParser.ProedreuontesContext,i)


        def speakers(self):
            return self.getTypedRuleContext(DebateGrammarParser.SpeakersContext,0)


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
            self.state = 45
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 44
                self.header()


            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 47
                self.simiosi()


            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1243144) != 0):
                self.state = 50
                self.table_of_contents()


            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 53
                self.subjects()


            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 56
                self.proedreuontes()
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 62
                self.speakers()


            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 65
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


    class HeaderContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sunedriasi(self):
            return self.getTypedRuleContext(DebateGrammarParser.SunedriasiContext,0)


        def getRuleIndex(self):
            return DebateGrammarParser.RULE_header

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeader" ):
                listener.enterHeader(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeader" ):
                listener.exitHeader(self)




    def header(self):

        localctx = DebateGrammarParser.HeaderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_header)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.sunedriasi()
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

        def PINAKAS_PERIEXOMENON(self, i:int=None):
            if i is None:
                return self.getTokens(DebateGrammarParser.PINAKAS_PERIEXOMENON)
            else:
                return self.getToken(DebateGrammarParser.PINAKAS_PERIEXOMENON, i)

        def anatheoritiki_bouli(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DebateGrammarParser.Anatheoritiki_bouliContext)
            else:
                return self.getTypedRuleContext(DebateGrammarParser.Anatheoritiki_bouliContext,i)


        def period_detail(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DebateGrammarParser.Period_detailContext)
            else:
                return self.getTypedRuleContext(DebateGrammarParser.Period_detailContext,i)


        def dimokratia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DebateGrammarParser.DimokratiaContext)
            else:
                return self.getTypedRuleContext(DebateGrammarParser.DimokratiaContext,i)


        def sunodos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DebateGrammarParser.SunodosContext)
            else:
                return self.getTypedRuleContext(DebateGrammarParser.SunodosContext,i)


        def sunedriasi(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DebateGrammarParser.SunedriasiContext)
            else:
                return self.getTypedRuleContext(DebateGrammarParser.SunedriasiContext,i)


        def ergasies(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DebateGrammarParser.ErgasiesContext)
            else:
                return self.getTypedRuleContext(DebateGrammarParser.ErgasiesContext,i)


        def date(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DebateGrammarParser.DateContext)
            else:
                return self.getTypedRuleContext(DebateGrammarParser.DateContext,i)


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
        self.enterRule(localctx, 6, self.RULE_table_of_contents)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 80
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3]:
                    self.state = 72
                    self.match(DebateGrammarParser.PINAKAS_PERIEXOMENON)
                    pass
                elif token in [12]:
                    self.state = 73
                    self.anatheoritiki_bouli()
                    pass
                elif token in [11]:
                    self.state = 74
                    self.period_detail()
                    pass
                elif token in [13]:
                    self.state = 75
                    self.dimokratia()
                    pass
                elif token in [15]:
                    self.state = 76
                    self.sunodos()
                    pass
                elif token in [14]:
                    self.state = 77
                    self.sunedriasi()
                    pass
                elif token in [17]:
                    self.state = 78
                    self.ergasies()
                    pass
                elif token in [20]:
                    self.state = 79
                    self.date()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 82 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1243144) != 0)):
                    break

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

        def THEMATA_SPACES(self):
            return self.getToken(DebateGrammarParser.THEMATA_SPACES, 0)

        def sectionContent(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DebateGrammarParser.SectionContentContext)
            else:
                return self.getTypedRuleContext(DebateGrammarParser.SectionContentContext,i)


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
            self.state = 84
            self.match(DebateGrammarParser.THEMATA_SPACES)
            self.state = 86 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 85
                self.sectionContent()
                self.state = 88 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==41 or _la==42):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SectionContentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sbcategory(self):
            return self.getTypedRuleContext(DebateGrammarParser.SbcategoryContext,0)


        def subject(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DebateGrammarParser.SubjectContext)
            else:
                return self.getTypedRuleContext(DebateGrammarParser.SubjectContext,i)


        def getRuleIndex(self):
            return DebateGrammarParser.RULE_sectionContent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSectionContent" ):
                listener.enterSectionContent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSectionContent" ):
                listener.exitSectionContent(self)




    def sectionContent(self):

        localctx = DebateGrammarParser.SectionContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_sectionContent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==41:
                self.state = 90
                self.sbcategory()


            self.state = 94 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 93
                    self.subject()

                else:
                    raise NoViableAltException(self)
                self.state = 96 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SbcategoryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUBJECT_BASIC_CATEGORY(self):
            return self.getToken(DebateGrammarParser.SUBJECT_BASIC_CATEGORY, 0)

        def getRuleIndex(self):
            return DebateGrammarParser.RULE_sbcategory

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSbcategory" ):
                listener.enterSbcategory(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSbcategory" ):
                listener.exitSbcategory(self)




    def sbcategory(self):

        localctx = DebateGrammarParser.SbcategoryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_sbcategory)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(DebateGrammarParser.SUBJECT_BASIC_CATEGORY)
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

        def SUBJECT_(self):
            return self.getToken(DebateGrammarParser.SUBJECT_, 0)

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
        self.enterRule(localctx, 14, self.RULE_subject)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(DebateGrammarParser.SUBJECT_)
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

        def PROEDREUONTES(self):
            return self.getToken(DebateGrammarParser.PROEDREUONTES, 0)

        def proedreuontes_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DebateGrammarParser.Proedreuontes_nameContext)
            else:
                return self.getTypedRuleContext(DebateGrammarParser.Proedreuontes_nameContext,i)


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
        self.enterRule(localctx, 16, self.RULE_proedreuontes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(DebateGrammarParser.PROEDREUONTES)
            self.state = 104 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 103
                self.proedreuontes_name()
                self.state = 106 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==19):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Proedreuontes_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(DebateGrammarParser.NAME, 0)

        def getRuleIndex(self):
            return DebateGrammarParser.RULE_proedreuontes_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProedreuontes_name" ):
                listener.enterProedreuontes_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProedreuontes_name" ):
                listener.exitProedreuontes_name(self)




    def proedreuontes_name(self):

        localctx = DebateGrammarParser.Proedreuontes_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_proedreuontes_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(DebateGrammarParser.NAME)
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

        def OMILITES(self):
            return self.getToken(DebateGrammarParser.OMILITES, 0)

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
        self.enterRule(localctx, 20, self.RULE_speakers)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(DebateGrammarParser.OMILITES)
            self.state = 112 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 111
                self.speaker_detail()
                self.state = 114 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==7 or _la==19):
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

        def speakers_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DebateGrammarParser.Speakers_nameContext)
            else:
                return self.getTypedRuleContext(DebateGrammarParser.Speakers_nameContext,i)


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
        self.enterRule(localctx, 22, self.RULE_speaker_detail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 116
                self.match(DebateGrammarParser.SPEAKER_CATEG_DETAIL)


            self.state = 120 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 119
                    self.speakers_name()

                else:
                    raise NoViableAltException(self)
                self.state = 122 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Speakers_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(DebateGrammarParser.NAME, 0)

        def getRuleIndex(self):
            return DebateGrammarParser.RULE_speakers_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpeakers_name" ):
                listener.enterSpeakers_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpeakers_name" ):
                listener.exitSpeakers_name(self)




    def speakers_name(self):

        localctx = DebateGrammarParser.Speakers_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_speakers_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(DebateGrammarParser.NAME)
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
        self.enterRule(localctx, 26, self.RULE_parliament_proceedings)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(DebateGrammarParser.PRAKTIKA_BOULIS)
            self.state = 127
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

        def date(self):
            return self.getTypedRuleContext(DebateGrammarParser.DateContext,0)


        def anatheoritiki_bouli(self):
            return self.getTypedRuleContext(DebateGrammarParser.Anatheoritiki_bouliContext,0)


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
            return DebateGrammarParser.RULE_parliament_detail

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParliament_detail" ):
                listener.enterParliament_detail(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParliament_detail" ):
                listener.exitParliament_detail(self)




    def parliament_detail(self):

        localctx = DebateGrammarParser.Parliament_detailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_parliament_detail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 129
                self.anatheoritiki_bouli()


            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 132
                self.period_detail()


            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 135
                self.dimokratia()


            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 138
                self.sunodos()


            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 141
                self.ergasies()


            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 144
                self.sunedriasi()


            self.state = 147
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
        self.enterRule(localctx, 30, self.RULE_anatheoritiki_bouli)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
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
        self.enterRule(localctx, 32, self.RULE_period_detail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
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
        self.enterRule(localctx, 34, self.RULE_dimokratia)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
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
        self.enterRule(localctx, 36, self.RULE_sunodos)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
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
        self.enterRule(localctx, 38, self.RULE_ergasies)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(DebateGrammarParser.TMIMA_DIAKOPIS)
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 158
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
        self.enterRule(localctx, 40, self.RULE_sunedriasi)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
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
        self.enterRule(localctx, 42, self.RULE_date)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(DebateGrammarParser.DATE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





