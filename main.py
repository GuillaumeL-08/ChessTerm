class Grille:
    def __init__(self):
        self.grille = [[Piece([i,j]) for j in range(8)] for i in range(8)]
        for i in range(len(self.grille[1])):
            self.grille[1][i] = Pion([1,i], "WHITE")

        for i in range(len(self.grille[7])):
            self.grille[6][i] = Pion([7,i], "BLACK")

    def display_grille(self):
        for row in self.grille:
            for col in row:
                print(col.icon)



class Piece:
    def __init__(self, case, color=None, icon = "."):
        self.color = color
        self.case = case
        self.icon = icon

class Pion(Piece):
    def __init__(self, case, color):
        self.has_move = False
        if color == "BLACK":
            icon = "♟"
        else:
            icon = "♙"
        super().__init__(case, color=color, icon = icon)

    def mouvement():
        pass

Plateau = Grille()

Plateau.display_grille()