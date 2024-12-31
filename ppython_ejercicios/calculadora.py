#calculadora

def suma(x,y):
    return x+y

def resta(x,y):
    return x-y

def multiplicar(x,y):
    return x*y

def dividir(x,y):
    return x/y


#menu
print("operacion a realizar ....")
print("1. suma....")
print("2. resta....")
print("3. multiplicacion ....")
print("4. division  ....")

choice =int(input("ingrese la operacion que desea realizar: (1/2/3/4..)"))
x=int(input("Ingrese el numero 1 : "))
y=int(input("Ingrese el numero 2: "))


if choice==1:
   print('num1', "+", 'num2', "=" , suma(x,y))
    
elif choice==2:
    print('num1', "+", 'num2',"=" , resta(x,y))
    
elif choice==3:
      print('num1', "+", 'num2',"=" , multiplicar(x,y))
elif choice==4:
     print('num1', "+", 'num2',"=" , dividir(x,y))
else:
    print("invalid input")
    
