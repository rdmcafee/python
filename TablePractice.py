import matplotlib.pyplot as plt
import numpy as np

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()

xVal = np.array([1, 2, 3, 4, 5])
yVal = np.asanyarray([6, 7, 8, 9, 10])

print(xVal)
print(yVal)

xVal = np.reshape(xVal, (-1,1))
yVal = np.reshape(yVal, (-1,1))

print(xVal)
print(yVal)

xVal = xVal.tolist()
yVal = yVal.tolist()

print(xVal)
print(yVal) 

ax.table(cellText = [xVal, yVal], loc = 0)
ax.axis('off')

plt.show()