import numpy as np 
#a = np.array([1,2,3])
#print(a)

#b = np.array([[1,2,3],[4,5,6]])
#print(b)

#c = np.zeros((8,8,3),np.uint8)
#print(c)

#d = np.zeros((8,8),np.uint8)
#print(d)

#e = np.ones((8,8,3),np.uint8)
#print(e)

#f = np.ones((8,8),np.uint8)
#print(f)

#full矩阵
#g = np.full((8,8,3),255,np.uint8)
#print(g)

#full矩阵
h = np.full((8,8),255,np.uint8)
print(h)
#单位矩阵
i = np.identity(4)
print(i)
#单位矩阵，可以不是正方形
j = np.eye(5)
print(j)
k = np.eye(5,7)
print(k)

l = np.eye(5,7,k=3)
print(l)
