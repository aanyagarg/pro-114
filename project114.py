import pandas as p 
import plotly.express as pe
import numpy as np 

data = p.read_csv("project114.csv")

ToeflScore = data["TOEFL Score"].tolist()

Chance = data["Chance of Admit "].tolist()

# fig = pe.scatter(x=ToeflScore , y = Chance)

# fig.show()

# ------------ Assumptions m=1 , c = 0 --------------------------

m = 1
c = 0
y = []

for x in ToeflScore:
    y_value = m*x + c

    y.append(y_value)


# fig = pe.scatter(x=ToeflScore , y = Chance)

# fig.update_layout(shapes=[
#     dict(
#         type='line',
#         y0 = min(y) , y1 = max(y) , 
#         x0 = min(ToeflScore) , x1 = max(ToeflScore
#     )
# ])


# fig.show()


# ------------ Assumptions m=0.95 , c = -93 --------------------------

m = 0.95
c = -93
y = []

for x in ToeflScore:
    y_value = m*x + c

    y.append(y_value)


fig = pe.scatter(x=ToeflScore , y = Chance)

fig.update_layout(shapes=[
    dict(
        type='line',
        y0 = min(y) , y1 = max(y) , 
        x0 = min(ToeflScore) , x1 = max(ToeflScore)
    )
])


# fig.show()

x = 250
y = m *x + c

# print("Chance  of someone for admission with ToeflScore - 250 using hit and trial --> " , y)

# ---------------------------------- Using Algorithm ------------------------------------

ToeflScoreArray = np.array(ToeflScore)
ChanceArray = np.array(Chance)

m , c = np.polyfit(ToeflScoreArray, ChanceArray, 1)

y = []

for x in ToeflScoreArray:
    y_value = m*x + c

    y.append(y_value)


fig = pe.scatter(x=ToeflScoreArray , y = ChanceArray)

fig.update_layout(shapes=[
    dict(
        type='line',
        y0 = min(y) , y1 = max(y) , 
        x0 = min(ToeflScoreArray) , x1 = max(ToeflScoreArray)
    )
])


# fig.show()

x = 250
y = m *x + c

print("Chances of admit if the TOEFL score 250 is using algorithm --> " , y)








