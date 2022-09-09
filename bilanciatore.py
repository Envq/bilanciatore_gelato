#!/usr/bin/python3
import json

with open("recipes.json") as recipes_file:
    recipes = json.load(recipes_file)
with open("ingredients.json") as ingredients_file:
    ingredients = json.load(ingredients_file)


recipe = recipes['gelato']
pool = [ingredients['melone']]