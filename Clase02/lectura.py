import csv

id=0


getId=int(input("Objeto a imprimir: "))

Filas=[]
Columnas=[]
with open('avocado.csv', newline='') as File:
      
    reader = csv.reader(File)
    for row in reader:
        id=id+1  
        '''if getId==id:
            print(id,row)'''   

        
        Filas.append(row)
    print ("Numeros de objetos en la lista", id)
    

    print (getId,Filas[getId])


    #print(id,row)


    

