﻿from MatrixObjects import *

class Man(MatrixObjects):
    def __init__(self,ligne,colonne):
        MatrixObjects.__init__(self,ligne,colonne)


if __name__ == "__main__":
    M1=Man(1,2)
    print M1.x
    print M1.y
