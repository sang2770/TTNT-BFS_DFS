from typing import Tuple
from tabulate import tabulate
from queue import PriorityQueue
import copy
class Node(object):
    neighbour = []
    value = ''
    weight = 0
    def __init__(self, value, weight):
        self.value = value
        self.weight = int(weight)

class BestFirstSearch:
    visited = []  # List for visited nodes.
    priorityQueue = PriorityQueue()  # Initialize a queue
    queue = PriorityQueue()
    road = [] # road 
    parents = [] # List for parent node
    table = [] # List for table

    # Read File
    def readFile(self, filename):
        graph = {}
        f = open(filename)
        # read weight
        firstRow = f.readline()
        nodeDraft = firstRow.split()
        for n in nodeDraft:
            key,value = n.split('-')
            graph[key]=Node(key, value)
        # read node start and node target
        node,target = f.readline().split() 

        rows = f.readlines()
        for row in rows:
            if row != '\n': 
                start, *neighbor = row.split()
                graph[start].neighbour = neighbor or []
        return graph, node, target

    def writeFile(self, filename):
        with open(filename, 'w', encoding="utf-8") as f:
            f.write(self.createTable())
        f.close()
    def getQueue(self):
        q = PriorityQueue()
        q.queue = copy.deepcopy(self.priorityQueue.queue)
        # print(repr(q), repr(self.priorityQueue))
        nodes = ''
        while q.empty() != True:
            node = q.get(0)
            if(node):
                nodes +=node[1].value
        return nodes
    def besrFirstSearch(self, graph, start, target):  # function for besrFirstSearch
        self.visited.append(start)
        self.priorityQueue.put((graph[start].weight, graph[start]))
        while self.priorityQueue.empty() != True:          # Creating loop to visit each node
            m: Tuple = self.priorityQueue.get(0)
            node = m[1].value
            self.parents.append(node)
            if node in graph.keys():
                for neighbour in graph[node].neighbour:
                    if neighbour not in self.visited:
                        self.visited.append(neighbour)
                        self.priorityQueue.put((graph[neighbour].weight, graph[neighbour]))
                row = [node, "TTKT" if node == target else ", ".join(graph[node].neighbour), ", ".join(self.visited.copy()), ", ".join(self.getQueue())]
                self.table.append(row)
                if(node == target):
                    parent = node
                    self.road.append(parent)
                    for p in reversed(self.parents):
                        if parent in graph[p].neighbour:
                            parent = p
                            self.road.append(parent)
                    return self.table

            else:
                print("Invalid input")
                break
        
        return False

    def createTable(self):
        print("------------- besrFirstSearch -------------")
        head = ["Trạng Thái Đầu", "Danh Sách Kề", "Danh sách đi qua", "Hàng đợi"]
        table_result = tabulate(self.table, headers=head, tablefmt="grid")
        return table_result

    def test(self, file_name):
        try:
            graph, start, target = self.readFile(file_name)
        except:
            print("File không hợp lệ")
            return
        table = self.besrFirstSearch(graph, start, target)
        if table:
            self.createTable()
            self.road.reverse()
            print("Đường đi: "," -> ".join(self.road))
            try:
                self.writeFile("resource/output.txt")
            except:
                print("File không hợp lệ")
                return
        else:
            print("Không tìm thấy")
        

bestFirstSearch = BestFirstSearch()
bestFirstSearch.test("resource/input/input_best_fist_search.txt")