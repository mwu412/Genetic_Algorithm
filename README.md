# Genetic_Algorithm 

## Notes

#### Mutation rate
Typically between 1/pop_size and 1/chromosome_length

#### Gray coding 
Gray coding is a mapping that “attempts” to improve causality, i.e., small changes in the genotype cause small changes in the phenotype, unlike binary coding.

#### Increasing crossover probability
Will increase the opportunity for recombination but also disruption of good combination

#### Premature convergence
Fitness too large.
Relatively super-fit individuals dominate population.
Population converges to a local maximum.
Too much exploitation; too few exploration.

#### Slow finishing
Fitness too small
After many generations, average fitness has converged, but no global maximum is found;
not sufficient difference between best and average fitness.
Too few exploitation; too much exploration.

## My point of view of GA

#### Illegal offsprings
e.g. If a TSP problem with cities not fully connected, need to deal with illegal offsprings (illegal paths).
