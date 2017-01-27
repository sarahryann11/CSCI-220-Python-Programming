'''
Name: Sarah Nicholson

Ch 4. True/False
1. False
2. True
3. True
4. False
5. True
6. False
7. True
8. False
9. False
10. False

Ch. 4 Multiple Choice
1. D
2. B
3. D
4. C
5. D
6. D
7. D
8. B
9. A

Purpose: It is to create a game of tic-tac-toe and when the two players are done
playing, the screen will close.

Authenticity: It is my own work, and I also discussed it with Jason Hughes.
'''

from graphics import *

# get window
win = GraphWin('TicTacToe', 300, 300)
win.setCoords(0.5, 0.5, 3.5, 3.5)
def main():
    board()
    #center()
    #drawX()
    #drawY()
    gameplay()
    close()

def board():    
    # draw vertical lines
    line1 = Line(Point(1.5,0.5),Point(1.5,3.5))
    line1.draw(win)
    line2 = line1.clone()
    line2.move(1,0)
    line2.draw(win)
    # draw horizontal lines
    line3 = Line(Point(3.5,1.5),Point(0.5,1.5))
    line3.draw(win)
    line4 = line3.clone()
    line4.move(0,1)
    line4.draw(win)
    
def center():
    # get center points
    pt = win.getMouse()
    ptX = pt.getX()
    ptY = pt.getY()
    return Point(round(ptX), round(ptY))

def drawX(pt):
    # get X's
    valx = Text(pt,'X')
    valx.setSize(36)
    valx.draw(win)
    
def drawO(pt):
    # get O's
    valo = Text(pt,'O')
    valo.setSize(36)
    valo.draw(win)

def gameplay():
    # get clicks for X's and O's
    for i in range(9):
        if i%2 == 0:
              drawX(center())
        else:
              drawO(center())

def close():
    # get last click to exit
    Text(Point(2, 2), "Click again to close").draw(win)
    win.getMouse()
    win.close()

main()
