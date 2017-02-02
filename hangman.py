#Sarah Nicholson

from graphics import *
from random import *
from time import *

class Words:
    '''reads a file of words and creates a list of words'''
    def __init__(self,filename):
        infile = open(filename, 'r')
        self.list_of_words = infile.read().split()
        infile.close()
        
    def get_word(self):
        '''returns a random word from the list'''
        random_word = self.list_of_words[randint(0,len(self.list_of_words))]
        return random_word
        
class Guess:
    '''creates an object with two lists. One contains the letters of the
    word and the other is the same length with blanks. When a letter is
    guessed, the letter in the word is swapped with the blank in that
    position, i.e. ['c','a','t'] and ['_','_','_'] that are created
    would change to ['c','_','t'] and ['_','a','_'] when the letter a
    is guessed'''
    def __init__ (self,word):
        self.word = word
        self.wordList = list(self.word)
        self.blankList = ['_'] * len(self.word)
        self.history = []
        self.badGuesses = 0
        
    def missed (self):
        '''returns the word string that could not be guessed'''
        return self.word
        
    def guess_letter (self,letter):
        '''uncovers letters that match the guess, counts the bad guesses
        and keeps track of the letters guessed. It returns a number, 0,
        if the letter has already been guessed, 1 if the letter is NOT
        in the word and 2 if the letter IS in the word'''
        if letter in self.history:
            return 0
        self.history.append(letter)
        if letter not in self.wordList:
            self.badGuesses += 1
            return 1
        for i in range(len(self.word)):
            if letter == self.word[i]:
                self.blankList[i] = letter
        return 2
        
    def gameover (self):
        '''returns Boolean, T if word is guessed or the number of guesses
        has exceeded the limit and F otherwise'''
        return '_' not in self.blankList or self.badGuesses == 7

    def num_of_guesses(self):
        '''returns a STRING with the number of remaining guesses'''
        return str(7 - self.badGuesses) + ' guesses left'
    
    def letters_guessed (self):
        '''returns a string, in alphabetical order, of all the letters
        that have been guessed'''
        self.history.sort()
        return ' '.join(self.history)
    
    def get_guess(self):
        '''returns a string with the letters in the word and _ for each
        unguessed letter separated by spaces exactly like the __str__'''
        return ' '.join(self.blankList)
        
    def   __str__ (self):
        '''returns a string with the letters in the word and _ for each'''
        return ' '.join(self.wordList)

    def badGuess(self):
        return self.badGuesses
        
class Noose:
    
    def __init__(self,win):
        '''creates a Noose object with 7 sections that can be drawn one at a
        time in the win canvas'''
        self.win = win
        self.sect_num = [Gallows(),Circle(Point(500,168),40),
                    Line(Point(500,208),Point(500,305)), Line(Point(500,235),Point(520,300)),
                    Line(Point(500,235),Point(480,300)), Line(Point(500,305),Point(520,405)),
                    Line(Point(500,305),Point(480,405))]
        self.current = 0
        
    def wrong(self):
        '''draws another of the 7 sections to the noose platform and/or figure'''
        self.sect_num[self.current].draw(self.win)
        self.current += 1
            
class Gallows:
    #creates the post for hangman
    def __init__(self):
        self.lines = [Line(Point(375,125),Point(375,500)),
                     Line(Point(375,125),Point(500,125))]

    def draw(self,win):
        for line in self.lines:
            line.draw(win)

    def undraw(self):
        for line in self.lines:
            line.undraw()
            
def main():
    #creates window
    win = GraphWin('Hangman',700,600)
    play_one_game(win)
    #creates buttons and entry box for letters
    enterButton = Button(win,Point(125,325),50,50,'Enter','yellow')
    enterButton.activate()
    yesButton = Button(win,Point(85,550),50,50,'Yes','green')
    noButton = Button(win,Point(175,550),50,50,'No','red')
    letterEntry = Entry(Point(125,275),3)
    letterEntry.draw(win)
    letterEntry.setText('')
    letter = letterEntry.getText()
    
    #creates the noose objects
    noose = Noose(win)
    
    #gets the random word
    filename = 'wordlist.txt'
    words = Words(filename)
    words = words.get_word()
    words = list(words)
    guess = Guess(words)
    
    #makes the text objects that need to be updated
    guessed_letters = Text(Point(125,400),guess.letters_guessed())
    guessed_letters.draw(win)
    num_guesses = Text(Point(125,500),guess.num_of_guesses())
    num_guesses.draw(win)
    mysteryWord = Text(Point(125,175),guess.get_guess())
    mysteryWord.draw(win)
    
    while not guess.gameover():
        #gets user's mouse clicks for Enter button
        p = win.getMouse()
        if enterButton.clicked(p):
            letter = letterEntry.getText()
            letterEntry.setText('')
            #sees if the word is in the word or not or has already been
            #guessed
            if valid(letter):
                x = guess.guess_letter(letter)
                if x == 0:
                    num_guesses.setText('You already guessed that.')
                    sleep(0.5)
                    num_guesses.setText(guess.num_of_guesses())
                if x == 1:
                    num_guesses.setText(guess.num_of_guesses())
                    guessed_letters.setText(guess.letters_guessed())
                    noose.wrong()
                else:
                    mysteryWord.setText(guess.get_guess())
                    guessed_letters.setText(guess.letters_guessed())
                

    while guess.gameover():
        #activates buttons and executes actions that would happen at the
        #end of the game
        yesButton.activate()
        noButton.activate()
        if guess.badGuess() >= 7:
            num_guesses.setText('Play Again?')
            mysteryWord.setText(guess.missed())
            gameoverText(win)
        else:
            num_guesses.setText('Play Again?')
            winText(win)
        #get users mouse clicks for yes and no button
        p = win.getMouse()
        if yesButton.clicked(p):
            #closes window and opens back up a new one
            win.close()
            playAgain()
        elif noButton.clicked(p):
            #closes window
            break  
    win.close()
    
def valid(letter):
    #checks if letter is valid
    ltr = str(letter).lower()
    return len(letter) == 1 and 'a' <= letter <= 'z'

def gameoverText(win):
    #if player loses, tells them they lost
    loseTxt = Text(Point(125,75),'You Lose!')
    loseTxt.setSize(25)
    loseTxt.draw(win)

def winText(win):
    #if player wins, tells them they won
    winTxt = Text(Point(125,75),'You Win!')
    winTxt.setSize(25)
    winTxt.draw(win)
    
def play_one_game(win):    
    #creates all of the text for the game
    mysteryTxt = Text(Point(125,125),'Mystery Word')
    mysteryTxt.draw(win)
    instructions = Text(Point(125,225),'Enter a letter and click Enter:')
    instructions.draw(win)
    lettersGuessed = Text(Point(125,375),'Letters guessed:')
    lettersGuessed.draw(win)

def playAgain():
    #opens the window back up if player wants to play again
    main()
        
class Button:
    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside it."""

    def __init__(self, win, center, width, height, label, color):
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit','yellow') """ 
        self.xmax, self.xmin = center.getX()+width/2.0, center.getX()-width/2.0
        self.ymax, self.ymin = center.getY()+height/2.0, center.getY()-height/2.0
        p1,p2 = Point(self.xmin, self.ymin), Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill(color)
        self.label = Text(center, label)
        self.win = win
        self.active = False

    def clicked(self, p):
        "Returns true if button active and p is inside"
        return (self.active and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

    def activate(self):
        "Sets this button to 'active'and draws the button."
        if self.active == False:
            self.active = True
            self.rect.draw(self.win)
            self.label.draw(self.win)

    def deactivate(self):
        "Sets this button to 'inactive' and undraws the button."
        if self.active == True:
            self.active = False
            self.rect.undraw()
            self.label.undraw()

main()
