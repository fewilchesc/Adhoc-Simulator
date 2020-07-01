import ply.lex as lex 
import re
import os
import codecs
import sys

reserved =['RUN','FIN','SI','ENTONCES','MIENTRAS','HACER','VAR',
 			'CONST','LLAMAR','FUNCION'
]

tokens = ['ID','NUMERO','MAS','MENOS','MULT','DIVIDIR',
		'PAR','ASIGNAR','DIFERENTE','MENOR','MENORIGUAL',
		'MAYOR','MAYORIGUAL','LPARENT','RPARENT','COMA',
		'PUNTOYCOMA','ACTUAL'
]

tokens = tokens+reserved

t_ignore= '\t'
t_MAS = r'\+'
t_MENOS = r'\-'
t_MULT = r'\*'
t_DIVIDIR = r'/'
t_PAR = r'PAR'
t_ASIGNAR = r'='
t_DIFERENTE = r'!='
t_MENOR = r'<'
t_MENORIGUAL = r'<='
t_MAYOR = r'>'
t_MAYORIGUAL = r'>='
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_COMA = r','
t_PUNTOYCOMA = r';'
t_ACTUAL = r':='

def t_ID(t):
	r'[a-zA-Z][a-zA-Z0-9_]*'
	if t.value.upper() in reserved:
		t.value = t.value.upper()
		t.type = t.value
	return t	

def t_NUEVALINEA(t):
	r'\n+'
	pass

def t_COMENTARIO(t):
	r'//.*'
	pass

def t_NUMERO(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_ccode_nonspace(t):
  	r'\s+'
  	pass

def t_error(t):
 	print ("Caracter ilegal '%s'" % t.value[0])
 	t.lexer.skip(1)

# directorio = 'C:\\Users\\user\\Desktop\\Lenguajes\\Proyecto\\test\\prueba3.wil'
# test = directorio
# fp = codecs.open(test,"r","utf-8")
# cadena = fp.read()
# fp.close()

analizador = lex.lex()

# analizador.input(cadena)



# while True:
#  	tok = analizador.token()
#  	if not tok : break
#  	print (tok)
