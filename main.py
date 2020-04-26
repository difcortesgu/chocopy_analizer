from analizer import SyntaxAnalizer
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

    syntax_analizer = SyntaxAnalizer(f, 4)
    eof = False 
    while(input() != 'a' and not eof):
        token = syntax_analizer.next_token()
        if token.id == 'EOF': eof = True
        print(token.toString())
