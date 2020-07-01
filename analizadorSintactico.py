import ply.yacc as yacc
import os
import codecs
import re
from analizadorLexico import tokens
from sys import stdin
#from analizadorSemantico import *

precedence = (
	('left','ID','LLAMAR','RUN','SI','MIENTRAS'),
	('left','FUNCION'),
	('left','VAR'),
	('right','ASIGNAR'),
	('right','ACTUAL'),
	('left','DIFERENTE'),
	('left','MENOR','MENORIGUAL','MAYOR','MAYORIGUAL'),
	('left','MAS','MENOS'),
	('left','MULT','DIVIDIR'),
	('right','PAR'),
	('left','LPARENT','RPARENT'),
	)


	  
def p_program(p):
	'''program : block'''
	archi1=open("datos.txt","a",encoding="utf-8") 
	archi1.write("program\n")
	archi1.close()
	print("program")
	#p[0]=program(p[1],"program")

def p_block(p):
	'''block : constDecl varDecl FunDecl statement'''
	archi1=open("datos.txt","a",encoding="utf-8") 
	archi1.write("block\n")
	archi1.close()
	print("block")
	#p[0] = block(p[1],p[2],p[3],p[4],"block")

def p_constDecl(p):
	'''constDecl : CONST constlist PUNTOYCOMA'''
	archi1=open("datos.txt","a",encoding="utf-8") 
	archi1.write("constDecl\n")
	archi1.close()
	print("constDecl")
	#p[0] = constDecl(p[2],"constDecl")

def p_const_DeclEmpty(p):
	'''constDecl : vacio'''	
	archi1=open("datos.txt","a",encoding="utf-8") 
	archi1.write("DeclEmpty\n")
	archi1.close()
	print("nulo")
	#p[0] = Null()

def p_constlist1(p):
	'''constlist : ID ASIGNAR NUMERO'''
	archi1=open("datos.txt","a",encoding="utf-8") 
	archi1.write("constlist1\n")
	archi1.close()
	print("constlist 1")
	#p[0] = constList1(ID(p[1]),ASIGNAR(p[2]),NUMERO(p[3]),"constList1")

def p_constlist2(p):
	'''constlist : constlist COMA ID ASIGNAR NUMERO'''
	archi1=open("datos.txt","a",encoding="utf-8") 
	archi1.write("constlist2\n")
	archi1.close()
	print("constlist 2")
	#p[0] = constList2(p[1],ID(p[3]),ASIGNAR(p[4]),NUMERO(p[5]),"constList2")

def p_varDecl1(p):
	'''varDecl : VAR identList PUNTOYCOMA'''
	archi1=open("datos.txt","a",encoding="utf-8") 
	archi1.write("varDecl1\n")
	archi1.close()
	print("v ")
	#p[0] = varDecl1(p[2],"VarDecl1")

def p_varDeclVacio(p):
	'''varDecl : vacio'''
	archi1=open("datos.txt","a",encoding="utf-8") 
	archi1.write("varDeclVacio\n")
	archi1.close()
	print("nulo")
	#p[0] = Null()

def p_identList1(p):
	'''identList : ID'''
	archi1=open("datos.txt","a",encoding="utf-8") 
	archi1.write("identList1\n")
	archi1.close()
	print("identList 1")	
	#p[0] = identList1(ID(p[1]),"identList1")

def p_identList2(p):
	'''identList : identList COMA ID'''
	archi1=open("datos.txt","a",encoding="utf-8") 
	archi1.write("identList2\n")
	archi1.close()
	print("identList 2")
	#p[0] = identList2(p[1],ID(p[3]),"identList2")

def p_FunDecl1(p):
	'''FunDecl : FunDecl FUNCION ID PUNTOYCOMA block PUNTOYCOMA'''
	archi1=open("datos.txt","a",encoding="utf-8") 
	archi1.write("FunDecl1\n")
	archi1.close()
	print("FunDecl 1")
	#p[0] = FunDecl1(p[1],ID(p[3]),p[5],"FunDecl1")


def p_FunDeclVacio(p):
	'''FunDecl : vacio'''
	archi1=open("datos.txt","a",encoding="utf-8") 
	archi1.write("FunDeclVacio\n")
	archi1.close()
	print("nulo")
	#p[0] = Null()

def p_statement1(p):
	'''statement : ID ACTUAL expr'''
	archi1=open("datos.txt","a",encoding="utf-8") 
	archi1.write("statement1\n")
	archi1.close()
	print("statement 1")
	#p[0] = statement1(ID(p[1]),ACTUAL(p[2]),p[3],"statement1")


def p_statement2(p):
	'''statement : LLAMAR ID'''
	archi1=open("datos.txt","a",encoding="utf-8") 
	archi1.write("statement2\n")
	archi1.close()
	print("statement 2")
	#p[0] = statement2(ID(p[2]),"statement2")

def p_statement3(p):
	'''statement : RUN statementList FIN'''
	archi1=open("datos.txt","a",encoding="utf-8") 
	archi1.write("statement3\n")
	archi1.close()
	print("statement 3")
	#p[0] = statement3(p[2],"statement3")

def p_statement4(p):
	'''statement : SI condition ENTONCES statement'''
	archi1=open("datos.txt","a",encoding="utf-8") 
	archi1.write("statement4\n")
	archi1.close()
	print("statement 4")
	#p[0] = statement4(p[2],p[4],"statement4")

def p_statement5(p):
	'''statement : MIENTRAS condition HACER statement PUNTOYCOMA'''
	archi1=open("datos.txt","a",encoding="utf-8") 
	archi1.write("statement5\n")
	archi1.close()
	print("statement 5")
	#p[0] = statement5(p[2],p[4],"statement5")

def p_statementVacio(p):
	'''statement : vacio'''
	archi1=open("datos.txt","a",encoding="utf-8") 
	archi1.write("statamentVacio\n")
	archi1.close()
	print("nulo")
	#p[0] = Null()

def p_statementList1(p):
	'''statementList : statement'''	
	archi1=open("datos.txt","a",encoding="utf-8") 
	archi1.write("statementList1\n")
	archi1.close()
	print("statementList 1")	
	#p[0] = statementList1(p[1],"statementList1")

def p_statementList2(p):
	'''statementList : statement PUNTOYCOMA statement'''
	archi1=open("datos.txt","a",encoding="utf-8") 
	archi1.write("statementList2\n")
	archi1.close()
	print("statementList 2")
	#p[0] = statementList2(p[1],p[3],"statementList2")

def p_condition1(p):
	'''condition : PAR expr'''
	archi1=open("datos.txt","a",encoding="utf-8") 
	archi1.write("condition1\n")
	archi1.close()
	print("condition 1")
	#p[0] = condition1(p[2],"condition1")

def p_condition2(p):
	'''condition : expr relacion expr'''
	archi1=open("datos.txt","a",encoding="utf-8") 
	archi1.write("condition2\n")
	archi1.close()
	print("condicion 2")
	#p[0] = condition2(p[1],p[2],p[3],"condition2")

def p_relacion1(p):
	'''relacion : ASIGNAR'''
	archi1=open("datos.txt","a",encoding="utf-8") 
	archi1.write("relacion1\n")
	archi1.close()
	print("Relacion 1")
	#p[0] = relacion1(ASIGNAR(p[1]),"relacion1")

def p_relacion2(p):
	'''relacion : DIFERENTE'''
	archi1=open("datos.txt","a",encoding="utf-8") 
	archi1.write("relacion2\n")
	archi1.close()
	print("Relacion 2")
	#p[0] = relacion2(DIFERENTE(p[1]),"relacion2")

def p_relacion3(p):
	'''relacion : MENOR'''
	archi1=open("datos.txt","a",encoding="utf-8") 
	archi1.write("relacion3\n")
	archi1.close()
	print("Relacion 3")
	#p[0] = relacion3(MENOR(p[1]),"relacion3")

def p_relacion4(p):
	'''relacion : MAYOR'''
	archi1=open("datos.txt","a",encoding="utf-8") 
	archi1.write("relacion4\n")
	archi1.close()
	print("Relacion 4")
	#p[0] = relacion4(MAYOR(p[1]),"relacion4")

def p_relacion5(p):
	'''relacion : MENORIGUAL'''
	archi1=open("datos.txt","a",encoding="utf-8") 
	archi1.write("relacion5\n")
	archi1.close()
	print("Relacion 5")
	#p[0] = relacion5(MENORIGUAL(p[1]),"relacion5")

def p_relacion6(p):
	'''relacion : MAYORIGUAL'''
	archi1=open("datos.txt","a",encoding="utf-8") 
	archi1.write("relacion6\n")
	archi1.close()
	print("Relacion 6")
	#p[0] = relacion6(MAYORIGUAL(p[1]),"relacion6")

def p_expr1(p):
	'''expr : termino'''
	archi1=open("datos.txt","a",encoding="utf-8") 
	archi1.write("expr1\n")
	archi1.close()
	print("expr 1")
	#p[0] = expr1(p[1],"expr1")

def p_expr2(p):
	'''expr : addingOperator termino'''
	archi1=open("datos.txt","a",encoding="utf-8") 
	archi1.write("expr2\n")
	archi1.close()
	print("expr 2")
	#p[0] = expr2(p[1],p[2],"expr2")

def p_expr3(p):
	'''expr : expr addingOperator termino'''
	archi1=open("datos.txt","a",encoding="utf-8") 
	archi1.write("expr3\n")
	archi1.close()
	print("expr 3")
	#p[0] = expr3(p[1],p[2],p[3],"expr3")

def p_termino1(p):
	'''termino : factor'''
	archi1=open("datos.txt","a",encoding="utf-8") 
	archi1.write("termino1\n")
	archi1.close()
	print("termino 1")
	#p[0] = termino1(p[1],"termino1")


def p_termino2(p):
	'''termino : termino multiplyingOperator factor'''
	archi1=open("datos.txt","a",encoding="utf-8") 
	archi1.write("termino2\n")
	archi1.close()
	print("termino 2")
	#p[0] = termino2(p[1],p[2],p[3],"termino2")


def p_addingOperator1(p):
	'''addingOperator : MAS'''
	archi1=open("datos.txt","a",encoding="utf-8") 
	archi1.write("addingOperator1\n")
	archi1.close()
	print("addingOperator 1")
	#p[0] = addingOperator1(MAS(p[1]),"addingOperator")	

def p_addingOperator2(p):
	'''addingOperator : MENOS'''
	archi1=open("datos.txt","a",encoding="utf-8") 
	archi1.write("addingOperator2\n")
	archi1.close()
	print("addingOperator 1")
	#p[0] = addingOperator2(MENOS(p[1]),"subtractionOperator")	


def p_multiplyingOperator1(p):
	'''multiplyingOperator : MULT'''
	archi1=open("datos.txt","a",encoding="utf-8") 
	archi1.write("multiplyingOperator1\n")
	archi1.close()
	print("multiplyingOperator 1")
	#p[0] = multiplyingOperator1(MULT(p[1]),"multiplyingOperator")

def p_multiplyingOperator2(p):
	'''multiplyingOperator : DIVIDIR'''
	archi1=open("datos.txt","a",encoding="utf-8") 
	archi1.write("multiplyingOperator2\n")
	archi1.close()
	print("multiplyingOperator 2")
	#p[0] = multiplyingOperator2(DIVIDIR(p[1]),"divisionOperator")

def p_factor1(p):
	'''factor : ID'''
	archi1=open("datos.txt","a",encoding="utf-8") 
	archi1.write("factor1\n")
	archi1.close()
	print("factor 1")
	#p[0] = factor1(ID(p[1]),"factor1")

def p_factor2(p):
	'''factor : NUMERO'''
	archi1=open("datos.txt","a",encoding="utf-8") 
	archi1.write("factor2\n")
	archi1.close()
	print("factor 2")
	#p[0] = factor2(NUMERO(p[1]),"factor2")


def p_factor3(p):
	'''factor : LPARENT expr RPARENT'''
	archi1=open("datos.txt","a",encoding="utf-8") 
	archi1.write("factor3\n")
	archi1.close()
	print("factor 3")
	#p[0] = factor3(p[2],"factor3")

def p_vacio(p):
	'''vacio :'''
	pass

def p_error(p):
	archi1=open("datos.txt","a",encoding="utf-8") 
	archi1.write("Sintax error\n")
	archi1.close()
	print("Sintax error",p)

	
# def traducir(resultado):
# 	graphfile = open('grafo.vz','w')
# 	graphfile.write(resultado.traducir())
# 	graphfile.close()
# 	print("El programa se guardo en \"grafo.vz\"")	



# directorio = 'C:\\Users\\user\\Desktop\\Lenguajes\\Proyecto\\test\\prueba3.wil'
# test = directorio
# fp = codecs.open(test,"r","utf-8")
# cadena = fp.read()
# fp.close()

# parser = yacc.yacc()
# result = parser.parse(cadena)

# print (result)

# directorio = 'C:\\Users\\user\\Desktop\\Lenguajes\\Proyecto\\test\\prueba3.wil'
# test = directorio
# fp = codecs.open(test,"r","utf-8")
# cadena = fp.read()
# fp.close()

# yacc.yacc()
# resultado = yacc.parse(cadena,debug=1)

# resultado.imprimir(" ")
#print(resultado.traducir())

# graphfile = open('grafo.vz','w')
# graphfile.write(resultado.traducir())
# graphfile.close()

#traducir(resultado)