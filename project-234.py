import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go 
import plotly.express as px


dataset=pd.read_csv('pro_234.csv')
goal_column=dataset['Goals']
sorted_club_data_asc_order=goal_column.groupby(dataset['Club'])
sum_of_goal_each_club=sorted_club_data_asc_order.sum()
sorted_goals_value=sum_of_goal_each_club.sort_values(ascending=False)
print("premier league goals of each club:",sorted_goals_value)

epl_top_goals=dataset.sort_values(by=['Goals'],ascending=False)[:10]
print("top goal scorer in league:",epl_top_goals)

fig=px.bar(epl_top_goals,x='Name',y='Goals',color='Goals',hover_data=['Club','Age'],text='Goals')
fig.show()