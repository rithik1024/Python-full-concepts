""" Creating Dictionary of city and population pairs using Dict Comprehension"""

cities = ['Tokyo',
          'Delhi',
          'Shanghai',
          'Sao Paulo',
          'Mumbai'
          ]
population =['38,001,000',
              '25,703,168',
              '23,740,778',
              '21,066,245',
              '21,042,538',345
]
city_population={}
for city, pop in zip(cities,population):
    city_population[city]=pop
print(city_population)
   
# city_pop={ city:pop for city,pop in zip(cities,population)}
# print(city_pop)