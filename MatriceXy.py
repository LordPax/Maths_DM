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

#Matrice identité (OK)
def MatId(n) :
	n = int(n)
	res=MatZero(n)
	
	for i in range(n) :
		for j in range(n) :
			if i == j :
				res[i][j] = 1
			else :
				res[i][j] = 0
			
	return res
	
#Renvoie la somme de A et B (OK)
def MatAdd(A, B) :
	nA, mA, nB, mB = len(A), len(A[0]), len(B), len(B[0])
	res = MatZero(nA, mA)
	if nA == mA and nB == mB and nA == nB :
		for i in range(nA) :
			for j in range(nA) :
				res[i][j] = FracAdd(A[i][j], B[i][j])
	
	return res
	
#Renvoie le produit de la matrice A par le nombre réel X (OK)
def MatProdX(A, X) :
	nA, mA = len(A), len(A[0])
	res = MatZero(nA, mA)
	for i in range(nA) :
		for j in range(mA) :
			res[i][j] = FracProd(A[i][j], X)
	return res
	
#Renvoie l'opposé de la matrice A (OK)
def MatOpp(A) :
	nA, mA = len(A), len(A[0])
	res = MatZero(nA, mA)
	for i in range(nA) :
		for j in range(mA) :
			res[i][j] = FracProd(A[i][j], -1)
	return res
	
#Renvoie la différence de A et B (OK)
def MatSous(A,B) : 
	nA, mA, nB, mB = len(A), len(A[0]), len(B), len(B[0])
	res = MatZero(nA, mA)
	if nA == mA and nB == mB and nA == nB :
		for i in range(nA) :
			for j in range(nA) :
				res[i][j] = FracSous(A[i][j], B[i][j])
	
	return res
	
#Renvoie le produit A*B (OK)
def MatProd(A, B) :
	nA, mA, mB, pB = len(A), len(A[0]), len(B), len(B[0])
	res = MatZero(mA)
	if nA == pB and mA == mB :
		for i in range(nA) :
			for j in range(pB) :
				for k in range(mA) :
					res[i][j] = FracAdd(res[i][j], FracProd(A[i][k], B[k][j]))
	return res
	
#Renvoie la matrice transposée (OK)
def MatTransp(A) : 
	nA, mA = len(A), len(A[0])
	res = MatZero(nA)
	if nA == mA :
		for i in range(nA) :
			for j in range(nA) :
				if i != j :
					res[i][j] = A[j][i]
				else :
					res[i][j] = A[i][j]
	return res

#Renvoie le mineur (OK)
def MatMineur(A,p,q) : 
	nA, mA = len(A), len(A[0])
	nA2 = nA - 1
	res = MatZero(nA2)
	if nA == mA :
		for i in range(nA2) :
			for j in range(nA2) :
				if i < p and j < q :
					res[i][j] = A[i][j]
				elif i < p and j >= q :
					res[i][j] = A[i][j+1]
				elif i >= p and j < q :
					res[i][j] = A[i+1][j]
				elif i >= p and j >= q :
					res[i][j] = A[i+1][j+1]

	return res

#Calcul le déterminant de A (OK)
def MatDet(A) :
	nA, mA = len(A), len(A[0])
	j = 0
	res = 0
	if nA == mA :
		if nA > 2:
			for i in range(nA) :
				res = FracAdd(res, FracProd((-1)**(i+j), FracProd(A[i][j], MatDet(MatMineur(A, i, j)))))
		elif nA == 2 :
			res = FracSous(FracProd(A[0][0], A[1][1]), FracProd(A[1][0], A[0][1]))
		elif nA == 1 :
			res = A[0][0]

	return res

				
	
#Renvoie la matrice des cofacteurs de A (OK)
def MatCofact(A) : 
	nA, mA = len(A), len(A[0])
	res = MatZero(nA)
	if nA == mA :
		for i in range(nA) :
			for j in range(nA) :
				res[i][j] = FracProd((-1)**(i+j), MatDet(MatMineur(A, i, j)))
	return res
	
#Renvoie la matrice inverse (faite)
def MatInv(A) : 
	if(not(MatIs(A))) : return "NaN"
	n = len(A)
	m = len(A[0])
	if(m != n) : return "NaN"
	
	d = MatDet(A)
	if(d == 0) : return "NaN"
	
	return MatProdX(MatTransp(MatCofact(A)), FracInv(d))

#Renvoie le résultat de A^p | p pouvant être négatif
def MatPuiss(A,p) :
	nA, mA = len(A), len(A[0])
	res = MatZero(nA)
	if nA == mA :
		res = A

		if p < -1 or p > 1 :
			for k in range(abs(p)) :
				res = MatProd(res, A)
		elif p == 0 :
			res = MatZero(nA)

		if p <= -1 :
			res = MatInv(res)
	return res
	

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
print("M*5=\n"+MatAff(MatProdX(M, 5)))
print("opp(M)=\n"+MatAff(MatOpp(M)))
print("M*Id3=\n"+MatAff(MatProd(M, MatId(3))))
print("transp(M)=\n"+MatAff(MatTransp(M)))
print("Id3-M=\n"+MatAff(MatSous(MatId(3),M)))
print("Le mineur M1,2 \n"+MatAff(MatMineur(M,0,1)))
print("Le mineur M2,2 \n"+MatAff(MatMineur(M,1,1)))
print("det(M)="+FracAff(MatDet(M)))
print("Co(M)=\n"+MatAff(MatCofact(M)))
print("L'inverse de M est\n"+MatAff(MatInv(M)))
print("M^p=\n"+MatAff(MatPuiss(M, -1)))
print("M*M^{-1}=\n"+MatAff(MatProd(M,MatInv(M))))
print("M^{-1}*M=\n"+MatAff(MatProd(MatInv(M),M)))
