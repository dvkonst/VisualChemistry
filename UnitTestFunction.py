def UnitTestFunction(TestingExpressionsAndExpectedResults, 
                     introdaction= 'Testing'):
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
    ListOfTestsAndResults = []
    #if type(ListOfVariableAndResults) == str:
    #ListOfVariableAndResults = ListOfVariableAndResults.split('; ')
    for variable_result in ListOfVariableAndResults:
        variable_result = variable_result.split('_')
        testingExpression = function.replace('VAR', variable_result[0])
        expectedResult = variable_result[1]
        ListOfTestsAndResults.append((testingExpression, expectedResult))
    return ListOfTestsAndResults

    
    
    
