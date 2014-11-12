# -----------------------------------------------------------------------------
# calc.py
#
# A simple calculator with variables.   This is from O'Reilly's
# "Lex and Yacc", p. 63.
# -----------------------------------------------------------------------------

import sys
#~ sys.path.insert(0,"../..")

tokens = (
    'AND', 'CHARGE','BEGIN_ION', 'COMMENT', 
    'CHARGE_VALUE', 'COM', 'ITOL', 'ITOLU', 'MODS', 'IT_MODS',
    'MASS', 'USERNAME', 'USEREMAIL', 'EMAIL', 'WORD'
    )

literals = ['=']

# Tokens

t_AND = r"and"
t_CHARGE = r"CHARGE"
t_BEGIN_ION = r"BEGIN[ ]ION"
t_COMMENT = r"(\#){3}.*"
t_CHARGE_VALUE = r"[0-9]+[+-]{0,1}"
t_COM = r"COM"
t_ITOL = r"ITOL"
t_ITOLU = r"ITOLU"
t_MODS = r"MODS"
t_IT_MODS = r"IT_MODS"
t_MASS = r"MASS"
t_USERNAME = r"USERNAME"
t_USEREMAIL = r"USEREMAIL"
t_EMAIL = r"[a-zA-Z0-9.-]*@[a-zA-Z0-9.-]*\.[a-z]{2,3}"
t_WORD = r"(Lou|Scene)"

t_ignore = " \t"

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
    #~ ('left','+','-'),
    #~ ('left','*','/'),
    #~ ('right','UMINUS'),
    #~ )

inions = -1
meta = { }
meta["charge"] = []
meta["username"] = ""
ions = { }

def p_statement_charge(p):
    'statement : CHARGE "=" charges'
    print "CHARGE"

def p_charges_add(p):
    '''charges : CHARGE_VALUE
               | CHARGE_VALUE AND charges'''
    if inions == -1:
        meta["charge"].append(p[1])
    else:
        if len(ions[inions]["charge"]) == 0:
            ions[inions]["charge"] = []
        ions[inions]["charge"].append(p[1])
    print "CHARGES"

def p_statement_useremail(p):
    'statement : USEREMAIL "=" EMAIL'
    meta["mail"] = p[3]
    print "MAIL"

def p_statement_username(p):
    'statement : USERNAME "=" sentence'
    print "USERNAME"

def p_sentence(p):
    '''sentence : WORD
                | WORD sentence'''
    meta['username'] = p[1] + " " + meta['username']
    print "SENTENCE"

def p_statement_bion(p):
    'statement : BEGIN_ION'
    print p[1]

def p_statement_comment(p):
    'statement : COMMENT'
    print "COMMENT"

def p_error(p):
    print "Syntax error at '%s'" % p.value
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
            
            
