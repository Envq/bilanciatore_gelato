#!/usr/bin/python3
import json
import numpy as np


with open("recipes.json") as recipes_file:
    recipes = json.load(recipes_file)
with open("ingredients.json") as ingredients_file:
    ingredients = json.load(ingredients_file)


recipe = recipes['gelato']
pool = [ingredients['melone']]

A = np.array([  [0, 100, 0, 0],
                [3, 0, 30, 0],
                [9, 0, 15, 100],
                [1, 1, 1, 1],
             ])
B = np.array([16, 6, 12, 1])
X = np.linalg.solve(A,B)
print(X)
R = X * 400
print("latte:", round(R[0],2), "g")
print("zucch:", round(R[1],2), "g")
print("polve:", round(R[3],2), "g")
print("tuorl:", round(R[2],2), "g")
print("---")
print("latte:", round(R[0],2), "g")
print("sacca:", round(R[1]/1.2,2), "g")
print("destr:", round(R[1]/1.2*0.2,2), "g")
print("polve:", round(R[3],2), "g")
print("tuorl:", round(R[2]/16,2), "pz")


print("#################")
A = np.array([  [0, 100, 0, 0],
                [3, 0, 28, 0],
                [9, 0, 0, 100],
                [1, 1, 1, 1],
             ])
B = np.array([16, 6, 12, 1])
X = np.linalg.solve(A,B)
print(X)
R = X * 400
print("latte:", round(R[0],2), "g")
print("sacca:", round(R[1]/1.2,2), "g")
print("destr:", round(R[1]/1.2*0.2,2), "g")
print("polve:", round(R[3],2), "g")
print("burro:", round(R[2],2), "g")


print("#################")
A = np.array([  [0, 100, 0],
                [9, 0, 100],
                [1, 1, 1],
             ])
B = np.array([16, 12, 1])
X = np.linalg.solve(A,B)
print(X)
R = X * 400
print("latte:", round(R[0],2), "g")
print("sacca:", round(R[1]/1.2,2), "g")
print("destr:", round(R[1]/1.2*0.2,2), "g")
print("polve:", round(R[2],2), "g")