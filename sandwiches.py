import random

def ingredients():
    return ["turkey", "ham", "cheese", "lettuce", "cucumber", "pickle", "mayo"]

def recipe(ingredients_list):
    random.shuffle(ingredients_list)
    options = ingredients_list[:3]  # Select the first 3 ingredients
    return options

def main():
    all_ingredients = ingredients()
    sandwich_fillings = recipe(all_ingredients)
    print(f"Your random sandwich will contain: {', '.join(sandwich_fillings)}")

if __name__ == "__main__":
    main()
