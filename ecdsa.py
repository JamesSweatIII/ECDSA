import sys
import random


def genKey(prime, order, xcordinate, ycordinate):
    
    d = random.randint(1, order-1)
    
    qx1, qy1 = multiplication(xcordinate, ycordinate, prime, d)
    
    return print(str(d) + '\n' + str(qx1)  + '\n' + str(qy1))

def signMessage(prime, order, xcordinate, ycordinate, d, hash):
    k = random.randint(1, order-1)
    r, r2 = multiplication(xcordinate, ycordinate, prime, k)
    k_inverse =  inverse(k, order)
    s = k_inverse * (hash + r * d) % order

    return print(str(r) + '\n' + str(s))

def verifyMessage(prime, order, xcordinate, ycordinate, qx, qy, r, s, hash):
    
    s_inv = inverse(s, order)
        
    RX1, RY1 = (multiplication(xcordinate, ycordinate, prime, s_inv * hash))
    RX2, RY2 = (multiplication(qx, qy, prime, s_inv * r))
            
    AX1, AY1 = addition(RX1, RY1, RX2, RY2, prime)
    
    return print(AX1 == r)

def inverse(denominator, prime):
    return pow(denominator, -1, prime)

def slope(x_cordinate_1, y_cordinate_1, x_cordinate_2, y_cordinate_2, prime):
    
    if x_cordinate_1 == x_cordinate_2 and y_cordinate_1 == -y_cordinate_2 % prime:  
        return None
    
    if x_cordinate_1 == x_cordinate_2 and y_cordinate_1 == y_cordinate_2:
            
        numerator = (3 * x_cordinate_1 * x_cordinate_1) % prime
        denominator = (2 * y_cordinate_1) % prime
            
    else:
        numerator = (y_cordinate_2 - y_cordinate_1) % prime
        denominator = (x_cordinate_2 - x_cordinate_1) % prime

    inverse_denominator = inverse(denominator, prime)
    slope_value = (numerator * inverse_denominator) % prime
    return slope_value

def addition(x_cordinate_1, y_cordinate_1, x_cordinate_2, y_cordinate_2, prime):
    
    if x_cordinate_1 is None or y_cordinate_1 is None:
        return x_cordinate_2, y_cordinate_2
    
    if x_cordinate_2 is None or y_cordinate_2 is None:
        return x_cordinate_1, y_cordinate_1

    if x_cordinate_1 == x_cordinate_2 and y_cordinate_1 == (-y_cordinate_2 % prime):
        return None, None 

    m = slope(x_cordinate_1, y_cordinate_1, x_cordinate_2, y_cordinate_2, prime)
    
    if m is None:
        return None, None

    x_cordinate_3 = (m**2 - x_cordinate_1 - x_cordinate_2) % prime
    y_cordinate_3 = ((m * (x_cordinate_1 - x_cordinate_3)) - y_cordinate_1) % prime

    return x_cordinate_3, y_cordinate_3

def multiplication(x_cordinate, y_cordinate, prime, scalar):
    result_x, result_y = None, None  
    intial_x, intial_y = x_cordinate, y_cordinate
    
    if scalar == 0:
        return None, None 
    
    negative = scalar < 0 
    scalar = abs(scalar)  

    while scalar > 0:
        
        if scalar % 2 == 1: 
            if result_x is None:
                
                result_x, result_y = intial_x, intial_y
            else:
                result_x, result_y = addition(result_x, result_y, intial_x, intial_y, prime)
                
        intial_x, intial_y = addition(intial_x, intial_y, intial_x, intial_y, prime)
        
        scalar //= 2  
    
    if negative and result_x is not None:
        result_x, result_y = point_negation(result_x, result_y, prime)
   
    return result_x, result_y

def exponentiation(x_cordinate, y_cordinate, prime, scalar, exponent):
    power = scalar ** exponent
    return print(multiplication(x_cordinate, y_cordinate, prime, power))

def point_negation(x_cordinate, y_cordinate, prime):
    x_cordinate = x_cordinate % prime
    y_cordinate = mod_negative(y_cordinate, prime)
    return x_cordinate, y_cordinate

def mod_negative(cordinate, prime):
    return (prime - (cordinate % prime))

def subtraction(x_cordinate_1, y_cordinate_1, x_cordinate_2, y_cordinate_2, prime):
    x_cordinate, y_cordinate = point_negation(x_cordinate_2, y_cordinate_2, prime)
    return addition(x_cordinate_1, y_cordinate_1, x_cordinate, y_cordinate)

def division(x_cordinate, y_cordinate, prime, scalar):
    fermat = inverse(scalar, prime)  
    return print(multiplication(x_cordinate, y_cordinate, prime, fermat))

def print_userid():
    print("jes9hd")
      
def main():
     
    if sys.argv[1] == 'userid':
        print_userid()
    elif sys.argv[1] == 'genkey':
        genKey(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]))
    elif sys.argv[1] == 'sign':
        signMessage(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]), int(sys.argv[7]))
    elif sys.argv[1] == 'verify':
        verifyMessage(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]), int(sys.argv[7]), int(sys.argv[8]), int(sys.argv[9]), int(sys.argv[10]))
    
if __name__ == "__main__":
    main()
