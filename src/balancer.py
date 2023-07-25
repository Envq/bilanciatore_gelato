#!/usr/bin/python3
import yaml
from tabulate import tabulate
import numpy as np
np.set_printoptions(precision=2, suppress=True)


class Balancer:
    name        = ""
    size        = 1
    recipe      = None
    labels      = list()
    ingredients = list()
    limits      = ["16-22", "6-10", "8-11", "1-5", "", "32-43", "100"]

    def __init__(self, name, size):
        self.name = name
        self.size = size
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
            ingredientsAvailables = yaml.safe_load(file)
            if ingredientsAvailables is None:
                print('ingredients.yaml not exists')
                exit(-1)
        matrix = list()
        for name, percentage in recipe.items():
            if name not in ingredientsAvailables:
                print(f'"{name}" not exists in ingredients.yaml')
                exit(-1)
            ingredient = ingredientsAvailables[name]
            self.ingredients.append(name)
            row = list(ingredient.values()) + [sum(ingredient.values()), 100, percentage]
            matrix.append(row)

        macro = list(ingredientsAvailables[list(ingredientsAvailables)[0]].keys())
        self.labels = ["ingredienti"] + macro + ["solidi totali", "peso", "percentuale"]
        self.recipe = np.array(matrix)
        # print(self.labels)
        # print(self.ingredients)
        # print(self.recipe)


    def process(self):
        # get percentage column
        percentage = self.recipe[:, -1]
        # remove last column 
        self.recipe = self.recipe[:, :-1]
        # multiply for percentage
        self.recipe *= percentage[:, np.newaxis]
        # get total row
        self.ingredients.append("somma")
        self.recipe = np.vstack((self.recipe, np.sum(self.recipe, axis=0).tolist()))
        #round all
        self.recipe = np.round(self.recipe, decimals=4)
        self.ingredients.append("limiti")
        self.recipe = np.vstack((self.recipe, self.limits))


    def printRecipe(self):
        data = self.recipe.tolist()
        for i in range(len(data)):
            data[i] = [self.ingredients[i]] + data[i]
        table = tabulate(data, headers=self.labels, tablefmt='grid')
        print(table)


    def printDosage(self):
        # get weight column
        weight = self.recipe[:, -1].astype(float) * self.size / 100
        print(f"{self.name}: {self.size}g")
        for i in range(len(self.ingredients)-2):
            print(f"  - {self.ingredients[i]:<25}: {weight[i]} g")
