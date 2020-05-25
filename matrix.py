from card import Card
import random

class Matrix :

    def init(self, size):
        self.size = size
        mat = []
        for pos1 in range(0,size-1):
            mat.append([])
            for pos2 in range(0,size-1):
                mat[pos1].append(Card((pos1, pos2)))
        self.cards = mat
        self.firstTeam = random.choice(['red', 'blue'])
        return 'OK'

    def assignColors(self):
        remainingCards = {'black': 1, 'white': 7, 'blue': 8, 'red': 8}
        remainingCards[self.firstTeam] += 1
        for row in cards:
            for card in row:
                col = self.chooseRandomColor(remainingCards['black'],remainingCards['white'],remainingCards['blue'],remainingCards['red'])
                card.setColor(col)
                if remainingCards[col] > 0 :
                    remainingCards[col] -=1

    def chooseRandomColor(self, black, white, blue, red):
        c = ['black', 'white', 'red', 'blue']
        return random.choices(c, weights=(black, white, red, blue), k=1)

    def assignWords(self, liste):
        words = random.choices(liste, k = self.size*self.size)
        n= 0
        for row in cards:
            for card in row:
                card.setWord(words[n])
                n+=1
