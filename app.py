import matplotlib.pyplot as plot


#set up the data
labels=('Python','C#','Java','PHP','Ruby')
index=(1,2,3,4,5)
sizes=90,20,54,76,18

#setting up bar chart
plot.bar(index,sizes,tick_label=labels)
plot.ylabel('Usage')
plot.xlabel('Programming Languages')


#display the chart
plot.show()
#pie chart set up
plot.pie(sizes,labels=labels,autopct='%1.f%%',counterclock=False,startangle=105)
plot.show()


import matplotlib.pyplot as plt
def draw_scatterplot(x_values, y_values):
    plt.scatter(x_values, y_values, s=20)
    plt.title("Scatter Plot")
    plt.xlabel("x values")
    plt.ylabel("y values")
    plt.show()
draw_scatterplot()