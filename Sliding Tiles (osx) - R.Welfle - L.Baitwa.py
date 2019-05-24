# Slide Puzzle
# By Al Sweigart al@inventwithpython.com
# http://inventwithpython.com/pygame
# Released under a "Simplified BSD" license

import pygame, sys, random, os
from pygame.locals import *

switch = 0 #this is a variable that is used later in the code to help the user switch 
           #between two iamges to use at the puzzle picture to solve 
IMAGE1 = pygame.image.load('magritte_1.bmp') #@@@@@@@@@@@@@@@@@@@@@@@@
IMAGE2 = pygame.image.load('magritte_2.bmp') #added a bunch of images so that \
IMAGE3 = pygame.image.load('magritte_3.bmp') #the objective of the sliding  \
IMAGE4 = pygame.image.load('magritte_4.bmp') #puzzle is to put together a \
IMAGE5 = pygame.image.load('magritte_5.bmp') #picture instead of lining up \
IMAGE6 = pygame.image.load('magritte_6.bmp') #numbers
IMAGE7 = pygame.image.load('magritte_7.bmp')
IMAGE8 = pygame.image.load('magritte_8.bmp')
IMAGE9 = pygame.image.load('magritte_9.bmp') 
IMAGE10 = pygame.image.load('magritte_10.bmp')
IMAGE11 = pygame.image.load('magritte_11.bmp') 
IMAGE12 = pygame.image.load('magritte_12.bmp')
IMAGE13 = pygame.image.load('magritte_13.bmp')
IMAGE14 = pygame.image.load('magritte_14.bmp') 
IMAGE15 = pygame.image.load('magritte_15.bmp')
IMAGE16 = pygame.image.load('magritte_16.bmp') 
IMAGE17 = pygame.image.load('magritte_17.bmp')
IMAGE18 = pygame.image.load('magritte_18.bmp')
IMAGE19 = pygame.image.load('magritte_19.bmp') 
IMAGE20 = pygame.image.load('magritte_20.bmp')
IMAGE21 = pygame.image.load('magritte_21.bmp') 
IMAGE22 = pygame.image.load('magritte_22.bmp')
IMAGE23 = pygame.image.load('magritte_23.bmp')
IMAGE24 = pygame.image.load('magritte_24.bmp') 
IMAGE25 = pygame.image.load('magritte_25.bmp')

# this is a list that contains all of the picture images
imagelist = [IMAGE25,IMAGE1,IMAGE2,IMAGE3,IMAGE4,IMAGE5,IMAGE6,IMAGE7,IMAGE8,IMAGE9,IMAGE10,IMAGE11,IMAGE12,IMAGE13,IMAGE14,IMAGE15,IMAGE16,IMAGE17,IMAGE18,IMAGE19,IMAGE20,IMAGE21,IMAGE22,IMAGE23,IMAGE24]

tIMAGE1 = pygame.image.load('ernst_1.bmp') #@@@@@@@@@@@@@@@@@@@@@@@@
tIMAGE2 = pygame.image.load('ernst_2.bmp') #added a bunch of images so that \
tIMAGE3 = pygame.image.load('ernst_3.bmp') #the objective of the sliding  \
tIMAGE4 = pygame.image.load('ernst_4.bmp') #puzzle is to put together a \
tIMAGE5 = pygame.image.load('ernst_5.bmp') #picture instead of lining up \
tIMAGE6 = pygame.image.load('ernst_6.bmp') #numbers
tIMAGE7 = pygame.image.load('ernst_7.bmp')
tIMAGE8 = pygame.image.load('ernst_8.bmp')
tIMAGE9 = pygame.image.load('ernst_9.bmp') 
tIMAGE10 = pygame.image.load('ernst_10.bmp')
tIMAGE11 = pygame.image.load('ernst_11.bmp') 
tIMAGE12 = pygame.image.load('ernst_12.bmp')
tIMAGE13 = pygame.image.load('ernst_13.bmp')
tIMAGE14 = pygame.image.load('ernst_14.bmp') 
tIMAGE15 = pygame.image.load('ernst_15.bmp')
tIMAGE16 = pygame.image.load('ernst_16.bmp') 
tIMAGE17 = pygame.image.load('ernst_17.bmp')
tIMAGE18 = pygame.image.load('ernst_18.bmp')
tIMAGE19 = pygame.image.load('ernst_19.bmp') 
tIMAGE20 = pygame.image.load('ernst_20.bmp')
tIMAGE21 = pygame.image.load('ernst_21.bmp') 
tIMAGE22 = pygame.image.load('ernst_22.bmp')
tIMAGE23 = pygame.image.load('ernst_23.bmp')
tIMAGE24 = pygame.image.load('ernst_24.bmp') 
tIMAGE25 = pygame.image.load('ernst_25.bmp')

# this is a list that contains all of the picture images
imagelist2 = [tIMAGE25,tIMAGE1,tIMAGE2,tIMAGE3,tIMAGE4,tIMAGE5,tIMAGE6,tIMAGE7,tIMAGE8,tIMAGE9,tIMAGE10,tIMAGE11,tIMAGE12,tIMAGE13,tIMAGE14,tIMAGE15,tIMAGE16,tIMAGE17,tIMAGE18,tIMAGE19,tIMAGE20,tIMAGE21,tIMAGE22,tIMAGE23,tIMAGE24]


BOARDWIDTH = 5  # number of columns in the board, which I have increased
BOARDHEIGHT = 5 # number of rows in the board, which I have increased
TILESIZE = 50 # size of the tiles themselves, which I have decreased 
WINDOWWIDTH = 800  #dimensions of window itself, which I increased
WINDOWHEIGHT = 380 #dimensions of window itself, which I decreased
FPS = 70 # increase FPS, so that new puzzle can be created faster or the computer can solve it quicker
BLANK = None

#                 R    G    B
BLACK =         (  0,   0,   0)
WHITE =         (255, 255, 255)
RED =           (255,   0,   0) # changed to "red" RGB values
GOLD =          (255, 215,   0) # changed RGB values, and corresponding colour variable name
GREEN =         (  0, 204,   0)

BGCOLOR = GOLD # changed corresponding variable name
TILECOLOR = BLACK # changed tile colour to black
TEXTCOLOR = WHITE
BORDERCOLOR = RED # changed colour variable name
BASICFONTSIZE = 30 # increased font size

BUTTONCOLOR = WHITE
BUTTONTEXTCOLOR = BLACK
MESSAGECOLOR = BLACK # changed message colour to black

XMARGIN = int((WINDOWWIDTH - (TILESIZE * BOARDWIDTH + (BOARDWIDTH - 1))) / 2)
YMARGIN = int((WINDOWHEIGHT - (TILESIZE * BOARDHEIGHT + (BOARDHEIGHT - 1))) / 2)

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, RESET_SURF, RESET_RECT, NEW_SURF, NEW_RECT, SOLVE_SURF, SOLVE_RECT, HARD_SURF, HARD_RECT, FIVE_SURF, FIVE_RECT, SOLV20_SURF, SOLV20_RECT, MUSIC_SURF, MUSIC_RECT, HARD2_SURF, HARD2_RECT, switch #added HARD_SURF, HARD_RECT, FIVE_SURF, FIVE_RECT, SOLV20_SURF, SOLV20_RECT, IMAGE as global variables

    pygame.init()
    
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Sliding Tiles') # changed window caption
    BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)
    
    
    MUSIC_SURF, MUSIC_RECT = makeText('Image #2 Easy Game',TEXTCOLOR, TILECOLOR, WINDOWWIDTH - 750, WINDOWHEIGHT - 227.5)#added button to initiate easy game with second image
    HARD2_SURF, HARD2_RECT = makeText('Image #2 Hard Game',TEXTCOLOR, TILECOLOR, WINDOWWIDTH - 750, WINDOWHEIGHT - 152.5)#added button to initiate hard game with second image
    FIVE_SURF,  FIVE_RECT  = makeText('Reset Last Five',TEXTCOLOR, TILECOLOR, WINDOWWIDTH - 250, WINDOWHEIGHT - 265) #added to select an option to reset last five move of a game
    RESET_SURF, RESET_RECT = makeText('Reset All',TEXTCOLOR, TILECOLOR, WINDOWWIDTH - 250, WINDOWHEIGHT - 227.5) # changed vertical/horizontal location of menu items 
    NEW_SURF,   NEW_RECT   = makeText('Image #1 Easy Game',TEXTCOLOR, TILECOLOR, WINDOWWIDTH - 750, WINDOWHEIGHT - 265) # changed vertical location of menu items
    HARD_SURF,  HARD_RECT  = makeText('Image #1 Hard Game',TEXTCOLOR, TILECOLOR, WINDOWWIDTH - 750, WINDOWHEIGHT - 190) # adding a harder mode, so this is the button for it
    SOLV20_SURF, SOLV20_RECT = makeText('Solve 20 Moves',TEXTCOLOR, TILECOLOR, WINDOWWIDTH - 250, WINDOWHEIGHT - 190) #adding option to help solve first 20 moves
    SOLVE_SURF, SOLVE_RECT = makeText('Solve All',    TEXTCOLOR, TILECOLOR, WINDOWWIDTH - 250, WINDOWHEIGHT - 152.5) # changed vertical location of menu items

    mainBoard, solutionSeq = generateNewPuzzle(0) #changed paramter to zero, so that a 'new game' doesn't start when program opens
    SOLVEDBOARD = getStartingBoard() # a solved board is the same as the board in a start state.
    allMoves = [] # list of moves made from the solved configuration

    while True: # main game loop
        slideTo = None # the direction, if any, a tile should slide
        msg = 'Click tile or press arrow keys to slide.' # contains the message to show in the upper left corner.
        if mainBoard == SOLVEDBOARD:
            msg ='Not bad for a human!' #change this message to something funnier!

        drawBoard(mainBoard, msg)

        checkForQuit()
        for event in pygame.event.get(): # event handling loop
            if event.type == MOUSEBUTTONUP:
                spotx, spoty = getSpotClicked(mainBoard, event.pos[0], event.pos[1])

                if (spotx, spoty) == (None, None):
                    
                    if RESET_RECT.collidepoint(event.pos):
                        resetAnimation(mainBoard, allMoves) # clicked on Reset All button
                        allMoves = []
                    elif HARD2_RECT.collidepoint(event.pos):
                        switch = 1 #this variable makes it so that image number 2 is used for the game
                        mainBoard, solutionSeq = generateNewPuzzle(350) # set parameter to 350, so that a game is created with 350 random slides
                        allMoves = [] 
                    elif MUSIC_RECT.collidepoint(event.pos):
                        switch = 1
                        mainBoard, solutionSeq = generateNewPuzzle(100) # set parameter to 350, so that a game is created with 350 random slides
                        allMoves = []  
                    elif FIVE_RECT.collidepoint(event.pos):
                        resetLastFive(mainBoard, allMoves) # clicked on Reset Last Five button
                        del allMoves[-5:]   #not resetting entire list, just removing last five moves, so that "Reset All" still works
                    elif NEW_RECT.collidepoint(event.pos):
                        switch = 0 #this variable makes it so that image number 1 is used for the game
                        mainBoard, solutionSeq = generateNewPuzzle(100) # clicked on Easy Game button
                        allMoves = []                                   # creates new game with 100 random moves
                    elif HARD_RECT.collidepoint(event.pos):
                        switch = 0
                        mainBoard, solutionSeq = generateNewPuzzle(350) # clicked on Hard Game button
                        allMoves = []                                   # creates new game with 350 random moves
                    elif SOLVE_RECT.collidepoint(event.pos):
                        resetAnimation(mainBoard, solutionSeq + allMoves) # clicked on Solve button
                        allMoves = []
                        solutionSeq = []   #setting solutionSeq to a blank list, since these moves no longer need to be recorded since puzzle is now solved 
                    elif SOLV20_RECT.collidepoint(event.pos):                   # clicked on Solve First 20 button
                        resetAnimation(mainBoard, solutionSeq[-20:] + allMoves) #solutionSeq[-20:] makes it so that only first 20 moves are solves
                        del solutionSeq[-20:] #deleting the first twenty solved moves from the solutionSeq list
                        allMoves = []
                        if mainBoard == SOLVEDBOARD: #checking to see if board is in solved state, so that solutionSeq and allMoves lists can be made blank as the moves are no longer needed
                            solutionSeq = []
                            allMoves = []
                else:

                    blankx, blanky = getBlankPosition(mainBoard)
                    if spotx == blankx + 1 and spoty == blanky:
                        slideTo = LEFT
                    elif spotx == blankx - 1 and spoty == blanky:
                        slideTo = RIGHT
                    elif spotx == blankx and spoty == blanky + 1:
                        slideTo = UP
                    elif spotx == blankx and spoty == blanky - 1:
                        slideTo = DOWN

            elif event.type == KEYUP:
                if event.key in (K_LEFT, K_a) and isValidMove(mainBoard, LEFT):
                    slideTo = LEFT
                elif event.key in (K_RIGHT, K_d) and isValidMove(mainBoard, RIGHT):
                    slideTo = RIGHT
                elif event.key in (K_UP, K_w) and isValidMove(mainBoard, UP):
                    slideTo = UP
                elif event.key in (K_DOWN, K_s) and isValidMove(mainBoard, DOWN):
                    slideTo = DOWN

        if slideTo:
            slideAnimation(mainBoard, slideTo, 'Click tile or press arrow keys to slide.', 8) # show slide on screen
            makeMove(mainBoard, slideTo)
            allMoves.append(slideTo) 
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def terminate():
    pygame.quit()
    sys.exit()


def checkForQuit():
    for event in pygame.event.get(QUIT): 
        terminate()
    for event in pygame.event.get(KEYUP): 
        if event.key == K_ESCAPE:
            terminate() 
        pygame.event.post(event) 


def getStartingBoard():
   
    
    
    counter = 1
    board = []
    for x in range(BOARDWIDTH):
        column = []
        for y in range(BOARDHEIGHT):
            column.append(counter)
            counter += BOARDWIDTH
        board.append(column)
        counter -= BOARDWIDTH * (BOARDHEIGHT - 1) + BOARDWIDTH - 1

    board[BOARDWIDTH-1][BOARDHEIGHT-1] = BLANK
    return board


def getBlankPosition(board):

    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            if board[x][y] == BLANK:
                return (x, y)


def makeMove(board, move):
    blankx, blanky = getBlankPosition(board)

    if move == UP:
        board[blankx][blanky], board[blankx][blanky + 1] = board[blankx][blanky + 1], board[blankx][blanky]
    elif move == DOWN:
        board[blankx][blanky], board[blankx][blanky - 1] = board[blankx][blanky - 1], board[blankx][blanky]
    elif move == LEFT:
        board[blankx][blanky], board[blankx + 1][blanky] = board[blankx + 1][blanky], board[blankx][blanky]
    elif move == RIGHT:
        board[blankx][blanky], board[blankx - 1][blanky] = board[blankx - 1][blanky], board[blankx][blanky]


def isValidMove(board, move):
    blankx, blanky = getBlankPosition(board)
    return (move == UP and blanky != len(board[0]) - 1) or \
           (move == DOWN and blanky != 0) or \
           (move == LEFT and blankx != len(board) - 1) or \
           (move == RIGHT and blankx != 0)


def getRandomMove(board, lastMove=None):

    validMoves = [UP, DOWN, LEFT, RIGHT]


    if lastMove == UP or not isValidMove(board, DOWN):
        validMoves.remove(DOWN)
    if lastMove == DOWN or not isValidMove(board, UP):
        validMoves.remove(UP)
    if lastMove == LEFT or not isValidMove(board, RIGHT):
        validMoves.remove(RIGHT)
    if lastMove == RIGHT or not isValidMove(board, LEFT):
        validMoves.remove(LEFT)


    return random.choice(validMoves)


def getLeftTopOfTile(tileX, tileY):
    left = XMARGIN + (tileX * TILESIZE) + (tileX - 1)
    top = YMARGIN + (tileY * TILESIZE) + (tileY - 1)
    return (left, top)


def getSpotClicked(board, x, y):

    for tileX in range(len(board)):
        for tileY in range(len(board[0])):
            left, top = getLeftTopOfTile(tileX, tileY)
            tileRect = pygame.Rect(left, top, TILESIZE, TILESIZE)
            if tileRect.collidepoint(x, y):
                return (tileX, tileY)
    return (None, None)





def drawTile(tilex, tiley, number, adjx=0, adjy=0):     
    left, top = getLeftTopOfTile(tilex, tiley)
    pygame.draw.rect(DISPLAYSURF, TILECOLOR, (left + adjx, top + adjy, TILESIZE, TILESIZE))
    if switch == 0:
        textSurf = imagelist[number]  #the "imagelist" list is used here to place each tiled image in the list to the sliding puzzle board
    if switch == 1:
        textSurf = imagelist2[number]  #the "imagelist" list is used here to place each tiled image in the list to the sliding puzzle board
    textRect = textSurf.get_rect()
    textRect.center = left + int(TILESIZE / 2) + adjx, top + int(TILESIZE / 2) + adjy
    DISPLAYSURF.blit(textSurf, textRect)


def makeText(text, color, bgcolor, top, left):

    textSurf = BASICFONT.render(text, True, color, bgcolor)
    textRect = textSurf.get_rect()
    textRect.topleft = (top, left)
    return (textSurf, textRect)


def drawBoard(board, message):
    DISPLAYSURF.fill(BGCOLOR)
    if message:
        textSurf, textRect = makeText(message, MESSAGECOLOR, BGCOLOR, 5, 5)
        DISPLAYSURF.blit(textSurf, textRect)

    for tilex in range(len(board)):
        for tiley in range(len(board[0])):
            if board[tilex][tiley]:
                drawTile(tilex, tiley, board[tilex][tiley])

    left, top = getLeftTopOfTile(0, 0)
    width = BOARDWIDTH * TILESIZE
    height = BOARDHEIGHT * TILESIZE
    pygame.draw.rect(DISPLAYSURF, BORDERCOLOR, (left - 5, top - 5, width + 11, height + 11), 4)

    DISPLAYSURF.blit(MUSIC_SURF, MUSIC_RECT)#this code displays the image #2 easy game
    DISPLAYSURF.blit(HARD2_SURF, HARD2_RECT)#this code displays the image #2 hard game
    DISPLAYSURF.blit(FIVE_SURF, FIVE_RECT) #this code displays the "reset last five" option box
    DISPLAYSURF.blit(RESET_SURF, RESET_RECT)
    DISPLAYSURF.blit(NEW_SURF, NEW_RECT)
    DISPLAYSURF.blit(HARD_SURF, HARD_RECT) #this code displays the box to choose a harder version of the game
    DISPLAYSURF.blit(SOLV20_SURF, SOLV20_RECT) #this code siplays the box to choose to solve first twenty moves
    DISPLAYSURF.blit(SOLVE_SURF, SOLVE_RECT)


def slideAnimation(board, direction, message, animationSpeed):

    blankx, blanky = getBlankPosition(board)
    if direction == UP:
        movex = blankx
        movey = blanky + 1
    elif direction == DOWN:
        movex = blankx
        movey = blanky - 1
    elif direction == LEFT:
        movex = blankx + 1
        movey = blanky
    elif direction == RIGHT:
        movex = blankx - 1
        movey = blanky

    drawBoard(board, message)
    baseSurf = DISPLAYSURF.copy()
    moveLeft, moveTop = getLeftTopOfTile(movex, movey)
    pygame.draw.rect(baseSurf, BGCOLOR, (moveLeft, moveTop, TILESIZE, TILESIZE))

    for i in range(0, TILESIZE, animationSpeed):
        checkForQuit()
        DISPLAYSURF.blit(baseSurf, (0, 0))
        if direction == UP:
            drawTile(movex, movey, board[movex][movey], 0, -i)
        if direction == DOWN:
            drawTile(movex, movey, board[movex][movey], 0, i)
        if direction == LEFT:
            drawTile(movex, movey, board[movex][movey], -i, 0)
        if direction == RIGHT:
            drawTile(movex, movey, board[movex][movey], i, 0)

        pygame.display.update()
        FPSCLOCK.tick(FPS)


def generateNewPuzzle(numSlides):
    sequence = []
    board = getStartingBoard()
    drawBoard(board, '')
    pygame.display.update()
    pygame.time.wait(500) 
    lastMove = None
    for i in range(numSlides):
        move = getRandomMove(board, lastMove)
        slideAnimation(board, move, 'Generating new puzzle...', animationSpeed=int(TILESIZE / 3))
        makeMove(board, move)
        sequence.append(move)
        lastMove = move
    return (board, sequence)


def resetAnimation(board, allMoves):
    revAllMoves = allMoves[:]
    revAllMoves.reverse()

    for move in revAllMoves:
        if move == UP:
            oppositeMove = DOWN
        elif move == DOWN:
            oppositeMove = UP
        elif move == RIGHT:
            oppositeMove = LEFT
        elif move == LEFT:
            oppositeMove = RIGHT
        slideAnimation(board, oppositeMove, '', animationSpeed=int(TILESIZE / 2))
        makeMove(board, oppositeMove)
        

def resetLastFive(board, allMoves): # new function for undoing only last five moves that the user has made
    revFiveMoves = allMoves[-5:] #making it so that we only return the last five items in the 
    revFiveMoves.reverse()       #allMoves list, which holds all the moves that the user has made in the current game

    for move in revFiveMoves:
        if move == UP:
            oppositeMove = DOWN
        elif move == DOWN:
            oppositeMove = UP
        elif move == RIGHT:
            oppositeMove = LEFT
        elif move == LEFT:
            oppositeMove = RIGHT
        slideAnimation(board, oppositeMove, '', animationSpeed=int(TILESIZE / 2))
        makeMove(board, oppositeMove)

if __name__ == '__main__':
    main()