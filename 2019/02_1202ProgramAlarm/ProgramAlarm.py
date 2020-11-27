
#load file and generate intcode lists here
input_code = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,2,19,13,23,1,23,10,27,1,13,27,31,2,31,10,35,1,35,9,39,1,39,13,43,1,13,43,47,1,47,13,51,1,13,51,55,1,5,55,59,2,10,59,63,1,9,63,67,1,6,67,71,2,71,13,75,2,75,13,79,1,79,9,83,2,83,10,87,1,9,87,91,1,6,91,95,1,95,10,99,1,99,13,103,1,13,103,107,2,13,107,111,1,111,9,115,2,115,10,119,1,119,5,123,1,123,2,127,1,127,5,0,99,2,14,0,0]
# in part 1: before running the program, replace position 1 with the value 12 and replace position 2 with the value 2.
input_code[1]=12
input_code[2]=2

#for part 2, experimentation with position 1 (noun) and 2 (verb) shows that the program follows the pattern 490634 + 320000*noun + verb, so the values needed must be noun 60, verb 86

def run_code(input_code):
    code = list(input_code)
    currentPos = 0
    while code[currentPos] != 99:
        if code[currentPos] == 1:
            #addition
            code[code[currentPos+3]]=code[code[currentPos+1]]+code[code[currentPos+2]]
            
        elif code [currentPos] == 2:
            #multiplication
            code[code[currentPos+3]]=code[code[currentPos+1]]*code[code[currentPos+2]]
            
        else:
            #undefined
            print("error: {} is not a valid intcode opcode, must be 1,2, or 99".format(code[currentPos]))
        currentPos +=4
        
    return code

print("input values: Noun {}    Verb {}".format(input_code[1],input_code[2]))
print(run_code(input_code)[0])