import numpy as np

class Life:

    def __init__(self, N, generations):
        '''Creates a random N x N initial state for life. Could be replaced by well
        known initial static states.'''

        self.N = N
        self.state = np.zeros((N, N))
        self.new_state = np.copy(self.state)
        self.generations = generations
        for i in range(N-1):
            for j in range(N-1):
                if np.random.random() < 0.75:
                    self.state[i][j] = 1
                else:
                    self.state[i][j] = 0
        print(self.state)

    def survival(self, x, y):
        '''Determines if the cell will be alive. Returns a boolean value'''

        #Count the living neighbors
        neighbors = np.sum(self.state[x-1:x+2, y-1:y+2]) - self.state[x][y]

        #check live cell for overpopulation, underpopulation, or stasis
        if self.state[x][y] == 1:
            if neighbors == 2 or neighbors == 3:
                return True
            if neighbors < 2 or neighbors > 3:
                return False

        #Check dead cell for spontaneos generation
        elif self.state[x][y] == 0:
            if neighbors == 3:
                return True
            else:
                return False



    def evolve(self):
        '''Creates new game state based on survivability of cells. Iterates
        over specified number of generations. '''
        t = 1

        while t < self.generations:
            for x in range(1, self.N):
                for y in range(1, self.N):
                    if self.survival(x, y):
                        self.new_state[x][y] = 1
                    else:
                        self.new_state[x][y] = 0

            self.state = self.new_state
            print(self.state)
            t += 1

if __name__ == '__main__':
    N = input("Specify the size of the life grid. Enter an integer between 1 and 50: ")
    T = input("How many generations should be observed? Enter an integer between 10 and 100: ")
    life = Life(N, T)
    life.evolve()
