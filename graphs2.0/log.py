
#                                      BEGIN LOG
def logging(graph,Qmax):
    log = open("/tmp/logging.txt","w")
    log.write("[LENGTH]-> (%d)\n" % len(graph))
    log.write("[Maximal Clique]-> %s  \n" % (str(Qmax)))
    for i in range(0,len(graph)):
        log.write("[%d] -> %s\n" % (i,str(graph[i])))
    log.close()

def logging_kruskal(graph,weight):
    log = open("/tmp/logging.txt","w")
    log.write("[LENGTH]-> (%d)\n" % len(graph))
    log.write(">> From <- Weight -> To \n")

    for i in range(0,len(graph)):
        for j in graph[i]:
            log.write("(%d <-%d-> %d) " % (i,weight[i][j],j))
        log.write("\n")
    log.close()

#                                    END LOG
