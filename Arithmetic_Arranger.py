enter = '\n'

def arithmetic_arranger(problems):
    sorted_through_problems = 0
    for problem_working in problems:
        lines = '______'
        problem_count = len(problems)
        problem = problems[sorted_through_problems]
        problems_working = problem
        problem_sorted = problems_working.split()
        problem_num1 = int(problem_sorted[0])
        problem_op = problem_sorted[1]
        problem_num2 = int(problem_sorted[2])
        if problem_op == '+':
            problem_answer_str = problem_num1 + problem_num2
            problem_answer = int(problem_answer_str)
        elif problem_op == '-':
            problem_answer = problem_num1 - problem_num2
        problem_num1_count = len(str(problem_num1))
        problem_num2_count = len(str(problem_num2))
        problem_answer_count = len(str(problem_answer))


        if problem_num1_count == 1:
            space1 = '     '
        elif problem_num1_count == 2:
            space1 = '    '
        elif problem_num1_count == 3:
            space1 = '   '
        elif problem_num1_count == 4:
            space1 = '  '
        else:
            print('ERROR : YOU CAN ONLY DO 4 DIGITS')
            exit()


        if problem_num2_count == 1:
            space2 = '   '
        elif problem_num2_count == 2:
            space2 = '  '
        elif problem_num2_count == 3:
            space2 = ' '
        elif problem_num2_count == 4:
            space2 = ''
        else:
            print('ERROR : YOU CAN ONLY DO 4 DIGITS')
            exit()


        if problem_answer_count == 1:
            space3 = '    '
        elif problem_answer_count == 2:
            space3 = '   '
        elif problem_answer_count == 3:
            space3 = '  '
        elif problem_answer_count == 4:
            space3 = ' '
        elif problem_answer_count == 5:
            space3 = ''
        else:
            print('ERROR : SOMETHING HAS GONE WRONG PLEASE TRY AGAIN')
            exit()
        sorted_through_problems = sorted_through_problems + 1
        print(space1,problem_num1,'\n',problem_op+space2,problem_num2,'\n',lines,'\n',space3,problem_answer,enter,enter)

        for problem_working in problems:
            lines = '______'
            problem = problems[sorted_through_problems]
            problems_working = problem
            problem_sorted = problems_working.split()
            problem_num1 = int(problem_sorted[0])
            problem_op = problem_sorted[1]
            problem_num2 = int(problem_sorted[2])
            if problem_op == '+':
                problem_answer_str = problem_num1 + problem_num2
                problem_answer = int(problem_answer_str)
            elif problem_op == '-':
                problem_answer = problem_num1 - problem_num2
            problem_num1_count = len(str(problem_num1))
            problem_num2_count = len(str(problem_num2))
            problem_answer_count = len(str(problem_answer))

            if problem_num1_count == 1:
                space1 = '     '
            elif problem_num1_count == 2:
                space1 = '    '
            elif problem_num1_count == 3:
                space1 = '   '
            elif problem_num1_count == 4:
                space1 = '  '
            else:
                print('ERROR : YOU CAN ONLY DO 4 DIGITS')
                exit()

            if problem_num2_count == 1:
                space2 = '   '
            elif problem_num2_count == 2:
                space2 = '  '
            elif problem_num2_count == 3:
                space2 = ' '
            elif problem_num2_count == 4:
                space2 = ''
            else:
                print('ERROR : YOU CAN ONLY DO 4 DIGITS')
                exit()

            if problem_answer_count == 1:
                space3 = '    '
            elif problem_answer_count == 2:
                space3 = '   '
            elif problem_answer_count == 3:
                space3 = '  '
            elif problem_answer_count == 4:
                space3 = ' '
            elif problem_answer_count == 5:
                space3 = ''
            else:
                print('ERROR : SOMETHING HAS GONE WRONG PLEASE TRY AGAIN')
                exit()
            if problem_count == 5:
                print('ERROR : NO MORE THAN 4 SUMS')
                exit()
            elif problem_count <= sorted_through_problems:
                sorted_through_problems = sorted_through_problems + 1
            print(space1, problem_num1, '\n', problem_op + space2, problem_num2, '\n', lines, '\n', space3,
                  problem_answer,enter,enter)

        return problems

arithmetic_arranger(['482 - 1343', '12 + 1782','482 - 1343', '12 + 1342',])
