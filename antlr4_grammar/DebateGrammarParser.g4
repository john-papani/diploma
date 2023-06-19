parser grammar DebateGrammarParser;

options {
	tokenVocab = DebateGrammarLexer;
}
start:
	header? simiosi? table_of_contents? subjects? proedreuontes* speakers? parliament_proceedings?;

simiosi: SIMIOSI;

header: sunedriasi;
//------- PERIEXOMENA
table_of_contents:
	(
		PINAKAS_PERIEXOMENON
		| anatheoritiki_bouli
		| period_detail
		| dimokratia
		| sunodos
		| sunedriasi
		| ergasies
		| date
	)+;

// ------- THEMATA
subjects: THEMATA_SPACES sectionContent+;
sectionContent: sbcategory? subject+;
sbcategory: SUBJECT_BASIC_CATEGORY;
subject: SUBJECT_;

// ------- PROEDREUONTES / PROEDROS
proedreuontes: PROEDREUONTES proedreuontes_name+;
proedreuontes_name: NAME;

// ------- SPEAKERS 
speakers: OMILITES speaker_detail+;
speaker_detail: SPEAKER_CATEG_DETAIL? speakers_name+;
speakers_name: NAME;

// ------- PRAKTIKA BOULIS
parliament_proceedings: PRAKTIKA_BOULIS parliament_detail;

parliament_detail:
	anatheoritiki_bouli? period_detail? dimokratia? sunodos? ergasies* sunedriasi? date;

anatheoritiki_bouli: ANATH_BOULI;
period_detail: PERIODOS;
dimokratia: DIMOKRATIA;
sunodos: SUNODOS;
ergasies: TMIMA_DIAKOPIS | THEROS;
sunedriasi: SUNDEDRIASI;
date: DATE;