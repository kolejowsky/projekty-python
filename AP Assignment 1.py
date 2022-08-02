import numpy as np
import pandas as pd

class MetaMat:
    __List = []
    __NMatrix = np.array(__List)
    __PFrame = pd.DataFrame(__List)
    __flag = 0

    def __init__(self, list):
        self.__List = list
        self.__NMatrix = np.array(list)
        self.__PFrame = pd.DataFrame(list)
        self.flag = 0



    def swapListRows(self, row1, row2):
        self.__List[row1-1] , self.__List[row2-1] = self.__List[row2-1] , self.__List[row1-1]
        self.flag = 1

    def swapMatrixColumns(self, col1, col2):
        self.__NMatrix[:, [col1-1, col2-1]] = self.__NMatrix[:, [col2-1, col1-1]]
        self.flag = 2

    def transposePSquare(self, key1, index1, key2, index2):
        #index - row
        #key - column
        if (key2 - key1) == (index2 - index1):
            self.__PFrame.iloc[index1 - 1:index2, key1 - 1:key2] = self.__PFrame.iloc[index1 - 1:index2, key1 - 1:key2].T
            self.flag = 3
        else:
            print("wrong input")

    def update(self):
        if self.flag == 1:
            self.__NMatrix = np.array(list)
            self.__PFrame = pd.DataFrame(self.__NMatrix)
        elif self.flag == 2:
            self.__List = self.__NMatrix.tolist()
            self.__PFrame = pd.DataFrame(self.__NMatrix)
        elif self.flag == 3:
            self.__List = self.__PFrame.values.tolist()
            self.__NMatrix = self.__PFrame.to_numpy()



    def print(self):
        print(self.__List, "\n")
        print(self.__NMatrix, "\n")
        print(self.__PFrame, "\n")


def main():

    list = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

    for i in range(len(list)):
        for j in range(len(list[i])):
            try:
                a = float(list[i][j])
            except:
                list[i][j] = 0

    m1 = MetaMat(list)
    m1.print()

    print("\n swapListRows")
    m1.swapListRows(1, 3)
    m1.print()

    print("\n swapMatrixColumns")
    m1.swapMatrixColumns(1, 3)
    m1.print()

    print("\n transposePSquare")
    m1.transposePSquare(1, 2, 3, 4)
    m1.print()

    print("\n update")
    m1.update()
    m1.print()

main()

