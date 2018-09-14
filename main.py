import numpy as np

def menorValor(array):
    countfor = 0
    index = 0
    counter = 100
    for i in array:
        if (i < counter and i != -1):
            counter = i
            index = countfor
        countfor+=1
    return index, counter
           
def FCFS(arrive, peaktime, nprocesses):
    index = 0
    counterwhile = 0
    duracao = 0
    copy = np.copy(arrive)
    while(nprocesses > 0):
        index, timearrive = menorValor(copy)
        copy[index] = 100
        duracao = duracao + peaktime[index]
        CPU[counterwhile,2] = duracao
        CPU[counterwhile,1] = peaktime[index]
        CPU[counterwhile,0] = index+1  
        counterwhile+=1
        nprocesses-=1
    counter = 0
    print("FCFS")
    print(CPU)

def order(copypeaktime, copyarrive, nprocesses):
    counter = 0
    orderpeaktime = np.zeros(nprocesses)
    orderarrive = np.zeros(nprocesses)
    while (nprocesses > 0):
        index, peaktimevalue = menorValor(copyarrive) 
        orderpeaktime[counter] = copypeaktime[index]
        orderarrive[counter] = copyarrive[index]
        copyarrive[index] = 100
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

    while(timer < soma):
        for i in orderarrive:
            if (i <= timer): 
                tamanho = counter             
            counter+=1    
        lista = np.copy(orderpeaktime[:tamanho])
        index, peaktimevalue = menorValor(lista)
        duracao = duracao + peaktimevalue
        CPUsjf[counterwhile,0] = index+1 
        CPUsjf[counterwhile,1] = peaktimevalue
        CPUsjf[counterwhile,2] = duracao
        timer = peaktimevalue + timer
        orderpeaktime[index]= -1
        counterwhile+=1
        counter = 1
    print("SJF")
    print(CPUsjf)

nprocesses = 0
counter = 0
txtfile = open('entry.txt', 'r')
txt = txtfile.readlines()

for line in txt :
    nprocesses=nprocesses+1

arrive = np.zeros(nprocesses)
peaktime = np.zeros(nprocesses)
CPU = np.zeros([nprocesses,3])
CPUsjf = np.zeros([nprocesses,3])

for line in txt :
    value = line.split()
    arrive[counter] = value[0]
    peaktime[counter] = value[1]
    counter+=1
txtfile.close()

FCFS(arrive, peaktime, nprocesses)
SJF(arrive, peaktime, nprocesses)
