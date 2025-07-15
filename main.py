class Grille:
    def __init__(self):
        self.tour = "WHITE"
        self.grille = [[Piece([i,j]) for j in range(8)] for i in range(8)]
        for i in range(len(self.grille[1])):
            self.grille[1][i] = Pion([6,i], "BLACK")

        for i in range(len(self.grille[6])):
            self.grille[6][i] = Pion([1,i], "WHITE")

        self.grille[4][4] = Pion([4,4], "WHITE")

    def display_grille(self):
        for row in self.grille:
            for col in row:
                print(col.icon, end='    ')
            print("\n")

    def change_tour(self):
        if self.tour == "WHITE":
            self.tour = "BLACK"
        else:
            self.tour = "WHITE"

    def grille_mouve(self, mouv):
        if mouv[0] == "T":
            pass
        elif mouv[0] == "C":
            pass
        elif mouv[0] == "F":
            pass
        elif mouv[0] == "D":
            pass
        elif mouv[0] == "R":
            pass
        else:
            if self.tour == "WHITE":
                if mouv[1] == "x":
                    pass
                else:
                    if (0 < (conv_case_chiffre(mouv[-1])+1) < 8) and type(self.grille[conv_case_chiffre(mouv[-1])][conv_case_lettre(mouv[0])]) == Piece:
                        if type(self.grille[conv_case_chiffre(mouv[-1])+1][conv_case_lettre(mouv[0])]) == Pion:
                            if self.grille[conv_case_chiffre(mouv[-1])+1][conv_case_lettre(mouv[0])].autorise_moove(mouv):
                                pass
                        elif 0 < (conv_case_chiffre(mouv[-1])+2) < 8:
                            if type(self.grille[conv_case_chiffre(mouv[-1])+2][conv_case_lettre(mouv[0])]) == Pion:
                                if self.grille[conv_case_chiffre(mouv[-1])+2][conv_case_lettre(mouv[0])].autorise_moove(mouv):
                                    pass
                        else:
                            print("Erreur")
                    else:
                        print("Erreur")


class Piece:
    def __init__(self, case, color=None, icon = "."):
        self.color = color
        self.case = case
        self.icon = icon

class Pion(Piece):
    def __init__(self, case, color):
        self.has_move = False
        if color == "WHITE":
            icon = "♟"
        else:
            icon = "♙"
        super().__init__(case, color=color, icon = icon)

    def autorise_moove(self, mouv):
        if self.case[0]+3 == conv_case_chiffre(mouv[-1]) and not self.has_move:
            self.has_move = True
            return True
        elif self.case[0]+2 == conv_case_chiffre(mouv[-1]):
            return True
        else:
            return False

def conv_case_lettre(lettre):
    return ord(lettre) - 97

def conv_case_chiffre(chiffre):
    return 8-int(chiffre)

Plateau = Grille()


Plateau.grille_mouve("e4")
Plateau.grille_mouve("e3")
Plateau.display_grille()