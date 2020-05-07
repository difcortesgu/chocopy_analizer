class Token:
    def __init__(self, id, lexema = "", line_number = 0, column_number = 0):
        self.id = id
        self.lexema = lexema
        self.column_number = column_number
        self.line_number = line_number
    
    def toString(self):
        string = '<' +self.id
        if self.lexema:
            string += ', ' + self.lexema
        if self.line_number:
            string += ', ' + str(self.line_number)
        if self.column_number:
            string += ', ' + str(self.column_number)
        string += '>'
        return string
