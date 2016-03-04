def writtenNumber(number):
    '''
    Converts a number spelled out in English into an integer
    
    number : a spelled out number 
            (e.g. forty two, one hundred,etc.)
    
    returns : numeric representation of the written number
    '''
    
    #Value of each number scale, hundred is a special case
    #so it's not included
    scaleVal = {'thousand': 1E3, 'million': 1E6,\
                'billion': 1E9, 'trillion': 1E12}
    
    #Value of each spelled out number
    numVal = {'one': 1, 'two': 2, 'three': 3, 'four': 4, \
              'five': 5, 'six': 6, 'seven': 7, 'eight': 8, \
              'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, \
              'thirteen': 13, 'fourteen': 14, 'fifteen': 15, \
              'sixteen': 16, 'seventeen': 17, 'eighteen': 18, \
              'nineteen': 19, 'twenty': 20, 'thirty': 30, \
              'forty': 40, 'fifty': 50, 'sixty': 60, \
              'seventy': 70, 'eighty': 80, 'ninety': 90}
    
    #convert spelled out number into lowercase
    number = number.lower()
    
    #if number is 'zero' return 0
    if number == 'zero':
        return 0
    
    #Separate the spelled out number into separate words
    number = number.split()
    
    #Remove all occurence of the word 'and'
    while 'and' in number:
        number.remove('and')

    res = 0
    temp = 0
    
    try:
        if not(number[0] in numVal):
            raise ValueError('A written number always starts ' + \
                                'with a number, not a scale')
    
    except ValueError as e:
        print e.message
    
    for i in range(len(number)):        
        if number[i] == 'hundred':
            temp *= 100
        
        elif number[i] in numVal:
            temp += numVal[number[i]]
            
        elif number[i] in scaleVal:
            temp *= scaleVal[number[i]]
            res += temp
            temp = 0
            
        else:
            raise ValueError("Unknown number")  
            
    if number[-1] not in scaleVal:
        res += temp
    
    return res