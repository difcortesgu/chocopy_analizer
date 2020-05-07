from lexical_analizer import LexicalAnalizer
from os import path
import sys

class SyntaxAnalizer:
	def __init__(self, file):
		self.CRED = '\033[91m'
		self.CEND = '\033[0m'
		self.lexical_analizer = LexicalAnalizer(file, 4)
		self.token = self.lexical_analizer.next_token()
		self.emparejar('tk_newline')

	def analize(self):
		self.PROGRAM()
		if (self.token.id != 'EOF'):
			sys.exit(self.CRED + "Error: Unexpected token '"+self.token.lexema+"' expecting 'EOF', line: "+str(self.token.line_number)+", column: "+str(self.token.column_number) + self.CEND)

	def emparejar(self, simbolo):
		if self.token.id == simbolo:
			self.token = self.lexical_analizer.next_token()
		else:
			self.syntaxError([simbolo])

	def syntaxError(self, tokens_esperados):
		error_message = self.CRED + "Error: Unexpected token '"+self.token.lexema+"' expecting "
		for x in tokens_esperados:
			error_message += "'" + x + "' "
		error_message = ", line: "+str(self.token.line_number)+", column: "+str(self.token.column_number) + self.CEND
		sys.exit(error_message)

	def PROGRAM(self):
		tokens_esperados = [
			'tk_global',
			'tk_nonlocal',
			'tk_None',
			'tk_suma',
			'tk_id',
		]
		if self.token.id == 'tk_global':
			self.GLOBAL_DECL()
			self.PROGRAM()
		elif self.token.id == 'tk_nonlocal':
			self.NONLOCAL_DECL()
			self.PROGRAM()
		elif self.token.id == 'tk_None':
			self.LITERAL()
			self.PROGRAM()
		elif self.token.id == 'tk_suma':
			self.BIN_OP()
			self.PROGRAM()
		elif self.token.id == 'tk_id':
			self.VAR_DEF()
			self.PROGRAM()
		else:
			self.syntaxError(tokens_esperados)

	def GLOBAL_DECL(self):
		tokens_esperados = [
			'tk_global',
		]
		if self.token.id == 'tk_global':
			self.emparejar('tk_global')
			self.emparejar('tk_id')
			self.emparejar('tk_newline')
		else:
			self.syntaxError(tokens_esperados)

	def NONLOCAL_DECL(self):
		tokens_esperados = [
			'tk_nonlocal',
		]
		if self.token.id == 'tk_nonlocal':
			self.emparejar('tk_nonlocal')
			self.emparejar('tk_id')
			self.emparejar('tk_newline')
		else:
			self.syntaxError(tokens_esperados)

	def LITERAL(self):
		tokens_esperados = [
			'tk_None',
			'tk_True',
			'tk_False',
			'tk_integer',
			'tk_idstring',
			'tk_string',
		]
		if self.token.id == 'tk_None':
			self.emparejar('tk_None')
		elif self.token.id == 'tk_True':
			self.emparejar('tk_True')
		elif self.token.id == 'tk_False':
			self.emparejar('tk_False')
		elif self.token.id == 'tk_integer':
			self.emparejar('tk_integer')
		elif self.token.id == 'tk_idstring':
			self.emparejar('tk_idstring')
		elif self.token.id == 'tk_string':
			self.emparejar('tk_string')
		else:
			self.syntaxError(tokens_esperados)

	def BIN_OP(self):
		tokens_esperados = [
			'tk_suma',
			'tk_resta',
			'tk_mult',
			'tk_div_entera',
			'tk_modulo',
			'tk_igual',
			'tk_diferente',
			'tk_menor_igual',
			'tk_mayor_igual',
			'tk_menor_que',
			'tk_mayor_que',
			'tk_is',
		]
		if self.token.id == 'tk_suma':
			self.emparejar('tk_suma')
		elif self.token.id == 'tk_resta':
			self.emparejar('tk_resta')
		elif self.token.id == 'tk_mult':
			self.emparejar('tk_mult')
		elif self.token.id == 'tk_div_entera':
			self.emparejar('tk_div_entera')
		elif self.token.id == 'tk_modulo':
			self.emparejar('tk_modulo')
		elif self.token.id == 'tk_igual':
			self.emparejar('tk_igual')
		elif self.token.id == 'tk_diferente':
			self.emparejar('tk_diferente')
		elif self.token.id == 'tk_menor_igual':
			self.emparejar('tk_menor_igual')
		elif self.token.id == 'tk_mayor_igual':
			self.emparejar('tk_mayor_igual')
		elif self.token.id == 'tk_menor_que':
			self.emparejar('tk_menor_que')
		elif self.token.id == 'tk_mayor_que':
			self.emparejar('tk_mayor_que')
		elif self.token.id == 'tk_is':
			self.emparejar('tk_is')
		else:
			self.syntaxError(tokens_esperados)

	def VAR_DEF(self):
		tokens_esperados = [
			'tk_id',
		]
		if self.token.id == 'tk_id':
			self.TYPED_VAR()
			self.emparejar('tk_asignacion')
			self.LITERAL()
			self.emparejar('tk_newline')
		else:
			self.syntaxError(tokens_esperados)

	def TYPED_VAR(self):
		tokens_esperados = [
			'tk_id',
		]
		if self.token.id == 'tk_id':
			self.emparejar('tk_id')
			self.emparejar('tk_dos_puntos')
			self.TYPE()
		else:
			self.syntaxError(tokens_esperados)

	def TYPE(self):
		tokens_esperados = [
			'tk_id',
			'tk_idstring',
			'tk_corchete_izq',
		]
		if self.token.id == 'tk_id':
			self.emparejar('tk_id')
		elif self.token.id == 'tk_idstring':
			self.emparejar('tk_idstring')
		elif self.token.id == 'tk_corchete_izq':
			self.emparejar('tk_corchete_izq')
			self.TYPE()
			self.emparejar('tk_corchete_der')
		else:
			self.syntaxError(tokens_esperados)