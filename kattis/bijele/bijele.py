
def convertStringToInt(chessString):
    converted = chessString.split(' ')
    result = map(int, converted)
    return result

def convertIntListToStringList(intList):
    convertedString = ''
    for value in intList:
        convertedString = convertedString + str(value) + ' '
    return convertedString

def compareChessSets(pieces):
    officialPieces = [1, 1, 2, 2, 2, 8]
    diffChessPieces = []
    for pieceKey in range(len(pieces)):
        numOfPiecesForOfficial = officialPieces[pieceKey] - pieces[pieceKey]
        diffChessPieces.append(numOfPiecesForOfficial)
    return diffChessPieces

if __name__ == "__main__":
    # The main function
    pieces = raw_input()
    pieces = convertStringToInt(pieces)
    diffChessPieces = compareChessSets(pieces)
    convertedString = convertIntListToStringList(diffChessPieces)
    print convertedString
