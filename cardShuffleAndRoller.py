'''
Sarah Nicholson

Outputs how many cards you want (randomly) with the blackjack values
and randomly rolls a pair of die.
'''

# Graphics program to roll a pair of dice. Uses custom widgets
# Button and DieView.

from random import *
from graphics import *

def main():
    n = askUser()
    for i in range(n):
        card = drawCard()
        cardInformation(i,card)
    
    # create the application window
    win = GraphWin("Dice Roller")
    win.setCoords(0, 0, 10, 10)
    win.setBackground("green2")

    # Draw the interface widgets
    die1 = DieView(win, Point(3,7), 2)
    die2 = DieView(win, Point(7,7), 2)
    rollButton = Button(win, Point(5,4.5), 6, 1, "Roll Dice")
    rollButton.activate()
    quitButton = Button(win, Point(5,1), 2, 1, "Quit")

    # Event loop
    pt = win.getMouse()
    while not quitButton.clicked(pt):
        if rollButton.clicked(pt):
            #gets random colors when roll button is clicked
            color = color_rgb(randrange(0,256),randrange(0,256),randrange(0,256))
            value1 = randrange(1,7)
            die1.setValue(value1)
            #sets the color of the first die
            die1.setColor(color)
            value2 = randrange(1,7)
            die2.setValue(value2)
            #sets the color of the second die
            die2.setColor(color)
            quitButton.activate()
        pt = win.getMouse()

    # close up shop
    win.close()
    
class Card:
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit

    def getRank(self):
        #Gets what the value of the card is
        ranks = ('Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King')
        return ranks[self.rank-1]

    def getSuit(self):
        #Gets what suit the card is
        suits = ('Clubs','Diamonds','Hearts','Spades')
        suitss = suits[['c','d','h','s'].index(self.suit)]
        return suitss

    def BJvalue(self):
        #Returns the blackjack value of the card
        if self.rank > 10:
            self.value = 10
        else:
            self.value = self.rank
        return self.value

    def __str__(self):
        #Returns the card number and suit
        return self.getRank() + ' of ' + self.getSuit()

def askUser():
    #asks user how many cards they want to draw
    n = 0
    n = eval(input('Enter how many cards you want: '))
    return n

def drawCard():
    #draws the card
    rank,suit = randomCard()
    card = Card(rank,suit)
    return card

def randomCard():
    #picks a random card
    rank = randint(1,13)
    suit = ['c','d','h','s'][randint(0,3)]
    return rank,suit

def cardInformation(i,card):
    #outputs the card's information
    print('Card',i+1,'is a',card, 'with a Blackjack value of',card.BJvalue())

# dieview.py
class DieView:
    """ DieView is a widget that displays a graphical representation
    of a standard six-sided die."""
    
    def __init__(self, win, center, size):
        """Create a view of a die, e.g.:
           d1 = GDie(myWin, Point(40,50), 20)
        creates a die centered at (40,50) having sides
        of length 20."""

        # first define some standard values
        self.win = win            # save this for drawing pips later
        self.background = "white" # color of die face
        self.foreground = "black" # color of the pips
        self.psize = 0.1 * size   # radius of each pip
        hsize = size / 2.0        # half the size of the die
        offset = 0.6 * hsize      # distance from center to outer pips

        # create a square for the face
        cx, cy = center.getX(), center.getY()
        p1 = Point(cx-hsize, cy-hsize)
        p2 = Point(cx+hsize, cy+hsize)
        rect = Rectangle(p1,p2)
        rect.draw(win)
        rect.setFill(self.background)

        # Create 7 circles for standard pip locations
        self.pip1 = self.__makePip(cx-offset, cy-offset)
        self.pip2 = self.__makePip(cx-offset, cy)
        self.pip3 = self.__makePip(cx-offset, cy+offset)
        self.pip4 = self.__makePip(cx, cy)
        self.pip5 = self.__makePip(cx+offset, cy-offset)
        self.pip6 = self.__makePip(cx+offset, cy)
        self.pip7 = self.__makePip(cx+offset, cy+offset)
        
        # Draw an initial value
        self.setValue(1)
        
    def setColor(self, color):
        self.foreground = color
        self.setValue(self.value)

    def __makePip(self, x, y):
        "Internal helper method to draw a pip at (x,y)"
        pip = Circle(Point(x,y), self.psize)
        pip.setFill(self.background)
        pip.setOutline(self.background)
        pip.draw(self.win)
        return pip
        
    def setValue(self, value):
        self.value = value
        "Set this die to display value."
        # turn all pips off
        self.pip1.setFill(self.background)
        self.pip2.setFill(self.background)
        self.pip3.setFill(self.background)
        self.pip4.setFill(self.background)
        self.pip5.setFill(self.background)
        self.pip6.setFill(self.background)
        self.pip7.setFill(self.background)

        # turn correct pips on
        if value == 1:
            self.pip4.setFill(self.foreground)
        elif value == 2:
            self.pip1.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        elif value == 3:
            self.pip1.setFill(self.foreground)
            self.pip7.setFill(self.foreground)        
            self.pip4.setFill(self.foreground)
        elif value == 4:
            self.pip1.setFill(self.foreground)
            self.pip3.setFill(self.foreground)
            self.pip5.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        elif value == 5:
            self.pip1.setFill(self.foreground)
            self.pip3.setFill(self.foreground)
            self.pip4.setFill(self.foreground)
            self.pip5.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        else:
            self.pip1.setFill(self.foreground)
            self.pip2.setFill(self.foreground)
            self.pip3.setFill(self.foreground)
            self.pip5.setFill(self.foreground)
            self.pip6.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
            
#button.py
class Button:

    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside it."""

    def __init__(self, win, center, width, height, label):
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """ 

        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        "Returns true if button active and p is inside"
        return (self.active and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False

main()
