nome = input (" digite seu nome  ")
n1= int ( input (" digite sua nota 1"))
n2= int ( input ( "digite sua nota 2"))
n3 = int ( input( " digite sua nota 3"))
try 
    media = ( n1 + n2 +n3) /3 
    with open (" pessoa.txt ","a") as arquivo :
        arquivo.write(nome + " | " + f " { nota 1 } " + " | " + F "{ nota 2} "+" | "+
        f " { n3 }" + " |  " +  f " media : .2f } \n ")
     except  :
        print (" digite  as notas corretamente !")
