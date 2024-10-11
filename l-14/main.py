class Graf:
    def __init__(self,n):
        self.n=n
        self.adj=[[]*n for i in range(n)]
    def adde(self,a,b):
        self.adj[a].append(b)
        self.adj[b].append(a)
    def DFS(self,temp,v,visited):
        visited[v]=True
        temp.append(v)
        for i in self.adj[v]:
            if visited [i] == False:
                temp = self.DFS(temp,i,visited)
        return temp
    def Connected_compnents(self):
        visited=[]
        cc = []
        for i in range(self.n):
            visited.append(False)
        for v in range(self.n):
            if visited[v] == False:
                temp = []
                cc.append(self.DFS(temp,v,visited))
        return cc 
    
g=Graf(5)
g.adde(2,0)
g.adde(3,1)
g.adde(3,4)
cc = g.Connected_compnents()
print("Following are the connected components : ")
print(cc)