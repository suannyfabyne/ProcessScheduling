import numpy as np
import time

def menorValor(array):
    countfor = 0
    index = 0
    counter = 999
    for i in array:
        if (i < counter and i != -1):
            counter = i
            index = countfor
        countfor+=1
    return index, counter
           
def FCFS(arrive, peaktime, nprocesses):
    copypeaktime = np.copy(peaktime)    
    copyarrive = np.copy(arrive) 
    orderpeaktime, orderarrive = order(copypeaktime, copyarrive, nprocesses)
    counter = 1
    lista = []
    timer = tamanho = index = peaktimevalue = counterwhile = duracao = 0
    soma = orderpeaktime.sum()
    orderarrive = orderarrive-orderarrive[0]
    arrives = np.copy(orderarrive)
    if (orderpeaktime.max() < orderarrive.max()): soma = orderarrive.max()+1

    while(timer < soma):
        for i in orderarrive:
            if (i <= timer): 
                tamanho = counter             
            counter+=1    
        lista = np.copy(orderarrive[:tamanho])
        index, peaktimevalue = menorValor(lista)

        if (peaktimevalue == 999):
            timer = timer + 1
            duracao = duracao + 1
        else: 
            orderarrive[index] = -1
            CPU[counterwhile,3] = duracao
            duracao = duracao + orderpeaktime[index]
            CPU[counterwhile,2] = duracao
            CPU[counterwhile,1] = orderpeaktime[index]
            CPU[counterwhile,0] = index+1  
            counterwhile+=1   
            timer = timer + orderpeaktime[index]     

        counter = 1    

    counter = 0
    RET = ReturnTimeT(CPU,nprocesses,arrives)
    RESP = ResponseTimeT(CPU,nprocesses,arrives)
    print("FCFS")
    print(CPU)
    return RET, RESP

def order(copypeaktime, copyarrive, nprocesses):
    counter = 0
    orderpeaktime = np.zeros(nprocesses)
    orderarrive = np.zeros(nprocesses)
    while (nprocesses > 0):
        index, peaktimevalue = menorValor(copyarrive) 
        orderpeaktime[counter] = copypeaktime[index]
        orderarrive[counter] = copyarrive[index]
        copyarrive[index] = -1
        nprocesses-=1
        counter+=1
    return orderpeaktime, orderarrive

def SJF(arrive, peaktime, nprocesses): 
    copypeaktime = np.copy(peaktime)    
    copyarrive = np.copy(arrive) 
    orderpeaktime, orderarrive = order(copypeaktime, copyarrive, nprocesses)
    counter = 1
    lista = []
    timer = tamanho = index = peaktimevalue = counterwhile = duracao = 0
    soma = orderpeaktime.sum()
    orderarrive = orderarrive-orderarrive[0]
    if (orderpeaktime.max() < orderarrive.max()): soma = orderarrive.max()+1

    while(timer < soma):
        for i in orderarrive:
            if (i <= timer): 
                tamanho = counter             
            counter+=1    
        lista = np.copy(orderpeaktime[:tamanho])
        index, peaktimevalue = menorValor(lista)

        if (peaktimevalue == 999):
            timer = timer + 1
            duracao = duracao + 1
        else: 
            timer = peaktimevalue + timer
            CPUsjf[counterwhile,3] = duracao
            duracao = duracao + peaktimevalue
            CPUsjf[counterwhile,0] = index+1 
            CPUsjf[counterwhile,1] = peaktimevalue
            CPUsjf[counterwhile,2] = duracao
            orderpeaktime[index]= -1
            counterwhile+=1
        counter = 1

    RET = ReturnTimeT(CPUsjf,nprocesses,orderarrive)
    REST = ResponseTimeT(CPUsjf,nprocesses,orderarrive)
    print("SJF")
    print(CPUsjf)
    return RET, REST

def RR(arrive, peaktime, nprocesses): 
    copypeaktime = np.copy(peaktime)    
    copyarrive = np.copy(arrive) 
    orderpeaktime, orderarrive = order(copypeaktime, copyarrive, nprocesses)
    counter = 1
    quantum = 2
    lista = []
    timer = tamanho = index = peaktimevalue = counterwhile = duracao = 0
    soma = orderpeaktime.sum()
    orderarrive = orderarrive-orderarrive[0]

    if (orderpeaktime.max() < orderarrive.max()): soma = orderarrive.max()+1
    while(timer < soma):
        for i in orderarrive:
            if (i <= timer): 
                tamanho = counter           
            counter+=1    
        lista = np.copy(orderarrive[:tamanho])
        index, peaktimevalue = menorValor(lista)
        if (peaktimevalue == 999):
            timer = timer + 1
        else:
            if (orderpeaktime[index] < quantum):
                CPUrr[counterwhile,1] = orderpeaktime[index]
                duracao = duracao + orderpeaktime[index]
                timer = orderpeaktime[index] + timer
                orderpeaktime[index] = 0
                orderarrive[index]= -1
            else:  
                duracao = duracao + quantum
                orderpeaktime[index] = orderpeaktime[index] - quantum
                CPUrr[counterwhile,1] = quantum
                timer = quantum + timer
                if(orderpeaktime[index] == 0): orderarrive[index]= -1
                else: orderarrive[index] = duracao

            CPUrr[counterwhile,0] = index+1 
            CPUrr[counterwhile,2] = duracao
            counterwhile+=1
        counter = 1
    print("RR")
    print(CPUrr[:counterwhile])

def ReturnTimeT(CPU,nprocesses,arrive):
    RET = 0
    arrives = 0
    print(arrive)
    for x,y,z,w in CPU:
        RET+=z
    for i in arrive:
        arrives = arrives + i
    return ((RET-arrives)/4)

def ResponseTimeT(CPU,nprocesses,arrive):
    RESP = 0
    arrives = 0
    for x,y,z,w in CPU[:nprocesses]:
        RESP+=w
    for i in arrive:
        arrives = arrives + i
    return ((RESP-arrives)/4)


nprocesses = counter = 0
txtfile = open('entry.txt', 'r')
txt = txtfile.readlines()

for line in txt :
    nprocesses=nprocesses+1

arrive = np.zeros(nprocesses)
peaktime = np.zeros(nprocesses)
CPU =  np.zeros([nprocesses,4])
CPUsjf =  np.zeros([nprocesses,4])
CPUrr = np.zeros([1000,3])
for line in txt :
    value = line.split()
    arrive[counter] = value[0]
    peaktime[counter] = value[1]
    counter+=1
txtfile.close()

RET_FCFS, RESP_FCFS = FCFS(arrive, peaktime, nprocesses)
RET_SJF, RESP_SJF = SJF(arrive, peaktime, nprocesses)
RR(arrive, peaktime, nprocesses)

print("FSFS " + str(RET_FCFS) + " " + str(RESP_FCFS) + " " + str(RESP_FCFS))
print("SJF " + str(RET_SJF) + " " + str(RESP_SJF) + " " + str(RESP_SJF)) 