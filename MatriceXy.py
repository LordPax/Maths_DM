#!/usr/bin/python
# -*- coding: utf-8-*-

#####################################################################
#																	#
#				BIBLIOTHEQE DE CALCUL MATRICIELLE					#
#																	#
#####################################################################

#importation de la bibliothèque de calcul matricielle
from FractionXy import *

#Dans cette bibliothèque, une matrice est un tableau (=dictionnaire)
#à deux entrées. Le premier indice est pour la ligne et la seconde pour la colonne.
#Toutes les fonction de cette bibliothèque doivent commencer par Mat

#LES FONCTIONS MARQUEES (faite) SONT FAITES.

#Renvoie True si A est une matrice (faite)
def MatIs(A) : 
	try :
		n=len(A)
		m=len(A[0])
		i=0
		while(i<n) :
			j=0
			while(j<m) :
				if(A[i][j]) : x=0	#On essaye d'acceder à la case mais peut importe ce qu'on fait
				j=j+1
			i=i+1
	except : 
		return False
	return True

#Matrice nulle à n ligne et m colonne (faite)
def MatZero(n, m=-1) :
	try :
		n=int(n)
		m=int(m)
	except :
		return MatZero(1,1)
	
	if(n<=0) : return MatZero(1,1)
	if(m<=0) : return MatZero(n,n)
	
	res=dict()
	i=0
	while(i<n) : 
		res[i]=dict()
		j=0
		while(j<m) : 
			res[i][j]=0
			j=j+1
		i=i+1
	return res

#Affiche La matrice (faite)
def MatAff(M) : 
	if(not(MatIs(M))) : return MatAff(MatZero(1))
	
	n=len(M)
	m=len(M[0])
	
	res=""
	i=0
	while(i<n) :
		j=0
		while(j<m) :
			res+=FracAff(M[i][j])
			if(j<m-1) : res+='\t'
			j=j+1
		res+='\n'
		i=i+1
	return res

	
#Matrice identité
def MatId(n) :
	res=MatZero(n)
	return res
	
#Renvoie la somme de A et B
def MatAdd(A, B) :
	res=MatZero(n)
	return res
	
#Renvoie le produit de la matrice A par le nombre réel X
def MatProdX(A, X) :
	res=MatZero(n)
	return res
	
#Renvoie l'opposé de la matrice A
def MatOpp(A) :
	res=MatZero(n)
	return res
	
#Renvoie la différence de A et B
def MatSous(A,B) : 
	res=MatZero(n)
	return res
	
#Renvoie le produit A*B
def MatProd(A, B) :
	res=MatZero(n)
	return res
	
#Renvoie la matrice transposée
def MatTransp(A) : 
	res=MatZero(n)
	return res

#Renvoie le mineur
def MatMineur(A,p,q) : 
	res=MatZero(n)
	return res

#Calcul le déterminant de A
def MatDet(A) :
	return 0
	
#Renvoie la matrice des cofacteurs de A
def MatCofact(A) : 
	res=MatZero(n)
	return res
	
#Renvoie la matrice inverse (faite)
def MatInv(A) : 
	if(not(MatIs(A))) : return "NaN"
	n=len(A)
	m=len(A[0])
	if(m!=n) : return "NaN"
	
	d=MatDet(A)
	if(d==0) : return "NaN"
	
	return MatProdX(MatTransp(MatCofact(A)), FracInv(d))

#Renvoie le résultat de A^p | p pouvant être négatif
def MatPuiss(A,p) :
	return A
	
"""
#Pour les test
M=MatZero(3)
M[0][0]=2
M[0][1]=0
M[0][2]=-1

M[1][0]=1
M[1][1]=1
M[1][2]=0

M[2][0]=2
M[2][1]=0
M[2][2]=1

print("M=\n"+MatAff(M))
print("Id3=\n"+MatAff(MatId(3)))
print("M+Id3=\n"+MatAff(MatAdd(M, MatId(3))))
print("Id3-M=\n"+MatAff(MatSous(MatId(3),M)))
print("La transposée de M est \n"+MatAff(MatTransp(M)))
print("Le mineur M1,2 \n"+MatAff(MatMineur(M,0,1)))
print("Le mineur M2,2 \n"+MatAff(MatMineur(M,1,1)))
print("det(M)="+FracAff(MatDet(M)))
print("L'inverse de M est\n"+MatAff(MatInv(M)))
print("M*M^{-1}=\n"+MatAff(MatProd(M,MatInv(M))))
print("M^{-1}*M=\n"+MatAff(MatProd(MatInv(M),M)))
#"""