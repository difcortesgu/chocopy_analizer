from queue import LifoQueue 
import analizer

with open(file = 'chocopy_example.py') as f:
    
    tab_size = 4
    indentation_stack = LifoQueue()
    indentation_stack.put(0) 

    for line_number, line in enumerate(f.readlines()):
        indentation_level = 0
        for column_number, char in enumerate(line):
            if char == '\n' or char == '#': 
                break
            elif char == ' ':
                indentation_level += 1
            elif char == '\t':
                indentation_level += tab_size
            else:
                print('<NEWLINE>')
                #Logic to check the indentation level
                #The indentation must be a multiple of TAB_SIZE
                if indentation_level % tab_size != 0: raise Exception("Indentation error")
                indentation_last_level = indentation_stack.get()       
                if indentation_level > indentation_last_level: 
                    #add a new indentation level
                    print("<INDENT>")
                    indentation_stack.put(indentation_last_level)
                    indentation_stack.put(indentation_level)
                elif indentation_level == indentation_last_level: 
                    #leave indentation level the same
                    indentation_stack.put(indentation_last_level)
                else:
                    #remove from the indentation stack until the desired level is reached
                    while indentation_level < indentation_last_level:
                        indentation_last_level = indentation_stack.get()
                        print("<DEDENT>")
                    print("<DEDENT>")
                    indentation_stack.put(indentation_level) 
                analizer.transition_function(line, line_number, column_number)
                break