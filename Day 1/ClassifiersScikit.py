from sklearn import tree
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import GaussianNB


#Vamos a tomar la altura, cintura y tamaño de zapato para predecir si
# a partir de ciertas medidas dadas determinar si es hombre/mujer
#Data set ["Alto,Ancho,T.Zapato"]
X = [[181,80,44],[177,70,43],[160,60,38],[154,54,37],
     [166,65,40 ],[190,90,47],[175,64,39],[177,70,40], [159,55,37],
     [171,75,42],[181,85,43]
    ]

Y = ['male','female','female','female','male','male',
     'male','female','male','female','male'
    ]

#Clasificadores
clfDecisionTree = tree.DecisionTreeClassifier()
clfNN =  MLPClassifier(alpha=1)
clfNaiveBayes = GaussianNB()

#Training the models
clfDecisionTree.fit(X,Y)
clfNN.fit(X,Y)
clfNaiveBayes.fit(X,Y)

predicDT = clfDecisionTree.predict([[150,80,44]])
predictNN = clfNN.predict([[150,80,44]])
predictNB = clfNaiveBayes.predict([[150,80,44]])

print ("Resultado Decision Tree:" , predicDT)
print ("Resultado Red Neuronal:" , predictNN)
print ("Resultado Naive Bayes:", predictNB)



