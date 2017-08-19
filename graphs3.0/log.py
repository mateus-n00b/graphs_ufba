
#                                      BEGIN LOG
# File to write logs
traceFile = open("/tmp/log_tracer.tr","w")
log = open("/tmp/algorithm_log.txt","w")

def LOGGER(msg):
    traceFile.write("[LOG] {0}\n".format(msg))

def closeFile():
    traceFile.close()
    log.close()


def logging(graph,Qmax):
    log.write("[LENGTH]-> (%d)\n" % len(graph))
    log.write("[Maximal Clique]-> %s  \n" % (str(Qmax)))
    for i in range(0,len(graph)):
        log.write("[%d] -> %s\n" % (i,str(graph[i])))

def logging_kruskal(graph,weight):
    log.write("[LENGTH]-> (%d)\n" % len(graph))
    log.write(">> From <- Weight -> To \n")

    for i in range(0,len(graph)):
        for j in graph[i]:
            log.write("(%d <-%d-> %d) " % (i,weight[i][j],j))
        log.write("\n")

#                                    END LOG
