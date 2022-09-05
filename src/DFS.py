from pickle import TRUE
from tkinter import Grid
from tabulate import tabulate

class DFS:
    visited = []  # List for visited nodes.
    stack = []  # Initialize a stack
    road = []
    parents = {}
    table = []
    node = 0
    target = 0

    def read_file(self, filename):
        graph = {}
    
        f = open(filename)
        first_row = f.readline()
        self.node, self.target = first_row.split()

        rows = f.readlines()
        for row in rows:
            if row != '\n': 
                row = row.split()
                graph[row.pop(0)] = row or ''
        return graph, self.node, self.target


    def dfs(self, graph, node, target):  # function for DFS
        self.visited.append(node)
        self.stack.insert(0,node)

        while self.stack:          # Creating loop to visit each node
            m = self.stack.pop(0)
            if m in graph.keys():
                for neighbour in graph[m]:
                    if neighbour not in self.visited:
                        self.visited.append(neighbour)
                        self.parents[neighbour] = m
                        self.stack.insert(0,neighbour)
                row = [m, "TTKT" if m == target else ", ".join(graph[m]), ", ".join(self.visited.copy()), ", ".join(self.stack.copy())]
                self.table.append(row)
                
            else:
                print("Invalid input")
                break

            if m == target:
                self.getRoad()
                return self.table
        return False
    def getRoad(self):
        while(self.node != self.target):
            self.road.append(self.target)
            self.target = self.parents[self.target]
        self.road.append(self.node)

    def create_table(self, table):
        print("------------- DFS -------------")
        head = ["Trạng Thái Đầu", "Danh Sách Kề", "Danh sách đi qua", "Ngăn xếp"]

        print(tabulate(table, headers=head, tablefmt="grid"))

    def test(self, file_name):
        try:
            self.graph, self.node, self.target= self.read_file(file_name)
        except:
            print("File không hợp lệ")
            return
        table = self.dfs(self.graph, self.node, self.target)
        if table:
            self.create_table(table)
        self.road.reverse()
        print("Đường đi: "," -> ".join(self.road))

dfs = DFS()
dfs.test("resource/input_BDFS.txt")