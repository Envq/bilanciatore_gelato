#!/usr/bin/python3
import yaml
from tabulate import tabulate
import numpy as np
np.set_printoptions(precision=2, suppress=True)


class Balancer:
    name = ""
    size = 100
    ingrediets = dict()

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
        for name, percentage in recipe.items():
            if name not in ingredientsAvailables:
                print(f'"{name}" not exists in ingredients.yaml')
                exit(-1)
            ingredient = ingredientsAvailables[name]
            self.ingrediets[name] = ingredient
            self.ingrediets[name]['solidi totali'] = sum(ingredient.values())
            self.ingrediets[name]['percentuale'] = percentage


    def printList(self):
        for name, values in self.ingrediets.items():
            print(f'{name}:')
            for k, v in values.items():
                print(f'  - {k:<20}: {round(v, 2)}')


    def printTable(self):
        macro = list(self.ingrediets[list(self.ingrediets)[0]].keys())
        table = [["ingredienti"] + macro]
        for k, v in self.ingrediets.items():
            l = list()
            l.append(k)
            for e in macro:
                l.append(v[e])
            table.append(l)

        print(table)

        table_str = tabulate(table, headers='firstrow', tablefmt='grid')
        print(table_str)

    def process(self):
        for macro in self.ingrediets.values():
            percentage = macro['percentuale']
            for k, v in macro.items():
                if k != 'percentuale':
                    v *= percentage
