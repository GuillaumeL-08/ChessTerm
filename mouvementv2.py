BLACK = 1
WHITE = 0

class Grille:
    def __init__(self):
        self.historique = []
        self.turn = WHITE
        self.coup_possible = {}
        self.grille = [[Piece([i,j]) for j in range(8)] for i in range(8)]
        for i in range(len(self.grille[1])):
            self.grille[1][i] = Pion([6,i], BLACK)

        for i in range(len(self.grille[6])):
            self.grille[6][i] = Pion([1,i], WHITE)

            self.grille[1][1] = Pion([6,1], WHITE)

    def display_grille(self):
        for row in self.grille:
            for col in row:
                print(col.icon, end='    ')
            print("\n")

    def change_tour(self):
        if self.turn == WHITE:
            self.turn = BLACK
        else:
            self.turn = WHITE
        self.coup_possible = {}

    def set_move(self):
        for row in self.grille:
            for elem in row:
                if elem.color == self.turn:
                    self.coup_possible[elem.get_coor()] = elem.coup_possible()
        print(self.coup_possible)

class Piece:
    def __init__(self, case, color=None, icon = "."):
        self.color = color
        self.case = case
        self.icon = icon

    def get_coor(self):
        return str(conv_chiffre_lettre(self.case[1])) + str(conv_chiffre_case(self.case[0]))
    

class Pion(Piece):
    def __init__(self, case, color):
        self.has_move = False
        if color == WHITE:
            icon = "♟"
        else:
            icon = "♙"
        super().__init__(case, color=color, icon = icon)

    """  
    def set_moove(self, mouv):
        self.case = [conv_case_lettre(mouv[-2]), conv_case_chiffre(mouv[-1])]
    """

    def coup_possible(self):
        res = []
        if self.color == WHITE:
            if self.case[0] == 6:
                res.append(set_coor(self.case[1], self.case[0]+1)+"=D")
                res.append(set_coor(self.case[1], self.case[0]+1)+"=C")
                res.append(set_coor(self.case[1], self.case[0]+1)+"=T")
                res.append(set_coor(self.case[1], self.case[0]+1)+"=F")                
                if test_case(self.case[1]-1):
                    res.append(conv_chiffre_lettre(self.case[1]) + "x" + set_coor(self.case[1]-1, self.case[0]+1)+"=D")
                    res.append(conv_chiffre_lettre(self.case[1]) + "x" + set_coor(self.case[1]-1, self.case[0]+1)+"=C")
                    res.append(conv_chiffre_lettre(self.case[1]) + "x" + set_coor(self.case[1]-1, self.case[0]+1)+"=T")
                    res.append(conv_chiffre_lettre(self.case[1]) + "x" + set_coor(self.case[1]-1, self.case[0]+1)+"=F")
                if test_case(self.case[1]+1):
                    res.append(conv_chiffre_lettre(self.case[1]) + "x" +set_coor(self.case[1]+1, self.case[0]+1)+"=D")
                    res.append(conv_chiffre_lettre(self.case[1]) + "x" +set_coor(self.case[1]+1, self.case[0]+1)+"=C")
                    res.append(conv_chiffre_lettre(self.case[1]) + "x" +set_coor(self.case[1]+1, self.case[0]+1)+"=T")
                    res.append(conv_chiffre_lettre(self.case[1]) + "x" +set_coor(self.case[1]+1, self.case[0]+1)+"=F")
            else:
                res.append(set_coor(self.case[1], self.case[0]+1))
                if not self.has_move:
                    res.append(set_coor(self.case[1], self.case[0]+2))
                if test_case(self.case[1]-1):
                    res.append(conv_chiffre_lettre(self.case[1]) + "x" + set_coor(self.case[1]-1, self.case[0]+1))
                if test_case(self.case[1]+1):
                    res.append(conv_chiffre_lettre(self.case[1]) + "x" +set_coor(self.case[1]+1, self.case[0]+1))
        return res

    def affiche_Coor_Pion(self):
        print("Le pion se trouve en", conv_chiffre_lettre(self.case[1]), conv_chiffre_case(self.case[0]))

def conv_case_lettre(lettre):
    return ord(lettre) - 97

def conv_case_chiffre(chiffre):
    return 8-int(chiffre)

def conv_chiffre_lettre(case):
    return chr(case + 97)

def conv_chiffre_case(case):
    return case + 1

def test_case(case):
    return 0 <= case < 8

def set_coor(lettre, chiffre):
    return conv_chiffre_lettre(lettre) + str(conv_chiffre_case(chiffre)) 

Plateau = Grille()

Plateau.set_move()