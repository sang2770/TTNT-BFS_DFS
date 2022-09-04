from tkinter import Grid
from tabulate import tabulate

class DFS:
    visited = []  # List for visited nodes.
    stack = []  # Initialize a stack
    road = []
    parents = []
    table = []

    def read_file(self, filename):
        graph = {}
    
        f = open(filename)
        first_row = f.readline()
        node,target = first_row.split()

        rows = f.readlines()
        for row in rows:
            if row != '\n': 
                row = row.split()
                graph[row.pop(0)] = row or ''
        return graph, node, target


    def dfs(self, graph, node, target):  # function for DFS
        self.visited.append(node)
        self.stack.insert(0,node)

        while self.stack:          # Creating loop to visit each node
            m = self.stack.pop(0)
            self.parents.append(m)

            if m in graph.keys():
                for neighbour in graph[m]:
                    if neighbour not in self.visited:
                        self.visited.append(neighbour)
                        self.stack.insert(0,neighbour)

                row = [m, "TTKT" if m == target else ", ".join(graph[m]), ", ".join(self.visited.copy()), ", ".join(self.stack.copy())]
                self.table.append(row)
                
            else:
                print("Invalid input")
                break

            if m == target:
                parent = m
                self.road.append(parent)
                for p in reversed(self.parents):
                    if parent in graph[p]:
                        parent = p
                        self.road.append(parent)
                return self.table
        return False

    def create_table(self, table):
        print("------------- DFS -------------")
        head = ["Trạng Thái Đầu", "Danh Sách Kề", "Danh sách đi qua", "Ngăn xếp"]

        print(tabulate(table, headers=head, tablefmt="grid"))

    def test(self, file_name):
        try:
            graph, node, target = self.read_file(file_name)
        except:
            print("File không hợp lệ")
            return
        table = self.dfs(graph, node, target)
        if table:
            self.create_table(table)
        self.road.reverse()
        print("Đường đi: "," -> ".join(self.road))

dfs = DFS()
dfs.test("input_BDFS.txt")