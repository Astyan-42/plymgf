import sys
#~ sys.path.insert(0,"../..")

tokens = (
    'AND', 'CHARGE','BEGIN_ION', 'COMMENT', 
    'CHARGE_VALUE', 'INT', 'COM', 'ITOL', 'ITOLU', 'MODS', 'IT_MODS',
    'MASS', 'USERNAME', 'USEREMAIL', 'EMAIL', 'EQUAL', 'CHAR',
    'CLE', 'COMMA', 'CUTOUT', 'DB', 'DECOY', 'ERRORTOLERANT', 'FRAMES',
    'INSTRUMENT', 'MULTI_SITE_MODS', 'PEP_ISOTOPE_ERROR',
    'PFA', 'FLOAT', 'PRECURSOR', 'QUANTITATION', 'REPORT', 'AUTO',
    'REPTYPE', 'SEARCH', 'SEG', 'TAXONOMY', 'USER'
    )

#~ literals = ["="]

# Tokens

t_CHARGE = r"CHARGE"
t_BEGIN_ION = r"BEGIN[ ]ION"
t_COM = r"COM"
t_ITOL = r"ITOL"
t_ITOLU = r"ITOLU"
t_MODS = r"MODS"
t_IT_MODS = r"IT_MODS"
t_MASS = r"MASS"
t_USERNAME = r"USERNAME"
t_USEREMAIL = r"USEREMAIL"
t_CLE = r"CLE" 
t_CUTOUT = r"CUTOUT"
t_DB = r"DB"
t_DECOY = r"DECOY"
t_ERRORTOLERANT = r"ERRORTOLERANT"
t_FRAMES = r"FRAMES"
t_INSTRUMENT = r"INSTRUMENT"
t_MULTI_SITE_MODS = r"MULTI_SITE_MODS"
t_PEP_ISOTOPE_ERROR = r"PEP_ISOTOPE_ERROR"
t_PFA = r"PFA"
t_PRECURSOR = r"PRECURSOR"
t_QUANTITATION = r"QUANTITATION"
t_REPORT = r"REPORT"
t_REPTYPE = r"REPTYPE"
t_SEARCH = r"SEARCH"
t_SEG = r"SEG"
t_TAXONOMY = r"TAXONOMY"
t_USER = r"USER"


t_AUTO = r"AUTO"
t_AND = r"and"
t_COMMENT = r"(\#){3}.*"
t_INT = r"-{0,1}[0-9]+"
t_FLOAT = r"-{0,1}[0-9]+\.[0-9]*"
t_CHARGE_VALUE = r"[0-9]+[+-]{1}"
t_EMAIL = r"[a-zA-Z0-9.-]*@[a-zA-Z0-9.-]*\.[a-z]{2,3}"
t_EQUAL = "="
t_COMMA = ","
t_CHAR = r"."

t_ignore = "\t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)
    
# Build the lexer
import ply.lex as lex
lex.lex()

# Parsing rules

#~ precedence = (
    #~ ('right','CHAR'),
    #~ )

inions = -1
sentence = ""
meta = { }
meta["charge"] = []
glist = []
ions = { }

#~ Comment
def p_statement_comment(p):
    'statement : COMMENT'
    print "COMMENT"

#~ charge

def p_statement_charge(p):
    'statement : CHARGE EQUAL charges'
    print "CHARGE"

def p_charges_add(p):
    '''charges : CHARGE_VALUE
               | CHARGE_VALUE CHAR AND CHAR charges
               | CHARGE_VALUE COMMA CHAR charges
               | INT
               | INT CHAR AND CHAR charges
               | INT COMMA CHAR charges'''
    global meta
    global inions
    global ions
    if inions == -1:
        meta["charge"].append(p[1])
    else:
        if len(ions[inions]["charge"]) == 0:
            ions[inions]["charge"] = []
        ions[inions]["charge"].append(p[1])
    print "CHARGES"

#~ useremail
def p_statement_useremail(p):
    'statement : USEREMAIL EQUAL EMAIL'
    global meta
    meta["mail"] = p[3]
    print "MAIL"

#~ username
def p_statement_username(p):
    'statement : USERNAME EQUAL sentence'
    global meta
    global sentence
    meta["username"] = sentence
    sentence = ""
    print "USERNAME"

#~ mass
def p_statement_mass(p):
    'statement : MASS EQUAL sentence'
    global meta
    global sentence
    meta["mass"] = sentence
    sentence = ""
    print "MASS"

#~ mods 
def p_statement_itmods(p):
    'statement : IT_MODS EQUAL sentence'
    global meta
    global sentence
    meta["it_mods"] = sentence
    sentence = ""
    print "IT_MODS"

#~ mods 
def p_statement_mods(p):
    'statement : MODS EQUAL sentence'
    global meta
    global sentence
    meta["mods"] = sentence
    sentence = ""
    print "MODS"

#~ itolu
def p_statement_itolu(p):
    'statement : ITOLU EQUAL sentence'
    global meta
    global sentence
    meta["itolu"] = sentence
    sentence = ""
    print "ITOLU"

#~ itol
def p_statement_itol(p):
    'statement : ITOL EQUAL INT'
    global meta
    meta["itol"] = p[3]
    print "ITOL"

#~ com
def p_statement_com(p):
    'statement : COM EQUAL sentence'
    global meta
    global sentence
    meta["com"] = sentence
    sentence = ""
    print "COM"

#~ cle 
def p_statement_cle(p):
    'statement : CLE EQUAL sentence'
    global meta
    global sentence
    meta["cle"] = sentence
    sentence = ""
    print "CLE"

#~ cutout
def p_statement_cutout(p):
    'statement : CUTOUT EQUAL list'
    global glist
    global meta
    meta["cutout"] = glist
    glist = []
    print "CUTOUT"

#~ DB 
def p_statement_db(p):
    'statement : DB EQUAL sentence'
    global meta
    global sentence
    meta["DB"] = sentence
    sentence = ""
    print "DB"
    
#~ DECOY
def p_statement_decoy(p):
    'statement : DECOY EQUAL INT'
    global meta
    meta["decoy"] = p[3]
    print "DECOY"

#~ ERRORTOLERANT 
def p_statement_errortolerant(p):
    'statement : ERRORTOLERANT EQUAL INT'
    global meta
    meta["errortolerant"] = p[3]
    print "ERRORTOLERANT"

#~ FRAMES 
def p_statement_frames(p):
    'statement : FRAMES EQUAL list'
    global glist
    global meta
    meta["frames"] = glist
    glist = []
    print "FRAMES"

#~ INSTRUMENT
def p_statement_instrument(p):
    'statement : INSTRUMENT EQUAL sentence'
    global meta
    global sentence
    meta["instrument"] = sentence
    sentence = ""
    print "INSTRUMENT"
        
#~ MULTI_SITE_MODS
def p_statement_multisitemods(p):
    'statement : MULTI_SITE_MODS EQUAL INT'
    global meta
    meta["multi_site_mods"] = p[3]
    print "MULTI_SITE_MODS"

#~ PEP_ISOTOPE_ERROR 
def p_statement_pepisotopeerror(p):
    'statement : PEP_ISOTOPE_ERROR EQUAL INT'
    global meta
    meta["pep_isotope_error"] = p[3]
    print "PEP_ISOTOPE_ERROR"

#~ PFA
def p_statement_pfa(p):
    'statement : PFA EQUAL INT'
    global meta
    meta["pfa"] = p[3]
    print "PFA"

#~ PRECURSOR
def p_statement_precursor(p):
    'statement : PRECURSOR EQUAL FLOAT'
    global meta
    meta["precursor"] = p[3]
    print "PRECURSOR"

#~ QUANTITATION
def p_statement_quantification(p):
    'statement : QUANTITATION EQUAL sentence'
    global meta
    global sentence
    meta["quantification"] = sentence
    sentence = ""
    print "QUANTITATION"
    
#~ REPORT 
def p_statement_report(p):
    '''statement : REPORT EQUAL INT
                 | REPORT EQUAL AUTO'''
    global meta
    meta["report"] = p[3]
    print "REPORT"

#~ REPTYPE
def p_statement_reptype(p):
    'statement : REPTYPE EQUAL sentence'
    global meta
    global sentence
    meta["reptype"] = sentence
    sentence = ""
    print "REPTYPE"

#~ SEARCH
def p_statement_search(p):
    'statement : SEARCH EQUAL sentence'
    global meta
    global sentence
    meta["search"] = sentence
    sentence = ""
    print "SEARCH"

#~ SEG
def p_statement_seg(p):
    '''statement : SEG EQUAL INT
                 | SEG EQUAL FLOAT'''
    global meta
    meta["seg"] = p[3]
    print "SEG"

#~ TAXONOMY
def p_statement_taxonomy(p):
    'statement : TAXONOMY EQUAL sentence'
    global meta
    global sentence
    meta["taxonomy"] = sentence
    sentence = ""
    print "TAXONOMY"
    
#~ USER
def p_statement_user(p):
    'statement : USER INT EQUAL sentence'
    global meta
    global sentence
    meta["user"+p[2]] = sentence
    sentence = ""
    print "USER"



#~ list 
def p_list(p):
    '''list : INT COMMA list
            | INT'''
    global glist
    glist.append(p[1])
    print "LIST"

#~ sentence
def p_sentence(p):
    '''sentence : CHAR
                | CHAR sentence
                | any
                | any sentence'''
    global sentence
    sentence = p[1] + sentence
    print "SENTENCE"

#~ any
def p_any(p):
    '''any : INT
           | FLOAT
           | CHARGE_VALUE
           | AND
           | EQUAL
           | COMMA'''
    p[0] = p[1]
    print "ANY"

def p_statement_bion(p):
    'statement : BEGIN_ION'
    print p[1]


def p_error(p):
    print "Syntax error at '%s'" % p.value
    global meta
    print meta
    exit(1)

import ply.yacc as yacc
yacc.yacc()

if __name__ == "__main__":
    try:
        s = open("test.mgf")
    except EOFError:
        pass
    for line in s:
        yacc.parse(line)
    
    print meta

