grammar DebateGrammar;
start:
	simiosi? table_of_contents? subjects? proedros? proedreuontes? speakers? parliament_proceedings;

simiosi: SIMIOSI;

//------- PERIEXOMENA
table_of_contents: periexomena+;
periexomena:
	'ΠΙΝΑΚΑΣ ΠΕΡΙΕΧΟΜΕΝΩΝ'
	| period_detail
	| dimokratia
	| sunodos
	| sunedriasi
	| ergasies
	| date;

// ------- THEMATA
subjects: THEMATA_SPACES subjects_category+;
subjects_category: SUBJECT_BASIC_CATEGORY? subject+;
THEMATA_SPACES: 'ΘΕΜΑΤΑ' SPACES;
SUBJECT_BASIC_CATEGORY: (
		BIG_LETTER (DOT | TONE | RIGHT_PARENTHESIS)
	)? SPACES (
		'ΕΙΔΙΚΑ ΘΕΜΑΤΑ'
		| 'ΚΟΙΝΟΒΟΥΛΕΥΤΙΚΟΣ ΕΛΕΓΧΟΣ'
		| 'ΝΟΜΟΘΕΤΙΚΗ ΕΡΓΑΣΙΑ'
	) SPACES;
subject: SUBJECT_ | ANY_TEXT;
// // SUBJECT_NUMBER | SUBJECT_GREEK_LETTER | SUBJECT_ROMAN_LETTER | ANY_TEXT; ( subject_name_ |
// subject_main_list_details_greek_ | subject_main_list_details_roman_ |
// subject_main_list_details_withoustarting_ ); subject_name_; subject_main_list_details_greek_:
// SUBJECT_GREEK_LETTER; subject_main_list_details_roman_: SUBJECT_ROMAN_LETTER;
// subject_main_list_details_withoustarting_: ANY_TEXT;

SUBJECT_:
	(
		(
			NUMBER
			| SMALL_GREEK_LETTER
			| ROMAN_NUMERAL_SMALL
			| ROMAN_NUMERAL
		)+ (DOT | RIGHT_PARENTHESIS) SPACES
	) ANY_TEXT;
// SUBJECT_GREEK_LETTER: SMALL_GREEK_LETTER (DOT | RIGHT_PARENTHESIS) SPACES ANY_TEXT;
// SUBJECT_ROMAN_LETTER: ROMAN_NUMERAL_SMALL (DOT | RIGHT_PARENTHESIS) SPACES ANY_TEXT;
// SUBJECT_SXEDIA_NOMON: (WORD | ' ')+ ':' ANY_TEXT+; ASD: ANY_TEXT;

// ------- PROEDROS
proedros: ('ΠΡΟΕΔΡΟΣ' | 'ΠΡΟΕΔΡΕΥΩΝ') proedros_name+;
proedros_name: NAME;

// ------- PROEDREUONTES 
proedreuontes: proedreuontes_ proedreuontes_name+;
proedreuontes_: PROED;
PROED: ( 'ΠΡΟΕΔΡΕΥΟΝΤΕΣ' | 'ΠΡΕΟΔΡΕΥΟΝΤΕΣ') SPACES;
proedreuontes_name: NAME;

// ------- SPEAKERS 
speakers: 'ΟΜΙΛΗΤΕΣ' speaker_detail+;
speaker_detail: SPEAKER_CATEG_DETAIL? speakers_name+;
speakers_name: NAME;

// ------------- PRAKTIKA BOULIS
parliament_proceedings: PRAKTIKA_BOULIS parliament_detail;

parliament_detail:
	anatheoritiki_bouli? period_detail dimokratia? sunodos? ergasies? sunedriasi? date;
// anatheoritiki_bouli |period_detail |dimokratia| sunodos| ergasies| sunedriasi| date;

anatheoritiki_bouli: ANATH_BOULI;

period_detail: PERIODOS;

dimokratia: DIMOKRATIA;

sunodos: SUNODOS;

ergasies: TMIMA_DIAKOPIS THEROS;

sunedriasi: SUNDEDRIASI;

date: DATE;

SIMIOSI: ('(Σημείωση: ' | 'ΣΗΜΕΙΩΣΗ: ') ANY_TEXT;
SPEAKER_CATEG_DETAIL: (
		(BIG_LETTER (DOT | RIGHT_PARENTHESIS))? (
			PAREMVASEIS
			| EPI
		)
	)
	| (BIG_LETTER DOT ANY_TEXT);
EPI: SPACES ('Επί' | 'ΕΠΙ') SPACES ANY_TEXT;
PAREMVASEIS: SPACES 'ΠΑΡΕΜΒΑΣΕΙΣ:';
NAME: ANY_TEXT PAGE SPACES;

PRAKTIKA_BOULIS:
	'Π Ρ Α Κ Τ Ι Κ Α' SPACES 'Τ Η Σ' SPACES 'Β Ο Υ Λ Η Σ'
	| 'Π Ρ Α Κ Τ Ι Κ Α' SPACES 'Β Ο Υ Λ Η Σ'
	| 'ΠΡΑΚΤΙΚΑ ΒΟΥΛΗΣ'
	| 'ΠΡΑΚΤΙΚΑ' SPACES 'ΒΟΥΛΗΣ'
	| 'ΠΡΑΚΤΙΚΑ ΤΗΣ ΒΟΥΛΗΣ';
PERIODOS:
	SPACES (
		ANY_TEXT_SPACE SPACES 'ΠΕΡΙΟΔΟΣ'
		| 'ΠΕΡΙΟΔΟΣ' SPACES ANY_TEXT_SPACE
		| ANY_TEXT_SPACE SPACES (
			'ΠΕΡΙΟΔΟΣ (ΠΡΟΕΔΡΕΥΟΜΕΝΗΣ ΔΗΜΟΚΡΑΤΙΑΣ)'
			| 'ΠΕΡΙΟΔΟΣ (ΠΡΟΕΔΡΕΥΟΜΕΝΗΣ ΚΟΙΝΟΒΟΥΛΕΥΤΙΚΗΣ ΔΗΜΟΚΡΑΤΙΑΣ)'
		)
	) SPACES;
ANATH_BOULI: ANY_TEXT_SPACE ' ΑΝΑΘΕΩΡΗΤΙΚΗ ΒΟΥΛΗ';

DIMOKRATIA:
	'ΠΡΟΕΔΡΕΥΟΜΕΝΗΣ ΚΟΙΝΟΒΟΥΛΕΥΤΙΚΗΣ ΔΗΜΟΚΡΑΤΙΑΣ'
	| 'ΠΡΟΕΔΡΕΟΜΕΝΗΣ ΚΟΙΝΟΒΟΥΛΕΥΤΙΚΗΣ ΔΗΜΟΚΡΑΤΙΑΣ'
	| '(ΠΡΟΕΔΡΕΥΟΜΕΝΗΣ ΔΗΜΟΚΡΑΤΙΑΣ)';
SUNDEDRIASI:
	SPACES (
		'ΣΥΝΕΔΡΙΑΣΗ'
		| 'ΣΥΕΝΔΡΙΑ'
		| 'Συνεδρίαση'
		| 'ΣΥΕΝΔΡΙΑΣΗ'
	) SPACES ANY_TEXT;

SUNODOS: ('ΣΥΝΟΔΟΣ' | 'Σ Υ Ν Ο Δ Ο Σ') SPACES SUNODOS_NUM;
SUNODOS_NUM: ANY_TEXT_SPACE;
TMIMA_DIAKOPIS:
	SPACES 'ΤΜΗΜΑ ΔΙΑΚΟΠΗΣ ΕΡΓΑΣΙΩΝ ΤΗΣ ΒΟΥΛΗΣ' SPACES;
THEROS: SPACES ('ΘΕΡΟΥΣ' | 'ΘΕΡΟΣ') SPACES NUMBER+;
DATE: ANY_TEXT;

NUMBER: [0-9];
NUMBER_WITH_DOT: [0-9]'.';
LEFT_PARENTHESIS: '(';
RIGHT_PARENTHESIS: ')';
PAGE: SPACES COMMA? SPACES 'σελ' (DOT | COMMA)? SPACES;
WORD: [\u0386-\u03CE]+;
DOT: '.';
COMMA: ',';
TONE: '\u0027';
BIG_LETTER: [\u0386-\u03A9]| 'ΣΤ';
//  (' ' | '\t' | '\r' | '\n');
SMALL_GREEK_LETTER: [\u03AC-\u03CE] | 'στ';
ROMAN_NUMERAL:
	(
		'I'
		| 'II'
		| 'III'
		| 'IV'
		| 'V'
		| 'VI'
		| 'VII'
		| 'VIII'
		| 'IX'
		| 'X'
		| 'XI'
		| 'XII'
		| 'XIII'
		| 'XIV'
		| 'XV'
		| 'XVI'
		| 'XVII'
		| 'XVIII'
		| 'XIX'
		| 'XX'
		| 'Ι'
		| 'ΙΙ'
		| 'ΙΙΙ'
	);
ROMAN_NUMERAL_SMALL:
	(
		'i'
		| 'ii'
		| 'iii'
		| 'iv'
		| 'v'
		| 'vi'
		| 'vii'
		| 'viii'
		| 'ix'
		| 'x'
		| 'ι'
		| 'ιι'
		| 'ιιι'
	);
ANY_TEXT_DOT: (~[.\r\n])+;
ANY_TEXT: (~[\r\n])+;
ANY_TEXT_SPACE: (~[ \r\n])+;
ANY_TEXT_COMMA: (~[,\r\n])+;
ANY_TEXT_C: (~[:\r\n])+;

fragment SPACES: ' '*;

WS: [- \t\r\n]+ -> skip;