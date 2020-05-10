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
		error_message += ", line: "+str(self.token.line_number)+", column: "+str(self.token.column_number) + self.CEND
		sys.exit(error_message)

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
			'tk_number',
			'tk_idstring',
			'tk_string',
		]
		if self.token.id == 'tk_None':
			self.emparejar('tk_None')
		elif self.token.id == 'tk_True':
			self.emparejar('tk_True')
		elif self.token.id == 'tk_False':
			self.emparejar('tk_False')
		elif self.token.id == 'tk_number':
			self.emparejar('tk_number')
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
			'tk_int',
			'tk_str',
			'tk_bool',
			'tk_object',
			'tk_idstring',
			'tk_corchete_izq',
		]
		if self.token.id == 'tk_id':
			self.emparejar('tk_id')
		elif self.token.id == 'tk_int':
			self.emparejar('tk_int')
		elif self.token.id == 'tk_str':
			self.emparejar('tk_str')
		elif self.token.id == 'tk_bool':
			self.emparejar('tk_bool')
		elif self.token.id == 'tk_object':
			self.emparejar('tk_object')
		elif self.token.id == 'tk_idstring':
			self.emparejar('tk_idstring')
		elif self.token.id == 'tk_corchete_izq':
			self.emparejar('tk_corchete_izq')
			self.TYPE()
			self.emparejar('tk_corchete_der')
		else:
			self.syntaxError(tokens_esperados)

	def PROGRAM(self):
		tokens_esperados = [
			'tk_def',
			'tk_id',
			'tk_class',
		]
		if self.token.id == 'tk_def' or self.token.id == 'tk_id' or self.token.id == 'tk_class':
			self.L_DEF()
			self.L_STMT()
		else:
			self.syntaxError(tokens_esperados)

	def L_DEF(self):
		tokens_esperados = [
			'tk_def',
			'tk_class',
			'tk_id',
			'tk_id',
		]
		if self.token.id == 'tk_def':
			self.FUNC_DEF()
			self.L_DEF()
		elif self.token.id == 'tk_class':
			self.CLASS_DEF()
			self.L_DEF()
		elif self.token.id == 'tk_id':
			self.emparejar('tk_id')
			self.emparejar('tk_dos_puntos')
			self.TYPE()
			self.emparejar('tk_asignacion')
			self.LITERAL()
			self.emparejar('tk_newline')
			self.L_DEF()
		elif self.token.id == 'tk_id':
			pass
		else:
			self.syntaxError(tokens_esperados)

	def L_STMT(self):
		tokens_esperados = [
			'tk_id',
			'$',
		]
		if self.token.id == 'tk_id':
			self.emparejar('tk_id')
			self.L_STMT()
		elif self.token.id == '$':
			pass
		else:
			self.syntaxError(tokens_esperados)

	def FUNC_DEF(self):
		tokens_esperados = [
			'tk_def',
		]
		if self.token.id == 'tk_def':
			self.emparejar('tk_def')
			self.emparejar('tk_id')
			self.emparejar('tk_par_izq')
			self.IL_TYPED_VAR()
			self.emparejar('tk_par_der')
			self.OPT_TYPE()
			self.emparejar('tk_dos_puntos')
			self.emparejar('tk_newline')
			self.emparejar('tk_indent')
			self.FUNC_BODY()
			self.emparejar('tk_dedent')
		else:
			self.syntaxError(tokens_esperados)

	def CLASS_DEF(self):
		tokens_esperados = [
			'tk_class',
		]
		if self.token.id == 'tk_class':
			self.emparejar('tk_class')
			self.emparejar('tk_id')
			self.emparejar('tk_par_izq')
			self.emparejar('tk_id')
			self.emparejar('tk_par_der')
			self.emparejar('tk_dos_puntos')
			self.emparejar('tk_newline')
			self.emparejar('tk_indent')
			self.CLASS_BODY()
			self.emparejar('tk_dedent')
		else:
			self.syntaxError(tokens_esperados)

	def IL_TYPED_VAR(self):
		tokens_esperados = [
			'tk_id',
			'tk_par_der',
		]
		if self.token.id == 'tk_id':
			self.emparejar('tk_id')
			self.emparejar('tk_dos_puntos')
			self.TYPE()
			self.L_TYPED_VAR()
		elif self.token.id == 'tk_par_der':
			pass
		else:
			self.syntaxError(tokens_esperados)

	def OPT_TYPE(self):
		tokens_esperados = [
			'tk_ejecuta',
			'tk_dos_puntos',
		]
		if self.token.id == 'tk_ejecuta':
			self.emparejar('tk_ejecuta')
			self.TYPE()
		elif self.token.id == 'tk_dos_puntos':
			pass
		else:
			self.syntaxError(tokens_esperados)

	def FUNC_BODY(self):
		tokens_esperados = [
			'tk_nonlocal',
			'tk_global',
			'tk_def',
			'tk_id',
		]
		if self.token.id == 'tk_nonlocal' or self.token.id == 'tk_global' or self.token.id == 'tk_def' or self.token.id == 'tk_id':
			self.L_FUNC_BODY()
			self.L_FUNC_STMT()
		else:
			self.syntaxError(tokens_esperados)

	def CLASS_BODY(self):
		tokens_esperados = [
			'tk_pass',
			'tk_def',
			'tk_id',
		]
		if self.token.id == 'tk_pass':
			self.emparejar('tk_pass')
			self.emparejar('tk_newline')
		elif self.token.id == 'tk_def' or self.token.id == 'tk_id':
			self.L_CLASS_BODY()
		else:
			self.syntaxError(tokens_esperados)

	def L_FUNC_BODY(self):
		tokens_esperados = [
			'tk_global',
			'tk_id',
			'tk_def',
			'tk_nonlocal',
			'tk_id',
		]
		if self.token.id == 'tk_global':
			self.emparejar('tk_global')
			self.emparejar('tk_id')
			self.emparejar('tk_newline')
			self.L_FUNC_BODY()
		elif self.token.id == 'tk_id':
			self.emparejar('tk_id')
			self.emparejar('tk_dos_puntos')
			self.TYPE()
			self.emparejar('tk_asignacion')
			self.LITERAL()
			self.emparejar('tk_newline')
			self.L_FUNC_BODY()
		elif self.token.id == 'tk_def':
			self.emparejar('tk_def')
			self.emparejar('tk_id')
			self.emparejar('tk_par_izq')
			self.IL_TYPED_VAR()
			self.emparejar('tk_par_der')
			self.OPT_TYPE()
			self.emparejar('tk_dos_puntos')
			self.emparejar('tk_newline')
			self.emparejar('tk_indent')
			self.FUNC_BODY()
			self.emparejar('tk_dedent')
			self.L_FUNC_BODY()
		elif self.token.id == 'tk_nonlocal':
			self.emparejar('tk_nonlocal')
			self.emparejar('tk_id')
			self.emparejar('tk_newline')
			self.L_FUNC_BODY()
		elif self.token.id == 'tk_id':
			pass
		else:
			self.syntaxError(tokens_esperados)

	def L_FUNC_STMT(self):
		tokens_esperados = [
			'tk_id',
		]
		if self.token.id == 'tk_id':
			self.emparejar('tk_id')
			self.L_FUNC_STMT_()
		else:
			self.syntaxError(tokens_esperados)

	def L_TYPED_VAR(self):
		tokens_esperados = [
			'tk_coma',
			'tk_par_der',
		]
		if self.token.id == 'tk_coma':
			self.emparejar('tk_coma')
			self.TYPED_VAR()
			self.L_TYPED_VAR()
		elif self.token.id == 'tk_par_der':
			pass
		else:
			self.syntaxError(tokens_esperados)

	def L_CLASS_BODY(self):
		tokens_esperados = [
			'tk_id',
			'tk_def',
		]
		if self.token.id == 'tk_id':
			self.emparejar('tk_id')
			self.emparejar('tk_dos_puntos')
			self.TYPE()
			self.emparejar('tk_asignacion')
			self.LITERAL()
			self.emparejar('tk_newline')
			self.L_CLASS_BODY_()
		elif self.token.id == 'tk_def':
			self.emparejar('tk_def')
			self.emparejar('tk_id')
			self.emparejar('tk_par_izq')
			self.IL_TYPED_VAR()
			self.emparejar('tk_par_der')
			self.OPT_TYPE()
			self.emparejar('tk_dos_puntos')
			self.emparejar('tk_newline')
			self.emparejar('tk_indent')
			self.FUNC_BODY()
			self.emparejar('tk_dedent')
			self.L_CLASS_BODY_()
		else:
			self.syntaxError(tokens_esperados)

	def L_FUNC_STMT_(self):
		tokens_esperados = [
			'tk_id',
			'tk_dedent',
		]
		if self.token.id == 'tk_id':
			self.emparejar('tk_id')
			self.L_FUNC_STMT_()
		elif self.token.id == 'tk_dedent':
			pass
		else:
			self.syntaxError(tokens_esperados)

	def L_CLASS_BODY_(self):
		tokens_esperados = [
			'tk_id',
			'tk_def',
			'tk_dedent',
		]
		if self.token.id == 'tk_id':
			self.VAR_DEF()
			self.L_CLASS_BODY_()
		elif self.token.id == 'tk_def':
			self.FUNC_DEF()
			self.L_CLASS_BODY_()
		elif self.token.id == 'tk_dedent':
			pass
		else:
			self.syntaxError(tokens_esperados)