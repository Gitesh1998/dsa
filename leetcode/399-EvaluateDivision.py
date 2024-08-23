def dfs(graph, s, start, end, result):
    
    if start == end:
        return True
    if start in s:
        return False

    temp = result[0]
    s.add(start)
    for i in range(len(graph)):
        if graph[start][i] != -1 and i not in s:
            result[0] = temp * graph[start][i]
            if dfs(graph, s, i, end, result):
                return True
    return False


class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        
        s = set()
        nodeToIn = {}
        inToNodes = {}
        
        for i in equations:
            if i[0] not in s:
                s.add(i[0])
            if i[1] not in s:
                s.add(i[1])
                
        l = list(s)
        
        for i, val in enumerate(l):
            nodeToIn[val] = i
            inToNodes[i] = val
        
        graph = [[-1 for _ in range(len(l))] for _ in range(len(l))]
        
        for i in range(len(l)):
            graph[i][i] = 1        
        

        for i, val in enumerate(equations):
            graph[nodeToIn[val[0]]][nodeToIn[val[1]]] = values[i]
            graph[nodeToIn[val[1]]][nodeToIn[val[0]]] = 1/values[i]
            
        result = []
        for i in queries:
            if i[0] not in s or i[1] not in s:
                result.append(-1)
                continue
            s1 = set()
            ans = [1]
            res = dfs(graph, s1, nodeToIn[i[0]], nodeToIn[i[1]], ans)
            if res:
                result.append(ans[0])
            else:
                result.append(-1)
        return result
    
    
equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

# equations = [["a","b"],["b","c"],["bc","cd"]]
# values = [1.5,2.5,5.0]
# queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]


# equations = [["a","b"]]
# values = [0.5]
# queries = [["a","b"],["b","a"],["a","c"],["x","y"]]

print(Solution().calcEquation(equations, values, queries))