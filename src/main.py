from balancer import Balancer


####################################
size = 700
# name = 'gelato al melone'
# name = 'fior di latte'
name = 'gelato al melone burro'
####################################


if __name__ == "__main__":
    b = Balancer(name, size)
    # b.printRecipe()
    b.process()
    b.printRecipe()
    b.printDosage()

