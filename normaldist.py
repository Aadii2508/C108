import pandas as pd
import csv
import plotly_express as px
import plotly.figure_factory as ff

file= pd.read_csv("data.csv")
heightList= file["Height(Inches)"].to_list()
weightList= file["Weight(Pounds)"].to_list()

figure= ff.create_distplot([weightList], ["Weights"])
figure.show()