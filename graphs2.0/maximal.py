import log


class MC(object):
    def __init__(self,Qmax):
        self.Q = []
        self.Qmax = Qmax
    #                                   BEGIN MC
    def expand(self,R,G):
        Rp = []
        while len(R) != 0:
            p = R[0]
            if (len(self.Q) + len(R)) > len(self.Qmax):
                self.Q.append(p)
                for y in G[p]:
                    if y in R:
                        Rp.append(y)
                if len(Rp) != 0:
                    self.expand(Rp,G)
                else:
                    if len(self.Q) > len(self.Qmax):
                        self.Qmax = self.Q

                self.Q = []
            R.remove(p)

    def basicMC(self,G,Qmax):
        V = [ i for i in range(0,len(G)) ]
        TMP = list(G)
        self.Qmax = Qmax
        self.expand(V,TMP)
        log.logging(TMP,self.Qmax)
        return self.Qmax
    #                                       END MC
