
from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from kivy.properties import StringProperty
from kivy.properties import NumericProperty

import time
import random
import words

class mainWidgie(BoxLayout):
    
    question = StringProperty('')
    answer0 = StringProperty('')
    answer1 = StringProperty('')
    answer2 = StringProperty('')
    answer3 = StringProperty('')
    answer4 = StringProperty('')
    answer5 = StringProperty('')
    score = StringProperty('')
    highscore = StringProperty('')
    hiscore = NumericProperty()
    
    
    def __init__(self, *args, **kwargs):
        super(mainWidgie, self).__init__(*args, **kwargs)
        
        #get highscore from file
        try:
            with open('highscore.txt','r') as infile:
                for line in infile:
                    line = line.rstrip()
                    self.hiscore = int(line)
                    break
        except:
            self.hiscore = 0
        self.highscore = 'highscore: ' + str(self.hiscore) + '   '
        mainWidgie.numscore = int(self.hiscore)
        self.score = str(0)
        self.newQ()

    def answerLeft(self,x):
        if self.answered :
            if self.tup[self.lan-1] == x :
                try :
                    self.score = str(int(self.score)+1)
                except :
                    self.score = str(1)
                self.answered = False
                self.newQ()
            else :
                try:
                    #update high score if improved
                    if self.hiscore < int(self.score) :
                        self.hiscore = int(self.score)
                        mainWidgie.numscore = int(self.hiscore)
                        self.highscore = 'highscore: ' + str(self.score) + '   '
                except :
                    pass
                self.score = str(self.tup[self.lan]+'\n'+'='+'\n'+self.tup[self.lan-1])
                self.answered = False
                time.sleep(1)
                self.newQ()
    
    def newQ(self):
        self.tup = random.sample(words.ws,1)[0]
        self.lan = random.randint(0,1)
        self.question = self.tup[self.lan]
        self.answers = []
        for i in range(5) :
            self.answers.append(random.sample(words.ws,1)[0][self.lan-1])
        self.answers.append(self.tup[self.lan-1])
        random.shuffle(self.answers)
        self.answer0 = self.answers[0]
        self.answer1 = self.answers[1]
        self.answer2 = self.answers[2]
        self.answer3 = self.answers[3]
        self.answer4 = self.answers[4]
        self.answer5 = self.answers[5]
        #self.answerIndex = self.answers.index(self.tup[self.lan-1])
        self.answered = True

class DutchApp(App):
    def build(self):
        return mainWidgie()
        
    def on_pause(self):
        return True
        
    def on_stop(self):
        with open('highscore.txt','w') as outfile :
            outfile.write(str(mainWidgie.numscore))
        return True
            
if __name__ == "__main__":
    DutchApp().run()
