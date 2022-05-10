
def CDT(usuario,capital,tiempo):
    
    if tiempo<=2:        
        valoraperder=capital*0.02 
        valortotal=capital-valoraperder
    else:
        valorintereses=capital*0.03*int(tiempo)/12
        valortotal=valorintereses+capital
        
    return f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valortotal}" 


     
print(CDT("AB1012",1000000,3))
print(CDT("QW3456",5000000,2))

        
     

