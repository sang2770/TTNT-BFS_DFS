from tkinter import Grid
from tabulate import tabulate

class BFS:
    visited = []  # List for visited nodes.
    queue = []  # Initialize a queue
    road = []
    parents = [] # List for parent node
    table = [] # List for table

    # Read File
    def readFile(self, filename):
        graph = {}
        f = open(filename)
        firstRow = f.readline()
        node,target = firstRow.split() 

        rows = f.readlines()
        for row in rows:
            if row != '\n': 
                row = row.split()
                graph[row.pop(0)] = row or ''
        return graph, node, target


    def bfs(self, graph, node, target):  # function for BFS
        self.visited.append(node)
        self.queue.append(node)

        while self.queue:          # Creating loop to visit each node
            m = self.queue.pop(0)
            self.parents.append(m)

            if m in graph.keys():
                for neighbour in graph[m]:
                    if neighbour not in self.visited:
                        self.visited.append(neighbour)
                        self.queue.append(neighbour)

                row = [m, "TTKT" if m == target else ", ".join(graph[m]), ", ".join(self.visited.copy()), ", ".join(self.queue.copy())]
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

    def createTable(self, table):
        print("------------- BFS -------------")
        head = ["Trạng Thái Đầu", "Danh Sách Kề", "Danh sách đi qua", "Hàng đợi"]

        print(tabulate(table, headers=head, tablefmt="grid"))

    def test(self, file_name):
        try:
            graph, node, target = self.read_file(file_name)
        except:
            print("File không hợp lệ")
            return
        table = self.bfs(graph, node, target)
        if table:
            self.create_table(table)
        self.road.reverse()
        print("Đường đi: "," -> ".join(self.road))

bfs = BFS()
bfs.test("resource/input_BDFS.txt")