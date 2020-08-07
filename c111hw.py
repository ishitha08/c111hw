import pandas as pd
import random
import csv
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics

df = pd.read_csv('medium_data.csv')
data = df['Math_score'].tolist()



mean = statistics.mean(data)
std_deviation = statistics.stdev(data)

print('mean-',mean)
print('std_deviation',std_deviation)

def randomSetOfMean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range(0,1000):
    setOfMeans = randomSetOfMean(100)
    mean_list.append(setOfMeans)

std_deviation = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)
print('mean for sample distribution',mean)
print('std_deviation for sample distribution -',std_deviation)

#fig = ff.create_distplot([data],['Math Scores'],show_hist = False)
#fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.20],mode = 'lines',name = 'mean'))
#fig.show()

df = pd.read_csv('medium_data.csv')
data = df['Math_score'].tolist()

meanofsample1 = statistics.mean(data)
print('mean of sample 1 -',meanofsample1)
std_deviation = statistics.stdev(data)

first_std_deviation_start,first_std_deviation_end = mean-std_deviation,mean+std_deviation
second_std_deviation_start,second_std_deviation_end = mean-(2*std_deviation),mean+(2*std_deviation)
third_std_deviation_start,third_std_deviation_end = mean-(3*std_deviation),mean+(3*std_deviation)
print('std1',first_std_deviation_start,first_std_deviation_end)
print('std2',second_std_deviation_start,second_std_deviation_end)
print('std3',third_std_deviation_start,third_std_deviation_end)

fig = ff.create_distplot([mean_list],['student marks'],show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.17],mode = 'lines',name = 'MEAN'))

fig.add_trace(go.Scatter(x = [first_std_deviation_start,first_std_deviation_start],y = [0,0.17],mode = 'lines',name = 'first std deviation start'))
fig.add_trace(go.Scatter(x = [first_std_deviation_end,first_std_deviation_end],y = [0,0.17],mode = 'lines',name = 'first std deviation end'))

fig.add_trace(go.Scatter(x = [second_std_deviation_start,second_std_deviation_start],y = [0,0.17],mode = 'lines',name = 'second std deviation start'))
fig.add_trace(go.Scatter(x = [second_std_deviation_end,second_std_deviation_end],y = [0,0.17],mode = 'lines',name = 'second std deviation end'))

fig.add_trace(go.Scatter(x = [third_std_deviation_start,third_std_deviation_start],y = [0,0.17],mode = 'lines',name = 'third std deviation start'))
fig.add_trace(go.Scatter(x = [third_std_deviation_end,third_std_deviation_end],y = [0,0.17],mode = 'lines',name = 'third std deviation end'))

fig.show()

zscore = (meanofsample1-mean)/std_deviation
print(zscore)