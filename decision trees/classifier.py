from math import log2
import numpy as np

def entropy(data: list):
    s = 0
    for i in set(data):
        Pi = data.count(i) / len(data)
        s += Pi * log2(Pi)

    return abs(-s)


def gini_index(data: list):
    s = 0
    for i in set(data):
        Pi = data.count(i) / len(data)
        s += Pi ** 2

    return 1 - s



class Node():

    def __init__(self, data: list):
        
        self.treshold = 0 
        self.entropy_sum = 1000

        """"break criterions"""
        if len(data) == 1 or data.count(data[0]) == len(data):
            self.is_terminate = True
            self.__to_terminal(data)
            
        else:
            self.is_terminate = False
            self.__find_split(data)


    def __find_split(self, data: list):

        """find treshold for best split"""
        for f in range(len(data)):
            left_node = [data[i] for i in range(len(data)) if i <= f]
            right_node = [data[i] for i in range(len(data)) if i > f]

            l_entropy = entropy(left_node)
            r_entropy = entropy(right_node)

            if (l_entropy + r_entropy) <= self.entropy_sum:
                self.entropy_sum = l_entropy + r_entropy
                self.treshold = f

        self.l_child = Node([data[i] for i in range(len(data)) if i <= self.treshold])
        self.r_child = Node([data[i] for i in range(len(data)) if i > self.treshold])

    def __to_terminal(self, data):
        self.label = max(set(data), key=data.count)


class Decisiontree():

    def fit(self, data: list):
        self.tree = Node(data)


    def predict(self, index):
        
        if not self.tree:
            print("First need to call \"fit\" function")
            return

        return self.__make_pred(self.tree, index)

    def __make_pred(self, tree: Node, index):
        if tree.is_terminate:
            return tree.label
        else:
            if index <= tree.treshold:
                return self.__make_pred(tree.l_child, index)
            else:
                return self.__make_pred(tree.r_child, index)


        
         





data = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

classifier = Decisiontree()
classifier.fit(data)
print(classifier.predict(1))





    





