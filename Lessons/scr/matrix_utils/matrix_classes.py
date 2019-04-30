# Создать класс Matrix. Атрибуты - data(содержит саму матрицу),
# n, m. Определить конструктор, переопределить магический метод __str__.

from random import randint


class Matrix:
    def __init__(self, data=None):
        if not data:
            self.n = self.m = 5
            data = [[randint(1, 9) for _ in range(self.m)] for _ in range(self.n)]
        else:
            self.n = len(data)
            self.m = len(data[0])

        self.data = data

    def __str__(self):
        return "\n".join(" ".join(str(x) for x in row) for row in self.data)

