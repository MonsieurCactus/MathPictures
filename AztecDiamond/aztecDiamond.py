import random

size = input("Aztec Diamond Size? ")
width = 16
empty, u,r,d,l = 0,1,2,3,4

def randblock(i,j,x):
	if(int(2*random.random())):
		x[i][j] = r
		x[i+1][j] = l
		x[i][j+1]=r
		x[i+1][j+1]=l
	else:
		x[i][j] = u
		x[i+1][j] = u
		x[i][j+1] = d
		x[i+1][j+1]=d
	return x
	
def bad(i,j,x):
	if( x[i][j] == r and x[i][j+1]==r and x[i+1][j] == l and x[i+1][j+1]==l):
		return (i+j+currentlevel+1)%2
	if( x[i][j] == u and x[i][j+1]==d and x[i+1][j] == u and x[i+1][j+1] == d):
		return (i + j + currentlevel+1)%2
	return 0

def deletebadblocks(x):
	for i in range(2*size - 1):
		for j in range(2*size -1):
			if(bad(i,j,x)):
				x[i][j] = empty
				x[i+1][j] = empty
				x[i][j+1] = empty
				x[i+1][j+1] = empty
	return x

def shuffle(x):
	z = []
	for m in range(2*size):
		z += [[]]
		for n in range(2*size):
			z[m] += [0]	
	for i in range(2*size):
		for j in range(2*size):
			if(x[i][j] != empty):
				if(x[i][j] == u):
					if((i+j+currentlevel)%2):
						z[i-1][j] = u
						z[i-1][j+1]=d
						x[i][j] = empty
						x[i][j+1]=empty
					else:
						z[i+1][j]=u
						z[i+1][j+1]=d
						x[i][j] = empty
						x[i][j+1]=empty
				if(x[i][j] == r):
					if((i+j+currentlevel)%2):
						z[i][j-1] = r
						z[i+1][j-1]=l
						x[i][j] = empty
						x[i+1][j] = empty
					else:
						z[i][j+1] = r
						z[i+1][j+1] = l
						x[i][j] = empty
						x[i+1][j] = empty
	return z
	
def create(x):
	for i in range(2*size):
		for j in range(2*size):
			if(x[i][j] == empty and abs(size - 0.5 - i) + abs(size - 0.5 - j) <= currentlevel):
				x = randblock(i,j,x)
	return x

import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
	
if __name__ == "__main__":

	ar = []
	for x in range(2*size):
		ar += [[]]
		for y in range(2*size):
			ar[x] += [0]
	ar = randblock(size-1, size-1, ar)
	currentlevel=1
	
	#for x in ar:
	#	print x
	
	for x in range(size-1):
		ar = deletebadblocks(ar)
		ar = shuffle(ar)
		currentlevel+= 1
		ar = create(ar)
	
	#print
	#for x in ar:
	#	print x
		
	fig = plt.figure()
	ax = fig.add_subplot(111)
	for i in range(2*size):
		for j in range(2*size):
			if(ar[i][j] == empty): pass
			else:
				if(ar[i][j] == d):
					verts = [(i,j),(i,j+1),(i+1,j+1),(i+1,j)]
				if(ar[i][j] == l):
					verts = [(i,j+1),(i+1,j+1),(i+1,j),(i,j)]
				if(ar[i][j] == r): 
					verts = [(i+1,j+1),(i,j+1),(i,j),(i+1,j)]
				if(ar[i][j] == u): 
					verts = [(i,j+1),(i,j),(i+1,j),(i+1,j+1)]
				codes = [ Path.MOVETO,
					Path.LINETO,
					Path.LINETO,
					Path.LINETO
					]
				path = Path(verts, codes)
				patch = patches.PathPatch(path, facecolor="white")
				ax.add_patch(patch)
	ax.set_aspect(1)
	ax.set_xlim(0,2*size)
	ax.set_ylim(0,2*size)
	plt.show()