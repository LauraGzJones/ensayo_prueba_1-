#🟡 Ejercicio 2 (medio)

#Una persona gana $600.000 y tiene:

#10% descuento AFP #sto se calula como 0.10 * sueldo bruto
#7% salud esto se calula como 0.07 * sueldo bruto

# 👉 ¿Cuál es el sueldo líquido?

sueldo_bruto = 600000
descuento_afp = sueldo_bruto * 0.10
descuento_salud = sueldo_bruto * 0.07
sueldo_liquido = sueldo_bruto - descuento_afp - descuento_salud

print("El sueldo liquido es de $", sueldo_liquido)