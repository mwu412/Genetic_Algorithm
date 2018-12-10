import numpy as np
import matplotlib.pyplot as plt
import random

class chromosome:
    def __init__(self, binary, num_bit):
        self.xbin = binary[0:int(num_bit/2)]
        self.ybin = binary[int(num_bit/2):num_bit]
        self.bin = self.xbin + self.ybin
        self.x = int(self.xbin, 2) * 0.0235294 - 3
        self.y = int(self.ybin, 2) * 0.0235294 - 3
        # ----- WARN: The fitness function should be carefully costimized ----- #
        # Keep in mind: fitness scores should be positive for roulette wheel 
        # in the case use int() to round off negative numbers to 0
        self.fit = np.ceil(np.exp((1-self.x)**2*np.exp(-self.x**2-(self.y+1)**2)
                -(self.x-self.x**3-self.y**3)*np.exp(-self.x**2-self.y**2)))  
        # --------------------------------------------------------------------- #

class population:
    def __init__(self, pop_size, genes_num, generation):
        self.pop_size = pop_size  # must be even number
        self.genes_num = genes_num
        self.generation = generation 
        self.pop_history = []

        first_population = []
        choosen_bin_list = []

        for i in range(self.pop_size):
            binary_str = ''
            for j in range(self.genes_num):
                binary_str+=str(random.randint(0,1))
            choosen_bin_list.append(binary_str)  # did not avoid duplicate

        for binary in choosen_bin_list:
            first_population.append(chromosome(binary, self.genes_num))
        self.pop_history.append(first_population)

    def pick_parent(self, prev_gen):
        # roulette wheel choose parents
        total = sum([c.fit for c in prev_gen])  # python list is so mighty!!!
        pick = random.randint(0, total-1)
        count = 0
        for chromo in prev_gen:
            count += chromo.fit
            if count > pick:
                return chromo
            
    def cross_decimal(self):
        dad = self.pick_parent(self.pop_history[-1])
        mom = self.pick_parent(self.pop_history[-1])
        if random.random() < 0.7:
            # 1-point crossover
            here = random.randint(1,self.genes_num-2)  # N=random.randint(a, b): a <= N <= b.
            # didn't prevent dad == mom
            brother_bin = mom.bin[0:here] + dad.bin[here:self.genes_num]
            sister_bin = dad.bin[0:here] + mom.bin[here:self.genes_num]
            return [brother_bin, sister_bin]
        return [dad.bin, mom.bin]

    def create_new_gen(self):
        this_generation = []
        for i in range(int(self.pop_size/2)):
            [bro, sis] = self.cross_decimal()
            this_generation.append(chromosome(bro, self.genes_num))
            this_generation.append(chromosome(sis, self.genes_num))
        self.pop_history.append(this_generation)

    def evolve(self):
        plt.title('GA')
        plt.xlabel('th generation')
        plt.ylabel('avg. output')
        for i in range(self.generation-1):
            self.create_new_gen()
        count = 1
        for pop in self.pop_history:
            avg_decimal_x = sum([c.x for c in pop])/self.pop_size
            avg_decimal_y = sum([c.y for c in pop])/self.pop_size
            plt.scatter(count, avg_decimal_x)
            plt.scatter(count, avg_decimal_y)

            count += 1
        
        axes = plt.gca()
        axes.set_xlim([1,self.generation])
        axes.set_ylim([0,int(2**self.genes_num-1)])
        
        plt.show()

def main():
    ga = population(6, 16, 10)
    ga.evolve()

if __name__ == '__main__':
    main()
    
