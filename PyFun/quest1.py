a = [1, 20, 300, 'bbdcc']

def findLetterInMatrix(letterToFind):
    for x in a:
        if isinstance(x, str):
            if letterToFind in x:
                print letterToFind

findLetterInMatrix('b')
findLetterInMatrix('bdc')

