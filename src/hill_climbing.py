import re
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


class HillClimbing:
    visited = []  # List for visited nodes.
    stack = []  # Initialize a queue
    L1 = PriorityQueue()
    L1_p = []
    road = []  # road
    parents = []  # List for parent node
    table = []  # List for table

    # Read File
    def readFile(self, filename):
        graph = {}
        f = open(filename)
        # read weight
        firstRow = f.readline()
        nodeDraft = firstRow.split()
        for n in nodeDraft:
            key, value = n.split('-')
            graph[key] = Node(key, value)
        # read node start and node target
        node, target = f.readline().split()

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

    def insertL1ToStack(self):
        nodes = []
        self.L1_p = []
        while self.L1.empty() != True:
            m: Tuple = self.L1.get(0)
            if (m):
                node = m[1].value
                nodes.insert(0, node)
        for node in nodes:
            self.stack.insert(0, node)
            self.L1_p.insert(0, node)

    def hillClimbing(self, graph, start, target):  # function for hillClimbing
        self.visited.append(start)
        self.stack.insert(0, start)
        while self.stack:          # Creating loop to visit each node
            node = self.stack.pop(0)
            self.parents.append(node)
            if node in graph.keys():
                for neighbour in graph[node].neighbour:
                    if neighbour not in self.visited:
                        self.visited.append(neighbour)
                        self.L1.put(
                            (graph[neighbour].weight, graph[neighbour]))
                self.insertL1ToStack()
                row = [node, "TTKT" if node == target else ", ".join(
                    graph[node].neighbour), ", ".join(self.visited.copy()), ", ".join(self.L1_p), ", ".join(self.stack)]
                self.table.append(row)
                if (node == target):
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
        print("------------- HillClimbing -------------")
        head = ["Trạng Thái Đầu", "Danh Sách Kề",
                "Danh sách đi qua", "Danh Sách L1", "Stack"]
        table_result = tabulate(self.table, headers=head, tablefmt="grid")
        return table_result

    def test(self, file_name):
        try:
            graph, start, target = self.readFile(file_name)
        except:
            print("File không hợp lệ")
            return
        table = self.hillClimbing(graph, start, target)
        if table:
            self.createTable()
            self.road.reverse()
            print("Đường đi: ", " -> ".join(self.road))
            try:
                self.writeFile("resource/output/output_hill.txt")
            except:
                print("File không hợp lệ")
                return
        else:
            print("Không tìm thấy")


hillClimbing = HillClimbing()
hillClimbing.test("resource/input/input_hill.txt")
