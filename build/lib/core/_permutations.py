from itertools import chain, combinations, permutations

# return all possible permutation for a username
# exemple : ["john", "doe"] -> ("john", "doe", "johndoe", "doejohn", "john.doe", "doe.john") 
def get_permutations(self):
    [self.items.append(separator) for separator in self.separators]

    combinations_list = list(chain(*map(lambda x: combinations(self.items, x), range(1, len(self.items) + 1))))   
    for combination in combinations_list:
        for perm in list(permutations(combination)):

            # True if there are two consecutive separators in the permutation, for exemple : ["john", ".", "-", "doe"]
            consecutives_separators = False in [(not perm[i] in self.separators) or (not perm[i + 1] in self.separators) for i in range(len(perm) - 1)]
            
            # Remove combinations that start or end by a dot or have consecutives separators
            if not perm[0] in self.separators and not perm[-1] in self.separators and not consecutives_separators:
                self.permutations_list.append("".join(perm))