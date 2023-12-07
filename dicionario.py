cliente = {
    "nome" : "Miguel",
    "idade " : "17anos",
    "email" : "celsomiguel710@gmail.com"
}

#print(type(cliente))
#print(cliente)
print (cliente["nome"])
cliente["nome"] = "joao" # troquei o nome 
print(cliente["nome"])
cliente.update({"cpf" : "123123123"})
print(cliente)

alunos =  {
      "aluno1": {

     "nome" : "mateus",
     "email" : "mateus@gmail.com",
      "fone" : ["129833213232","12987676767"],
      "cursos" : ["tecnico em internet", "Python"],
    },
"aluno2":  {
   "nome" : "mateus",
   "email" : "mateus@gmail.com",
   "fone" : ["129833213232","12987676767"],   "cursos" : ["tecnico em internet", "Python"],
}

print(type[alunos])
