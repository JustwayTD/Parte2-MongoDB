import pymongo
from pymongo import MongoClient
from lefunciones import menu , agregar ,editaMoh , eliminaMoh , urbanDic , whatIsLove

if __name__ =="__main__":
    choo = menu()
    if choo == 1:
        palabra1 = input("Cual sera la palabra a agregar?\n")
        palabra2 = input("Y que significa eso?\n")
        agregar(palabra1,palabra2)
    elif choo == 2:
        palabra1 = input ("Cual palabra quieres editar?\n")
        palabra2 = input("Cual sera el nuevo significado?\n")
        editaMoh(palabra1,palabra2)
    elif choo == 3:
        palabra1 = input("Que palabra quieres eliminar?\n")
        eliminaMoh(palabra1)
    elif choo == 4:
        palabras = urbanDic()
        for x in palabras:
            print(x["Word","Meaning"])
    elif choo == 5:
        palabra1 = input("De que palabra quieres el significado (case sensitive)")
        palabras = whatIsLove(palabra1)


