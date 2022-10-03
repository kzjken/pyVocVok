import os

def readTxt(txtFile):
    """Function reading text file."""
    with open(txtFile, 'r', encoding='UTF-8') as fileIn:
        lstFileLines = fileIn.readlines()
    return lstFileLines

def saveFile(csvFile, lstIn):
    """Function saving csv file."""
    with open(csvFile, 'w', encoding='UTF-8') as fileOut:
        for content in lstIn:
            fileOut.write(content)

def main():
    os.system('cls')
    lstEnSrc = readTxt('vocList.txt')
    for idx, vocabulary in enumerate (lstEnSrc):
        # if vocabulary[0:-1].count(' ') > 1:
        #     print(str(idx) + ': ' + vocabulary[0:-1] + '  space No.: ' + str(vocabulary[0:-1].count(' ')))
        if len(vocabulary[0:-1]) == 1:           
            print(str(idx) + ': ' + vocabulary[0:-1])
    # saveFile('vocListDest.csv', lstEnSrc)

if __name__ == "__main__":
    main()