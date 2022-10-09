import random
def emptyList_XO():
    tmp_lst = []
    for i in range (1,9):
        tmp_list.append(' ')
    #print(tmp_lst)
    return tmp_lst

def printBoard(xoList):
    print(xoList[0], "   |   ",xoList[1], "   |   ",xoList[2])
    print("---------------------------")
    print(xoList[3], "   |   ",xoList[4], "   |   ",xoList[5])
    print("---------------------------")
    print(xoList[6], "   |   ",xoList[7], "   |   ",xoList[8])

def whoWillGoFirst():
    a = random.randint(0,1)
    if a==0:
        print('Player A will go first')
    else:
        print('Player B will go first')

    return player

def takeInput(player,xoList):
    flag=0
    while flag==0:
    pos = int(input("hey "+str(player)+ " please enter the position for your next move (0-8)"))
        if pos>=0 and pos<=8:
            print("valid input")
            flag = 1
            if xoList[pos] == '   ':
                print("valid input")
                if player ==0:
                    xoList[pos]= 'X'
                else:
                    xoList[pos] = 'O'
                return xoList
                flag =1
            else:
                print("Please enter again")
                flag =0
        else:
            print("Please give valid input again")
            flag =0

def checkWin(xoList):
    for i in range(9):
        if xoList[i] == '  ':
            flag = 1
    if flag == 0:
        return
