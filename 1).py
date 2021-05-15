from random import randint
from pruebaaa import altura
from consumo_api import get_charter_by_id
from pruebaaa import peso






id1 = randint(1,83),
personaje1 = get_charter_by_id(1)


id2 = randint(1,83),
personaje2 = get_charter_by_id(2)




if (altura(personaje1) > altura(personaje2)) :
   print ("El personaje mas alto es",personaje1["name"],"la altura es", altura(personaje1))

else:
    print ("El personaje mas alto es",personaje2["name"],"la altura es", altura(personaje2))


if (peso(personaje1)) > (peso(personaje2)):

   print ("El personaje mas pesado es",personaje1["name"],"el peso es", altura(personaje1))

else:
    print ("El personaje mas pesado es",personaje2["name"],"el peso es", altura(personaje2))



if (personaje1 == "Yoda" or personaje2 == "Grievous" or  personaje1 == "Grievous" or personaje2 == "Yoda") :
    print(personaje1)
    print(personaje2)

    import json
import requests
import random

