import pandas
import functions

#Step 1: getting the data
#Step 2: Normalizing
#Step 3: cleaning
#Step 4: Transforming the data
#Step 5: Data split for Training

data = pandas.read_json('inmuebles.json')

dataset = functions.json_to_df(data)

# x_train, x_test, y_train, y_test = train_dataset(dataset['column'])

# #Model 1: Linear Regresion
# #Model 1: Training
# #Model 1: R2

# linear_regresion_r2 = linear_regresion()

# #Model 2: Desition Tree
# #Model 2: Training
# #Model 2: R2

# desicion_tree_r2 = desicion_tree()

# #Model 3: Random Forest
# #Model 3: Training
# #Model 3: R2

# random_forest_r2 = random_forest()

# conclusion = get_conclusion(desicion_tree_r2, random_forest_r2, linear_regresion_r2)

# prediction = get_price(conclusion)