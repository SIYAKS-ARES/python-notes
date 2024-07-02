from prettytable import PrettyTable

table_1 = PrettyTable()

table_1.add_column('Pokemon Name', ['Pikachu', 'Squirtle', 'Charmander'])
table_1.add_column('Type', ['Electric', 'Water', 'Fire'])
table_1.align = 'l'

print(table_1)
