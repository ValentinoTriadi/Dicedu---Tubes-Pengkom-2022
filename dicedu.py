from time import *
from pygame.locals import *
import pygame, os, sys
from mechanism import *
from gui import *

def init_map():
    global lis, titik, tempat, posisi
    lis = []
    titik = []
    tempat = []
    posisi = []
    lis, titik, tempat = makeMap(titik, lis, tempat)

def init_all():
    init_color()
    init_display()
    init_map()
    init_sound()
    init_text()

def init_display():
    #screen
    global screen
    screen = pygame.display.set_mode((800, 600))

    #important
    global path, star, chal, en
    path = pygame.image.load("Resource\\Background\\tile jalan.png")
    star = pygame.image.load("Resource\\Background\\start tile.png")
    chal = pygame.image.load("Resource\\Background\\challenge.png")
    en = pygame.image.load("Resource\\Background\\end.png")

    #player
    global p1, p2, p3, p4
    p1 = pygame.image.load("Resource\\Character\\blue.png")
    p2 = pygame.image.load("Resource\\Character\\green.png")
    p3 = pygame.image.load("Resource\\Character\\red.png")
    p4 = pygame.image.load("Resource\\Character\\yellow.png")

    #background
    global bg1, bg2, bg3, bg4, bg5, bg6, bg7, bg8, bg9, bg10, bg11, bg12
    bg1 = pygame.image.load("Resource\\Background\\flower.png")
    bg2 = pygame.image.load("Resource\\Background\\log 2.png")
    bg3 = pygame.image.load("Resource\\Background\\log.png")
    bg4 = pygame.image.load("Resource\\Background\\mushroom.png")
    bg5 = pygame.image.load("Resource\\Background\\bg w grass.png")
    bg6 = pygame.image.load("Resource\\Background\\rock.png")
    bg7 = pygame.image.load("Resource\\Background\\rock 2.png")
    bg8 = pygame.image.load("Resource\\Background\\sunflower.png")
    bg9 = pygame.image.load("Resource\\Background\\tree 2.png")
    bg10 = pygame.image.load("Resource\\Background\\tree w apple.png")
    bg11 = pygame.image.load("Resource\\Background\\tree.png")
    bg12 = pygame.image.load("Resource\\Background\\back.png")

    #dice
    global dice1, dice2, dice3, dice4, dice5, dice6
    dice1 = pygame.image.load("Resource\\Dice\\one-01.png")
    dice2 = pygame.image.load("Resource\\Dice\\two-01.png")
    dice3 = pygame.image.load("Resource\\Dice\\three-01.png")
    dice4 = pygame.image.load("Resource\\Dice\\four-01.png")
    dice5 = pygame.image.load("Resource\\Dice\\five-01.png")
    dice6 = pygame.image.load("Resource\\Dice\\six-01.png")

    #window
    global choose1, choose2, choose3, choose4, welcome, story, howto, mennu, sidebar, icon_window
    global win_player1, win_player2, win_player3, win_player4
    choose1 = pygame.image.load("Resource\\Window\\choose1.png")
    choose2 = pygame.image.load("Resource\\Window\\choose2.png")
    choose3 = pygame.image.load("Resource\\Window\\choose3.png")
    choose4 = pygame.image.load("Resource\\Window\\choose4.png")
    welcome = pygame.image.load("Resource\\Window\\welcome.png")
    story = pygame.image.load("Resource\\Window\\storyline.png")
    howto = pygame.image.load("Resource\\Window\\howto.png")
    mennu = pygame.image.load("Resource\\Window\\menu.png")
    sidebar = pygame.image.load("Resource\\Window\\side bar.png")
    win_player1 = pygame.image.load("Resource\\Window\\Win\\player1.png")
    win_player2 = pygame.image.load("Resource\\Window\\Win\\player2.png")
    win_player3 = pygame.image.load("Resource\\Window\\Win\\player3.png")
    win_player4 = pygame.image.load("Resource\\Window\\Win\\player4.png")
    icon_window = pygame.image.load("Resource\\Window\\icon.png")

    #sidebar
    global sp1, sp2, sp3, sp4
    sp1 = pygame.image.load("Resource\\Window\\1.png")
    sp2 = pygame.image.load("Resource\\Window\\2.png")
    sp3 = pygame.image.load("Resource\\Window\\3.png")
    sp4 = pygame.image.load("Resource\\Window\\4.png")

def init_color():
    #color
    global white, green, blue, krem, black, coklat
    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)
    krem = (253, 175, 107)
    black = (0, 0, 0)
    coklat = (226, 194, 142)

def init_sound():
    global main_musik, klik1, next1, masukchallenge, dicesound, sound_gamestart, sound_win, sound_storyline
    main_musik = pygame.mixer.Sound("Resource\\Music\\main.mp3")
    klik1 = pygame.mixer.Sound("Resource\\Music\\click1.wav")
    next1 = pygame.mixer.Sound("Resource\\Music\\next.wav")
    masukchallenge = pygame.mixer.Sound("Resource\\Music\\challenge.mp3")
    dicesound = pygame.mixer.Sound("Resource\\Music\\dice.mp3")
    sound_gamestart = pygame.mixer.Sound("Resource\\Music\\gamestart.wav")
    sound_win = pygame.mixer.Sound("Resource\\Music\\win1.wav")
    sound_storyline = pygame.mixer.Sound("Resource\\Music\\storyline.wav")
    
def init_text():
    #font
    global font1, roll_text, watermark
    font1 = pygame.font.Font('Resource\\Font\\Stdw.ttf', 25)
    roll_text = font1.render('Roll Dice', True, green, blue)
    watermark = font1.render('233, 239, 269, 295; 196-J\'22', True, coklat)

def tiles(map1):  
    for y, line in enumerate(map1):
        for x, c in enumerate(line):
            if c == 1:
                screen.blit(p1, (x * 30, y * 30))
            elif c == 2:
                screen.blit(p2, (x * 30, y * 30))
            elif c == 3:
                screen.blit(p4, (x * 30, y * 30))
            elif c == 4:
                screen.blit(p3, (x * 30, y * 30))
            elif c == "*":
                screen.blit(path, (x * 30, y * 30))
            elif c == "S":
                screen.blit(star, (x * 30, y * 30))
            elif c == "X":
                screen.blit(en, (x * 30, y * 30))
            elif c == "!":
                screen.blit(chal, (x * 30, y * 30))
            elif c == ".":
                screen.blit(bg1, (x * 30, y * 30))
            elif c == ",":
                screen.blit(bg2, (x * 30, y * 30))
            elif c == "@":
                screen.blit(bg3, (x * 30, y * 30))
            elif c == "$":
                screen.blit(bg4, (x * 30, y * 30))
            elif c == " ":
                screen.blit(bg5, (x * 30, y * 30))
            elif c == "-":
                screen.blit(bg6, (x * 30, y * 30))
            elif c == "%":
                screen.blit(bg7, (x * 30, y * 30))
            elif c == ">":
                screen.blit(bg8, (x * 30, y * 30))
            elif c == "<":
                screen.blit(bg9, (x * 30, y * 30))
            elif c == "?":
                screen.blit(bg10, (x * 30, y * 30))
            elif c == "+":
                screen.blit(bg11, (x * 30, y * 30))
            elif c == "#":
                screen.blit(bg12, (x * 30, y * 30))

def showDice(dice):
    pygame.mixer.Sound.play(dicesound)
    if dice == 1:
        screen.blit(dice1, (600, 0))
    elif dice == 2:
        screen.blit(dice2, (600, 0))
    elif dice == 3:
        screen.blit(dice3, (600, 0))
    elif dice == 4:
        screen.blit(dice4, (600, 0))
    elif dice == 5:
        screen.blit(dice5, (600, 0))
    elif dice == 6:
        screen.blit(dice6, (600, 0))
    pygame.display.update()

def showSidebar(i):
    if i == 0:
        screen.blit(sp1, (600, 0))
    elif i == 1:
        screen.blit(sp2, (600, 0))
    elif i == 2:
        screen.blit(sp3, (600, 0))
    elif i == 3:
        screen.blit(sp4, (600, 0))

def showPlayerNum(num):
    if num == 1:
        screen.blit(choose1, (0,0))
    elif num == 2:
        screen.blit(choose2, (0,0))
    elif num == 3:
        screen.blit(choose3, (0,0))
    elif num == 4:
        screen.blit(choose4, (0,0))

def main_game(lis, posisi, tempat, titik):
    posisi = choose_player(posisi)
    loop = 1; i = 0; win = False
    screen.blit(sidebar, (600,0))
    while loop and not win:    
        tiles(lis)
        showSidebar(i)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                loop = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 645 <= mouse[0] <= 755 and 240 <= mouse[1] <= 290:
                    lis, posisi, dice = diceRoll(i, lis, posisi, titik, tempat)
                    showDice(dice)
                    lis = updateMap(posisi[i] - dice, lis, posisi, tempat, titik)
                    sleep(1)
                    tiles(lis)
                    pygame.display.update()  
                    if posisi[i] == len(titik) - 1:
                        win = True
                    elif posisi[i] in tempat:
                        pygame.mixer.Sound.play(masukchallenge)
                        sleep(1)
                        if mulai():
                            posisi[i] += 3
                            lis = updateMap(posisi[i], lis, posisi, tempat, titik)
                            lis = updateMap(posisi[i] - 3, lis, posisi, tempat, titik)
                            tiles(lis)
                        else:
                            posisi[i] -= 3 
                            lis = updateMap(posisi[i], lis, posisi, tempat, titik)
                            lis = updateMap(posisi[i] + 3, lis, posisi, tempat, titik)
                            tiles(lis)
                    if not win:
                        i += 1
        if i > len(posisi) - 1:
            i = 0      
        mouse = pygame.mouse.get_pos()
        pygame.display.update()  
    if win:
        pygame.mixer.Sound.play(sound_win)
        sleep(1)
        win_screen(i)
    
def welcome_screen():
    screen.blit(welcome, (0,0))
    screen.blit(watermark, (270, 535))
    pencet = False
    while not pencet:
        global mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 315 <= mouse[0] <= 475 and 240 <= mouse[1] <= 305:
                    pencet = True
                elif 315 <= mouse[0] <= 475 and 320 <= mouse[1] <= 385:
                    pencet = True
                elif 760 <= mouse[0] <= 785 and 10 <= mouse[1] <= 30:
                    pencet = True
        pygame.display.update()
        mouse = pygame.mouse.get_pos()
    if pencet:
        if 315 <= mouse[0] <= 475 and 240 <= mouse[1] <= 305:
            pygame.mixer.Sound.play(klik1)
            main_game(lis, posisi, tempat, titik)
        elif 315 <= mouse[0] <= 475 and 320 <= mouse[1] <= 385:
            pygame.mixer.Sound.play(klik1)
            menu_screen()
        elif 760 <= mouse[0] <= 785 and 10 <= mouse[1] <= 30:
            pygame.quit()
       
def menu_screen():
    screen.blit(mennu, (0,0))
    pygame.display.update() 
    pencet = False
    while not pencet:
        global mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 255 <= mouse[0] <= 520 and 250 <= mouse[1] <= 320:
                    pencet = True
                elif 260 <= mouse[0] <= 520 and 350  <= mouse[1] <= 420:
                    pencet = True
                elif 10 <= mouse[0] <= 65 and 530 <= mouse[1] <= 580:
                    pencet = True
        pygame.display.update()
        mouse = pygame.mouse.get_pos()

    if pencet:
        if 255 <= mouse[0] <= 520 and 250 <= mouse[1] <= 320:
            pygame.mixer.Sound.play(klik1)
            storyline_screen()
        elif 260 <= mouse[0] <= 520 and 350  <= mouse[1] <= 420:
            pygame.mixer.Sound.play(klik1)
            tutorials_screen()
        elif 10 <= mouse[0] <= 65 and 530 <= mouse[1] <= 580:
            pygame.mixer.Sound.play(klik1)
            welcome_screen()

def tutorials_screen():
    screen.blit(howto, (0,0))
    pygame.display.update() 
    pencet = False
    while not pencet:
        global mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 10 <= mouse[0] <= 65 and 535 <= mouse[1] <= 580:
                    pencet = True
        pygame.display.update()
        mouse = pygame.mouse.get_pos()
    if pencet:
        if 10 <= mouse[0] <= 65 and 535 <= mouse[1] <= 580:
            pygame.mixer.Sound.play(klik1)
            menu_screen()

def storyline_screen():
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.Sound.play(sound_storyline)
    screen.blit(story, (0,0))
    pygame.display.update() 
    pencet = False
    while not pencet:
        global mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 12 <= mouse[0] <= 65 and 530 <= mouse[1] <= 580:
                    pencet = True
        pygame.display.update()
        mouse = pygame.mouse.get_pos()

    if pencet:
        if 12 <= mouse[0] <= 530 and 65 <= mouse[1] <= 580:
            pygame.mixer.Sound.stop(sound_storyline)
            pygame.mixer.Sound.play(klik1)
            pygame.mixer.music.set_volume(1.0)
            menu_screen()

def win_screen(playerNum):
    if playerNum == 0:
        screen.blit(win_player1, (0,0))
    elif playerNum == 1:
        screen.blit(win_player2, (0,0))
    elif playerNum == 2:
        screen.blit(win_player4, (0,0))
    elif playerNum == 3:
        screen.blit(win_player3, (0,0))
    
    pencet = False
    while not pencet:
        global mouse
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 675 <= mouse[0] <= 780 and 530 <= mouse[1] <= 575:
                    pencet = True
        mouse = pygame.mouse.get_pos()
    
    if pencet:
        if 675 <= mouse[0] <= 780 and 530 <= mouse[1] <= 575:
            pygame.mixer.Sound.play(klik1)
            init_map()
            welcome_screen()

def choose_player(posisi):
    pencet = False
    jumlah_player = 1

    screen.blit(choose1, (0,0))

    #fungsi pilih player
    while len(posisi) == 0  or not pencet:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    pygame.mixer.Sound.play(next1)
                    jumlah_player = (jumlah_player % 4) + 1
                    showPlayerNum(jumlah_player)
                if event.key == pygame.K_LEFT:
                    pygame.mixer.Sound.play(next1)
                    if jumlah_player == 1:
                        jumlah_player = 4
                    else:
                        jumlah_player -= 1
                    showPlayerNum(jumlah_player)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 12 <= mouse[0] <= 66 and 20 <= mouse[1] <= 75:
                    pygame.mixer.Sound.play(klik1)
                    welcome_screen()
                elif 280 <= mouse[0] <= 530 and 420 <= mouse[1] <= 520:
                    pygame.mixer.Sound.play(sound_gamestart)
                    posisi = [0 for i in range(jumlah_player)]
                    pencet = True
                elif 255 <= mouse[0] <= 315 and 245 <= mouse[1] <= 300:
                    pygame.mixer.Sound.play(next1)
                    if jumlah_player == 1:
                        jumlah_player = 4
                    else:
                        jumlah_player -= 1
                    showPlayerNum(jumlah_player)
                elif 500 <= mouse[0] <= 560 and 245 <= mouse[1] <= 300:
                    pygame.mixer.Sound.play(next1)
                    jumlah_player = (jumlah_player % 4) + 1
                    showPlayerNum(jumlah_player)
        mouse = pygame.mouse.get_pos()
        pygame.display.update()
    return posisi

pygame.init(); 
if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)
init_all()

pygame.display.set_caption("Dicedu The Game")
pygame.display.set_icon(icon_window)
pygame.mixer.music.load("Resource\\Music\\main.mp3")
pygame.mixer.music.play(-1)

welcome_screen()
pygame.quit()