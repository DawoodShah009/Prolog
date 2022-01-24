# MINIMUM COST SPANNING TREE (GREEDY APPROACH). 
def baaltiWithTree(graph,router):
    bucket = []
    Q = []
    bucket.append(router)
    Q.extend(graph[router])
    print("Router = 'a'")

    while len(graph) != len(bucket): # Q = [f,k,b]   !=== Q = [(f,8),(k,3),(b,7)] !==== templist = [f,8,k,3,b,7] 
                                        ##(odd index represents vertex and even index represents weights)
        print("Bucket:" , bucket)
        print("Queue:", Q)
        temp = []
        for v in Q:
            for i in v:
                temp.append(i)
        minimum = temp[1]
        for i in range(1,len(temp),2):
            if temp[i] < minimum:
                minimum = temp[i]
                D = i                       # saving index value.
        adjacentVertex = Q[D//2]
        if adjacentVertex[0] not in bucket:      
            bucket.append(adjacentVertex[0])
            Q.extend(graph[adjacentVertex[0]])
        else:
            Q.remove(adjacentVertex)
            

    return bucket 

graph = { "a" : [("k", 9),("f" , 3),("b" , 2)] , "b" : [("c" , 2),("d" , 3),("a" , 2)] , "c" : [("k" , 5),("b" , 2)]\
    ,"d" : [("b" , 3),("f" , 2),("e" , 1)] , "e" : [("d" , 1)] , "f" : [("g" , 4),("a" , 3),("d" , 2)]\
    , "g" : [("f" , 4),("h" , 2)] , "h" : [("g" , 2),("j" , 4),("i" , 6)] ,"i":[("j" , 3),("k" , 3),("h" , 6 )]\
    , "j" : [("i" , 3),("h" , 4)] ,"k": [("i" , 3),("a" , 9),("c" , 5)]}

router = "a"


myBucket = baaltiWithTree(graph , router)
print("Spaining Tree:" , myBucket)
