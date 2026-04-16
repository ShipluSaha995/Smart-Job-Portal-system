def dijkstra(graph,start):
    dist={n:9999 for n in graph}
    visited={n:False for n in graph}
    dist[start]=0

    while True:
        min_node=None
        min_val=9999

        for n in graph:
            if not visited[n] and dist[n]<min_val:
                min_val=dist[n]
                min_node=n

        if min_node is None:
            break

        visited[min_node]=True

        for nei in graph[min_node]:
            if dist[min_node]+graph[min_node][nei]<dist[nei]:
                dist[nei]=dist[min_node]+graph[min_node][nei]

    return dist