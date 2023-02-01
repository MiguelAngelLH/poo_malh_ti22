import math

R=float(input("Escribe el radio del circulo :"))
circunferencia=2*math.PI*R #formula para la circunferencia de un circulo
area=math.PI*R*R
superficiedearea=4*math.PI*R*R
print ( "Circunferencia:% .2f" % circunferencia)
print ( "Area del circulo:% .2f"% area) # imprimer el resultado del area del circulo
print ( "Area de superficie del circulo:% .2f"%superficiedearea)