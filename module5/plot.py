import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[10,20,3,11,2]
plt.bar(x,y,label='asdf')
plt.plot(x,y,color='red',label='square')
plt.title("PLOt")
plt.xlabel("Xaxis")
plt.ylabel("Yaxis")
plt.legend()
plt.grid(True)
plt.show()