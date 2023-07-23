import bilanciatore


####################################
size = 400
name = 'gelato al melone'
####################################


if __name__ == "__main__":
    recipe, ingredients = bilanciatore.init(name)

    print(recipe)
    print(ingredients)