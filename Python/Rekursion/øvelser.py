# 1. Forklar hvad funktionen gør og udskriv kaldene for sum(5):
def sum(n):
    if n == 0 or n == 1 :
        return 1
    if n > 1 :
        return n + sum(n-1)
# Ved sum(5) returneres 15, som er 5+4+3+2+1

# 2. Skriv en rekursiv funktion, der beregner eksponenten af et tal.
def pow(a, n):
    if n == 0:
        return 1
    if n == 1:
        return a
    return a*(pow(a, n-1))

# 3. Skriv en funktion der rekursivt skifter mellem at addere og subtrahere tal i en liste. Hvis listen eksempelvis er [5,3,1,2,4] så skal funktionen udregne: 5-3+1-2+4=5.
def addSub(list):
    if len(list) == 1:
        return list[0]
    if len(list) == 2:
        return list[0] - list[1]
    return list[0] - list[1] + addSub(list[2:])

# 4. Skriv en rekursiv funktion der undersøger om et tal er lige eller ulige
def parity(n):
    if n % 2:
        return "odd"
    return "even"

# 5. Hvad gør følgende funktion. Forklar koden i detaljer:
import math

def binSearch(n, arr) : # listen der indputtes skal være sorteret i størrelses orden, mindst til størst.
    mid = math.floor(len(arr) / 2) # Vi finder midten af listen.
    if len(arr) == 1 and arr[0] != n : # Hvis det sidste element ikke er det vi søger efter, returneres False.
        return False
  
    if n == arr[mid] : # Hvis tallet vi leder efter er det midterste element i listen, returneres True
        return True 
    elif n < arr[mid] : # Hvis tallet vi leder efter er større end det midterste element i listen, kaldes funktionen igen med den sidste halvdel af listen
        return binSearch(n, arr[0: mid]) # Hvis tallet vi leder efter er større end det midterste element i listen, kaldes funktionen igen med det sidste halvdel af listen
    elif n > arr[mid] : # Hvis tallet vi leder efter er større end det midterste element i listen, kaldes funktionen igen med den sidste halvdel af listen
        return binSearch(n, arr[mid:len(arr)-1]) # Hvis tallet vi leder efter er større end det midterste element i listen, kaldes funktionen igen med det sidste halvdel af listen
    
# 6. Skriv en rekursiv funktion, der undersøger om et ord er et palindrome. Dvs. hvorvidt det læses forfra og bagfra på samme måde.
def palindrom(ord):
    if len(ord) <= 1:
        return True
    if ord[0] == ord[-1]:
        return palindrom(ord[1:-1])    
    return False

# 7. Skriv en rekursiv funktion, der finder største fælles divisor af to tal
def GCD(a, b):
    if b == 0:
        return a
    
    return GCD(b, a % b)

# 8. Skriv en rekursiv funktion, der returnerer alle tænkelige permutationer af et ord (eksempel: ”abc” så er ”acb” en permutation.
# (med loop)
def permutationer(ord):
    numOfPerms = math.factorial(len(ord))
    if numOfPerms > 25:
        return print("please choose a shorter word, to not crash your computer")

    if len(ord) <= 1:
        return [ord]
    perms = []
    for i in range(len(ord)):
        for perm in permutationer(ord[:i] + ord[i+1:]):
            perms.append(ord[i] + perm)
    return perms


# check en liste igennem, for et ord, hvis det ikke findes:
def permuter(ord):
    combinations = len(ord)
    if combinations > 25:
        return "Please choose a shorter word"

    if  perms == None:
        perms = []
    
    
    
    
    # check if there are multiple same digit of a word:
    check()  

def check(word):
    for char in word:
        return


# 9. Skriv en rekursiv funktion, der beregner mindste fælles divisor, som ikke er 1
"""def SCD(a, b):
    if a % b != 0:
        return SCD(b, a % b)

    if r == 1:
        return """