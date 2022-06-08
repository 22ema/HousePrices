
import matplotlib.pyplot as plt
import math
class MakeGraph():

    def __init__(self, dataframe):
        self.dataframe = dataframe
        self.figure = plt.figure(figsize=(14, 12))

    def bivariate_graph(self, M, N, number, count):
        '''
        Make bivariate graph
        :param M: x axis
        :param N: y axis
        :param number: total graph number
        :param count: current graph number
        '''
        ax = self.figure.add_subplot(math.ceil(math.sqrt(number)), math.ceil(math.sqrt(number)), count)
        ax.scatter(self.dataframe[M], self.dataframe[N])
        ax.set_title('Scatterplot of {} and {}'.format(M, N))
        ax.set_xlabel(M)
        ax.set_ylabel(N)

    def graph_show(self):
        '''
        show all plt graph
        '''
        plt.show()

    def clear_graph(self):
        plt.clf()

    def save_graph(self, path):
        plt.savefig(path)