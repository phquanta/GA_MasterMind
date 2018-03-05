# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 17:37:32 2018

@author: Andrei
"""

import ga_ma
from imp import reload
import matplotlib.pyplot as plt
import numpy as np

reload(ga_ma)


guessN=[[],[],[],[],[],[],[],[],[],[],[],[],[]]

EiSizes=[]
for i in range(0,500):
    G0 =  ga_ma.GA_Mastermind(['0','1','2','3','4','5'],0.03, 2,0.5, P=4,a=1,b=1,pSwapMut=0.03,pInvMut=0.02)
    G1 =  ga_ma.GA_Mastermind(['0','1','2','3','4','5'],0.3, 2,0.5, P=4,a=1,b=1,pSwapMut=0.3,pInvMut=0.2)
    G2 =  ga_ma.GA_Mastermind(['0','1','2','3','4','5'],0.003, 2,0.5, P=4,a=1,b=1,pSwapMut=0.003,pInvMut=0.002)
    G3 =  ga_ma.GA_Mastermind(['0','1','2','3','4','5'],0.03, 2,0.05, P=4,a=2,b=1,pSwapMut=0.03,pInvMut=0.02)
    G00 =  ga_ma.GA_Mastermind(['0','1','2','3','4','5'],0.03, 2,0.5, P=4,a=2,b=2,pSwapMut=0.03,pInvMut=0.02)
    G10 =  ga_ma.GA_Mastermind(['0','1','2','3','4','5'],0.3, 2,0.5, P=4,a=2,b=2,pSwapMut=0.3,pInvMut=0.2)
    G20 =  ga_ma.GA_Mastermind(['0','1','2','3','4','5'],0.003, 2,0.5, P=4,a=3,b=3,pSwapMut=0.003,pInvMut=0.002)
    G30 =  ga_ma.GA_Mastermind(['0','1','2','3','4','5'],0.03, 2,0.05, P=4,a=3,b=3,pSwapMut=0.03,pInvMut=0.02)
    G01 =  ga_ma.GA_Mastermind(['0','1','2','3','4','5'],0.03, 2,0.5, P=4,a=4,b=4,pSwapMut=0.03,pInvMut=0.02)
    G11 =  ga_ma.GA_Mastermind(['0','1','2','3','4','5'],0.3, 2,0.5, P=4,a=4,b=4,pSwapMut=0.3,pInvMut=0.2)
    G21 =  ga_ma.GA_Mastermind(['0','1','2','3','4','5'],0.003, 2,0.5, P=4,a=4,b=4,pSwapMut=0.003,pInvMut=0.002)
    G31 =  ga_ma.GA_Mastermind(['0','1','2','3','4','5'],0.03, 2,0.05, P=4,a=4,b=4,pSwapMut=0.03,pInvMut=0.02)
    G41 =  ga_ma.GA_Mastermind(['0','1','2','3','4','5'],0.03, 2,0.5, P=4,a=1,b=0,pSwapMut=0.03,pInvMut=0.02)





    G0.runMain()
    G1.runMain()
    G2.runMain()
    G3.runMain()
    G00.runMain()
    G10.runMain()
    G20.runMain()
    G30.runMain()
    G01.runMain()
    G11.runMain()
    G21.runMain()
    G31.runMain()
    G41.runMain()

    guessN[0].append(len(G0.guess))
    guessN[1].append(len(G1.guess))
    guessN[2].append(len(G2.guess))
    guessN[3].append(len(G3.guess))
    guessN[4].append(len(G00.guess))
    guessN[5].append(len(G10.guess))
    guessN[6].append(len(G20.guess))
    guessN[7].append(len(G30.guess))
    guessN[8].append(len(G01.guess))
    guessN[9].append(len(G11.guess))
    guessN[10].append(len(G21.guess))
    guessN[11].append(len(G31.guess))
    guessN[12].append(len(G31.guess))
    
    print i
    
    #EiSizes.append(G0.EiSize)
#    EiSizes.append()
    
print(np.std(guessN))    