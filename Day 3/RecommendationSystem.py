import numpy as np 
from lightfm.datasets import fetch_movielens
from lightfm.datasets import fetch_stackexchange
from lightfm import LightFM 

#Datos traidos desde lightfm
data = fetch_movielens(min_rating=4.0)
dataStack = fetch_stackexchange(dataset='crossvalidated',min_training_interactions=1)

#Datos de pelicula
print(repr(data['train']))
print(repr(data['test']))

#Datos de StackOverflow
print(repr(dataStack['train']))
print(repr(dataStack['test']))


#El parametro loss indica al algoritmode ML si el resultado es 
#correcto o erroneo, indicando que entre mas grande el valor, indica que esta mas equivocado
#WRAP= Pérdida de pareja ponderada de rango aproximado
model = LightFM(loss='warp')
modelStack = LightFM(loss='warp')

#Entrenamos el modelo, epoch= las veces que la NN va a iterar sobre los datos
model.fit(data['train'],epochs=30,num_threads=2)
modelStack.fit(dataStack['train'],epochs=30,num_threads=2)

print(dataStack['item_features'])

def sampleRecomendation(model,data,user_ids):
	#Obtenemos el numero de peliculas y usuarios en el banco de datos
	nUsers,nItems = data['train'].shape

	for user_id in user_ids:
		#Peliculas que el usuario ya le dio like
		knowPositives = data['item_labels'][data['train'].tocsr()[user_id].indices]

		#Peliculas que modelo va predecir que le gustan al usuario
		scores = model.predict(user_id,np.arange(nItems))

		#Ordenamos del mas likeado al menos
		topItems = data['item_labels'][np.argsort(-scores)]

		print("Usuarios %s", user_id)
		print("Likes:")

		#Imprimimos los 3 que le gustan
		for x in knowPositives[:3]:
			print("         %s" %x)

		print("Recomendaciones:")

		for x in topItems[:3]:
			print("          %s" %x)

#Mandamos a llamar la funcion con un usuario random

#sampleRecomendation(model,data,[3,25,450])


def stackRecomendations(model,data,user_ids):
	#Obtenemos el numero de peliculas y usuarios en el banco de datos
	nUsers,nItems = data['train'].shape

	for user_id in user_ids:
		#Peliculas que el usuario ya le dio like
		knowPositives = data['item_features'][data['train'].tocsr()[user_id].indices]

		#Peliculas que modelo va predecir que le gustan al usuario
		scores = model.predict(user_id,np.arange(nItems))

		#Ordenamos del mas likeado al menos
		topItems = data['item_features'][np.argsort(-scores)]

		print("Usuarios %s", user_id)
		print("Likes:")

		#Imprimimos los 3 que le gustan
		for x in knowPositives[:3]:
			print("         %s" %x)

		print("Recomendaciones:")

		for x in topItems[:3]:
			print("          %s" %x)


stackRecomendations(modelStack,dataStack,[3,25,450])
