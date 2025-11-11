

def es_bisiesto(año):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0): # Una año es bisiesto si es divisible por 4 pero no por 100, o si es divisible por 400
        return True
    else:
        return False
    
    