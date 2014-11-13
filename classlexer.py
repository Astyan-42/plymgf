#!/usr/bin/env python

import ply.lex as lex
import ply.yacc as yacc

import sys

class Content:
    
    def __init__(self):
        self.meta = { }
        self.meta["charge"] = []
        self.sentence = ""
        self.glist = []

class MGFLexer:
    
    def __init__(self):
        self.lexer = lex.lex(module=self)
    
    head_tokens = ['CLE', 'COM', 'PFA']
    local_tokens = []
    head_local_tokens = ['CHARGE']
    other_tokens = ['EQUAL', 'COMMA',  'CHAR', 'INT', 'COMMENT', 'AND',
    'CHARGE_VALUE']
    
    tokens = head_tokens+local_tokens+head_local_tokens+other_tokens
    
    #~ option only header
    t_CLE = r"((CLE))"
    t_COM = r"((COM))"
    t_PFA = r"((PFA))"
    
    #~ option only local
    
    #~ option header and local
    t_CHARGE = r"((CHARGE))"
    
    #~ other tokens 
    t_EQUAL = r"="
    t_COMMA = r","
    t_CHAR = r"[^=,]"
    t_INT = r"-{0,1}[0-9]+"
    t_COMMENT = r"(\#){3}.*"
    t_AND = r"((and))"
    t_CHARGE_VALUE = r"[0-9]+[+-]{1}"
    
    t_ignore = '\n'

    def t_error(self,t):
        print "Illegal character '%s'" % t.value[0]
        t.lexer.skip(1)
        

    def tokenize(self,data):
        'Debug method!'
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if tok:
                yield tok
            else:
                break

class MGFParser:
    
    def __init__(self):
        self.lexer = MGFLexer()
        self.content = Content()
        self.tokens = self.lexer.tokens
        self.parser = yacc.yacc(module=self,write_tables=0,debug=True)

    def parse(self,data):
        if data:
            return self.parser.parse(data,self.lexer.lexer,0,0,None)
        else:
            return []

    def p_error(self,p):
        print "Syntax error at '%s'" % p.value
        exit(1)

#~ COMMENT 

    def p_statement_comment(self, p):
        'statement : COMMENT'
        print "COMMENT"
        pass

#~ TERMINAL 
    
    def p_statement_cle(self, p):
        'statement : CLE EQUAL sentence'
        self.content.meta["cle"] = self.content.sentence
        self.content.sentence = ""
        print "CLE"
    
    def p_statement_com(self, p):
        'statement : COM EQUAL sentence'
        self.content.meta["com"] = self.content.sentence
        self.content.sentence = ""
        print "COM"
    
    def p_statement_pfa(self, p):
        'statement : PFA EQUAL INT'
        self.content.meta["pfa"] = p[3]
        print "PFA"
        
    def p_statement_charge(self, p):
        'statement : CHARGE EQUAL charges'
        print "CHARGE"
        pass

#~ NON TERMINAL 
    
    def p_sentence(self, p):
        '''sentence : CHAR
                    | CHAR sentence '''
        self.content.sentence = p[1] + self.content.sentence
        print "sentence"
        
    def p_charges_add(self, p):
        """charges : CHARGE_VALUE
                   | CHARGE_VALUE CHAR AND CHAR charges
                   | CHARGE_VALUE COMMA CHAR charges
                   | INT
                   | INT CHAR AND CHAR charges
                   | INT COMMA CHAR charges"""
        self.content.meta["charge"].append(p[1])
        print "charges"
        
def main(argv):
    parser = MGFParser()
    try:
        s = open("temp.mgf")
    except EOFError:
        pass
    for line in s:
        print line
        parser.parse(line)
    print parser.content.meta

if __name__ == '__main__':
    main(sys.argv)
