##################################################################################

# Self explanatory
def base_neg2_to_int(bs):
    # Converts base negative 2 number to decimal
    out = 0
    for (i, b) in enumerate(bs[::-1]):
        out += int(b)*(-2)**i
    return out
  

##################################################################################





#### SOLUTION

def solution(A):
    n = base_neg2_to_int(A) + 1
    bits = []
    while n != 0:
        remainder = n % -2
        n //= -2
        if remainder < 0:
            # https://en.wikipedia.org/wiki/Negative_base#Calculation
            # "To arrive at the correct conversion, the value for c must 
            # be chosen such that d is non-negative and minimal
            remainder += 2
            n += 1
        bits.append(remainder)
    return bits[::-1]

  
  


######## TESTS ###############################################################################

if __name__ == "__main__":
    for value, expected_dec, expected_sol in [
        ("11111", 11, "11100"),
        ("1111", -5, "1100"),
        ("", 0, "1"),
        ("1", 1, "110"),
    ]:
        print("{} -> {} (expected {})".format(value, base_neg2_to_int(value), expected_dec))
        print("solution({}) -> {} (expected {})".format(value, solution(value), expected_sol))
        print()
        
################################################################################################
