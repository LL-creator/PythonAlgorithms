class Solution:
    def __init__(self, string, rows):
        self.rows = rows
        self.string = string
        self.list = []

    def convert(self, W = False) -> list:
        """
        the w is for if you want your zig zag to look like
        this: \    /\    / or this: |  /|  /
               \  /  \  /           | / | /
                \/    \/            |/  |/
        """
        l_index = len(self.string) - 1
        offset = 2 * self.rows - 2
        self.list = []
        for i in range(self.rows):
            self.list.append(" ")
        if(W != False):
            for i in range(self.rows):
                for j in range(i):
                    self.list[i] += " "

        for x in range(0, l_index + 1, offset):
            for j in range(len(self.list)):

                if (x + j <= l_index and j != self.rows - 1):
                    self.list[j] += self.string[x + j]
                    for d in range(1, offset - 2 * j, 1):
                        self.list[j] += " "

                if (x + offset - j <= l_index):
                    if ((j != 0)):
                        self.list[j] += self.string[x + (offset - j)]
                        for d in range(1, 2 * j, 1):
                            self.list[j] += " "
        for i in range(self.rows):
            for j in range(i):
                self.list[i] += " "

    def show(self):
        for i in self.list:
            print(i)
