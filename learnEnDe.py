import os

def readTxt(txtFile):
    """Function reading text file."""
    with open(txtFile, 'r', encoding='UTF-8') as fileIn:
        lstFileLines = fileIn.readlines()
    return lstFileLines

def saveFile(csvFile, lstIn):
    """Function saving csv file."""
    with open(csvFile, 'w', encoding='utf-8-sig') as fileOut:
        for content in lstIn:
            fileOut.write(content)

def main():
    os.system('cls')
    lstEnSrc = readTxt('vocList.txt')
    lstDest = []
    for idx, vocabulary in enumerate (lstEnSrc):
        if vocabulary[0:-1].count(' ') > 0:
            # print(str(idx) + ': ' + vocabulary[0:-1] + '  space No.: ' + str(vocabulary[0:-1].count(' ')))
            firstSpaceIdx = vocabulary.index(' ')
            lstDest.append(vocabulary[:firstSpaceIdx] + ',' + vocabulary[(firstSpaceIdx + 1):])
        # 26 letter lines: no space
        else:
            lstDest.append(vocabulary)
            print(vocabulary)

    saveFile('vocListDest.csv', lstDest)

if __name__ == "__main__":
    main()
    print('END')