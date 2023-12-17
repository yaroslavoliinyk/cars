from fastapi.encoders import jsonable_encoder

from models import CarDB

car = {'damage': 0, 'brand':'Fiat', 'make':'500', 'km':4000,'cm3':2000,'price':3000, 'year':1998, 'fuel': 'petrol'}

cdb = CarDB(**car)

print(cdb)
print(jsonable_encoder(cdb))

