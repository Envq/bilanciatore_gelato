#!/usr/bin/python3
import numpy as np
import yaml

def init(name):
    with open('data/recipes.yaml', 'r') as file:
        recipes = yaml.safe_load(file)
        if recipes is None:
            print('recipes.yaml not exists')
            exit(-1)
    recipe = recipes[name]
    if recipes is None:
        print(f'"{name}" not exists in recipes.yaml')
        exit(-1)

    with open('data/ingredients.yaml', 'r') as file:
        ingredients = yaml.safe_load(file)
        if ingredients is None:
            print('ingredients.yaml not exists')
            exit(-1)
    recipe_ingredients = dict()
    for e in recipe:
        i = ingredients[e]
        if i is None:
            print(f'"{i}" not exists in ingredients.yaml')
            exit(-1)
        recipe_ingredients[e] = i

    return recipe, recipe_ingredients
