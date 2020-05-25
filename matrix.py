from card import Card

class Matrix :

    def init(self, size):
        self.size = size
        mat = []
        for pos1 in range(0,size-1):
            mat.append([])
            for pos2 in range(0,size-1):
                mat[pos1].append(Card((pos1, pos2)))
        self.cards = mat

    def assignColors(self):
        #for each position

    def assignWords(self):
