from turtle import clear


def funcA():
    print("Начали выполнять А")
    funcB()
    print("Закончили А")

def funcB():
    print("Начали выполнять B")
    funcC()
    print("Закончили B")

def funcC():
    print("Начали выполнять C")
    print("Закончили C")

funcA()

def endless():
    print("endless")
    endless()

endless()

clear
