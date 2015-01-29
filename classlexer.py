#!/usr/bin/env python

import ply.lex as lex
import ply.yacc as yacc

import sys

class Content(object):
    
    def __init__(self):
        self.sentence = ""
        self.glist = []
        
        self.meta = {}
        
        self.ionslist = []
        self.ionsinfo = {}
        self.peaklist = []
        self.inions = -1 # to put at -1 when finish 
        
    def get_right(self):
        if self.inions == -1:
            return self.meta
        else:
            return self.ionsinfo
        

class MGFLexer(object):
    
    def __init__(self):
        self.lexer = lex.lex(module=self)
    
    local_tokens = ['COMP', 'ETAG', 'LOCUS', 'PEPMASS', 'RAWFILE',
    'RAWSCANS', 'RTINSECONDS', 'SEQ', 'TAG', 'TITLE']
    head_tokens = ['CLE', 'COM', 'CUTOUT', 'DB', 'DECOY',
    'ERRORTOLERANT', 'FORMAT', 'FRAMES', 'ITOLU', 'ITOL', 'MASS', 
    'MODS', 'MULTI_SITE_MODS', 'PEP_ISOTOPE_ERROR', 'PFA', 'PRECURSOR',
    'QUANTITATION', 'REPORT', 'REPTYPE', 'SEARCH', 'SEG', 'TAXONOMY',
    'USEREMAIL', 'USERNAME', 'USER', 'BEGIN', 'END', 'IONS']
    head_local_tokens = ['CHARGE', 'INSTRUMENT', 'IT_MODS', 'TOLU',
    'TOL']
    other_tokens = ['EQUAL', 'COMMA',  'CHAR', 'INT', 'FLOAT', 
    'COMMENT', 'AND', 'AUTO', 'CHARGE_VALUE']
    
    tokens = head_tokens+local_tokens+head_local_tokens+other_tokens


#~ /!\ order is important (not greedy)

#~ option only local
    
    def t_COMP(self, t):
        r"COMP"
        return t
    
    def t_ETAG(self, t):
        r"ETAG"
        return t
    
    def t_LOCUS(self, t):
        r"LOCUS"
        return t
    
    def t_PEPMASS(self, t):
        r"PEPMASS"
        return t
    
    def t_RAWFILE(self, t):
        r"RAWFILE"
        return t
    
    def t_RAWSCANS(self, t):
        r"RAWSCANS"
        return t
    
    def t_RTINSECONDS(self, t):
        r"RTINSECONDS"
        return t
    
    def t_SEQ(self, t):
        r"SEQ"
        return t
        
    def t_TAG(self, t):
        r"TAG"
        return t
        
    def t_TITLE(self, t):
        r"TITLE"
        return t
    
#~ option only header
    def t_CLE(self, t):
        r"CLE"
        return t
    
    def t_COM(self, t):
        r"COM"
        return t
    
    def t_CUTOUT(self, t):
        r"CUTOUT"
        return t
    
    def t_DB(self, t):
        r"DB"
        return t

    def t_DECOY(self, t):
        r"DECOY"
        return t
    
    def t_ERRORTOLERANT(self, t):
        r"ERRORTOLERANT"
        return t
    
    def t_FORMAT(self, t):
        r"FORMAT"
        return t
    
    def t_FRAMES(self, t):
        r"FRAMES"
        return t
    
    def t_ITOLU(self, t):
        r"ITOLU"
        return t
    
    def t_ITOL(self, t):
        r"ITOL"
        return t
    
    def t_MASS(self, t):
        r"MASS"
        return t
    
    def t_MODS(self, t):
        r"MODS"
        return t
    
    def t_MULTI_SITE_MODS(self, t):
        r"MULTI_SITE_MODS"
        return t
        
    def t_PEP_ISOTOPE_ERROR(self, t):
        r"PEP_ISOTOPE_ERROR"
        return t
    
    def t_PFA(self, t):
        r"PFA"
        return t
    
    def t_PRECURSOR(self, t):
        r"PRECURSOR"
        return t
    
    def t_QUANTITATION(self, t):
        r"QUANTITATION"
        return t
    
    def t_REPORT(self, t):
        r"REPORT"
        return t
    
    def t_REPTYPE(self, t):
        r"REPTYPE"
        return t
    
    def t_SEARCH(self, t):
        r"SEARCH"
        return t
    
    def t_SEG(self, t):
        r"SEG"
        return t
    
    def t_TAXONOMY(self, t):
        r"TAXONOMY"
        return t
    
    def t_USEREMAIL(self, t):
        r"USEREMAIL"
        return t
    
    def t_USERNAME(self, t):
        r"USERNAME"
        return t
    
    def t_USER(self, t):
        r"USER"
        return t
    
    def t_BEGIN(self, t):
        r"BEGIN"
        return t
    
    def t_END(self, t):
        r"END"
        return t
    
    def t_IONS(self, t):
        r"IONS"
        return t

#~ option header and local
    def t_CHARGE(self, t):
        r"CHARGE"
        return t
    
    def t_INSTRUMENT(self, t):
        r"INSTRUMENT"
        return t
    
    def t_IT_MODS(self, t):
        r"IT_MODS"
        return t
    
    def t_TOLU(self, t):
        r"TOLU"
        return t
    
    def t_TOL(self, t):
        r"TOL"
        return t
    
#~ other tokens 
    def t_EQUAL(self, t):
        r"="
        return t
    
    def t_COMMA(self, t):
        r","
        return t
    
    def t_COMMENT(self, t):
        r"(\#){3}.*"
        return t
    
    def t_CHARGE_VALUE(self, t):
        r"[0-9]+(\+|-)"
        return t
    
    def t_FLOAT(self, t):
        r"-{0,1}[0-9]+\.[0-9]+"
        t.value = float(t.value)
        return t
    
    def t_INT(self, t):
        r"-{0,1}[0-9]+"
        t.value = int(t.value)
        return t
    
    def t_AND(self, t):
        r"and"
        return t
    
    def t_AUTO(self, t):
        r"AUTO"
        return t
    
    def t_CHAR(self, t):
        r"[^,=]"
        return t
    
    t_ignore = '\n\r'

    def t_error(self, t):
        print "ERROR"
        print "Illegal character '%s'" % t.value[0]
        t.lexer.skip(1)
        

    def tokenize(self, data):
        'Debug method!'
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if tok:
                yield tok
            else:
                break

class MGFParser(object):
    
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

    def p_error(self, p):
        print "ERROR"
        print "Syntax error at '%s'" % p.value
        exit(1)

    def in_header(self):
        if self.content.inions != -1:
            raise Exception
        else:
            return True
    
    def in_local(self):
        if self.content.inions != 1:
            raise Exception
        else:
            return True

#~ COMMENT 

    def p_statement_comment(self, p):
        'statement : COMMENT'
        print "COMMENT"
        pass

#~ TERMINAL 

#~ option only header
    def p_statement_cle(self, p):
        'statement : CLE EQUAL sentence'
        self.in_header()
        self.content.meta["cle"] = self.content.sentence
        self.content.sentence = ""
        print "CLE"
    
    def p_statement_com(self, p):
        'statement : COM EQUAL sentence'
        self.in_header()
        self.content.meta["com"] = self.content.sentence
        self.content.sentence = ""
        print "COM"
    
    def p_statement_cutout(self, p):
        'statement : CUTOUT EQUAL list'
        self.in_header()
        self.content.meta["cutout"] = self.content.glist
        self.content.glist = []
        print "CUTOUT"
    
    def p_statement_db(self, p):
        'statement : DB EQUAL sentence'
        self.in_header()
        self.content.meta["db"] = self.content.sentence
        self.content.sentence = ""
        print "DB"
    
    def p_statement_decoy(self, p):
        'statement : DECOY EQUAL INT'
        self.in_header()
        self.content.meta["decoy"] = p[3]
        self.content.sentence = ""
        print "DECOY"
    
    def p_statement_errortolerant(self, p):
        'statement : ERRORTOLERANT EQUAL INT'
        self.in_header()
        self.content.meta["errortolerant"] = p[3]
        self.content.sentence = ""
        print "ERRORTOLERANT"
    
    def p_statement_format(self, p):
        'statement : FORMAT EQUAL sentence'
        self.in_header()
        self.content.meta["format"] = self.content.sentence
        self.content.sentence = ""
        print "FORMAT"
    
    def p_statement_frames(self, p):
        'statement : FRAMES EQUAL list'
        self.in_header()
        self.content.meta["frames"] = self.content.glist
        self.content.glist = []
        print "FRAMES"
    
    def p_statement_itol(self, p):
        '''statement : ITOL EQUAL INT
                     | ITOL EQUAL FLOAT'''
        self.in_header()
        self.content.meta["itol"] = p[3]
        print "ITOL"
    
    def p_statement_itolu(self, p):
        'statement : ITOLU EQUAL sentence'
        self.in_header()
        self.content.meta["itolu"] = self.content.sentence
        self.content.sentence = ""
        print "ITOLU"
    
    def p_statement_mass(self, p):
        'statement : MASS EQUAL sentence'
        self.in_header()
        self.content.meta["mass"] = self.content.sentence
        self.content.sentence = ""
        print "MASS"
    
    def p_statement_mods(self, p):
        'statement : MODS EQUAL sentence'
        self.in_header()
        self.content.meta["mods"] = self.content.sentence
        self.content.sentence = ""
        print "MODS"
        
    def p_statement_multi_site_mods(self, p):
        'statement : MULTI_SITE_MODS EQUAL INT'
        self.in_header()
        self.content.meta["multi_site_mods"] = p[3]
        print "MULTI_SITE_MODS"
    
    def p_statement_pep_isotope_error(self, p):
        'statement : PEP_ISOTOPE_ERROR EQUAL INT'
        self.in_header()
        self.content.meta["pep_isotope_error"] = p[3]
        print "PEP_ISOTOPE_ERROR"
    
    def p_statement_pfa(self, p):
        'statement : PFA EQUAL INT'
        self.in_header()
        self.content.meta["pfa"] = p[3]
        print "PFA"
    
    def p_statement_precursor(self, p):
        'statement : PRECURSOR EQUAL FLOAT'
        self.in_header()
        self.content.meta["precursor"] = p[3]
        print "PRECURSOR"
    
    def p_statement_quantification(self, p):
        'statement : QUANTITATION EQUAL sentence'
        self.in_header()
        self.content.meta["quantitation"] = self.content.sentence
        self.content.sentence = ""
        print "QUANTITATION"
    
    def p_statement_report(self, p):
        '''statement : REPORT EQUAL AUTO
                     | REPORT EQUAL INT'''
        self.in_header()
        self.content.meta["report"] = p[3]
        print "REPORT"
    
    def p_statement_reptype(self, p):
        '''statement : REPTYPE EQUAL sentence'''
        self.in_header()
        self.content.meta["reptype"] = self.content.sentence
        self.content.sentence = ""
        print "REPTYPE"
    
    def p_statement_search(self, p):
        '''statement : SEARCH EQUAL sentence'''
        self.in_header()
        self.content.meta["search"] = self.content.sentence
        self.content.sentence = ""
        print "SEARCH"
    
    def p_statement_seg(self, p):
        '''statement : SEG EQUAL FLOAT'''
        self.in_header()
        self.content.meta["seg"] = p[3]
        print "SEG"
        
    def p_statement_taxonomy(self, p):
        '''statement : TAXONOMY EQUAL sentence'''
        self.in_header()
        self.content.meta["taxonomy"] = self.content.sentence
        self.content.sentence = ""
        print "TAXONOMY"
        
    def p_statement_useremail(self, p):
        '''statement : USEREMAIL EQUAL sentence'''
        self.in_header()
        self.content.meta["email"] = self.content.sentence
        self.content.sentence = ""
        print "USEREMAIL"
    
    def p_statement_username(self, p):
        '''statement : USERNAME EQUAL sentence'''
        self.in_header()
        self.content.meta["username"] = self.content.sentence
        self.content.sentence = ""
        print "USERNAME"
    
    def p_statement_user(self, p):
        '''statement : USER INT EQUAL sentence'''
        self.in_header()
        self.content.meta["user"+str(p[2])] = self.content.sentence
        self.content.sentence = ""
        print "USER"+str(p[2])
        
    def p_statement_begin_ions(self, p):
        '''statement : BEGIN CHAR IONS'''
        self.in_header()
        self.content.inions = 1
        print "BEGIN_IONS"
    
#~ option only local

    def p_statement_end_ions(self, p):
        '''statement : END CHAR IONS'''
        self.in_local()
        self.content.ionsinfo['peaklist'] = self.content.peaklist
        self.content.ionslist.append(self.content.ionsinfo)
        self.content.peaklist = []
        self.content.ionsinfo = {}
        self.content.inions = -1
        print "END_IONS"
    
    def p_statement_comp(self, p):
        '''statement : COMP EQUAL sentence'''
        self.in_local()
        self.content.ionsinfo["comp"] = self.content.sentence
        self.content.sentence = ""
        print "COMP"
    
    def p_statement_etag(self,p):
        'statement : ETAG EQUAL sentence'
        self.in_local()
        self.content.ionsinfo["etag"] = self.content.sentence
        self.content.sentence = ""
        print "ETAG"
    
    def p_statement_locus(self, p):
        'statement : LOCUS EQUAL sentence'
        self.in_local()
        self.content.ionsinfo["locus"] = self.content.sentence
        self.content.sentence = ""
        print "LOCUS"
    
    def p_statement_pepmass(self, p):
        'statement : PEPMASS EQUAL FLOAT'
        self.in_local()
        self.content.ionsinfo["pepmass"] = p[3]
        print "PEPMASS"
    
    def p_statement_rawfile(self, p):
        'statement : RAWFILE EQUAL sentence'
        self.in_local()
        self.content.ionsinfo["rawfile"] = self.content.sentence
        self.content.sentence = ""
        print "RAWFILE"
        
    def p_statement_rawscans(self, p):
        'statement : RAWSCANS EQUAL sentence'
        self.in_local()
        self.content.ionsinfo["rawscans"] = self.content.sentence
        self.content.sentence = ""
        print "RAWSCANS"
    
    def p_statement_rtinseconds(self, p):
        'statement : RTINSECONDS EQUAL sentence'
        self.in_local()
        self.content.ionsinfo["rtinseconds"] = self.content.sentence
        self.content.sentence = ""
        print "RTINSECONDS"
    
    def p_statement_seq(self, p):
        'statement : SEQ EQUAL sentence'
        self.in_local()
        self.content.ionsinfo["seq"] = self.content.sentence
        self.content.sentence = ""
        print "SEQ"
    
    def p_statement_tag(self, p):
        'statement : TAG EQUAL sentence'
        self.in_local()
        self.content.ionsinfo["tag"] = self.content.sentence
        self.content.sentence = ""
        print "TAG"
        
    def p_statement_title(self, p):
        'statement : TITLE EQUAL sentence'
        self.in_local()
        self.content.ionsinfo["title"] = self.content.sentence
        self.content.sentence = ""
        print "TITLE"
        
    def p_statement_peak(self, p):
        '''statement : FLOAT CHAR FLOAT CHAR INT
                     | FLOAT CHAR FLOAT CHAR CHARGE_VALUE
                     | FLOAT CHAR FLOAT'''
        self.in_local()
        if len(p) == 6:
            self.content.peaklist.append((p[1], p[3], p[5]))
        else:
            self.content.peaklist.append((p[1], p[3], 0))
        print "PEAK"
    
#~ option header and local

    def p_statement_charge(self, p):
        'statement : CHARGE EQUAL charges'
        self.content.get_right()["charges"] = self.content.glist
        self.content.glist = []
        print "CHARGE"
    
    def p_statement_instrument(self, p):
        'statement : INSTRUMENT EQUAL sentence'
        self.content.get_right()["instrument"] = self.content.sentence
        self.content.sentence = ""
        print "INSTRUMENT"
    
    def p_statement_it_mods(self, p):
        'statement : IT_MODS EQUAL sentence'
        self.content.get_right()["it_mods"] = self.content.sentence
        self.content.sentence = ""
        print "IT_MODS"
    
    def p_statement_tol(self, p):
        '''statement : TOL EQUAL INT
                     | TOL EQUAL FLOAT'''
        self.content.get_right()["tol"] = p[3]
        print "TOL"
    
    def p_statement_tolu(self, p):
        'statement : TOLU EQUAL sentence'
        self.content.get_right()["tolu"] = self.content.sentence
        self.content.sentence = ""
        print "TOLU"

#~ NON TERMINAL 
    
    
    def p_sentence(self, p):
        '''sentence : CHAR
                    | INT
                    | FLOAT
                    | AND
                    | EQUAL
                    | COMMA
                    | CHARGE_VALUE
                    | CHAR sentence
                    | INT sentence
                    | FLOAT sentence
                    | AND sentence
                    | EQUAL sentence
                    | COMMA sentence
                    | CHARGE_VALUE sentence '''
        self.content.sentence = str(p[1]) + self.content.sentence
        print "sentence"
        
    def p_charges(self, p):
        """charges : CHARGE_VALUE
                   | CHARGE_VALUE CHAR AND CHAR charges
                   | CHARGE_VALUE COMMA CHAR charges
                   | INT
                   | INT CHAR AND CHAR charges
                   | INT COMMA CHAR charges"""
        self.content.glist.append(p[1])
        print "charges"
    
    def p_list(self, p):
        '''list : INT COMMA list
                | INT'''
        self.content.glist.append(p[1])
        print "LIST"
        
def main(argv):
    parser = MGFParser()
    try:
        s = open("temp2.mgf")
    except EOFError:
        pass
    for line in s:
        print line
        parser.parse(line)
    #~ print parser.content.meta
    #~ print parser.content.ionslist

if __name__ == '__main__':
    main(sys.argv)
