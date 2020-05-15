def validate_bin(check_number):
    '''
    Si el numero ingresado es binario solo se pueden aceptar 0's o 1's
    retorna: True/False
    '''
    check_list = [int(item) for item in (sorted(set(list(str(check_number)))))]

    for n in check_list:
        print (f'Verificando {n} - {type(n)}')
        if n not in [0,1]:
            print (f'numero binario incorrecto')
            return False
    return True

def validate_input(input_number):
    '''
    Es necesario verificar que lo ingresado sea correcto
    Al ser un conversor de bases solo pueden ingresarse caracteres del 0 al 9 y las letras a,b,c,d,e,f en caso de ser hexadecimal
    '''
    legal_char = '0123456789abcdef'
    for n in input_number:
        if n not in legal_char:
            return False
    return True

def validator(input_number,input_base,output_base):
    #Valida que los datos ingresados sean correctos
    if validate_input(input_number) and input_base.isdigit() and output_base.isdigit():

        #Verifica si la base ingresada es 2 (binario)
        if int(input_base) == 2:
            #Si es base 2 debe verificarse de que el numero ingresado esté correctamente ingresado
            if not validate_bin(input_number):
                print ("ERROR: Numero binario incorrecot. Un numero binario solo puede contener 0's o 1's")
                return False

        #Verifica que si lo ingresado es alfanumerico y la base sea 16
        if input_number.isdigit() and input_number.isalpha():
            if int(input_base) != 16:
                print ('ERROR: Los numeros hexadecimales deben ser de base 16')
                return False

        return True

def convert_number_system(input_number, input_base, output_base):
    '''
    Método que se encarga de convertir un numero de cualquier base a otra base
    Retorna el numero en la base deseada
    '''

    #Lista que contiene los numeros que se retornaran al final
    remainder_list = []

    #Valor de inicio para sum_base_10. Todos los calculos van a través de base-10
    sum_base_10 = 0

    #Validando los input

    #Si la base a la que se quiere convertir es binaria solo se debe retornar este método
    #se toma desde esa posicion ya que los primeros 2 caracteres se utilizan para indicar que es un valor binario
    if output_base == 2:
        return (bin(input_number)[2:])

    # we want to convert to base-10 before the actual calculation:
    # queremos convertir a base-10 antes del cálculo real:
    elif input_base != 10:

        # Se invierte la cadena para empezar a calcular desde el ultimo numero
        # Si no hacemos esto en este momento al final tocaría invertir el valor, así que por comodidad decidimos hacerlo
        #desde un principio así
        reversed_input_number = input_number[::-1]

        #comprueba si el usuario escribió una letra en el rango HEX.
        
        hex_helper_dict = {'a' : 10 , 'b' : 11 , 'c' : 12 , 'd' : 13 , 'e' : 14 , 'f' : 15}
        for index, number in enumerate(reversed_input_number):
            for key,value in hex_helper_dict.items():
                if str(number).lower() == key:
                    number = value

            sum_base_10 += (int(number)*(int(input_base)**index))

    # Si el numero ya está en base-10 se empieza con la conversión
    elif input_base == 10:
        sum_base_10 = int(input_number)


    # Hacemos un loop hasta obtener 0, cuando esto pasa ya está el numero deseado
    while sum_base_10 > 0:

        # Encuentra el numero a pasar debajo en el loop
        divided = sum_base_10// int(output_base)

        # guarda el remainder
        remainder_list.append(str(sum_base_10 % int(output_base)))

        # será el nuevo valor a enviar a la siguiente iteracion
        sum_base_10 = divided

    # si se requiere un valor hexadecimal para retornar, primero debemos conservar cualquier valor por encima de 10
    if int(output_base) == 16:
        hex_dict = {'10' : 'a' , '11' : 'b' , '12' : 'c' , '13' : 'd' , '14' : 'e' , '15' : 'f'}

        # Se mueve en remainder_list y convierte los valores mayores a 10 en letras
        for index, each in enumerate(remainder_list):
            for key, value in hex_dict.items():
                if each == key:
                    remainder_list[index] = value.upper()

    return ''.join(remainder_list[::-1])

def ejecutar_convertidor():
    user_number = ''
    user_input_base = ''
    user_output_base = ''

    proceed = 's'

    while proceed.lower() == 's':
        valid_input = False
        while valid_input == False:
            user_number = input('\nIngrese el valor a convertir: ')
            user_input_base = input('Ingrese la base del valor a convertir (por ejemplo, 10): ')
            user_output_base = input('Ingrese la base a cual quiere convertir (por ejemplo, 2): ')

            valid_input = validator(user_number,user_input_base,user_output_base)

        print (f'\nConvirtiendo {user_number} desde Base-{user_input_base} a Base-{user_output_base}: ')
        print (f'>> RESULTADO: {convert_number_system(user_number, user_input_base, user_output_base)} <<')

        print (f'\n¿Quieres convertir algun otro numero? escribe s/n: ')
        proceed = input('')


    print (f'cerrando converter...')

if __name__ == '__main__':
    ejecutar_convertidor()