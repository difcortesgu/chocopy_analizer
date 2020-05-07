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