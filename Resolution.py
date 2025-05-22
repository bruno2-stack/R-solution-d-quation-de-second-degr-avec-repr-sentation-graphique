from cmath import *
import matplotlib.pyplot as plt
import numpy as np
print("Resolution des équations de la forme aX² + bX + c = 0")

# Convertir les nombres en flottant
a=''
while type(a)!=float or a==0:
    a=input('Veuillez entrer le coefficient a de votre équation')
    try:
        a=float(a)
    except   ValueError:
        print("vous n'avez pas saisir un nombre") 
        a='e'
        continue
    if a==0 :
        print(" Erreur le coéfficient a doit etre supérieur à 0")

b=''
while type(b)!=float:
    b=input('Veuillez entrer le coefficient b de votre équation ')
    try:
        b=float(b)
    except   ValueError:
        print("vous n'avez pas saisir un nombre ") 
        b='a' 
c=''
while type(c)!=float :
    c=input('Veuillez entrez le coefficient c de votre équation ')
    try:
        c=float(c)
    except   ValueError:
        print("vous n'avez pas saisir un nombre") 
        c='c'
x0=-b/(2*a)
f_xo=a*(x0**2)+(b*x0)+c


# Recherche des solutions 
def solutions():
    discriminant=b**2-(4*a*c)
    if discriminant==0:
        X0=-b/(2*a)
        print("L'équation admet une solution double X0 \n X0 = ",X0)
    elif discriminant<0:
        print("L'équation n'admet de solution réelle (dans R)")
    else:
        x1=(-b-sqrt(discriminant))/(2*a) 
        x2=(-b+sqrt(discriminant))/(2*a) 
        print("L'équation admet deux solution réelle X1 et X2 \n X1 = ",x1,"\n X2 = ",x2)
print(solutions())


# étude de fonction 
def variation():
    x0=-b/(2*a)
    f_xo=a*(x0**2)+(b*x0)+c
    print("la derivé de notre equation est : df = ",2*a,"X + ",b,"\n La solution de l'équation df = 0 est :\n X=",x0)
    if a<0:
        print("La fonction f est croissante sur l'intervalle ]-~,",x0,"[ et  décroissante sur ]",x0,",+~[")
    else:
            print("La fonction f est décroissante sur l'intervalle ]-~,",x0,"[ et croissante sur ]",x0,",+~[")
print(variation())


# le tracé de la courbe
fig=plt.clf()
plt.scatter(x0,f_xo,color='red',marker='o',label='Point critique')
X=np.linspace(-100,100,1000) 
Y=(a*X**2)+b*X+c       
plt.plot(X,Y,color='red')
plt.xlabel("axe des X ")
plt.ylabel("Axe des Y")
plt.title("Le tracé de la courbe de la fonction f ")
plt.legend()
plt.show()
