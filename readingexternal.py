# - FP2-F01 - Reading External Files - #
# - Xzavier Moosomin - #
# - 04/09/2024 - #

# - Developer Notes - #
# To be honest, I thought this was really cool
# I didn't expect this free Python app being able to do this
# reading other files in the same folder
# being able to do thigs with it

# - Functions - #

def reading():
    file = open('powerful.txt', 'r')

    all_lines = file.read()
    
    print(all_lines)
    
    file.close()
    
def listing():
    
    file = open('powerful.txt', 'r')
    
    literal = file.readlines()
    print(literal)
    
    print("But wait, what did he say on the 7th line?")
    topic = (literal[6])
    print("Easy, on the seventh line he said", topic)
    
    file.close()
    
def onebyone():
    
    file = open('powerful.txt', 'r')
    
    print("Lets read in between the lines.")
    for line in file:
        line1 = file.readline()
        print(line1)
        
        line2 = file.readline()
        print(line2)
        
    file.close()

def halfofit():
    print("Wait, I only want to read a part of it.")
    
    powerful = open('powerful.txt', 'r')
    
    fifteen = powerful.read(15)
    print(fifteen)
    
    powerful.close()
    
# - Code - #

reading()
listing()
onebyone()
halfofit()
