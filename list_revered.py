cities = ['seatle, NC, usa', 'chappel hill, NC, usa', 'United States']


def city_adjustment(city):
    city = city.split(',')
    cit = city[:: -1]
    try:
        cit = cit[2]
    except IndexError:
         cit = 'N/a' 
    return cit
    
for city in cities:
    town = city_adjustment(city)
    print(town)