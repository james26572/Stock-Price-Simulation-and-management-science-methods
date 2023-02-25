

y = [1,2,3,4,5]
y_probs = [0.9650963656,0.03331428873,0.001486791541,0.00008627182039,0.00001628228723]

y_expected = 0

for i in range(len(y)):
    y_expected += y[i] * y_probs[i]

print("Expected value of y is ",y_expected)


y_squared_expected = 0
import math
for i in range(len(y)):
    y_squared_expected+= math.pow(y[i],2) * y_probs[i]

var_y = y_squared_expected - math.pow(y_expected,2)

print("Variance of y is ", var_y)



import matplotlib.pyplot as plt

plt.bar(y, y_probs)
plt.xlabel('Number of children')
plt.ylabel('Probability')
plt.title('Histogram of Number of Children Born per Single Birth 2006')
plt.show()


x = [1,2,3,4,5]
x_freqs = [3971276,137085,6118,355,67]
x_probs = x_freqs[:]
x_probs = [x/sum(x_freqs) for x in x_freqs]

plt.bar(x,x_probs)
plt.xlabel("Number of Children")
plt.ylabel("Probability")
plt.title('Histogram of Number of Children Born per Single Birth 2016')
plt.show()

