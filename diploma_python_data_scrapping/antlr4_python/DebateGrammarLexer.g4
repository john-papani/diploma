lexer grammar DebateGrammarLexer;
WS: [- \t\r\n]+ -> skip;

SIMIOSI: SPACES ('(Σημείωση:' | '(ΣΗΜΕΙΩΣΗ:') SPACES ANY_TEXT;
PINAKAS_PERIEXOMENON:
	SPACES ('ΠΙΝΑΚΑΣ ΠΕΡΙΕΧΟΜΕΝΩΝ' | 'ΠΙΝΑΚΑΣ ΠΕΡΙΕΧΟΜΕΝΩN') SPACES;

// ------- THEMATA
THEMATA_SPACES: 'ΘΕΜΑΤΑ' SPACES -> pushMode(subjects);

// ------- SPEAKERS

OMILITES: (SPACES 'ΟΜΙΛΗΤΕΣ' SPACES);
PROEDREUONTES: (
		(
			'ΠΡΟΕΔΡΕΥΟΝΤΕΣ'
			| 'ΠΡΕΟΔΡΕΥΟΝΤΕΣ'
			| 'ΠΡΟΕΔΡΕΥΩΝ'
			| 'ΠΡΟΕΔΡΕΥΟΥΣΑ'
			| 'ΠΡΟΕΔΡΟΥΣΑ'
			| 'ΠΡΟΕΔΡΟΣ'
		) SPACES
	);
SPEAKER_CATEG_DETAIL: (
		(
			(
				(
					(
						BIG_LETTER
						| SMALL_GREEK_LETTER
						| NUMBER
						| ROMAN_NUMERAL
					) (DOT | RIGHT_PARENTHESIS)
				)? (PAREMVASEIS | EPI | (ANY_TEXT ':'))
			)
		)
	);
EPI: SPACES ('Επί' | 'ΕΠΙ') SPACES ANY_TEXT;
PAREMVASEIS: SPACES 'ΠΑΡΕΜΒΑΣΕΙΣ:';

// ------------- PRAKTIKA BOULIS
PRAKTIKA_BOULIS:
	SPACES (
		'Π Ρ Α Κ Τ Ι Κ Α' SPACES 'Τ Η Σ' SPACES 'Β Ο Υ Λ Η Σ'
		| 'Π Ρ Α Κ Τ Ι Κ Α' SPACES 'Β Ο Υ Λ Η Σ'
		| 'ΠΡΑΚΤΙΚΑ ΒΟΥΛΗΣ'
		| 'ΠΡΑΚΤΙΚΑ' SPACES 'ΒΟΥΛΗΣ'
		| 'ΠΡΑΚΤΙΚΑ ΤΗΣ ΒΟΥΛΗΣ'
		| 'Π Ρ Α Κ Τ Ι Κ Α    Β Ο Υ Λ Η Σ'
	) SPACES;
PERIODOS:
	SPACES (
		ANY_TEXT_SPACE SPACES 'ΠΕΡΙΟΔΟΣ'
		| 'ΠΕΡΙΟΔΟΣ' SPACES ANY_TEXT_SPACE
		| ANY_TEXT_SPACE SPACES (
			'ΠΕΡΙΟΔΟΣ' SPACES LEFT_PARENTHESIS SPACES (
				'ΠΡΟΕΔΡΕΥΟΜΕΝΗΣ ΔΗΜΟΚΡΑΤΙΑΣ'
				| 'ΠΡΟΕΔΡΕΥΟΜΕΝΗΣ ΚΟΙΝΟΒΟΥΛΕΥΤΙΚΗΣ ΔΗΜΟΚΡΑΤΙΑΣ'
				| 'ΠΡΟΕΔΡΕΟΜΕΝΗΣ ΔΗΜΟΚΡΑΤΙΑΣ'
				| 'ΠΡΟΕΔΡΕΥΜΕΝΗΣ ΔΗΜΟΚΡΑΤΙΑΣ'
				| 'ΠΡΟΕΔΡΕΥΟΜΕΝΗ ΔΗΜΟΚΡΑΤΙΑΣ'
			) SPACES RIGHT_PARENTHESIS
		)
	) SPACES;
ANATH_BOULI: SPACES ANY_TEXT_SPACE ' ΑΝΑΘΕΩΡΗΤΙΚΗ ΒΟΥΛΗ' SPACES;

DIMOKRATIA:
	SPACES (
		'ΠΡΟΕΔΡΕΥΟΜΕΝΗΣ ΚΟΙΝΟΒΟΥΛΕΥΤΙΚΗΣ ΔΗΜΟΚΡΑΤΙΑΣ'
		| 'ΠΡΟΕΔΡΕΟΜΕΝΗΣ ΚΟΙΝΟΒΟΥΛΕΥΤΙΚΗΣ ΔΗΜΟΚΡΑΤΙΑΣ'
		| '(ΠΡΟΕΔΡΕΥΟΜΕΝΗΣ ΔΗΜΟΚΡΑΤΙΑΣ)'
		| 'ΠΡΟΕΔΡΕΥΟ0ΜΕΝΗΣ ΚΟΙΝΟΒΟΥΛΕΥΤΙΚΗΣ ΔΗΜΟΚΡΑΤΙΑΣ'
	) SPACES;
SUNDEDRIASI:
	SPACES (
		'ΣΥΝΕΔΡΙΑΣΗ'
		| 'ΣΥΕΝΔΡΙΑ'
		| 'Συνεδρίαση'
		| 'ΣΥΕΝΔΡΙΑΣΗ'
		| 'Σ Υ Ν Ε Δ Ρ Ι Α Σ Η'
	) SPACES ANY_TEXT? SPACES;

SUNODOS: ('ΣΥΝΟΔΟΣ' | 'Σ Υ Ν Ο Δ Ο Σ' | 'Σ Υ Ν Ο Δ Ο') SPACES SUNODOS_NUM SPACES;
SUNODOS_NUM: ANY_TEXT_SPACE;
TMIMA_DIAKOPIS:
	SPACES (
		'ΤΜΗΜΑ ΔΙΑΚΟΠΗΣ ΕΡΓΑΣΙΩΝ ΤΗΣ ΒΟΥΛΗΣ'
		| 'ΤΜΗΜΑ ΔΙΑΚΟΠΗΣ ΕΡΓΑΣΙΩΝ ΒΟΥΛΗΣ'
		| 'ΤΜΗΜΑ ΔΙΑΚΟΠΗΣ ΕΡΓΑΣΙΩΝ ΤΗΣ  ΒΟΥΛΗΣ'
	) SPACES THEROS?;
THEROS: SPACES ('ΘΕΡΟΥΣ' | 'ΘΕΡΟΣ') SPACES NUMBER+ SPACES;
NAME: (
		WORD
		| ' '
		| DASH
		| '’'
		| DOT
		| RIGHT_PARENTHESIS
		| LEFT_PARENTHESIS
	)+ (COMMA | PAGE)? SPACES;
DATE: ANY_TEXT;

NUMBER: [0-9];
NUMBER_WITH_DOT: [0-9]'.';
LEFT_PARENTHESIS: '(';
RIGHT_PARENTHESIS: ')';
PAGE: SPACES COMMA? SPACES 'σελ' (DOT | COMMA)? SPACES;
WORD: ([\u0386-\u03CE] | [\u0041-\u005A])+;
DOT: '.';
COMMA: ',';
TONE: '\u0027';
BIG_LETTER: [\u0386-\u03A9]| 'ΣΤ';
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
DASH: SPACES '-' SPACES;
fragment SPACES: ' '*;

mode subjects;
WS1: [ \t\r\n]+ -> skip;
SUBJECT_BASIC_CATEGORY: (
		BIG_LETTER (DOT | TONE | RIGHT_PARENTHESIS)
	)? SPACES (
		'ΕΙΔΙΚΑ ΘΕΜΑΤΑ'
		| 'ΚΟΙΝΟΒΟΥΛΕΥΤΙΚΟΣ ΕΛΕΓΧΟΣ'
		| 'ΝΟΜΟΘΕΤΙΚΗ ΕΡΓΑΣΙΑ'
	) SPACES;
EXIT_SUBJECT:
	PROEDREUONTES -> type(PROEDREUONTES), mode(DEFAULT_MODE);
EXIT_SUBJECT1:
	OMILITES -> type(OMILITES), mode(DEFAULT_MODE);
EXIT_SUBJECT2:
	PRAKTIKA_BOULIS -> type(PRAKTIKA_BOULIS), popMode;
SUBJECT_: ANY_TEXT;