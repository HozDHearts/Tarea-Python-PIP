import pandas as pd
print("______________________________________________________")
print("          Lista de compras de Juan")
print("______________________________________________________")
data = {
    'Tocino': [8], 
    'Aguacates': [5],
    'Leche': [4],
    'Uvas': [10]
}
product = pd.DataFrame(data)


product = pd.DataFrame(data, index=['Juan'])
   

print(product)
