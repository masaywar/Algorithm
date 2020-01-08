from functools import reduce
from itertools import permutations
from math import log10, log2, log
from fractions import Fraction
import math

def Problem21():
    """
    Amicable numbers
    Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n). If d(a) = b
    and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
    For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
    The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
    Evaluate the sum of all the amicable numbers under 10000.
    :return:
    """

    N = 10001
    sum = 0

    def Amic(n):
        sum = 0
        for j in range(1, int(n**0.5)+1):
            if n % j == 0:
                sum = sum + n//j + j if n//j != j else sum + n//j
        return sum - n

    for k in range(1, N):
        temp = Amic(k)
        Amic_temp = Amic(temp)
        if Amic_temp == k and k != temp:
            sum += temp

    print(sum)


def Problem22():

    """
    Names scores
    Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first
    names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply
    this value by its alphabetical position in the list to obtain a name score. For example, when the list is sorted
    into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN
    would obtain a score of 938 × 53 = 49714. What is the total of all the name scores in the file?
    :return:
    """

    with open("Problem22.txt", "r") as f:
        s = f.readlines()[0].replace('"', "")
        L = sorted(s.split(","))
    print(L)

    alphabet_dict = {chr(ord("A") + k) : k + 1 for k in range(26)}
    print(alphabet_dict)

    res = 0
    idx = 1
    for k in L:
        sum = 0
        for j in k:
            sum += alphabet_dict[j]
        res += sum * idx
        idx += 1

    print(res)


def Problem23():

    """
    Non-abundant sums
    A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example,
    the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
    A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this
    sum exceeds n. As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be
    written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers
    greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced
    any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two
    abundant numbers is less than this limit. Find the sum of all the positive integers which cannot be written as the
    sum of two abundant numbers.
    """

    N = 28123
    res = set(k for k in range(1, 28124))
    sum_set = set()
    L = []
    abundant = dict()
    for k in range(1, N):
        sm = 0
        for j in range(1, int(k**0.5) + 1):
            if k % j == 0:
                L.append(j)
                sm = sm + j + k//j if j != k//j else sm + j
        sm -= k
        if sm > k:
            abundant[k] = sm

    for k in abundant.keys():
        for j in abundant.keys():
            if k + j > 28123:
                break
            sum_set.add(k+j)

    print(sum(res - sum_set))


def Problem24():
    count = 0
    for k in permutations("0123456789"):
        count += 1
        if count == 1000000:
            return k


def Problem25():
    fib1, fib2 = 1, 1
    count = 1
    while log10(fib1) < 999:
        fib1, fib2 = fib2, fib1 + fib2
        count += 1
    return count


def Problem26():
    max = [0, 0] # index 0 is max value and the other one is max value's index
    for k in range(100, 1001):
        rem_dict = dict()
        dom = k
        rem = 10 % dom
        string = f"{10 // dom}"
        rem_dict[rem] = 1
        rem *= 10
        while rem not in rem_dict and rem != 0:
            string += f"{rem // dom}"
            rem_dict[rem] = 1
            rem = rem % dom
            rem *= 10
        if max[0] < len(string):
            max[0] = len(string)
            max[1] = k
    return max


def Eratosthenes_seive(N):
    L = [True]*1000000
    L[0], L[1] = False, False
    i = 2
    while i**2 < len(L):
        k = i
        for _ in range(len(L)):
            k = k+i
            try:
                L[k] = False 
            except IndexError:
                break
        i += 1
    return L


def Problem27():
    a = []
    mx = []
    L = Eratosthenes_seive(1002)
    for k in range(2, 1002):
        if L[k]:
            a.append(k)
            a.append(-k)
    fx = lambda x, a, b: x**2 + a*x + b
    li = []
    for k in range(-999, 1000):
        for j in a:
            n = 0
            while True:
                idx = fx(n, k, j)
                if L[idx] and idx > 0:
                    li.append((idx, k, j))
                    n += 1
                else:
                    if len(mx) < len(li):
                        mx = li.copy()
                    li = []
                    break
    print(mx[0][1] * mx[0][2])

def _find_dist(a, b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5    

def closetPair(L):
    if len(L) <= 2:
        return _find_dist(L[0], L[1])
    if len(L) <= 3:
        return min(list(_find_dist(L[0], L[1]), _find_dist(L[0], L[2]), 
                        _find_dist(L[1], L[2])))
    L = sorted(L)
    left = L[:len(L)//2]
    right = L[len(L)//2:]
    print(f"left : {left}, right : {right}")
    left_min = closetPair(left)
    right_min = closetPair(right)
    pivot_coor = L[len(L)//2+1][0] - L[len(L)//2-1][0]
    pivot_len = min(left_min, right_min)
    middle = []
    for k in L:
        if k[0] > pivot_coor - pivot_len and k[0] < pivot_coor + pivot_len:
            middle.append(k)
            
    middle.sort(key = lambda element : element[1])
    min_len = pivot_len
    
    for k in middle:
        for j in middle:
            if k is j or j[1] < k[1]:
                continue
            else:
                res = _find_dist(k, j)
                if res > pivot_len:
                    break
                if min_len < res:
                    min_len = res
    
    return min(left_min, right_min, min_len)
    
if __name__ == "__main__":
    L = [(10, 15), (5, 15), (20, 3), (6,1), (9, 7), (15, 9), (8, 15), (20, 14)
    , (17, 13), (16, 11), (7, 12), (10,10), (1, 19), (8, 8), (30, 9), (22, 4)]
    
    L = sorted(L)
    print(L)
  
    print(closetPair(L))


def Problem28():
    sm = 0
    N = 1001
    arr = [[N*N+1 for _ in range(N)] for _ in range(N)]
    x, y, dx, dy, count = 0, N-1, 0, -1, 1
    while arr[x][y] == N*N+1:
        arr[x][y] -= count
        count += 1
        x, y = x + dx, y + dy
        if x in [-1, N] or y in [-1, N] or arr[x][y] != N*N+1:
            x, y = x - dx, y - dy
            dx, dy = -dy, dx
            x, y = x + dx, y + dy
    for k in range(N):
        sm += arr[k][k] + arr[0+k][N-1-k]
    print(sm - arr[N//2][N//2])


def judge(N):
    while (N % 2 == 0 or N % 5 == 0) and N != 1:
        if N % 2 == 0:
            N //= 2
        if N % 5 == 0:
            N //= 5
    return N == 1


def Problem183():
    max_sum = 0
    for N in range(5, 10001):
        divisor = int(N/math.exp(1))
        if (1.0 * (divisor + 1) / divisor) ** (divisor + 1) >= 1.0 * N / divisor: pass
        else:
            divisor += 1
        denom = divisor / gcd(N, divisor)
        if judge(denom):
            max_sum += - N
        else:
            max_sum += N
        if N % 100 == 0:
            print(N, max_sum)
    return max_sum


def P(n, k):
    r = 1.0*n/k
    return r**k

def Max_P_and_K(n):
    k = int(n/math.exp(1))
    max1 = P(n, k)
    max2 = P(n, k+1)
    if max1 > max2 :
        return max1, k
    else:
        return max2, k+1

def k_makes_the_max(n, k):
    return (1.0*(k+1)/k)**(k+1) >= 1.0*n/k

def k_makes_the_max(n, k):
    return (1.0*(k+1)/k)**(k+1) >= 1.0*n/k

def K_for_Max_P(n):
    k = int(n/math.exp(1))
    if k_makes_the_max(n, k):
        return k
    else:
        return k+1

def gcd(max, min):
    if max % min == 0:
        return min
    else:
        return gcd(min, max%min)


def M_is_nonterminating_decimal(n):
    k = K_for_Max_P(n)
    #print n, k
    k = k/ gcd(n,k) # At 1st trial, I miss this condition, which is actaully evident.
    while k % 2 == 0 or k % 5 == 0:
        if k % 2 == 0:
            k /= 2
        if k % 5 == 0:
            k /= 5
    if k == 1:
        return False
    else:
        return True

def D(n):
    if M_is_nonterminating_decimal(n) :
    #print n, n
        return n
    else:
    #print n, -n
        return -n

def Problem29():
    dic = dict()

    for i in range(2, 101):
        for j in range(2, 101):
            dic[pow(i, j)] = (i, j)

    return len(dic)


def Problem30():
    result_list = []
    #num = 2
    for i in range(10, 354294):
        temp = i
        sum_of_num = 0
        while i/1 != 0:
            sum_of_num += (i%10)**5
            i //= 10
        #print(sum_of_num)
        if sum_of_num == temp: result_list.append(temp)
    return sum(result_list)


if __name__ == "__main__":
    print(Problem30())

