from queue import LifoQueue 

indentation_stack = LifoQueue() 
#Read an entire line and returns the number of character read
def read_line(string):
    for i,char in enumerate(string):
        if char == '\n' : return i + 1  

def check_F(string, state = 0):
    if state == 0:
        if string[0] == 'a':
            return check_F(string[1:], 1)
        return check_F(string, 6)
    if state == 1:
        if string[0] == 'l':
            return check_F(string[1:], 2)
        return check_F(string, 6)
    if state == 2:
        if string[0] == 's':
            return check_F(string[1:], 3)
        return check_F(string, 6)
    if state == 3:
        if string[0] == 'e':
            return check_F(string[1:], 4)
        return check_F(string, 6)
    if state == 4:
        if string[0] == ' ' or string[0] == '\t':
            return "<False>"
        return check_F(string, 6)
    if state == 6:
        if string[0] == ' ' or string[0] == '\t':
            return "<ID>"
        return check_F(string[1:], 6)
a=False#sdvsvsv ddd
print(check_F('nkjnkjnjnkjnkjnkjnkjnkj#n '))




def transition_function (string, state, space_counter = 0):
    char = string[0]
    if char == '#':
        #Is a commented line, read a complete line and continue
        return transition_function(char[read_line(string):],0)
    elif char == ' ':
        #A trailing space add it to the counter
        return transition_function(char[1:],0,space_counter + 1)
    elif char == '\n' or char == '\r':
        #Is a white line, just ignore it
        return transition_function(char[1:],0)
    elif char == '\t':
        #Is a tab, add 8 spaces to the counter
        return transition_function(char[1:],0,space_counter + 8)
    else:
        #Logic to check the indentation level
        #The indentation must be a multiple of 8
        if space_counter % 8 != 0: raise Exception("Indentation error")
        indentation_level = indentation_stack.get()       
        if space_counter > indentation_level: 
            #add a new indentation level
            print("<INDENT>")
            indentation_stack.put(space_counter)
        elif space_counter == indentation_level: 
            #leave indentation level the same
            indentation_stack.put(indentation_level)
        else:
            #remove from the indentation stack until the desired level is reached
            while space_counter <= indentation_level:
                indentation_level = indentation_stack.get()
                print("<DEDENT>")
            indentation_stack.put(space_counter) 
        if char == 'F':
                       
        if char == 'N':
            pass
        if char == 'T':
            pass
        if char == 'a':
            pass
        if char == 'b':
            pass
        if char == 'c':
            pass
        if char == 'd':
            pass
        if char == 'e':
            pass
        if char == 'f':
            pass
        if char == 'g':
            pass
        if char == 'i':
            pass
        if char == 'l':
            pass
        if char == 'n':
            pass
        if char == 'o':
            pass
        if char == 'p':
            pass
        if char == 'r':
            pass
        if char == 't':
            pass
        if char == 'w':
            pass
        if char == 'y':
            pass

transition_function('hola mundo', 0)