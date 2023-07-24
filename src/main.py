from balancer import Balancer


####################################
size = 400
name = 'gelato al melone'
####################################


if __name__ == "__main__":
    b = Balancer(name, size)
    b.printTable()
    # b.process()
    # b.print()