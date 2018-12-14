import numpy as np
import matplotlib.pyplot as plt
import random

class chromosome:
    def __init__(self, binary, num_bit):
        self.xbin = binary[0:int(num_bit/2)]  # number of bit must be even number
        self.ybin = binary[int(num_bit/2):num_bit]
        self.bin = binary
        self.x = int(self.xbin, 2) * 0.0235294 - 3
        self.y = int(self.ybin, 2) * 0.0235294 - 3
        # ----- WARN: The fitness function should be carefully costimized ----- #
        # Keep in mind: fitness scores should be positive for roulette wheel 
        # in the case use int() to round off negative numbers to 0
        self.fit = (np.exp((1-self.x)**2*np.exp(-self.x**2-(self.y+1)**2)
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
                binary_str += str(random.randint(0,1))
            choosen_bin_list.append(binary_str)  # did not avoid duplicate

        for binary in choosen_bin_list:
            first_population.append(chromosome(binary, self.genes_num))
        self.pop_history.append(first_population)

    def pick_parent(self, prev_gen):
        # roulette wheel choose parents
        total = sum([c.fit for c in prev_gen])  # python list is so mighty!!!
        pick = random.uniform(0, total-0.01)
        count = 0
        for chromo in prev_gen:
            count += chromo.fit
            if count > pick:
                return chromo

    def mutation(self, binary):
        if random.random() < 0.05:
            here = random.randint(0, self.genes_num-1)
            list_binary = list(binary)
            list_binary[here] = str(1 - int(list_binary[here]))
            return "".join(list_binary)
        return binary
            
    def cross_decimal(self):
        dad = self.pick_parent(self.pop_history[-1])
        mom = self.pick_parent(self.pop_history[-1])
        if random.random() < 0.7:
            # 1-point crossover
            here = random.randint(1,self.genes_num-1)  # N=random.randint(a, b): a <= N <= b.
            # didn't prevent dad == mom
            brother_bin = self.mutation(mom.bin[0:here] + dad.bin[here:self.genes_num])
            sister_bin = self.mutation(dad.bin[0:here] + mom.bin[here:self.genes_num])
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
        for i in range(self.generation-1):
            self.create_new_gen()
        count = 1
        
        f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
        ax1.set_title('x')
        ax1.set_xlabel('th gen.')
        ax1.set_ylabel('avg. value of x')
        ax2.set_title('y')
        ax2.set_xlabel('th gen.')
        ax2.set_ylabel('avg. value pf y')

        for pop in self.pop_history:
            avg_decimal_x = sum([c.x for c in pop])/self.pop_size
            avg_decimal_y = sum([c.y for c in pop])/self.pop_size

            ax1.scatter(count, avg_decimal_x)
            ax2.scatter(count, avg_decimal_y)

            count += 1
        
        #axes = plt.gca()
        #axes.set_xlim([1,self.generation])
        #axes.set_ylim([0,int(2**self.genes_num-1)])
        
        plt.show()

    def plot_history(self):
        fig = plt.figure()
        fig.subplots_adjust(hspace=1, wspace=0.8)
        for i in range(1, self.generation+1):
            ax = fig.add_subplot(5, 20, i)  # a*b should >= self.generation
            ax.set_xlim(-3, 3)
            ax.set_xticks(np.arange(-3, 3, step=3))
            ax.set_title(str(i)+'th gen.')
            ax.hist([c.x for c in self.pop_history[i-1]])

        plt.show()

        fig = plt.figure()
        fig.subplots_adjust(hspace=1, wspace=0.8)
        for i in range(1, self.generation+1):
            ax = fig.add_subplot(5, 20, i)  # a*b should >= self.generation
            ax.set_xlim(-3, 3)
            ax.set_xticks(np.arange(-3, 3, step=3))
            ax.set_title(str(i)+'th gen.')
            ax.hist([c.y for c in self.pop_history[i-1]])

        plt.show()

def main():
    ga = population(6, 16, 100)
    ga.evolve()
    ga.plot_history()

if __name__ == '__main__':
    main()
    
