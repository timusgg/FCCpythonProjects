def arithmetic_arranger(problem_list, optionalArgument = False):
    separatedProblemList = []
    LineOne = ''
    LineTwo = ''
    LineThree = ''
    result = ''

    if len(problem_list) > 5 :
        return 'Error: Too many problems.' 
       

    for problem in problem_list :
        separatedProblemList.append(problem.split(' '))

    for separatedProblem in separatedProblemList:
        try: 
            operandOne = int(separatedProblem[0])
            operandTwo = int(separatedProblem[2])
        except:
            return 'Error: Numbers must only contain digits.'
        
        
        if len(str(operandOne)) > 4 or len(str(operandTwo)) > 4:
            return 'Error: Numbers cannot be more than four digits.'


        required_spaces = 1
        required_spaces += max(len(separatedProblem[0]), len(separatedProblem[2]))

        LineOne += ' ' + ' '*(required_spaces - len(separatedProblem[0])) + separatedProblem[0] + '    '
        LineTwo += separatedProblem[1] + ' '*(required_spaces - len(separatedProblem[2])) + separatedProblem[2] + '    '
        LineThree += '-' * required_spaces + '-' + '    '

        if separatedProblem[1] == '+':
            sum = operandOne + operandTwo
            result += ' ' + ' '*(required_spaces - len(str(sum))) + str(sum) + '    '
        elif separatedProblem[1] == '-':
            difference = operandOne - operandTwo
            result += ' ' + ' '*(required_spaces - len(str(difference))) + str(difference) + '    '
        else:
            return 'Error: Operator must be \'+\' or \'-\'.'
        

    LineOne = LineOne.rstrip()
    LineTwo = LineTwo.rstrip()
    LineThree = LineThree.rstrip()
    result = result.rstrip()

    LineOne += '\n'
    LineTwo += '\n'
 

    if optionalArgument == True:
        return LineOne + LineTwo + LineThree + '\n' + result

    return LineOne + LineTwo + LineThree

    

problem_list = ['3 + 855', '3801 - 2', '45 + 43', '123 + 49']
print(arithmetic_arranger(problem_list))

#print(separatedProblemList)