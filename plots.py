from collections import Counter
from linear_algebra import distance
from statistics import mean
import math, random
import matplotlib.pyplot as plt
from data import cities
import knn

def plot_state_borders(plt, color='0.8'):
    pass

def plot_cities(cities):

    
    plots = { "Java" : ([], []), "Python" : ([], []), "R" : ([], []) }

    
    markers = { "Java" : "o", "Python" : "s", "R" : "^" }
    colors  = { "Java" : "r", "Python" : "b", "R" : "g" }

    for (longitude, latitude), language in cities:
        plots[language][0].append(longitude)
        plots[language][1].append(latitude)

    
    for language, (x, y) in plots.items():
        plt.scatter(x, y, color=colors[language], marker=markers[language],
                          label=language, zorder=10)

    plot_state_borders(plt)    

    plt.legend(loc=0)          
    plt.axis([-130,-60,20,55]) 
    plt.title("Favorite Programming Languages")
    plt.show()


def classify_and_plot_grid(cities, k=1):
    """
    TODO
    Classify and plot for Python, Java, and R languages.
    """
    plots = { "Java" : ([], []), "Python" : ([], []), "R" : ([], []) }
    markers = { "Java" : "o", "Python" : "s", "R" : "^" }
    colors  = { "Java" : "r", "Python" : "b", "R" : "g" }

  

    for i in range(-130,-59):
        for j in range(20,56):
            pred=knn.knn_classify(k,cities,(i,j))
            plots[pred][0].append(i)
            plots[pred][1].append(j)

    
    
    for language, (x, y) in plots.items():
        plt.scatter(x, y, color=colors[language], marker=markers[language],
                          label=language, zorder=10)

    plot_state_borders(plt)    

    plt.legend(loc=0)          
    plt.axis([-130,-60,20,55]) 
    plt.title("Favorite Programming Languages")
    plt.show()



if __name__ == "__main__":
    plot_cities(cities)
    classify_and_plot_grid(cities)
    classify_and_plot_grid(cities, 3)
    classify_and_plot_grid(cities, 5)
