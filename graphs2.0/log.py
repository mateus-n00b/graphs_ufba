
#                                      BEGIN LOG
def logging(TMP,Qmax):
    log = open("/tmp/logging.txt","w")
    log.write("[LENGTH]-> (%d)\n" % len(TMP))
    log.write("[Maximal Clique]-> %s  \n" % (str(Qmax)))
    for i in range(0,len(TMP)):
        log.write("[%d] -> %s\n" % (i,str(TMP[i])))
    log.close()
#                                    END LOG
