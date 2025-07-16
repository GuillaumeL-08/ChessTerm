class Grille:
    def __init__(self):
        self.historique = []
        self.tour = "WHITE"
        self.grille = [[Piece([i,j]) for j in range(8)] for i in range(8)]
        for i in range(len(self.grille[1])):
            self.grille[1][i] = Pion([6,i], "BLACK")

        for i in range(len(self.grille[6])):
            self.grille[6][i] = Pion([1,i], "WHITE")


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
        self.historique.append(mouv)
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
                    lettre_case_init = conv_case_lettre(mouv[0])
                    lettre_case_arrive = conv_case_lettre(mouv[2])
                    chiffre_case = conv_case_chiffre(mouv[-1])
                    if type(self.grille[chiffre_case-1][lettre_case_init]) == Pion:
                        pass
                    else:
                        print("Error")
                else:
                    chiffre_case = conv_case_chiffre(mouv[-1])
                    lettre_case = conv_case_lettre(mouv[0])
                    if test_case(chiffre_case+1) and type(self.grille[chiffre_case][lettre_case]) == Piece:
                        if type(self.grille[chiffre_case+1][lettre_case]) == Pion:
                            self.grille[chiffre_case+1][lettre_case].has_move = True
                            self.grille[chiffre_case][lettre_case] = self.grille[chiffre_case+1][lettre_case]
                            self.grille[chiffre_case][lettre_case].set_moove(mouv)
                            self.grille[chiffre_case+1][lettre_case] = Piece([chiffre_case+1,lettre_case])
                            self.grille[chiffre_case][lettre_case].get_Pion()
                        elif test_case(chiffre_case+2) and type(self.grille[chiffre_case][lettre_case]) == Piece:
                            if type(self.grille[chiffre_case+2][lettre_case]) == Pion:
                                if self.grille[chiffre_case+2][lettre_case].autorise_moove(mouv):
                                    self.grille[chiffre_case][lettre_case] = self.grille[chiffre_case+2][lettre_case]
                                    self.grille[chiffre_case][lettre_case].set_moove(mouv)
                                    self.grille[chiffre_case+2][lettre_case] = Piece([chiffre_case+2, lettre_case])
                                    self.grille[chiffre_case][lettre_case].get_Pion()
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
        if self.case[0]+3 == conv_case_lettre(mouv[0]) and not self.has_move:
            self.has_move = True
            return True
        else:
            return False
        
    def set_moove(self, mouv):
        self.case = [conv_case_lettre(mouv[-2]), conv_case_chiffre(mouv[-1])]

    def get_Pion(self):
        print("Le pion se trouve en", conv_chiffre_lettre(self.case[0]), conv_chiffre_case(self.case[1]))

def conv_case_lettre(lettre):
    return ord(lettre) - 97

def conv_case_chiffre(chiffre):
    return 8-int(chiffre)

def conv_chiffre_lettre(case):
    return chr(case + 97)

def conv_chiffre_case(case):
    return 8-case

def test_case(case):
    return 0 <= case < 8

Plateau = Grille()

Plateau.display_grille()
Plateau.grille_mouve("e3")
Plateau.grille_mouve("e4")
Plateau.grille_mouve("a4")
Plateau.display_grille()