class Token:
    def __init__(self, id, lexema = None, line_number = None, column_number = None):
        self.id = id
        self.lexema = lexema
        self.column_number = column_number
        self.line_number = line_number
    
    def toString(self):
        string = '<' +self.id
        if self.lexema:
            string += ', ' + self.lexema
        if self.line_number:
            string += ', ' + str(self.column_number)
        if self.column_number:
            string += ', ' + str(self.line_number)
        string += '>'
        return string
