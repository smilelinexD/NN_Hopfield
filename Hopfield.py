import numpy as np


def sgn(x) -> int:
    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1


class Hopfield:
    def __init__(self, n=3, dim=[12, 9]):
        self.n = n
        self.dim = dim
        self.size = int(dim[0] * dim[1])
        self.w = np.zeros((self.size, self.size))
        self.origins = np.zeros((self.n, self.size))
        self.results = np.zeros((self.n, self.size))
        # theta = 0

    def train(self, directory="./Data/Basic_Training.txt"):
        with open(directory, "r") as f:
            for x in range(self.n):
                vec = np.ones((self.size, 1), dtype=np.int32)
                for i in range(self.dim[0]):
                    line = f.readline()
                    for j in range(self.dim[1]):
                        if line[j] == " ":
                            vec[i * self.dim[1] + j] = -1
                print("Case {:d}:".format(x))
                self.show(vec)
                self.origins[x] = np.copy(np.squeeze(vec))
                self.w = self.w + np.matmul(vec, vec.transpose())
                f.readline()
        for i in range(self.size):
            self.w[i][i] = 0
        self.w = self.w / self.size
        # print(self.w)
        # self.theta = self.w.sum(axis=0).transpose()
        # print(self.theta)

    def test(self, directory="./Data/Basic_Testing.txt", case=3):
        xs = []
        with open(directory, "r") as f:
            for n in range(case):
                x = np.ones(self.size, dtype=np.int32)
                for i in range(self.dim[0]):
                    line = f.readline()
                    for j in range(self.dim[1]):
                        if line[j] == " ":
                            x[i * self.dim[1] + j] = -1
                # self.show(x)
                xs.append(x)
                f.readline()

        for n in range(case):
            print("Case {:d}:".format(n))
            x = xs[n]
            last_x = np.copy(x)
            while True:
                for i in range(self.size):
                    y = sgn(np.dot(np.squeeze(self.w[i]), x))
                    if y == 0:
                        pass
                    else:
                        x[i] = y
                if (last_x == x).all():
                    break
                last_x = np.copy(x)
            self.show(x)
            np.copyto(self.results[n], x)

    def show(self, x):
        for i in range(self.dim[0]):
            for j in range(self.dim[1]):
                if x[i * self.dim[1] + j] == 1:
                    print("█", end="")
                else:
                    print(" ", end="")
            print()


if __name__ == "__main__":
    model = Hopfield()
    model.train()
    model.test()
    # model = Hopfield(n=15, dim=[10, 10])
    # model.load_data(directory="./Data/Bonus_Training.txt")
    # print("\n\n")
    # model.retrieve(directory="./Data/Bonus_Testing.txt", case=15)
