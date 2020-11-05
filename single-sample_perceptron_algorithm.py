import numpy as np
import matplotlib.pyplot as plt

sample = np.array([[1,0,1], [1,-1,1], [4,0,1], [-3,-2,1], [0,3,1], [-1,2,1], [2,6,1]])
w = np.array([1, 1, 1]) #initial weight
b = 4 #safety margin 0,4,16,64
iteration = 0

while(True):
   chk = len(sample)
   for idx in range(len(sample)): #sample반복
      if idx<=3: #class1
         if sum(sample[idx]*w)<=b:
            w=w+sample[idx] #update
         else:
            chk -=1 #noupdate
      else: #class2
         if sum(sample[idx]*w)>=b:
            w=w-sample[idx] #update
         else:
            chk -=1 #noupdate
      iteration+=1 #count iteration
   if(chk == 0): #모든 sample에 대해 no update면 break
         break
iteration=iteration-len(sample)
print('iteration: ', iteration) #수렴하기까지 걸린 총 iteration 횟수
print('w: ', w)

x1=np.array([])
y1=np.array([])
x2=np.array([])
y2=np.array([])
for i in range(len(sample)):
   if i<=3:
      x1 = np.append(x1, sample[i][0])
      y1 = np.append(y1, sample[i][1])
   else:
      x2 = np.append(x2, sample[i][0])
      y2 = np.append(y2, sample[i][1])
plt.scatter(x1, y1, c='red')
plt.scatter(x2, y2, c='blue', marker='>')

plt.axvline(x=0, color='gray')
plt.axhline(y=0, color='gray')
x = np.arange(-20,20)
y=((-w[0])/w[1])*x+w[2]/(-w[1])
plt.xlim(-5, 5)
plt.ylim(-4, 7)
plt.plot(x, y, color='black')
plt.title('b={}, w={},iteration={}'.format(b,w,iteration))
plt.show()


