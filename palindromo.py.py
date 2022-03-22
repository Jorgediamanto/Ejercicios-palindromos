#Pregunta adicional: ¿por qué se muestra RADAR después de la instanciación Palindromo("sonar")?
#Por que estas creando una instancia con el mismo nombre que la anterior por lo que se elimina la anterior para utilizar la nueva

class Palindromo:
  
  def __init__(self, palabra):
    self.palabra = palabra




  def __del__(self):
    
    x6784 = self.palabra.upper()    
    print(x6784)

    
  def test(self):
    
    
    x2=self.palabra[::-1]
    skrr=True
    
    for z in range(len(self.palabra)):
      if(self.palabra[z].lower()!=x2[z].lower()):
        
        skrr=False

    
   

    return skrr
    

  
  def esPalindromo(self):
    x=self
    
    x2=x[::-1]
    skrr=True
    
    for z in range(len(x)):
      if(x[z].lower()!=x2[z].lower()):
        
        skrr=False

    
   

    return skrr


p = Palindromo("L O L")
print(p.test())
p = Palindromo("radar") 
print(p.test())
p = Palindromo("sonar")
print(p.test())

p = Palindromo("para que imprima la ultima vez como pide en el ejercicio porq si no no lo imprime") 

#print(Palindromo.esPalindromo('radar')) 
#print(Palindromo.esPalindromo('sonar')) 
#print(Palindromo.esPalindromo('Arde ya la yedra')) 
#print(Palindromo.esPalindromo('Ardeyalayedra')) 
#print(Palindromo.esPalindromo('!@#$% %$#@!')) 
#print(Palindromo.esPalindromo('L O L')) 

