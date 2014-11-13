import sys
#~ sys.path.insert(0,"../..")

tokens = (
    'AND', 'CHARGE','BEGIN_ION', 'COMMENT', 
    'CHARGE_VALUE', 'INT', 'COM', 'ITOL', 'ITOLU', 'MODS', 'IT_MODS',
    'MASS', 'USERNAME', 'USEREMAIL', 'EMAIL', 'EQUAL', 'CHAR'
    )

literals = ['=']

# Tokens

t_AND = r"and"
t_CHARGE = r"CHARGE"
t_BEGIN_ION = r"BEGIN[ ]ION"
t_COMMENT = r"(\#){3}.*"
t_INT = r"[0-9]+"
t_CHARGE_VALUE = r"[0-9]+[+-]{1}"
t_COM = r"COM"
t_ITOL = r"ITOL"
t_ITOLU = r"ITOLU"
t_MODS = r"MODS"
t_IT_MODS = r"IT_MODS"
t_MASS = r"MASS"
t_USERNAME = r"USERNAME"
t_USEREMAIL = r"USEREMAIL"
t_EMAIL = r"[a-zA-Z0-9.-]*@[a-zA-Z0-9.-]*\.[a-z]{2,3}"
t_EQUAL = "="
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
               | INT
               | INT CHAR AND CHAR charges'''
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
    '''any : INT'''
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
            
            
