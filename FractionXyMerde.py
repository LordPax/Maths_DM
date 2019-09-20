#!/usr/bin/python
# -*- coding: utf-8-*-

#####################################################################
#																	#
#				BIBLIOTHEQE DE CALCUL FRACTIONNAIRE					#
#																	#
#####################################################################


#Dans cette bibliothèque, une fraction est un tableau (=dictionnaire)
#à deux entrées. 
#La première case (case numéro 0) est numérateur, 
#la seconde case (case numéro 1) est le dénominateur.
#Par exemple
#X=dict()
#X[0]=-12
#X[1]=7
#Alors dans ce cas X est la fraction -12/7 
#Toutes les fonction de cette bibliothèque doivent commencer par Frac

#LES FONCTIONS MARQUEES (faite) SONT FAITES

#Renvoie true si la variable est une fraction (faite)
def FracIs(F) : 
	try :
		F[0]=int(F[0])
		F[1]=int(F[1])
	except : 
		return False

	return True
	
#Renvoie la fraction nulle, cad 0/1 (faite)
def FracZero() :
	res=dict()
	res[0]=0
	res[1]=1
	return res

#Renvoie 1/1 (faite)
def FracUn() :
	res=FracZero()
	res[0]=1
	return res

#Si X est un entier alors la fonction renvoie X/1
#Si X est une fraction alors la fonction renvoie X
#Sinon la fonction renvoie la fraction nulle
# (faite)
def FracPlonge(X) : 

	res=FracZero()
	try : 
		if(FracIs(X)) : return X
		X=int(X)
	except : 
		return res
	
	res[0]=X
	return res
	
#renvoie la valeur (réel) de la fraction en paramètre (faite)
def FracEval(F) : 
	try : 
		num=F[0]
		den=F[1]
	except : 
		return "NaN"   #NaN : Not A Number, pour l'infini
	
	if(den==0) : return "NaN"
	return num/den

#Affiche la fraction sout la forme A/B ou simplement A si B=1 (faite)
def FracAff(F) : 
	F=FracPlonge(F)
	
	if(F[1]==0) : return "NaN"
	if(F[1]==1) : return str(F[0])
	return str(F[0])+"/"+str(F[1])
	
#La fonction renvoie 
#-1 si F1<F2
# 1 si F1>F2
# 0 si F1=F2
#La fonction gère aussi les infinis (cad dénominateur nul) (OK)
def FracComp(F1,F2) :
	F1 = FracEval(F1)
	F2 = FracEval(F2)

	if F1 < F2 :
		return -1
	elif F1 > F2 :
		return 1
	else :
		return 0

#Calcul le PGCD de deux entiers (peut etre OK)
"""def FracPGCD(a, b) : 
	#a = FracEval(a)
	#b = FracEval(b)
	res = None

	while res != 0 :
		if res != None : a = res
		if a < b : a, b = b, a
		res = round(a - b, 1)
		print(a, "-", b, "=", res)

	return a"""
	
def FracPGCD(a, b) : 
	#a = FracEval(a)
	#b = FracEval(b)
	if  : 
	if a == 0 : return b
	if b == 0 : return a
	
	return (FracPGCD(b, a%b))

#Renvoie la fraction simplifiée par le PGCD, et dénominateur toujours positif
def FracSimplif(F) :
	res=FracZero()
	try : 
		num = F[0]
		den = F[1]
	except : return F
	
	p = FracPGCD(num, den)
	res[0] = num
	res[1] = den
	if res[]
		
	return res

def memeDenom(F1, F2) :
	F1 = FracPlonge(F1)
	F2 = FracPlonge(F2)
	if F1[1] != F2[1] :
		Ftmp = FracZero()
		Ftmp[0] = F1[0]
		Ftmp[1] = F1[1]
		F1[0] *= F2[1]
		F1[1] *= F2[1]
		F2[0] *= Ftmp[1]
		F2[1] *= Ftmp[1]
	return F1, F2

#Calcul et simplifie l'addition de deux fractions (OK)
def FracAdd(F1, F2) : 
	res=FracZero()
	F1 = FracPlonge(F1)
	F2 = FracPlonge(F2)
	F1, F2 = memeDenom(F1, F2)
	
	res[0] = F1[0] + F2[0]
	res[1] = F2[1]
	return res
	
#Renvoie l'opposé d'une fraction 
def FracOpp(F) : 
	res=FracZero()
	return res
	
#Renvoie la différence entre F1 et F2 (OK)
def FracSous(F1, F2) :  
	res=FracZero()
	F1 = FracPlonge(F1)
	F2 = FracPlonge(F2)
	F1, F2 = memeDenom(F1, F2)
	
	res[0] = F1[0] - F2[0]
	res[1] = F2[1]
	return res

#Calcul et simplifie le produit de deux fractions (OK)
def FracProd(F1, F2) :
	res=FracZero()
	F1 = FracPlonge(F1)
	F2 = FracPlonge(F2)
	res[0] = F1[0] * F2[0]
	res[1] = F1[1] * F2[1]
	return res

#Calcul l'inverse d'une fraction (OK)
def FracInv(F) : 
	res=FracZero()
	res[0], res[1] = F[1], F[0]
	return res

#Calcul le quotient de fraction (OK)
def FracDiv(F1, F2) : 
	res=FracZero()
	F1 = FracPlonge(F1)
	F2 = FracPlonge(F2)
	res[0] = F1[0] / F2[0]
	res[1] = F1[1] / F2[1]
	return res
	
	
#Pour les tests

X=FracZero()
X[0]=12
X[1]=8

Y=FracZero()
Y[0]=9
Y[1]=-4

a, b = 59.65, 48.45

print("X="+FracAff(X)+"="+FracAff(FracSimplif(X)))
print("Y="+FracAff(Y)+"="+FracAff(FracSimplif(Y)))
print("X = " + str(FracEval(X)))
print("Y = " + str(FracEval(Y)))
print("X = ", FracAff(X), "inverse = ", FracAff(FracInv(X)))
print("X comp Y = "+ str(FracComp(X, Y)))
print("Y comp X = "+ str(FracComp(Y, X)))
print("X comp X = "+ str(FracComp(X, X)))
#print("PGCD(a, b) = " + str(FracPGCD(a, b)))
print("X+Y="+FracAff(FracAdd(X,Y)))
print("X-Y="+FracAff(FracSous(X,Y)))
print("X+1="+FracAff(FracAdd(X,1)))
print("2Y="+FracAff(FracProd(2,Y)))
print("2X="+FracAff(FracProd(2,X)))
print("X^2/Y="+FracAff(FracDiv(FracProd(X,X),Y)))
