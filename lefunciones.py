import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://josel12:password@cluster0-rytv6.mongodb.net/slangs?retryWrites=true&w=majority")
db = cluster["Slangs"]
collection = db["slangs"]

post1= {"Word":"Que Xopa","Meaning":"Un Saludo"}
collection.insert_one(post1)

# def agregar(word1,palabraS):
#     """Adds a new word to our data base"""
#     word1 = word1.strip()
#     palabraS = palabraS.strip()
#     new_word = slangs(word = word1 , meaning = palabraS)
#     c.session.add(new_word)
#     c.session.commit()
#     print("Cool! La palabra ",word1,"ha sido añadida")
# def menu():
#     """Menú principal del programa """
#     opc = int(input("Bienvenido Fren! ¿Que vamos a hacer hoy?\n1) Agregar nueva palabra \n2) Editar palabra existente \n3) Eliminar alguna palabra existente \n4) Ver listado de palabras \n5) Buscar significado de palabra \n6) Salir\n"))
#     return opc
# def editaMoh(wordto,newmean):
#     """Edits an already existing word from our database"""
#     wordto.strip()
#     newmean.strip()
#     search_word = slangs.query.filter_by(word = wordto).first
#     search_word.definition = newmean
#     c.session.commit()

# def eliminaMoh (word_todel):
#     """Deletes certain word from our database"""
#     del_wor= slangs.query.filter_by(word = word_todel).first
#     c.session.delete(del_wor)
#     c.session.commit()

# def urbanDic():
#     """Shows all elements from my database slangs"""
#     words = slangs.query.all()
#     return words
# def whatIsLove(babyDont):
#     """Shows a Description of a certain word"""
#     babyDont.strip()
#     print("la palabra es:", babyDont)
    