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
        4,1,43,169,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,1,0,3,0,48,8,0,1,0,3,0,51,8,0,1,0,3,0,54,
        8,0,1,0,3,0,57,8,0,1,0,3,0,60,8,0,1,0,3,0,63,8,0,1,0,3,0,66,8,0,
        1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,4,2,77,8,2,11,2,12,2,78,1,3,
        1,3,4,3,83,8,3,11,3,12,3,84,1,4,3,4,88,8,4,1,4,4,4,91,8,4,11,4,12,
        4,92,1,5,1,5,1,6,1,6,1,7,1,7,4,7,101,8,7,11,7,12,7,102,1,8,1,8,1,
        9,1,9,4,9,109,8,9,11,9,12,9,110,1,10,1,10,1,11,1,11,4,11,117,8,11,
        11,11,12,11,118,1,12,3,12,122,8,12,1,12,4,12,125,8,12,11,12,12,12,
        126,1,13,1,13,1,14,1,14,1,14,1,15,3,15,135,8,15,1,15,3,15,138,8,
        15,1,15,3,15,141,8,15,1,15,3,15,144,8,15,1,15,3,15,147,8,15,1,15,
        3,15,150,8,15,1,15,1,15,1,16,1,16,1,17,1,17,1,18,1,18,1,19,1,19,
        1,20,1,20,1,20,1,21,1,21,1,22,1,22,1,22,0,0,23,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,0,0,173,0,47,1,0,0,
        0,2,67,1,0,0,0,4,76,1,0,0,0,6,80,1,0,0,0,8,87,1,0,0,0,10,94,1,0,
        0,0,12,96,1,0,0,0,14,98,1,0,0,0,16,104,1,0,0,0,18,106,1,0,0,0,20,
        112,1,0,0,0,22,114,1,0,0,0,24,121,1,0,0,0,26,128,1,0,0,0,28,130,
        1,0,0,0,30,134,1,0,0,0,32,153,1,0,0,0,34,155,1,0,0,0,36,157,1,0,
        0,0,38,159,1,0,0,0,40,161,1,0,0,0,42,164,1,0,0,0,44,166,1,0,0,0,
        46,48,3,2,1,0,47,46,1,0,0,0,47,48,1,0,0,0,48,50,1,0,0,0,49,51,3,
        4,2,0,50,49,1,0,0,0,50,51,1,0,0,0,51,53,1,0,0,0,52,54,3,6,3,0,53,
        52,1,0,0,0,53,54,1,0,0,0,54,56,1,0,0,0,55,57,3,14,7,0,56,55,1,0,
        0,0,56,57,1,0,0,0,57,59,1,0,0,0,58,60,3,18,9,0,59,58,1,0,0,0,59,
        60,1,0,0,0,60,62,1,0,0,0,61,63,3,22,11,0,62,61,1,0,0,0,62,63,1,0,
        0,0,63,65,1,0,0,0,64,66,3,28,14,0,65,64,1,0,0,0,65,66,1,0,0,0,66,
        1,1,0,0,0,67,68,5,2,0,0,68,3,1,0,0,0,69,77,5,3,0,0,70,77,3,34,17,
        0,71,77,3,36,18,0,72,77,3,38,19,0,73,77,3,42,21,0,74,77,3,40,20,
        0,75,77,3,44,22,0,76,69,1,0,0,0,76,70,1,0,0,0,76,71,1,0,0,0,76,72,
        1,0,0,0,76,73,1,0,0,0,76,74,1,0,0,0,76,75,1,0,0,0,77,78,1,0,0,0,
        78,76,1,0,0,0,78,79,1,0,0,0,79,5,1,0,0,0,80,82,5,4,0,0,81,83,3,8,
        4,0,82,81,1,0,0,0,83,84,1,0,0,0,84,82,1,0,0,0,84,85,1,0,0,0,85,7,
        1,0,0,0,86,88,3,10,5,0,87,86,1,0,0,0,87,88,1,0,0,0,88,90,1,0,0,0,
        89,91,3,12,6,0,90,89,1,0,0,0,91,92,1,0,0,0,92,90,1,0,0,0,92,93,1,
        0,0,0,93,9,1,0,0,0,94,95,5,42,0,0,95,11,1,0,0,0,96,97,5,43,0,0,97,
        13,1,0,0,0,98,100,5,7,0,0,99,101,3,16,8,0,100,99,1,0,0,0,101,102,
        1,0,0,0,102,100,1,0,0,0,102,103,1,0,0,0,103,15,1,0,0,0,104,105,5,
        20,0,0,105,17,1,0,0,0,106,108,5,6,0,0,107,109,3,20,10,0,108,107,
        1,0,0,0,109,110,1,0,0,0,110,108,1,0,0,0,110,111,1,0,0,0,111,19,1,
        0,0,0,112,113,5,20,0,0,113,21,1,0,0,0,114,116,5,5,0,0,115,117,3,
        24,12,0,116,115,1,0,0,0,117,118,1,0,0,0,118,116,1,0,0,0,118,119,
        1,0,0,0,119,23,1,0,0,0,120,122,5,8,0,0,121,120,1,0,0,0,121,122,1,
        0,0,0,122,124,1,0,0,0,123,125,3,26,13,0,124,123,1,0,0,0,125,126,
        1,0,0,0,126,124,1,0,0,0,126,127,1,0,0,0,127,25,1,0,0,0,128,129,5,
        20,0,0,129,27,1,0,0,0,130,131,5,11,0,0,131,132,3,30,15,0,132,29,
        1,0,0,0,133,135,3,32,16,0,134,133,1,0,0,0,134,135,1,0,0,0,135,137,
        1,0,0,0,136,138,3,34,17,0,137,136,1,0,0,0,137,138,1,0,0,0,138,140,
        1,0,0,0,139,141,3,36,18,0,140,139,1,0,0,0,140,141,1,0,0,0,141,143,
        1,0,0,0,142,144,3,38,19,0,143,142,1,0,0,0,143,144,1,0,0,0,144,146,
        1,0,0,0,145,147,3,40,20,0,146,145,1,0,0,0,146,147,1,0,0,0,147,149,
        1,0,0,0,148,150,3,42,21,0,149,148,1,0,0,0,149,150,1,0,0,0,150,151,
        1,0,0,0,151,152,3,44,22,0,152,31,1,0,0,0,153,154,5,13,0,0,154,33,
        1,0,0,0,155,156,5,12,0,0,156,35,1,0,0,0,157,158,5,14,0,0,158,37,
        1,0,0,0,159,160,5,16,0,0,160,39,1,0,0,0,161,162,5,18,0,0,162,163,
        5,19,0,0,163,41,1,0,0,0,164,165,5,15,0,0,165,43,1,0,0,0,166,167,
        5,21,0,0,167,45,1,0,0,0,23,47,50,53,56,59,62,65,76,78,84,87,92,102,
        110,118,121,126,134,137,140,143,146,149
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
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'('", "')'", "<INVALID>", "<INVALID>", "'.'", "','", 
                     "'\\u0027'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'-'" ]

    symbolicNames = [ "<INVALID>", "WS", "SIMIOSI", "PINAKAS_PERIEXOMENON", 
                      "THEMATA_SPACES", "OMILITES", "PROEDREUONTES", "PROEDROS", 
                      "SPEAKER_CATEG_DETAIL", "EPI", "PAREMVASEIS", "PRAKTIKA_BOULIS", 
                      "PERIODOS", "ANATH_BOULI", "DIMOKRATIA", "SUNDEDRIASI", 
                      "SUNODOS", "SUNODOS_NUM", "TMIMA_DIAKOPIS", "THEROS", 
                      "NAME", "DATE", "NUMBER", "NUMBER_WITH_DOT", "LEFT_PARENTHESIS", 
                      "RIGHT_PARENTHESIS", "PAGE", "WORD", "DOT", "COMMA", 
                      "TONE", "BIG_LETTER", "SMALL_GREEK_LETTER", "ROMAN_NUMERAL", 
                      "ROMAN_NUMERAL_SMALL", "ANY_TEXT_DOT", "ANY_TEXT", 
                      "ANY_TEXT_SPACE", "ANY_TEXT_COMMA", "ANY_TEXT_C", 
                      "DASH", "WS1", "SUBJECT_BASIC_CATEGORY", "SUBJECT_" ]

    RULE_start = 0
    RULE_simiosi = 1
    RULE_table_of_contents = 2
    RULE_subjects = 3
    RULE_sectionContent = 4
    RULE_sbcategory = 5
    RULE_subject = 6
    RULE_proedros = 7
    RULE_proedros_name = 8
    RULE_proedreuontes = 9
    RULE_proedreuontes_name = 10
    RULE_speakers = 11
    RULE_speaker_detail = 12
    RULE_speakers_name = 13
    RULE_parliament_proceedings = 14
    RULE_parliament_detail = 15
    RULE_anatheoritiki_bouli = 16
    RULE_period_detail = 17
    RULE_dimokratia = 18
    RULE_sunodos = 19
    RULE_ergasies = 20
    RULE_sunedriasi = 21
    RULE_date = 22

    ruleNames =  [ "start", "simiosi", "table_of_contents", "subjects", 
                   "sectionContent", "sbcategory", "subject", "proedros", 
                   "proedros_name", "proedreuontes", "proedreuontes_name", 
                   "speakers", "speaker_detail", "speakers_name", "parliament_proceedings", 
                   "parliament_detail", "anatheoritiki_bouli", "period_detail", 
                   "dimokratia", "sunodos", "ergasies", "sunedriasi", "date" ]

    EOF = Token.EOF
    WS=1
    SIMIOSI=2
    PINAKAS_PERIEXOMENON=3
    THEMATA_SPACES=4
    OMILITES=5
    PROEDREUONTES=6
    PROEDROS=7
    SPEAKER_CATEG_DETAIL=8
    EPI=9
    PAREMVASEIS=10
    PRAKTIKA_BOULIS=11
    PERIODOS=12
    ANATH_BOULI=13
    DIMOKRATIA=14
    SUNDEDRIASI=15
    SUNODOS=16
    SUNODOS_NUM=17
    TMIMA_DIAKOPIS=18
    THEROS=19
    NAME=20
    DATE=21
    NUMBER=22
    NUMBER_WITH_DOT=23
    LEFT_PARENTHESIS=24
    RIGHT_PARENTHESIS=25
    PAGE=26
    WORD=27
    DOT=28
    COMMA=29
    TONE=30
    BIG_LETTER=31
    SMALL_GREEK_LETTER=32
    ROMAN_NUMERAL=33
    ROMAN_NUMERAL_SMALL=34
    ANY_TEXT_DOT=35
    ANY_TEXT=36
    ANY_TEXT_SPACE=37
    ANY_TEXT_COMMA=38
    ANY_TEXT_C=39
    DASH=40
    WS1=41
    SUBJECT_BASIC_CATEGORY=42
    SUBJECT_=43

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
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 46
                self.simiosi()


            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2478088) != 0):
                self.state = 49
                self.table_of_contents()


            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 52
                self.subjects()


            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 55
                self.proedros()


            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 58
                self.proedreuontes()


            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 61
                self.speakers()


            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 64
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
            self.state = 67
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

        def PINAKAS_PERIEXOMENON(self, i:int=None):
            if i is None:
                return self.getTokens(DebateGrammarParser.PINAKAS_PERIEXOMENON)
            else:
                return self.getToken(DebateGrammarParser.PINAKAS_PERIEXOMENON, i)

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
        self.enterRule(localctx, 4, self.RULE_table_of_contents)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 76
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3]:
                    self.state = 69
                    self.match(DebateGrammarParser.PINAKAS_PERIEXOMENON)
                    pass
                elif token in [12]:
                    self.state = 70
                    self.period_detail()
                    pass
                elif token in [14]:
                    self.state = 71
                    self.dimokratia()
                    pass
                elif token in [16]:
                    self.state = 72
                    self.sunodos()
                    pass
                elif token in [15]:
                    self.state = 73
                    self.sunedriasi()
                    pass
                elif token in [18]:
                    self.state = 74
                    self.ergasies()
                    pass
                elif token in [21]:
                    self.state = 75
                    self.date()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 78 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2478088) != 0)):
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
        self.enterRule(localctx, 6, self.RULE_subjects)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(DebateGrammarParser.THEMATA_SPACES)
            self.state = 82 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 81
                self.sectionContent()
                self.state = 84 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==42 or _la==43):
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
        self.enterRule(localctx, 8, self.RULE_sectionContent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==42:
                self.state = 86
                self.sbcategory()


            self.state = 90 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 89
                    self.subject()

                else:
                    raise NoViableAltException(self)
                self.state = 92 
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
        self.enterRule(localctx, 10, self.RULE_sbcategory)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
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
        self.enterRule(localctx, 12, self.RULE_subject)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(DebateGrammarParser.SUBJECT_)
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

        def PROEDROS(self):
            return self.getToken(DebateGrammarParser.PROEDROS, 0)

        def proedros_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DebateGrammarParser.Proedros_nameContext)
            else:
                return self.getTypedRuleContext(DebateGrammarParser.Proedros_nameContext,i)


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
        self.enterRule(localctx, 14, self.RULE_proedros)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(DebateGrammarParser.PROEDROS)
            self.state = 100 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 99
                self.proedros_name()
                self.state = 102 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==20):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Proedros_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(DebateGrammarParser.NAME, 0)

        def getRuleIndex(self):
            return DebateGrammarParser.RULE_proedros_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProedros_name" ):
                listener.enterProedros_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProedros_name" ):
                listener.exitProedros_name(self)




    def proedros_name(self):

        localctx = DebateGrammarParser.Proedros_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_proedros_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(DebateGrammarParser.NAME)
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
        self.enterRule(localctx, 18, self.RULE_proedreuontes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(DebateGrammarParser.PROEDREUONTES)
            self.state = 108 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 107
                self.proedreuontes_name()
                self.state = 110 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==20):
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
        self.enterRule(localctx, 20, self.RULE_proedreuontes_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
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
        self.enterRule(localctx, 22, self.RULE_speakers)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(DebateGrammarParser.OMILITES)
            self.state = 116 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 115
                self.speaker_detail()
                self.state = 118 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==8 or _la==20):
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
        self.enterRule(localctx, 24, self.RULE_speaker_detail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 120
                self.match(DebateGrammarParser.SPEAKER_CATEG_DETAIL)


            self.state = 124 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 123
                    self.speakers_name()

                else:
                    raise NoViableAltException(self)
                self.state = 126 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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
        self.enterRule(localctx, 26, self.RULE_speakers_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
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
        self.enterRule(localctx, 28, self.RULE_parliament_proceedings)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(DebateGrammarParser.PRAKTIKA_BOULIS)
            self.state = 131
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
        self.enterRule(localctx, 30, self.RULE_parliament_detail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 133
                self.anatheoritiki_bouli()


            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 136
                self.period_detail()


            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 139
                self.dimokratia()


            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 142
                self.sunodos()


            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 145
                self.ergasies()


            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 148
                self.sunedriasi()


            self.state = 151
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
        self.enterRule(localctx, 32, self.RULE_anatheoritiki_bouli)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
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
        self.enterRule(localctx, 34, self.RULE_period_detail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
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
        self.enterRule(localctx, 36, self.RULE_dimokratia)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
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
        self.enterRule(localctx, 38, self.RULE_sunodos)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
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
        self.enterRule(localctx, 40, self.RULE_ergasies)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(DebateGrammarParser.TMIMA_DIAKOPIS)
            self.state = 162
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
        self.enterRule(localctx, 42, self.RULE_sunedriasi)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
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
        self.enterRule(localctx, 44, self.RULE_date)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(DebateGrammarParser.DATE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





