import numpy as np
'''
#x=np.zeros((2,3,4))
x = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
#x=np.empty((2,2))
#x=np.arange(2,15)
x=np.random.randn(3,3)
print(x)
y=x[1:2,:2]
print('output ;\n',y)
print(x.size)
print(y.shape)
print(x.dtype)'''

x=np.arange(15)
print(x)

x=np.reshape(x,(3,5))
print(x)