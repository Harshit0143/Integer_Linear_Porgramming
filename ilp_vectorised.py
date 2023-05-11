import sys
# import time
import math
import numpy as np
# import test_gen
# import final_test


class ratn:
    def __init__(self, numerator=0, denominator=1):
        self.num = numerator
        self.den = denominator
        self.reduce()

    def fractional_part(self):
        if self.den == 1:
            return ratn()
        elif self.num > 0:
            q = self.num//self.den
            return ratn(self.num-q*self.den, self.den)
        else:
            return ratn(1)-self.neg().fractional_part()

    def is_int(self):
        return self.den == 1

    def reduce(self):
        if (self.den < 0):
            self.den *= -1
            self.num *= -1

        g = math.gcd(self.num, self.den)
        self.num //= g
        self.den //= g

    def neg(self):
        return ratn(-self.num, self.den)

    def __add__(self, other):
        sum = ratn(self.num * other.den + other.num *
                   self.den, self.den * other.den)
        sum.reduce()
        return sum

    def __sub__(self, other):
        diff = ratn(self.num * other.den - other.num *
                    self.den, self.den * other.den)
        diff.reduce()
        return diff

    def __mul__(self, other):
        pro = ratn(self.num * other.num, self.den * other.den)
        pro.reduce()
        return pro

    def __truediv__(self, other):
        q = ratn(self.num * other.den, self.den * other.num)
        q.reduce()
        return q

    def __eq__(self, other):
        return self.num * other.den == self.den * other.num

    def __lt__(self, other):
        return self.num * other.den < self.den * other.num

    def __le__(self, other):
        return self.num * other.den <= self.den * other.num

    def __gt__(self, other):
        return self.num * other.den > self.den * other.num

    def __ge__(self, other):
       return self.num * other.den >= self.den * other.num

    def __repr__(self):
        return str(round(self.num/self.den, 4))

    # def __repr__(self):
    #     if self.den==1:
    #         return str(self.num)
    #     return f'{self.num}/{self.den}'

    def __str__(self):
        return f'{self.num}/{self.den}'

    def float_v(self):
        return self.num/self.den


global n, m
global tableau
global xB
global cost_red
global sn, sm


def show():
    print('variables:', sn, 'constraints:', sm)
    print(tableau[0:sm+1, 0:sn+1])
    print(xB[1:sm+1])
    print()


def get_input(file):
    global n, m, tableau, cost_red, xB
    xB = np.full(1000, 0)
    tableau = np.full((1000, 1000), ratn(), dtype=ratn)

    with open(file, 'r') as file:
        line = file.readline().strip().split()
        n = int(line[0])
        m = int(line[1])

        line = file.readline().strip().split()
        tableau[1:m+1, 0] = np.vectorize(lambda x: ratn(int(x)))(line)

        cost_red = np.full(n+m+1, ratn(), ratn)
        line = file.readline().strip().split()
        cost_red[1: n+1] = np.vectorize(lambda x: ratn(-1*int(x)))(line)

        for i in range(1, m+1):
            f = -1 if tableau[i][0].num < 0 else 1
            tableau[i][0].num *= f
            line = file.readline().strip().split()

            tableau[i, 1:n+1] = np.vectorize(lambda x: ratn(f*int(x)))(line)
            tableau[i][i+n] = ratn(f)
            tableau[i][i+n+m] = ratn(1)


def piv_col_aux(row):
    global tableau,n,m
    zero = ratn()
    return np.where(tableau[row,1:n+m+1] != zero)[0][0]+1


def drive_out_auxillary():
    global n, m, tableau, xB
    for row in range(1, m+1):
        if xB[row] > m+n:   # non artificial
            change_basis(row, piv_col_aux(row))



def fill_reduced_costs():
    global n, m, tableau, xB, cost_red
    cB = np.vectorize(lambda x: cost_red[x])(xB[0:m+1])
    tableau[0, 0:n+m+1] = cost_red[0:n+m+1]
    tableau[0, 0:n+m+1] -= np.dot(cB[1:m+1], tableau[1:m+1, 0:n+m+1])


def simplex_phase1():
    global n, m, sn, sm, tableau, xB, cost_red
    tableau[0, 0:n+m+1] -= np.sum(tableau[1:m+1, 0:n+m+1], axis=0)
    xB[1:m+1] = np.arange(n+m+1, n+2*m+1)
    sn = n+2*m
    sm = m
    simplex()
    if (tableau[0][0].num < 0):
        print("Infeasible Problem. Detected during simplex Phase 1")
        sys.exit()
    drive_out_auxillary()
    sn -= m
    tableau[0:sm+1, sn+1:sn+m+1] = ratn()
    fill_reduced_costs()
    simplex()


def change_basis(piv_row, piv_col):
    global xB, tableau
    xB[piv_row] = piv_col
    pivot = tableau[piv_row][piv_col]
    tableau[piv_row, 0: sn+1] /= pivot

    for i in range(0, sm+1):
        if i != piv_row:
            fac = tableau[i][piv_col]
            temp = np.vectorize(lambda x: x*fac)(tableau[piv_row, 0:sn+1])
            tableau[i, 0:sn+1] -= temp





def lexicography_dual(piv_row, i, j):  # True <==> j is strictly better
    global tableau
    if i == None:
        return True
    return tableau[0][i]/tableau[piv_row][i].neg() > tableau[0][j]/tableau[piv_row][j].neg()


def choose_col_dual(piv_row):
    global tableau
    id = None
    for j in range(1, len(tableau[0])):
        if tableau[piv_row][j].num < 0 and lexicography_dual(piv_row, id, j):
            id = j
    return id


def choose_row_dual():
    global tableau
    zero = ratn()
    indices = np.where(tableau[1:sm+1, 0] < zero)[0]
    return None if len(indices) == 0 else 1 + indices[0]


def dual_simplex():
    while True:
        piv_row = choose_row_dual()
        if piv_row == None:
            return
        piv_col = choose_col_dual(piv_row)
        if piv_col == None:
            print("Infeasible Problem. Dual Optimal found +Infinity")
            sys.exit()
        change_basis(piv_row, piv_col)


def lexicography_primal(piv_col, i, j):
    if i == None:
        return True
    z1 = tableau[j][0]/tableau[j][piv_col] < tableau[i][0]/tableau[i][piv_col]
    z2 = tableau[j][0]/tableau[j][piv_col] == tableau[i][0] / \
        tableau[i][piv_col] and xB[j] < xB[i]
    return z1 or z2


def choose_row_primal(piv_col):
    global tableau, sm
    id = None
    for j in range(1, sm+1):
        if tableau[j][piv_col].num > 0 and lexicography_primal(piv_col, id, j):
            id = j
    return id


def choose_col_primal():
    global tableau, sn
    zero = ratn()
    ind = np.where(tableau[0, 1:sn+1] < zero)[0]
    return None if (len(ind) == 0) else 1 + ind[0]


def simplex():
    while True:
        piv_col = choose_col_primal()
        if piv_col == None:
            return  # found optimal
        piv_row = choose_row_primal(piv_col)
        if piv_row == None:
            print("Optimal Value is +Infinity")
            sys.exit()
        change_basis(piv_row, piv_col)


def non_int():
    global sm, tableau
    id = np.argmax(np.vectorize(lambda x: x.fractional_part())(tableau[1:sm+1, 0]))
    return None if tableau[id+1][0].fractional_part() == ratn() else id+1


def build_sol():
    # print("Objective_value:", tableau[0][0].neg().num)
    sol = [0]*n
    for i in range(1, sm+1):
        if xB[i] <= n:
            sol[xB[i]-1] = tableau[i][0].num
    return sol


def add_cut(r):
    global sn, sm, tableau, xB
    sn += 1
    sm += 1
    xB[sm] = sn
    tableau[sm, 0:sn] = np.vectorize(
        lambda x: x.fractional_part().neg())(tableau[r, 0:sn])
    tableau[sm][sn] = ratn(1)


def gomory(file):
    get_input(file)
    simplex_phase1()
    while True:
        fr = non_int()
        if fr == None:
            return build_sol()
        add_cut(fr)
        dual_simplex()

# print(gomory('input.txt'))
