
def triangulo():
    a=int(input("ingrese el primer angulo: "))
    b=int(input("ingrese el segundo angulo: "))
    c=int(input("ingrese el tercer angulo: "))
    suma=a+b+c
    if suma==180:
        print("Es triangulo ya que la suma de sus angulos internos da igaul a 180°")
    else:
         print("No es un triangulo ya que su suma")
triangulo()