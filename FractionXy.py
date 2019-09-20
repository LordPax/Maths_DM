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
	F=FracPlonge(F)
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
#La fonction gère aussi les infinis (cad dénominateur nul)
def FracComp(F1,F2) :
	res=FracZero()
	F1=FracPlonge(F1)
	F2=FracPlonge(F2)
	try : 	
		num1=F1[0]
		num2=F2[0]
		den1=F1[1]
		den2=F2[1]
	except : return 0
	x1=FracEval(F1)
	x2=FracEval(F2)
	if(den1==0) :
		if(den2==0) :
			if(num1<=0 and num2<=0) : return 0
			if(num1<=0 and num2>0) : return -1
			if(num1>0 and num2<=0) : return 1
			if(num1>0 and num2>0) : return 0
		else :
			if(num1<=0) : return -1
			return 1
	else :
		if(den2==0):
			if(num2<=0) : return 1
			return -1
		
	if(x1<x2) : return -1
	if(x1>x2) : return 1
	return 0

#Calcul le PGCD de deux entiers
def FracPGCD(a,b) : 
	if(a<0) : return FracPGCD(-a,b)
	if(b<0) : return FracPGCD(a,-b)
	if(a==0) : return b
	if(b==0) : return a
	return(FracPGCD(b, a%b))

#Renvoie la fraction simplifiée par le PGCD, et dénominateur toujours positif
def FracSimplif(F) :
	F=FracPlonge(F)
	try : 
		num=F[0]
		den=F[1]
	except : return F
	p=FracPGCD(num, den)
	res=FracZero()
	res[0]=num//p#res[0]=int(num/p)
	res[1]=den//p
	if(res[1]<0) :
		res[0]=-res[0]
		res[1]=-res[1]
	return res

#Calcul et simplifie l'addition de deux fractions
def FracAdd(F1, F2) : 
	F1=FracPlonge(F1)
	F2=FracPlonge(F2)
	res=FracZero()
	res[0]=F1[0]*F2[1]+F2[0]*F1[1]
	res[1]=F1[1]*F2[1]
	return FracSimplif(res)
	
#Renvoie l'opposé d'une fraction
def FracOpp(F) : 
	F=FracPlonge(F)
	res=FracZero()
	res[0]=-F[0]
	res[1]=F[1]
	return res
	
#Renvoie la différence entre F1 et F2
def FracSous(F1, F2) :  
	return FracAdd(F1, FracOpp(F2))

#Calcul et simplifie le produit de deux fractions
def FracProd(F1, F2) :
	F1=FracPlonge(F1)
	F2=FracPlonge(F2)
	res=FracZero()
	res[0]=F1[0]*F2[0]
	res[1]=F1[1]*F2[1]
	return FracSimplif(res)

#Calcul l'inverse d'une fraction
def FracInv(F) :  
	F=FracPlonge(F)
	res=FracZero()
	res[0]=F[1]
	res[1]=F[0]
	return res

#Calcul le quotient de fraction
def FracDiv(F1, F2) : 
	return FracProd(F1, FracInv(F2))
	
	
"""
#Pour les tests

X=FracZero()
X[0]=12
X[1]=8

Y=FracZero()
Y[0]=9
Y[1]=-4

print("X="+FracAff(X)+"="+FracAff(FracSimplif(X)))
print("Y="+FracAff(Y)+"="+FracAff(FracSimplif(Y)))
print("X+Y="+FracAff(FracAdd(X,Y)))
print("X-Y="+FracAff(FracSous(X,Y)))
print("X+1="+FracAff(FracAdd(X,1)))
print("2Y="+FracAff(FracProd(2,Y)))
print("2X="+FracAff(FracProd(2,X)))
print("X^2/Y="+FracAff(FracDiv(FracProd(X,X),Y)))
#"""
