ar =[1,2,3,4,5]

print ("cantidad de datos en el array: ", len(ar))
print ("tipo de dato que utiliza la función 'len()': ", type(len(ar)))

def simpleArraySum(ar):
    # Write your code here
    result = 0
    for i in range(len(ar)):
        print('valor de i: ', ar[i])
        result += ar[i]
    return result
    
resultadoFinal = simpleArraySum(ar)
print(resultadoFinal)