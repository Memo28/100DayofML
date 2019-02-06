import csv 
import numpy as np 
from sklearn.svm import SVR
import matplotlib.pyplot as plt 
plt.switch_backend('TKAgg')  

dates = []
prices = []

#Leemos el csv y lo guardamos en los arreglos para luego mapearlos
# en una grafica usando plt
def getData(filename):
	with open(filename,'r') as csvfile:
		csvFileReader = csv.reader(csvfile)
		next(csvFileReader)
		for row in csvFileReader:
			#leemos la fecha y guardamos cada dato en una seccion del array
			dates.append(int(row[0].split('-')[0]))
			prices.append(float(row[1])) 

		return

#Creamos el modelo de predición
def predictPrices(dates,prices,x):
	#Recreamos el arreglo y lo pasamos a un arreglo de una sola dimension
	dates = np.reshape(dates,(len(dates),1))
	#Creamos un Support Vector Machine
	#un SVM trabaja con datos que ya estan estan clasificados
	#e intenta meter datos que aun no estan clasificados dentro de una clase
	#en este caso en especifico, no queremos clasificar, lo que se hara es 
	#regresion, que es cuando a partir de una serie de datos se predice cual sera el
	#el siguiente valor, a lo que se le llama un SVR
	#kernal = tipo de SVM
	#C es el error posible
	svrLen = SVR(kernel="linear",C=1e3)
	svrPoly = SVR(kernel="poly",C=1e3)
	svrRbf = SVR(kernel="rbf",C=1e3,gamma=0.1)

	#Entrenamos los modelos
	svrLen.fit(dates,prices)
	svrPoly.fit(dates,prices)
	svrRbf.fit(dates,prices)
	#Mandamos a graficar los modelos

	plt.scatter(dates,prices,color="black",label="Data")
	plt.plot(dates,svrLen.predict(dates),color="red",label="Linear Model")
	plt.plot(dates,svrPoly.predict(dates),color="blue",label="Poly Model")
	plt.plot(dares,svrRbf.predict(dates),color="green",label="RBF Model")
	plt.xlabel('Dates')
	plt.ylabel('Prices')
	plt.title('Support Vector Regression')
	plt.legend()
	plt.show()

	return svrRbf.predict[0],svrLen.predict[0],svrPoly.predict[0]

getData('LALAB.MX.csv')

predictPricesV = predictPrices(dates,prices,29)

print(predictPricesV) 