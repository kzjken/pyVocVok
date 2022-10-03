import random

# read list
with open('vocList.txt', 'r', encoding='UTF-8') as fileEn4:
    fileEn4Lines = fileEn4.readlines()

# # search
# for i in range(50):
#     # get random content
#     searchContent = random.choice(fileEn4Lines)[0:-1]
#     print(str(i) + ": " + searchContent)

for idx, vocabulary in enumerate (fileEn4Lines):
    # if idx <= 10:
    #     print(str(idx) + ': ' + vocabulary[0:-1] + '  space No.: ' + str(vocabulary[0:-1].count(' ')))
    if vocabulary[0:-1].count(' ') > 1:     
        print(str(idx) + ': ' + vocabulary[0:-1] + '  space No.: ' + str(vocabulary[0:-1].count(' ')))
        