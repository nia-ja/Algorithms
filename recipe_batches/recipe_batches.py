#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # look into every ingredient in recipe dictionary and compare with simiar in ingredients
  batches = []
  # for each pair
  for k, v in recipe.items():
    # if no such ingredient return 0
    if k not in ingredients:
      return 0
    # batches.append(ingr.amount in ingredients // ingr.amount in recipe)
    batches.append(ingredients[k] // v)
  return min(batches)

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))