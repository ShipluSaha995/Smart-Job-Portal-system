def find(p, x):
    while p[x]!=x:
        x=p[x]
    return x

def union(p,r,x,y):
    a=find[p,x]; b=find(p,y)
    if(a!=b):
        if r[a]>r[b]:
            p[b]=a
        else:
            p[a]=b
            if r[a]==r[b]:
                r[b]+=1


def kruskal(edges):
    for i in range(len(edges)):
        for j in range (i+1, len(edges)):
            if edges[i][2]>edges[j][2]:
                edges[i],edges[j]=edges[j], edges[i]
    nodes=set()
    for u,v,w in edges:
        nodes.add(u)
        nodes.add(v)

    p={n:n for n in nodes}
    r={n:0 for n in nodes}

    mst=[]
    cost=0

    for u,v,w in edges:
        if find(p,u)!=find(p,v):
            union(p,r,u,v)
            mst.append((u,v,w))
            cost+=w
    return mst, cost
            

