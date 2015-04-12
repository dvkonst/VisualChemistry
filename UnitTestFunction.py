def UnitTestFunction(TestingExpressionsAndExpectedResults, 
                     introdaction= 'Testing'):
    """
    UnitTestFunction() - универсальная тест-функция
    Variables:
    TestingExpressionsAndExpectedResults - список кортежей: (строка-выражение, ожидаемый результат)
    introdaction - строка, содержащая вводный текст (по умолчанию 'Testing')
    Description:
    В цикле пробегается весь список,
    из кортежей вынимаются тестируемые выражения(строки)
    и преобразуются в исполняемый код;
    результат его работы сравнивается с ожидаемым;
    если верно, то ok, иначе - fail
    Example:
    >>>from math import*
    >>> UnitTestFunction([('sin(3.14)', '0'), ('sin(0)', '0')])
    Testing 

    Test №  1
    (  sin(3.14) ) == 0 
    result =  0.0015926529164868282
	Fail
    Test №  2
    (  sin(0) ) == 0 
    result =  0.0
	Fail

    End of Test
    >>> 
    
    """
    print(introdaction, '\n')
    numberOfTest = 1
    for testingExpression, expectedResult in TestingExpressionsAndExpectedResults:
        print('Test № ', numberOfTest)
        result = eval(testingExpression)
        print('( ', testingExpression, ') ==', expectedResult,
              '\nresult = ', result)
        if result == expectedResult:
            print('\tOk')
        else:
            print('\tFail')
        numberOfTest += 1
    print('\nEnd of Test')

def ListOfTestingExpressionsAndExpectedResults(function, ListOfVariableAndResults):
    """
    ListOfTestingExpressionsAndExpectedResults() - возвращает список
    кортежей с тестируемыми выражениями и ожидаемыми результатами
    Variables:
    function - строка-выражение, обычно содержащая функцию с переменной VAR 
    ListOfVariableAndResults - список специально форматированных строк:
    "переменные_ожидаемый результат"
    Description:
    В цикле пробегает список ListOfVariableAndResults;
    где необходимо заменяет VAR на переменные;
    Возвращает список ListOfTestsAndResults
    Example:
    >>> ListOfTestingExpressionsAndExpectedResults("5+3", [(, 8), (, 9)])
    [('5+3', '8'), ('5+3', '9')]
    >>> from math import*
    >>> ListOfTestingExpressionsAndExpectedResults("sin(VAR)", ["3.14_0", "0_0"])
    [('sin(3.14)', '0'), ('sin(0)', '0')]
    
    """
    ListOfTestsAndResults = []
    for variable_result in ListOfVariableAndResults:
        variable = variable_result[0]
        testingExpression = function.replace('VAR', str(variable))
        expectedResult = variable_result[1]
        ListOfTestsAndResults.append((testingExpression, expectedResult))
    return ListOfTestsAndResults

    
    
    
