baseMP = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
mp = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]



class Player:
    def __init__(self, name, symbol, color):
        self.name = name         
        self.symbol = symbol
        self.color = color


# api 相關
from dotenv import load_dotenv
import os
load_dotenv()
my_api_key = os.getenv("MY_API_KEY")

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


# 刷新頁面
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

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
def printMap()
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