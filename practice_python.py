import re
import math
import statistics



# Variables for testing
lista = [1,2,-3,4,-5,6]


# Maximum Product of Three Numbers [D.E. Shaw Python Interview Question]
def max_three(input):
    f = (input[0] * input[1] * input[2])
    print(input[0])
    print(input[1])
    print(input[2])
    print(f)
    for i in range(len(input)-2):
        for j in range(i+1, len(input)-1):
            for k in range(j+1, len(input)):
                if (input[i]*input[j]*input[k]> f):
                    f = input[i]*input[j]*input[k]
    return f	      

# Factorial
def factorial(n):
  if (n == 0):
        return 1
  else:
    fact = 1
    for i in range(1,n+1):
      fact = fact * i 
    return fact
print(factorial(5))


# Two Sum [Amazon Python Interview Question]
# Verify in a list if two elements reach the sum of a defined "target", return the indexes
def two_sum(input: list[int], target: int) -> list[int]:
    for i in range(len(input) - 1):
        for j in range(i+1, len(input)):
        	if ((input[i] + input[j]) == target):
                    return [i,j]
    else:
            return[-1,-1]
print(two_sum([1,2,4,5,7,9],22))



# Largest Prime Factor [Facebook Python Interview Question]
## My solution
def largest_prime_factor(target):
  primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
  lista = []
  while (target != 1):
      for i in range(len(primes)):
        if (target % (primes[i]) == 0):
            lista.append(primes[i])
            target = target / primes[i]
            i = 0         
  lista = list(dict.fromkeys(lista))
  return (lista)

# print(largest_prime_factor(1428))


## Optimous solution
# def largest_prime_factor(target):
#   i = 2
#   while i * i <= target:
#       if (target % i) != 0:
#           i += 1
#       else:
#           target //= i
#   return target


def multiplyList(myList):
    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result


# Primes for a number
# def primes(target):
#   lista = [1]
#   i = 2
#   while ((multiplyList(lista)) < target):
#       if (target % i) != 0:
#           i += 1
#       else:
#         target = target / i
#         lista.append(i)
#   lista = list(dict.fromkeys(lista))
#   return lista

# # Smallest Multiple [Google Python Interview Question]
def smallest_multiple(target):
   n = 1
   for i in (range(1,target+1)):
        n = (i * n)
   return(multiplyList(largest_prime_factor(n))) 

# Pearson Correlation Coefficient [AQR Python Interview Question]
#The Pearson correlation coefficient (r) is the most common way of measuring a linear correlation.
#It is a number between –1 and 1 that measures the strength and direction of the relationship between two variables.

def corr(x, y):
  return (covarianza(x,y)/(standard_dev(x)*standard_dev(y)))

lista_1 = [50,19,20,6,22,17,21,26,32,9]
lista_2 = [183,179,173,177,182,171,173,168,189,179]
lista_3 = [80,74,75,74,67,68,73,68,84,76]

# Python program to get average of a list 
def Average(lst): 
    return sum(lst) / len(lst) 

def covarianza(lista1,lista2):
    x = 0
    for i in range(len(lista1)):
      x = ((lista1[i] - (Average(lista1))) * (lista2[i] - (Average(lista2)))) + x
    x = x/(len(lista1))
    return x

def standard_dev(lista):
    x = 0
    for i in range(len(lista)):
        x = (lista[i]-Average(lista)) ** 2 + x
    x = math.sqrt(x / (len(lista)-1))
    return x

def corr(x, y):
  return (covarianza(x,y)/(standard_dev(x)*standard_dev(y)))

print(corr(lista_1,lista_2))
print(statistics.correlation(lista_1,lista_2))
print(corr(lista_1,lista_3))
print(corr(lista_2,lista_3))
# print(covarianza(lista_1,lista_2))
# print(statistics.covariance(lista_1,lista_2))
# print(standard_dev(lista_1))
# print(statistics.stdev(lista_1))

# Merge Conflicts [Microsoft Python Interview Question]

# Your job is to write a function called has_merge_conflict which returns True or False, depending on if there is or is not any merge conflict.
# In this case, a merge conflict means two different pull requests are trying to change the same exact lines.
# For example, if you were given the input pull_requests = [[5, 10], [15, 40], [25, 50]].
# We'd output True because there is a merge conflict: two different pull requests trying to change lines between 25 and 40.

def has_merge_conflict(pull_requests)-> bool:
  for i in range(len(pull_requests)-1):
      first_pr = pull_requests[i]
      for j in range(i+1,len(pull_requests)):
        second_pr = pull_requests[j]
        if (second_pr[0] <= first_pr[0]) & (first_pr[0] <= second_pr[1]) | (second_pr[0] <= first_pr[1]) & (first_pr[1] <= second_pr[1]):
              return True
  return False

# list_test = [[10,15],[24,29],[12,17]]
# print(has_merge_conflict(list_test))

# Largest Contiguous Subarray Sum [Akuna Capital Python Interview Question]

def max_subarray_sum(input):
    x = 0
    for i in range(len(input)-1):
        if ((input[i]+input[i+1]) > x):
          x = input[i]+input[i+1]
    return x

print(max_subarray_sum([1,-1,2,7,1,-8,-7,5,1]))


def regular_expresion(expresion, file):
  """
  Encuentra todas las apariciones de una expresion regular en un archivo de texto
  """
  p = re.compile("abc")
  p = re.compile(expresion)
  doc = open("archivo.txt", "r")
  doc = open(file, "r")
  matches = re.findall(p, doc)
  return matches

def find_platform_line(lines):
  """
  Encuentra la primera línea que comienza con el sufijo //platform.

  Args:
    lines: Una lista de líneas de texto.

  Returns:
    True si se encuentra la línea, False si no se encuentra.
  """

  for line in lines:
    if line.startswith("//platform"):
      print(line)
      return True
  return False

def ListaDivisible(numero,tope):
    result = []
    for i in range(1,tope+1):
        if i % numero == 0:
            result.append(i)
    return result

def Exponente(numero,exponente):
    return numero**exponente

def Exponente2(numero,exponente):
    resultado = 1
    for i in range(exponente):
        if exponente == 0:
            resultado = 1
        else:
             resultado = numero * resultado
    return resultado

def Factorial(numero):
    if numero < 0:
        resultado = 'no existe'
    elif numero == 0:
        resultado = 1
    else:
        resultado2 = 1
        for i in range(1,numero+1):
            resultado2 = resultado2 * i
            resultado = resultado2
    return resultado

numerosPrimo = [1,2,3,5,7,11,13,17,19,23,29,31,37,41,53]

def Esprimo(numero):
    return numero in numerosPrimo

def ListaDePrimos(desde,hasta):
    lista = []
    for i in range(desde,hasta+1):
        if i in numerosPrimo:
            lista.append(i)
    return lista