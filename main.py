import pandas as pd
import numpy as np
# data = pd.series([0.25, 0.5, 0.75, 1.0],
#     index=['a','b','c','d'])


# data = pd.Series([0.25, 0.5, 0.75, 1.0],
#                  index=[2, 5, 3, 7])  # indeksy są liczbami, ale nie muszą mieć konkretnej kolejności
# print(data)
# population_dict = {'California': 38332521,
#                    'Texas'     : 26448193,
#                    'New York'  : 19651127,
#                    'Florida'   : 19552860,
#                    'Illinois'  : 12882135}
# population = pd.Series(population_dict)
# print(population)
# print(population['California':'ilinois'])
# pd.Series([2, 4, 6]),  # z listy
#
# print(pd.series)
# pd.Series(5, index=[1, 2, 3])
#
# print(pd.Series)
# pd.Series(np.arange(10))  # z tablicy numpy

# area_dict = {'California': 423967,
#              'Texas'     : 695662,
#              'New York'  : 141297,
#              'Florida'   : 170312,
#              'Illinois'  : 149995}
# area = pd.Series(area_dict)
# print (area)
# states = pd.DataFrame({
#     'population': population,
#     'area'      : area
# })  # Tworzymy obiekt typu `DataFrame`
# print(states)
# pd.DataFrame(population, columns=['population'])

# data = [{'a': i, 'b': 2 * i} for i in range(3)]
#
# pd.DataFrame(data)  # z listy słow
#
# print(pd.DataFrame(data))

# data = pd.Series(['a', 'b', 'c'], index=[1, 3, 5])

# area = pd.Series({
#     'California': 423967,   'Texas'  : 695662,
#     'New York'  : 141297,   'Florida': 170312,
#     'Illinois'  : 149995
# })
# pop = pd.Series({
#     'California': 38332521, 'Texas'  : 26448193,
#     'New York'  : 19651127, 'Florida': 19552860,
#     'Illinois'  : 12882135
# })
# data = pd.DataFrame({'area':area, 'pop':pop})
# print(data)

# print(data['area'])
# print(data['density']=data['pop']/data['area'])
#
# print(data.iloc[:3, :2])

# vals1= np.array ([1,None, 2,4])
# print(vals1)
# print(vals1.dtype)
# 2
vals2 = np.array([1, np.nan, 3, 4])
print(vals2.dtype)
# print(vals2.sum)
print(np.nansum(vals2))
