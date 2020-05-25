class Card :

    def init(self, position = (0,0), color = 'white', word = ''):
        self.color = color
        self.position = position
        self.word = word

    def setColor(self, color):
        self.color = color

    def setWord(self, word):
        self.word = word
