import pandas as pd

foods = pd.DataFrame([
    ['Turkey', 'Meat', 135, 29],
    ['Beef', 'Meat', 250, 26],
    ['Salmon', 'Fish', 208, 20],
    ['Tuna', 'Fish', 132, 29],
    ['Rice', 'Grains', 130, 2.7],
    ['Oats', 'Grains', 389, 16.9],
    ['Almonds', 'Nuts', 579, 21],
    ['Walnuts', 'Nuts', 654, 15],
    ['Apple', 'Fruit', 52, 0.3],
    ['Avocado', 'Fruit', 160, 2]
], columns=['Product', 'Category', 'Calories', 'Protein'])

print(foods.to_string(index=False))
print('\nOver 300 calories:\n', foods[foods['Calories'] > 300].to_string(index=False))
print('\nAverage protein by category:\n', foods.groupby('Category', as_index=False)['Protein'].mean().round(2).to_string(index=False))
print('\nSorted by calories:\n', foods.sort_values(by='Calories', ascending=False).to_string(index=False))
