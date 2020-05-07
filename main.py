from lexical_analizer import LexicalAnalizer
from syntax_analizer import SyntaxAnalizer
from os import path
import sys

CRED = '\033[91m'
CEND = '\033[0m'

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        f = sys.argv[1]
    else:
        sys.exit(CRED +"Error: Debe pasar el nombre del archivo como argumento"+ CEND)
    if not path.isfile(f):
        sys.exit(CRED +'Error: El archivo especificado no existe'+ CEND)

    lexical_analizer = LexicalAnalizer(f, 4)
    syntax_analizer = SyntaxAnalizer(f)
    syntax_analizer.analize()
    # eof = False 
    # while(not eof):
    #     token = lexical_analizer.next_token()
    #     if token.id == 'tk_eof': eof = True
    #     print(token.toString())
