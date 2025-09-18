import copy

def main():

    #Shallow
    ages = [1, [2, 3, 4], 5]

    ages.slice = ages[:]

    ages.cp = ages.copy()

    ages_list = list(ages)

    # Deep

    ages_deep_copy = copy.deepcopy(ages)

if __name__ == '__main__':
    main()