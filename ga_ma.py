# -*- coding: utf-8 f-*-
"""
Created on Sat Jan 27 17:11:32 2018

@author: Andrei
"""
import random as rnd
import numpy as np

from datetime import datetime
class GA_Mastermind:
    rnd.seed(datetime.now())
    
    def __init__(self, alphabet, pMut=1., c=1,pCross=0.1,  P=4, g=['1','1','2','2'],code=['1','2','3','4'],a=1,b=1,pSwapMut=0.03,pInvMut=0.02):
         self.popSize,self.maxGen = 150, 100
         self.maxEiSize=500
         self.EiSize=[]
         self.fitProbs=[]
         self.guess=[g]
         self.xdiff=[]
         self.ydiff=[]
         self.fVals=[]
         #self.code=code
         

         self.a=a
         self.b=b
         self.Eis=[]
         self.itN=0
         self.pSwapMut=pSwapMut
         self.pInvMut=pInvMut
         self.ind=[]
         self.new_pop=[]
         self.old_pop=[]
         self.fitAll=[]
         self.alphabet = alphabet 
         self.pMut= pMut
         self.length=P
         self.pCross = pCross 
         self.kP =int(c)  
         
         self.fitnessFun = getattr(self, 'sel_fps_mastermind')
         
         self.code=[self.alphabet[rnd.randint(0, len(self.alphabet)-1)] for x in range(self.length)] 
         
         self.scores=[[self.scoreX(g,self.code),self.scoreY(g,self.code)]]
         self.pop =[]
         self.reinit()
        
         
                    
    def reinit(self):
        #print('hell1o',self.code)

        while len(self.pop)<self.popSize:
            self.pop=[[self.alphabet[rnd.randint(0, len(self.alphabet)-1)] 
                                 for x in range(self.length)]  
                                    for y in range(self.popSize)
                                        ]
            self.pop=list(set([(',').join(self.pop[i]) for i in range(0,self.popSize)]))

        self.pop= [(self.pop[i]).split(',') for i in range(0,self.popSize)]
        #return 
        
    def scoreX(self,seq1,seq2):
        return sum([int(seq1[i]==seq2[i]) for i in range(len(seq1))])

    def scoreY(self,seq1,seq2):
        arr1=np.argwhere(np.asarray([int(seq1[i]!=seq2[i]) for i in range(len(seq1))])==1)
        ind=[arr1[i][0]
                    for i in range(len(arr1))]
        
        if len(ind)>0:        
            #seq1minX=(np.asarray(seq1)[np.asarray(ind)]).tolist()
        
            seq1minX=list(set((np.asarray(seq1)[np.asarray(ind)]).tolist()))
            seq2minX=(np.asarray(seq2)[np.asarray(ind)]).tolist()
            #seq2minX=list(set((np.asarray(seq2)[np.asarray(ind)]).tolist()))


   #print("In scoreY:",seq1,seq2,sum([int(seq1minX[i] in seq2minX) for i in range(len(seq1minX))]))

            return sum([int(seq1minX[i] in seq2minX) for i in range(len(seq1minX))])
        
        else:
            return 0
            
    
    def fitness(self,pop,itN):
        fVals=[]
        for i in range(0,self.popSize):
            #print(i)
            #self.xdiff.append(sum([abs(self.scoreX(pop[i],self.guess[j])-self.scores[j][0]) for j in range(len(self.guess))]))
            #self.ydiff.append(sum([abs(self.scoreY(pop[i],self.guess[j])-self.scores[j][1]) for j in range(len(self.guess))]))
            xdiff=sum([abs(self.scoreX(pop[i],self.guess[j])-self.scores[j][0]) for j in range(len(self.guess))])
            ydiff=sum([abs(self.scoreY(pop[i],self.guess[j])-self.scores[j][1]) for j in range(len(self.guess))])
            fitF=self.a*xdiff+ydiff+self.b*self.length*(itN-1.)
            fVals.append(fitF)                
        (self.fVals)=fVals
        
        totalFitness = sum(fVals)
        self.fitProbs = [float(x) /float(totalFitness) for x in fVals]
        
        
    def sel_fps_mastermind(self, pop,itN):
        popNew=[]
        potTemp=pop[:]
        self.fitness(pop,itN)

        allElem=zip(pop,self.fitProbs)
        sorted(allElem,key=lambda x: int(x[1]))


        pp=[allElem[i][0] for  i in range(0,self.popSize)]
        self.fitProbs=[allElem[i][1] for  i in range(0,self.popSize)]


        mu=self.popSize
        s=1.5
        probs=[(2.-s)/mu+2.*x*(s-1.)/(mu*(mu-1.)) for x in range(0,self.popSize)]
        self.ind = np.random.choice([x for x in range(0,self.popSize)],self.popSize, replace=True, p=probs)
        potTemp=pp[:]


        #self.fitnessVals = [len(filter(lambda x: x=='1', pop[x])) for x in range(0,self.popSize)]
        #self.totalFitness = sum(self.fitnessVals)
        #self.fitProbs = [float(x) /float(self.totalFitness) for x in self.fitnessVals]
        #self.ind = np.random.choice([x for x in range(0,self.popSize)],self.popSize, replace=True, p=self.fitProbs)
        for i in self.ind:

            if  potTemp[i]  in popNew:
                while potTemp[i] in popNew:
                    #potTemp[i]=self.rnd_mutate(potTemp[i])
                    potTemp[i]=self.random_code()

                    #print(potTemp[i] in popNew)
#                print (potTemp[i] in popNew, popNew,potTemp[i])
            popNew.append(potTemp[i])
        self.fitness(popNew,itN)

        #print(popNew)
        #print("Len true:",len(set([(',').join(i) for i in popNew])))


        #wait = input("PRESS ENTER TO CONTINUE.")

 #               if po
    #    popNew = [pop[i] for i in self.ind]

        return popNew        
        
        
        
    def sel_fps_mastermind1(self, pop,itN):
        popNew=[]
        potTemp=pop[:]
        self.fitness(pop,itN)
        self.ind = np.random.choice([x for x in range(0,self.popSize)],self.popSize, replace=True, p=self.fitProbs)
        
        
        #self.fitnessVals = [len(filter(lambda x: x=='1', pop[x])) for x in range(0,self.popSize)]
        #self.totalFitness = sum(self.fitnessVals)
        #self.fitProbs = [float(x) /float(self.totalFitness) for x in self.fitnessVals]
        #self.ind = np.random.choice([x for x in range(0,self.popSize)],self.popSize, replace=True, p=self.fitProbs)
        for i in self.ind:
            
            if  potTemp[i]  in popNew:
                while potTemp[i] in popNew:
                    #potTemp[i]=self.rnd_mutate(potTemp[i])
                    potTemp[i]=self.random_code()
                    
                    #print(potTemp[i] in popNew)    
#                print (potTemp[i] in popNew, popNew,potTemp[i])           
            popNew.append(potTemp[i]) 
        self.fitness(popNew,itN)
   
        #print(popNew)     
        #print("Len true:",len(set([(',').join(i) for i in popNew])))

        
        #wait = input("PRESS ENTER TO CONTINUE.")
       
 #               if po
    #    popNew = [pop[i] for i in self.ind]
        
        return popNew



    def GetEligible(self,pop):
        Eis=[]
        for i in range(0,self.popSize):
            #print(i)
            xdiff=sum([abs(self.scoreX(pop[i],self.guess[j])-self.scores[j][0]) for j in range(len(self.guess))])
            ydiff=sum([abs(self.scoreY(pop[i],self.guess[j])-self.scores[j][1]) for j in range(len(self.guess))])
            if ((xdiff==0) and (ydiff==0)): 
               # print(xdiff,ydiff)
                Eis.append(pop[i])
        return Eis    
                                   
    def rnd_mutate(self, chromosome):
            newChromosome=chromosome[:]
            if rnd.random() < self.pMut:
                locus=rnd.randint(0,self.length-1)
                color=rnd.randint(0,len(self.alphabet)-1)
                newChromosome[locus]=self.alphabet[color]
                #print('locus:',locus)
       
            return newChromosome

    def random_mutate(self, chromosome):
        newChromosome=[]
        for x in chromosome:
            if rnd.random() < self.pMut and x not in '.':
                if len(self.alphabet) > 2:
                        diffSet =   list(set(self.alphabet).difference(x))[0]  
                        x = diffSet[rnd.randint(0, len(diffSet)-1)]
                else:
                        x=list(set(self.alphabet).difference(x))[0]
            newChromosome.append(x)           
        return newChromosome

    def getUnique(self,lst):
              elUn=list(set([(',').join(i) for i in lst]))
              elUn1=[elUn[i].split(',') for i in range(0,len(elUn))]
              return elUn1

    def random_code(self):
            newChromosome=[self.alphabet[rnd.randint(0, len(self.alphabet)-1)]  for x in range(self.length)]  
            return newChromosome


    

    def inv_mutate(self, chromosome):
        crossA=[]
        newChromosome=chromosome[:]
        if rnd.random() < self.pInvMut:
                while (len(crossA)<2):
                    crossA = list({rnd.randint(0,len(self.alphabet)-1) for x in range(2)})
                rnd.shuffle(crossA)
                #crossA.sort()
                #print(crossA)
                t=crossA[1]     
                if crossA[1]< self.length: t=crossA[1]+1 
                if crossA[0]>crossA[1]:
                      temp=chromosome[crossA[1]+1:crossA[0]]+(chromosome[crossA[0]:]+chromosome[:t])[::-1]
                      newChromosome=list(np.roll(temp,(crossA[1]+1)))
                else:
                      newChromosome[crossA[0]:t]=chromosome[crossA[0]:t][::-1]
                    

        
        return newChromosome



#    def inv_mutate(self, chromosome):
#        crossA=[]
#        newChromosome=chromosome[:]
#        if rnd.random() < self.pInvMut:
#                while (len(crossA)<2):
#                    crossA = list({rnd.randint(0,len(self.alphabet)-1) for x in range(2)})
#                rnd.shuffle(crossA)
#                t=crossA[1]     
#                if crossA[1]< self.length: t=crossA[1]+1 
#                if crossA[0]>crossA[1]:

#                      temp=chromosome[crossA[1]+1:crossA[0]]+(chromosome[crossA[0]:]+chromosome[:t])[::-1]
#                      newChromosome=list(np.roll(temp,(crossA[1]+1)))
#                else:
#                      newChromosome[crossA[0]:t]=chromosome[crossA[0]:t][::-1]
                    

        
 #       return newChromosome
    
    
    
    def swap_mutate(self, chromosome):
        crossA=[]
        newChromosome=chromosome[:]
        if rnd.random() < self.pSwapMut:
                while (len(crossA)<2):
                    crossA = list({rnd.randint(0,self.length-1) for x in range(2)})
        #print(crossA)
        if len(crossA)>0:
           newChromosome[crossA[0]],newChromosome[crossA[1]]=chromosome[crossA[1]],chromosome[crossA[0]]
                            
                            
        
        return newChromosome
    
    
    
    
    
    
    def crossover(self, p1, p2):
      off1=[]
      off2=[]
      crossA = []     
      if rnd.random()< self.pCross:

         kPs = list({rnd.randint(0,self.length) for x in range(self.kP)})
         crossA = kPs[:] 
         #print(kPs)         
         crossA.sort()
         if(crossA and crossA[0] ==0): 
             p1,p2 = p2,p1
         else:
              crossA.insert(0,0)
         if crossA[-1] != self.length:   crossA.insert(len(kPs), self.length)
            
      crossA.sort()
      #print (crossA)
      for i in range(len(crossA)-1):
            indx1=crossA[i]
            indx2=crossA[i+1]
            #if indx2 < self.length-1: indx2=indx2+1
            if i % 2 ==0:
                    off1.extend(p1[indx1:indx2])
                    off2.extend(p2[indx1:indx2])
            else:
                    off1.extend(p2[indx1:indx2])
                    off2.extend(p1[indx1:indx2])
      if not off1: 
          off1=p1[:]
          off2=p2[:]
      return off1, off2   
   



    def runMain(self):
       self.old_pop=self.pop[:]
       self.new_pop=self.pop[:]
 
       
       while self.scores[-1][0]!=self.length:
            self.itN = self.itN+1 
            #print(self.itN)
            #self.new_pop=self.fitnessFun(self.old_pop,self.itN+1)

            gen=1
            Eis=[]
            while gen < self.maxGen and len(Eis) < self.maxEiSize:
                    
                    self.fitness(self.new_pop,self.itN)  
            
                    #crosMates =  [(i,i+1) for i in range(0,self.popSize,2)]
                    for i in range(self.popSize/2):
                            crossMates=np.random.choice([x for x in range(0,self.popSize)],2, replace=True, p=self.fitProbs)
                            m = crossMates[0]
                            p = crossMates[1]
                            #print(m,p)
                            self.new_pop[m], self.new_pop[p] = self.crossover(self.new_pop[m],self.new_pop[p])                
            
                    #crosMates =  [(i,i+1) for i in range(0,self.popSize,2)]
                    #for i in range(len(crosMates)):
                    #        m = crosMates[i][0]
                    #        p = crosMates[i][1]
                            #print(m,p)
                     #       self.new_pop[m], self.new_pop[p] = self.crossover(self.new_pop[m],self.new_pop[p])                
                
                    for i in range(0,self.popSize):
                           self.new_pop[i]=self.rnd_mutate(self.new_pop[i])
                           #rnd.shuffle(self.new_pop)
            #        rnd.seed(datetime.now())
             #       for i in range(0,self.popSize):
                           self.new_pop[i]=self.inv_mutate(self.new_pop[i])

              #      rnd.seed(datetime.now())
               #     for i in range(0,self.popSize):
                           self.new_pop[i]=self.swap_mutate(self.new_pop[i])    
                    
                    popNewUn=self.getUnique(self.new_pop)
                    popNew=popNewUn
                    while len(popNew)!=self.popSize:
                            potTemp=popNew[0]    
                            if  potTemp  in popNew:
                                     while potTemp in popNew:
                    #potTemp[i]=self.rnd_mutate(potTemp[i])
                                         potTemp=self.random_code()
                    
                    #print(potTemp[i] in popNew)    
#                print (potTemp[i] in popNew, popNew,potTemp[i])           
                            popNew.append(potTemp) 
                    
                    #potTemp[i]=self.rnd_mutate(potTemp[i])
             #                   potTemp[i]=self.random_code()
                    
                    #print(potTemp[i] in popNew)    
#                print (potTemp[i] in popNew, popNew,potTemp[i])           
            #popNew.append(potTemp[i]) 
                        
                    #print('Length',len(popNew))
                                
                    self.new_pop=popNew      
                    self.fitness(self.new_pop,self.itN)
                    elSet= self.getUnique(self.GetEligible(self.new_pop))
                    #elUn=list(set([(',').join(i) for i in elSet]))
                    #elUn1=[elUn[i].split(',') for i in range(0,len(elUn))]


                
                    for i in elSet:
                             if i not in Eis:  Eis.append(i)       
                               #print([(i,j,self.scoreX(i,j),self.scoreY(i,j)) for  j in self.guess])

                    #popUn=list(set([(',').join(Eis[i]) for i in range(len(Eis))]))
                    #Eis.append([popUn[i].split(',') for i in range(len(Eis))])
            
                    #Eis.extend(self.GetEligible(self.new_pop))
                    #print(Eis)
                    #Eisl=set(tuple(Eis))
        
 #                   wait = input("PRESS ENTER TO CONTINUE.")

                    #print("Len true:",len(set([(',').join(i) for i in self.new_pop])))
                    self.old_pop=self.new_pop[:]
                    self.new_pop=self.fitnessFun(self.old_pop,self.itN)
                    self.fitness(self.new_pop,self.itN)
                        
                    gen=gen+1
    
            #print(len(Eis), Eis)
            
            #print(self.EiSize)        
            #popUn=list(set([(',').join(Eis[i]) for i in range(len(Eis))]))
            #popUn1=[popUn[i].split(',') for i in range(0,len(popUn))]
            #print(popUn1)         
            #self.EiSize.append(len(popUn1))
            self.EiSize.append(len(Eis))
            
            
#            if len(popUn1)>0: 
                #self.Eis.extend(popUn1)
                #self.Eis=popUn1[:]                    
            self.Eis=Eis[:]                    
                
#            self.guess.append(self.Eis[-1][rnd.randint(0,len(popUn1)-1)])   

            #print(self.Eis)
            #lastG=self.Eis[-1][0            

            #set1=list(set([(',').join(self.guess[i]) for i in range(0,len(self.guess))]))
        
            #lst1=[set1[i].split(',') for i in range(0,len(set1))]
            self.guess=self.getUnique(self.guess)

            #self.guess.append(lastG[rnd.randint(0,len(lastG)-1)])   
            #self.guess.append(self.Eis[rnd.randint(0,len(self.Eis)-1)])   
            if len(Eis) >0 :
                while True:
                    i=self.Eis[rnd.randint(0,len(self.Eis)-1)]
                    #print('looping',i)
                    if i not in self.guess:   
                        self.guess.append(i)       
                        #print('inside')
                        break
                    
            #guess=[]
            #while guess=self.Eis[rnd.randint(0,len(self.Eis)-1)]  in 
#                self.guess.append(self.Eis[rnd.randint(0,len(self.Eis)-1)])   
            
             
            self.scores=[[self.scoreX(j,self.code),self.scoreY(j,self.code)] for j in self.guess]




     
            #print(self.guess[-1])
            #self.scores.append([self.scoreX(self.guess[-1],self.code),self.scoreY(self.guess[-1],self.code)])
            
            #self.old_pop=self.pop[:]
            #self.new_pop=self.fitnessFun(self.old_pop)

        
        #self.bestChromosome.append(max(self.fitnessVals))
            
