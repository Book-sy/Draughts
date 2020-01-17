import sys
import pygame
import random
import math

pygame.init()
pygame.font.init()
chess_size = 40
space = 30
score_size = 200
screencaption = pygame.display.set_caption('HS国际跳棋')
screen = pygame.display.set_mode((chess_size*10+space*2+score_size,chess_size*10+space*2))
color = ((223,4,4),(255,218,75),(102,187,106),(59,119,167),(255,127,0),(95,99,104),(6,41,69),(0,0,0),(198,115,255),(3,73,127),(223,4,4),(255,218,75),(102,187,106),(59,119,167),(255,127,0),(95,99,104),(6,41,69),(0,0,0),(198,115,255),(3,73,127),(223,4,4),(255,218,75),(102,187,106),(59,119,167),(255,127,0),(95,99,104),(6,41,69),(0,0,0),(198,115,255),(3,73,127),(223,4,4),(255,218,75),(102,187,106),(59,119,167),(255,127,0),(95,99,104),(6,41,69),(0,0,0),(198,115,255),(3,73,127),(223,4,4),(255,218,75),(102,187,106),(59,119,167),(255,127,0),(95,99,104),(6,41,69),(0,0,0),(198,115,255),(3,73,127),(223,4,4),(255,218,75),(102,187,106),(59,119,167),(255,127,0),(95,99,104),(6,41,69),(0,0,0),(198,115,255),(3,73,127),(223,4,4),(255,218,75),(102,187,106),(59,119,167),(255,127,0),(95,99,104),(6,41,69),(0,0,0),(198,115,255),(3,73,127),(223,4,4),(255,218,75),(102,187,106),(59,119,167),(255,127,0),(95,99,104),(6,41,69),(0,0,0),(198,115,255),(3,73,127),(223,4,4),(255,218,75),(102,187,106),(59,119,167),(255,127,0),(95,99,104),(6,41,69),(0,0,0),(198,115,255),(3,73,127),(223,4,4),(255,218,75),(102,187,106),(59,119,167),(255,127,0),(95,99,104),(6,41,69),(0,0,0),(198,115,255),(3,73,127),(223,4,4),(255,218,75),(102,187,106),(59,119,167),(255,127,0),(95,99,104),(6,41,69),(0,0,0),(198,115,255),(3,73,127),(223,4,4),(255,218,75),(102,187,106),(59,119,167),(255,127,0),(95,99,104),(6,41,69),(0,0,0),(198,115,255),(3,73,127),(223,4,4),(255,218,75),(102,187,106),(59,119,167),(255,127,0),(95,99,104),(6,41,69),(0,0,0),(198,115,255),(3,73,127),(223,4,4),(255,218,75),(102,187,106),(59,119,167),(255,127,0),(95,99,104),(6,41,69),(0,0,0),(198,115,255),(3,73,127),(223,4,4),(255,218,75),(102,187,106),(59,119,167),(255,127,0),(95,99,104),(6,41,69),(0,0,0),(198,115,255),(3,73,127),(223,4,4),(255,218,75),(102,187,106),(59,119,167),(255,127,0),(95,99,104),(6,41,69),(0,0,0),(198,115,255),(3,73,127),(223,4,4),(255,218,75),(102,187,106),(59,119,167),(255,127,0),(95,99,104),(6,41,69),(0,0,0),(198,115,255),(3,73,127),(223,4,4),(255,218,75),(102,187,106),(59,119,167),(255,127,0),(95,99,104),(6,41,69),(0,0,0),(198,115,255),(3,73,127),(223,4,4),(255,218,75),(102,187,106),(59,119,167),(255,127,0),(95,99,104),(6,41,69),(0,0,0),(198,115,255),(3,73,127),(223,4,4),(255,218,75),(102,187,106),(59,119,167),(255,127,0),(95,99,104),(6,41,69),(0,0,0),(198,115,255),(3,73,127),(223,4,4),(255,218,75),(102,187,106),(59,119,167),(255,127,0),(95,99,104),(6,41,69),(0,0,0),(198,115,255),(3,73,127),(223,4,4),(255,218,75),(102,187,106),(59,119,167),(255,127,0),(95,99,104),(6,41,69),(0,0,0),(198,115,255),(3,73,127),(223,4,4),(255,218,75),(102,187,106),(59,119,167),(255,127,0),(95,99,104),(6,41,69),(0,0,0),(198,115,255),(3,73,127),(223,4,4),(255,218,75),(102,187,106),(59,119,167),(255,127,0),(95,99,104),(6,41,69),(0,0,0),(198,115,255),(3,73,127))

class checkerBoard(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = [[0 for i in range(10)] for j in range(10)]
        self.choose = (-1,-1)
        self.now = 1
        self.step = 0
        self.probably = []
        self.maxstep = 1
        self.aiB = 0
        self.aiW = 0
        self.wg = 0
    def createAll(self):
        for i in range(11):
            pygame.draw.line(screen, (0,0,0), (self.x + i * chess_size ,self.y), (self.x + i * chess_size ,self.y + 10 * chess_size), 1)
            pygame.draw.line(screen, (0,0,0), (self.x ,self.y + i * chess_size), (self.x + 10 * chess_size ,self.y + i * chess_size), 1)
        pygame.draw.line(screen, (0,0,0),(self.x + 10 * chess_size ,self.y ) ,(self.x + 10 * chess_size + score_size ,self.y ) , 1)
        pygame.draw.line(screen, (0,0,0),(self.x + 10 * chess_size ,self.y + 10 * chess_size) ,(self.x + 10 * chess_size + score_size ,self.y + 10 * chess_size) , 1)
        pygame.draw.line(screen, (0,0,0),(self.x + 10 * chess_size + score_size ,self.y ) ,(self.x + 10 * chess_size + score_size ,self.y + 10 * chess_size) , 1)
    def createChess(self):
        c=0
        for i in range(10):
            for j in range(10):
                font = pygame.font.SysFont("simsunnsimsun",30)
                if (i + j) % 2 == 0:
                    pygame.draw.rect(screen, (255,204,153), (self.x + i * chess_size,self.y + j * chess_size,chess_size,chess_size) ,0)
                else:
                    pygame.draw.rect(screen, (128,0,0), (self.x + i * chess_size,self.y + j * chess_size,chess_size,chess_size) ,0)
                if self.state[i][j] == 1:
                    pygame.draw.ellipse(screen, (0,0,0), (self.x + i * chess_size,self.y + j * chess_size,chess_size,chess_size) ,0)
                    pygame.draw.ellipse(screen, (255,255,255), (self.x + i * chess_size,self.y + j * chess_size,chess_size,chess_size) ,1)
                elif self.state[i][j] == -1:
                    pygame.draw.ellipse(screen, (255,255,255), (self.x + i * chess_size,self.y + j * chess_size,chess_size,chess_size) ,0)
                    pygame.draw.ellipse(screen, (0,0,0), (self.x + i * chess_size,self.y + j * chess_size,chess_size,chess_size) ,1)
                elif self.state[i][j] == 2:
                    pygame.draw.ellipse(screen, (0,0,0), (self.x + i * chess_size,self.y + j * chess_size,chess_size,chess_size) ,0)
                    pygame.draw.ellipse(screen, (255,255,255), (self.x + i * chess_size,self.y + j * chess_size,chess_size,chess_size) ,1)
                    font_king = font.render("王",2,(255,255,255))
                    screen.blit(font_king,(5+self.x + i * chess_size,5+self.y + j * chess_size,chess_size,chess_size))
                elif self.state[i][j] == -2:
                    pygame.draw.ellipse(screen, (255,255,255), (self.x + i * chess_size,self.y + j * chess_size,chess_size,chess_size) ,0)
                    pygame.draw.ellipse(screen, (0,0,0), (self.x + i * chess_size,self.y + j * chess_size,chess_size,chess_size) ,1)
                    font_king = font.render("王",2,(0,0,0))
                    screen.blit(font_king,(5+self.x + i * chess_size,5+self.y + j * chess_size,chess_size,chess_size))
        if self.choose != (-1,-1):
            x,y = self.choose
            pygame.draw.rect(screen, (255,255,255), (self.x + x * chess_size,self.y + y * chess_size,chess_size,chess_size) ,0)
            if self.now == 1:
                pygame.draw.ellipse(screen, (100,100,100), (self.x + x * chess_size,self.y + y * chess_size,chess_size,chess_size) ,0)
                pygame.draw.ellipse(screen, (255,255,255), (self.x + x * chess_size,self.y + y * chess_size,chess_size,chess_size) ,1)
            else:
                pygame.draw.ellipse(screen, (155,155,155), (self.x + x * chess_size,self.y + y * chess_size,chess_size,chess_size) ,0)
                pygame.draw.ellipse(screen, (0,0,0), (self.x + x * chess_size,self.y + y * chess_size,chess_size,chess_size) ,1)
        for stpe in self.probably:
            pygame.draw.ellipse(screen, (108,148,255), (self.x + stpe[2] * chess_size,self.y + stpe[3] * chess_size,chess_size,chess_size) ,0)
        for i in self.probably:
            pygame.draw.line(screen,color[c],(i[4][0][0]*chess_size+chess_size/2+self.x,i[4][0][1]*chess_size+chess_size/2+self.y),(i[0]*chess_size+chess_size/2+self.x,i[1]*chess_size+chess_size/2+self.y),3)
            if len(i[4]) > 0:
                for line in range(len(i[4]))[1:]:
                    pygame.draw.line(screen,color[c],(i[4][line][0]*chess_size+chess_size/2+self.x,i[4][line][1]*chess_size+chess_size/2+self.y),(i[4][line-1][0]*chess_size+chess_size/2+self.x,i[4][line-1][1]*chess_size+chess_size/2+self.y),3)
            c+=1
                
    def createBoard(self):
        pygame.draw.rect(screen, (240,240,240), (self.x + 10 * chess_size ,self.y ,score_size,10*chess_size) ,0)
        font = pygame.font.SysFont("simsunnsimsun",20)
        font_now = font.render("当前执子方:",1,(0,0,0))
        screen.blit(font_now,(self.x + 10 * chess_size + score_size / 2 - font_now.get_width() / 2,self.y+30))
        if self.now == 1:
            pygame.draw.circle(screen, (0,0,0), (int(self.x + 10 * chess_size + score_size / 2) , self.y+100), 25, 0)
        elif self.now == -1:
            pygame.draw.circle(screen, (255,255,255), (int(self.x + 10 * chess_size + score_size / 2) , self.y+100), 25, 0)
        font_step = font.render("已下步数: "+str(self.step),1,(0,0,0))
        screen.blit(font_step,(self.x + 10 * chess_size + score_size / 2 - 140 / 2,self.y+200))
        font_aiB = font.render("黑棋AI模式:",1,(0,0,0))
        screen.blit(font_aiB,(self.x + 10 * chess_size + score_size / 2 - 140 / 2,self.y+250))
        font_aiW = font.render("白棋AI模式:",1,(0,0,0))
        screen.blit(font_aiW,(self.x + 10 * chess_size + score_size / 2 - 140 / 2,self.y+300))
        font_wg = font.render("外挂模式:",1,(0,0,0))
        screen.blit(font_wg,(self.x + 10 * chess_size + score_size / 2 - 140 / 2,self.y+350))
        pygame.draw.rect(screen,(0,0,0),(self.x + 10 * chess_size + score_size / 2 - 140 / 2 + 130,self.y+250,20,20),2)
        pygame.draw.rect(screen,(0,0,0),(self.x + 10 * chess_size + score_size / 2 - 140 / 2 + 130,self.y+300,20,20),2)
        pygame.draw.rect(screen,(0,0,0),(self.x + 10 * chess_size + score_size / 2 - 140 / 2 + 130,self.y+350,20,20),2)
        font_yes = font.render("√",2,(0,0,0))
        if board.aiB==1:
            screen.blit(font_yes,(self.x + 10 * chess_size + score_size / 2 - 140 / 2 + 130,self.y+250))
        if board.aiW==1:
            screen.blit(font_yes,(self.x + 10 * chess_size + score_size / 2 - 140 / 2 + 130,self.y+300))
        if board.wg==1:
            screen.blit(font_yes,(self.x + 10 * chess_size + score_size / 2 - 140 / 2 + 130,self.y+350))

class wg(object):
    def __init__(self, x, y, mx ,my):
        self.x=x
        self.y=y
        self.mx=mx
        self.my=my
    def create(self):
        font = pygame.font.SysFont("simsunnsimsun",12)
        pygame.draw.rect(screen,(255,255,255),(self.mx,self.my,50,90),0)
        pygame.draw.rect(screen,(0,0,0),(self.mx,self.my,50,90),1)
        pygame.draw.line(screen, (0,0,0), (self.mx,self.my+30), (self.mx+50,self.my+30), 1)
        pygame.draw.line(screen, (0,0,0), (self.mx,self.my+60), (self.mx+50,self.my+60), 1)
        pygame.draw.line(screen, (0,0,0), (self.mx+25,self.my+30), (self.mx+25,self.my+90), 1)
        font_k = font.render("移除棋子",1,(0,0,0))
        screen.blit(font_k,(25+self.mx+25-font_k.get_width(),self.my+5))
        font_b = font.render("黑棋:",1,(0,0,0))
        screen.blit(font_b,(20+self.mx+12-font_b.get_width(),self.my+35))
        font_w = font.render("白棋",1,(0,0,0))
        screen.blit(font_w,(20+self.mx+37-font_b.get_width(),self.my+35))
        font_kb = font.render("黑王",1,(0,0,0))
        screen.blit(font_kb,(20+self.mx+12-font_b.get_width(),self.my+65))
        font_kw = font.render("白王",1,(0,0,0))
        screen.blit(font_kw,(20+self.mx+37-font_b.get_width(),self.my+65))
    def change(self,z):
        board.state[self.x][self.y] = z
        pro()
        
        
def eat(f):
    if f[5]>1:
        board.state[int(abs(f[4][0][0]+f[0])/2)][int(abs(f[4][0][1]+f[1])/2)]=0
        if len(f[4])>1:
            for i in range(len(f[4]))[1:]:
                board.state[int(abs(f[4][i][0]+f[4][i-1][0])/2)][int(abs(f[4][i][1]+f[4][i-1][1])/2)]=0
# 求整体可下路径
def pro():
    board.maxstep = 1
    for i in range(10):
        for j in range(10):
            if board.state[i][j] == board.now or board.state[i][j] == board.now*2:
                board.choose = (i,j)
                rode(i,j,board.state,0,[])
                for z in board.probably:
                    if z[1]==z[3] and z[0]==z[2]:
                        board.probably.remove(z)
    board.probably = [x for x in board.probably if x[5]==board.maxstep]
    board.choose = (-1,-1)
                
# 求单个可下路径
def rode(x,y,a,stpe,already):
    stpe += 1
    next_step = rode_jump(x,y)
    for z in next_step:
        b=already[:]
        a[int((x+z[2])/2)][int((y+z[3])/2)] = 3
        b.append((z[2],z[3]))
        rode(z[2],z[3],a,stpe,b)
        a[int((x+z[2])/2)][int((y+z[3])/2)] = board.now*-1
    if len(next_step) == 0:
        board.probably.append (board.choose+(x,y,already,stpe))
    if board.maxstep < stpe:
        board.maxstep = stpe
    if stpe == 1 and next_step == []:
        rode_run(x,y)
# 求单格内可跳路径
def rode_jump(x,y):
    a = []
    if not (x<2 or y<2):
        if board.state[x-1][y-1] == board.now*-1 and board.state[x-2][y-2] == 0:
            a.append((x,y,x-2,y-2))
    if not (x>7 or y<2):
        if board.state[x+1][y-1] == board.now*-1 and board.state[x+2][y-2] == 0:
            a.append((x,y,x+2,y-2))
    if not (x<2 or y>7):
        if board.state[x-1][y+1] == board.now*-1 and board.state[x-2][y+2] == 0:
            a.append((x,y,x-2,y+2))
    if not (x>7 or y>7):
        if board.state[x+1][y+1] == board.now*-1 and board.state[x+2][y+2] == 0:
            a.append((x,y,x+2,y+2))
    return a
# 求单格内可走路径
def rode_run(x,y):
    a = []
    if not (x<1 or y<1) and board.state[x][y] == -1:
        if board.state[x-1][y-1] == 0:
            board.probably.append((x,y,x-1,y-1,[(x-1,y-1)],1))
    if not (x>8 or y<1) and board.state[x][y] == -1:
        if board.state[x+1][y-1] == 0:
            board.probably.append((x,y,x+1,y-1,[(x+1,y-1)],1))
    if not (x<1 or y>8) and board.state[x][y] == 1:
        if board.state[x-1][y+1] == 0:
            board.probably.append((x,y,x-1,y+1,[(x-1,y+1)],1))
    if not (x>8 or y>8) and board.state[x][y] == 1:
        if board.state[x+1][y+1] == 0:
            board.probably.append((x,y,x+1,y+1,[(x+1,y+1)],1))
# 加载界面
def GUI():
    board.createChess()
    board.createBoard()
    board.createAll()
def ready():
    pygame.draw.rect(screen,(255,255,255),((chess_size*10+space*2+score_size)/2-200,(chess_size*10+space*2)/2,400,100))
# 玩家下棋
def player(x,y):
    if board.choose == (-1,-1) and board.state[x][y] ==  board.now:
        board.choose = (x,y)
    elif board.choose == (x,y):
        board.choose = (-1,-1)
    elif board.choose != (-1,-1) and board.state[x][y] == board.now:
        board.choose = (x,y)
    elif board.choose != (x,y) and board.choose != (-1,-1) and [(board.probably[x][2],board.probably[x][3]) for x in range(len(board.probably))].count((x,y))>0:
        board.state[x][y] = board.now
        board.state[board.choose[0]][board.choose[1]] = 0
        eat([f for f in board.probably if f[0]==board.choose[0] and f[1]==board.choose[1] and f[2]==x and f[3]==y][0])
        board.choose = (-1,-1)
        board.probably = []
        board.now *= -1
        board.step += 1
        pro()

wg = wg(-1,-1,-1,-1)
board = checkerBoard(30,30)
for i in [0,2,4,6,8]:
    board.state[i+1][0] = 1
    board.state[i][1] = 1
    board.state[i+1][2] = 1
    board.state[i][3] = 1
    board.state[i+1][6] = -1
    board.state[i][7] = -1
    board.state[i+1][8] = -1
    board.state[i][9] = -1
state = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONUP:
            x,y = pygame.mouse.get_pos()
            if state == 1:
                if x > board.x + 10 * chess_size + score_size / 2 - 140 / 2 + 130 and x < board.x + 10 * chess_size + score_size / 2 - 140 / 2 + 150:
                    if y > board.y+250 and y < board.y + 270:
                        board.aiB= 1 if(board.aiB==0) else 0
                    elif y > board.y+300 and y < board.y + 320:
                        board.aiW=1 if(board.aiW==0) else 0
                    elif y > board.y+350 and y < board.y + 370:
                        board.wg=1 if(board.wg==0) else 0
                elif wg.mx!=-1 and wg.my!=-1 and x>wg.mx and x<wg.mx+50 and y>wg.my and y<wg.my+90:
                    if y<30+wg.my:
                        wg.change(0)
                    elif y<60+wg.my and x< 25+wg.mx:
                        wg.change(1)
                    elif y<60+wg.my:
                        wg.change(-1)
                    elif x<25+wg.mx:
                        wg.change(2)
                    else:
                        wg.change(-2)
                    wg.mx=-1
                    wg.my=-1
                elif wg.mx!=-1 and wg.my!=-1:
                    wg.mx=-1
                    wg.my=-1
                elif x >= board.x and x <= board.x+10 * chess_size and y >= board.y and y <= board.y+10 * chess_size and board.wg==0:
                    player(int((x-board.x)/chess_size),int((y-board.y)/chess_size))
                elif x >= board.x and x <= board.x+10 * chess_size and y >= board.y and y <= board.y+10 * chess_size:
                    wg.x=int((x-board.x)/chess_size)
                    wg.y=int((y-board.y)/chess_size)
                    wg.mx=x
                    wg.my=y
                    if(wg.y>4):
                        wg.my -= 90
            elif state == 0:
                if x > (chess_size*10+space*2+score_size)/2-200 and x < (chess_size*10+space*2+score_size)/2+200 and y>(chess_size*10+space*2)/2 and y<(chess_size*10+space*2)/2+100:
                    pro()
                    state = 1
                 
                                  
    screen.fill((230,230,230))
    
    if state == 1:
        GUI()
        if wg.mx!=-1 and wg.my!=-1:
            wg.create()
    elif state == 0:
        ready()
    
    pygame.display.update()
