# api 相關
from dotenv import load_dotenv
import os
load_dotenv()
my_api_key = os.getenv("MY_API_KEY")

# 刷新頁面
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


mp = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

# 顏色選擇
colorDict = {'RED' : '\033[31m',
         'GREEN' : '\033[32m',
         'YELLOW' : '\033[33m',
         'BLUE' : '\033[34m',
         'RESET' : '\033[0m'}
def printColor(x, chooseColor):
    global colorDict
    print(colorDict[chooseColor] + x + colorDict['RESET'], end = '')

# game function
def changePlayer(player):
    if player == 1:
        return 2
    else :
        return 1
def printMap(color1, color2):
    print()
    for i in range(0, 3):
        for j in range(0, 3):
            if mp[i][j] == 'O':
                printColor(" " + mp[i][j] + " ", color1)
            elif mp[i][j] == 'X':
                printColor(" " + mp[i][j] + " ", color2)
            else:
                print(" " + mp[i][j] + " ", end = '')
            if j != 2:
                print("│", end = '')
        print()
        if i != 2:
            print("───┼───┼───")
    print()
def findWinner():
    if (mp[0][0] == mp[1][1] and mp[1][1] == mp[2][2]):
        return mp[1][1]
    if (mp[0][2] == mp[1][1] and mp[1][1] == mp[2][0]):
        return mp[1][1]
    for i in range(0, 3):
        if (mp[i][0] == mp[i][1] and mp[i][1] == mp[i][2]):
            return mp[i][1]
        if (mp[0][i] == mp[1][i] and mp[1][i] == mp[2][i]):
            return mp[1][i]
    cnt = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if mp[i][j] == 'O' or mp[i][j] == 'X':
                cnt = cnt + 1
    if cnt == 9:
        return 'noWinner'
    return None

# ai 方
from google import genai
client = genai.Client(api_key= my_api_key)
def formatMp(mp):
    board = "\n".join([" | ".join(row) for row in mp])
    return f"目前的棋盤狀態如下：\n{board}"
def askAI():
    mp_content = formatMp(mp)
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=f"以下是井字棋的棋盤狀態：\n{mp_content}\n，你是'X'，玩家是'O'，請分析並選出你要選擇的選項(1~9)。請注意，請你不要進行其他的敘述，直接回答我一個1~9的數字做為選項就好"
    )
    return int(response.text)

# 遊戲流程 function
def chooseMode():
    yn = 0
    while(yn == 0):
        mode = int(input("請選擇模式(1:人對電腦, 2:人對人)："))
        if mode == 1 or mode == 2:
            yn = 1
    return mode
def chooseColor(name):
    name = str(name)
    while 1:
        print("請選擇" + name + "的顏色")
        printColor('RED ', 'RED')
        printColor('GREEN ', 'GREEN')
        printColor('YELLOW ', 'YELLOW')
        printColor('BLUE', 'BLUE')
        print(": ", end = '')
        color = input()
        if (color in colorDict):
            break
    return color
def HumanVSHumanMode(color1, color2):
    player = 1
    while 1:
        clear()
        printMap(color1, color2)
        while 1:
            print("請玩家 " + str(player) + " 選擇位置(輸入1~9)：", end = '')
            choose = int(input())
            if choose > 0 and choose < 10 :
                x = (choose + 2) // 3 - 1
                y = choose % 3 - 1
                if mp[x][y] != 'O' and mp[x][y] != 'X':
                    break
        if (player == 1):
            mp[x][y] = 'O'
        else :
            mp[x][y] = 'X'
        player = changePlayer(player)
        find = findWinner()
        if (find == 'O'):
            clear()
            print("贏家是player 1 !!!")
            printMap(color1, color2)
            break
        elif (find == 'X'):
            clear()
            print("贏家是player 2 !!!")
            printMap(color1, color2)
            break
        elif (find == 'noWinner'):
            clear()
            print("平手！！！")
            printMap(color1, color2)
            break
def HumanVSComputer(color1, color2):
    player = 1
    while 1:
        clear()
        printMap(color1, color2)
        if (player == 1):
            while 1:
                choose = int(input())
                if choose > 0 and choose < 10 :
                    x = (choose + 2) // 3 - 1
                    y = choose % 3 - 1
                    if mp[x][y] != 'O' and mp[x][y] != 'X':
                        break
        else:
            print("現在輪到 gemini 選擇了！等他選擇一下......")
            choose = askAI()
            print("他的選擇是：" + str(choose))
            x = (choose + 2) // 3 - 1
            y = choose % 3 - 1
        
        if (player == 1):
            mp[x][y] = 'O'
        else :
            mp[x][y] = 'X'
        player = changePlayer(player)
        find = findWinner()
        if (find == 'O'):
            print("你是贏家！！！")
            printMap(color1, color2)
            break
        elif (find == 'X'):
            print("贏家是 gemini ！！！")
            printMap(color1, color2)
            break
        elif (find == 'noWinner'):
            print("平手！！！")
            printMap(color1, color2)
            break
    

# main
mode = chooseMode()
if mode == 1: # 人對電腦
    humanColor = chooseColor()
    computerColor = 'RED'
    if (humanColor == 'RED'):
        humanColor = 'GREEN'
    HumanVSComputer(humanColor, computerColor)
else : # 人對人
    player1Color = chooseColor('Player 1')
    player2Color = chooseColor('Player 2')
    HumanVSHumanMode(player1Color, player2Color)
    
    
    
