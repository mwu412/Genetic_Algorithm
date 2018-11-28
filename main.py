import numpy as np
import random

random.random()
random.randint(0,1)

class chromosome:
    def __init__(self, decimal, num_bit):
        self.decimal = decimal
        self.bin = ("{0:0"+str(num_bit)+"b}").format(decimal) 
        self.fit = 16*decimal-4*(decimal**2)

class population:
    def __init__(self, pop_size, genes_num, generation):
        self.pop_size = pop_size
        self.genes_num = genes_num
        self.generation = generation
        self.population = []
        choosen_decimal = random.sample(range(2**genes_num), pop_size)  # sample without duplicates
        for i in range(pop_size):
            self.population.append(chromosome(choosen_decimal, genes_num))

    def pick_parant(self):
        # roulette wheel choose parents
        total = sum([c.fit for c in self.population])  # python list is so mighty!!!
        pick = random.randint(0, total)
        count = 0
        for chromo in self.population:
            if pick > count:
                return chromo
            count += chromo.fit

    def crossover(self):
        if random.random() < 0.7:
            # 1-point crossover
            here = random.randint(1,self.genes_num-1)  # N=random.randint(a, b): a <= N <= b.

            c_dad = self.pick_parent()
            c_mom = self.pick_parant()  # didn't prevent dad == mom

             = c_mom.bin(0:here) + c_dad.bin(here:self.genes_num+1)
        
