import random
import plotly_express as px
import plotly.figure_factory as ff

sumList= []

for i in range(0, 100):
    dice1= random.randint(1, 6)
    dice2= random.randint(1, 6)
    sum= dice1+ dice2
    sumList.append(sum)

figure= ff.create_distplot([sumList], ["sums"])
figure.show()