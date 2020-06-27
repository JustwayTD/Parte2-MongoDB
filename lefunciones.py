import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://josel12:passsword@cluster0-rytv6.mongodb.net/slangs?retryWrites=true&w=majority")
db = cluster["Slangs"]
collection = db["slangs"]

post1= {"Word":"Que Xopa","Meaning":"Un Saludo"}
collection.insert_one(post1)

def agregar(word1,palabraS):
    """Adds a new word to our data base"""
    word1 = word1.strip()
    palabraS = palabraS.strip()
    post1= {"Word":word1 , "Meaning":palabraS}
    collection.insert_one(post1)
    print("Cool! La palabra ",word1,"ha sido añadida")
def menu():
    """Menú principal del programa """
    opc = int(input("Bienvenido Fren! ¿Que vamos a hacer hoy?\n1) Agregar nueva palabra \n2) Editar palabra existente \n3) Eliminar alguna palabra existente \n4) Ver listado de palabras \n5) Buscar significado de palabra \n6) Salir\n"))
    return opc
def editaMoh(wordto,newmean):
    """Edits an already existing word from our database"""
    wordto.strip()
    newmean.strip()
    collection.update_one({"Word":wordto} , {"$set":newmean})
    

def eliminaMoh (word_todel):
    """Deletes certain word from our database"""
    collection.delete_one({"Word":word_todel})
    print("Perfecto! La palabra: ", word_todel," ha sido eliminada")

def urbanDic():
    """Shows all elements from my database slangs"""
    words = collection.find()
    return words
def whatIsLove(babyDont):
    """Shows a Description of a certain word"""
    babyDont.strip()
    print("la palabra es:", babyDont)
    res = collection.find({"Word":babyDont} , {"_id":0,"Word":0,"Meaning":1})
    for x in res:
        print(x)