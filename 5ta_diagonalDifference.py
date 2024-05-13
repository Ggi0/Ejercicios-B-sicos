'''
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix arr is shown below:
1 2 3
4 5 6
9 8 9  
The left-to-right diagonal = 1+5+9 = 15 . The right to left diagonal = 3+5+9= 15. Their absolute difference is |15-17|=2.

Function description

Complete the diagonalDifference function.

diagonalDifference takes the following parameter:

int arr[n][m]: an array of integers
Return

int: the absolute diagonal difference
Input Format

The first line contains a single integer, n , the number of rows and columns in the square matrix arr.
Each of the next n lines describes a row, arr[i], and consists of n space-separated integers arr[i][j].
'''

arr = [
    [5],
    [11, 2, 4, 3, 5],
    [4, 11, 6, 13, 35],
    [10, 8, 11, 21, 12],
    [4, 11, 6, 19, 25],
    [10, 8, 11, 2, 22]
]

print('longitud de la matriz: ', len(arr))
print('Posicion 0, 0 (inicial): ',arr[0][0])

def diagonalDifference(arr):
    # Write your code here
    sumDer = 0
    sumIzq = 0
    indice = 0
    
    primerValor = arr[0][0]
    
    
    # Matriz con el formato correcto
    if len(arr[0]) == 1:
        # Filas: Cantidad de listas dentro de la matriz, sin contar la primera
        filas = len(arr) - 1
        print('filas: ', filas, '\n')
        
        for i in range(1, len(arr)):
            columnas = len(arr[i])
            print(f'Longitud del arreglo {i}: ', columnas, '\n')
            print('valores dentro de los arreglos ', arr[i])
            
            if (columnas, filas, primerValor % 2 != 0) and (columnas == filas == primerValor):
                print('Todos los valores correctos para realizar la operación')
                
                #invertir el orden de la lista, para la suma de la diagonal izquierda
                arr2 = arr[i][::-1]
                for j in range(columnas):
                    sumDer += arr[i][indice]
                    sumIzq += arr2[indice]
                    indice += 1
                    print('valor de indice: ', indice)
                    break
                
                    
            else:
                print('El numero de filas y columnas no coinciden,\nla operación no se puede realizar')
                break
        print(sumDer)
        print(sumIzq)
        resultado = abs(sumDer - sumIzq)
        return resultado

    else:
        print('Matriz con el formato incorrecto.')
    
    
print(diagonalDifference(arr))
