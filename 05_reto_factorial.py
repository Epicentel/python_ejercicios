
#FACTORIAL

def factorial(n:int)->int:

    if n < 0:
        raise ValueError("el número debe ser igual o mayor que cero")
    
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2,n+1):
        result = result*i
    return result


    

   
