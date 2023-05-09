from rational_numbers import rationals as ratn
import show
import sys
import final_test
import time 


global n, m
global tableau
global xB
global cost_red


def get_input():
    global n, m, tableau, xB, cost_red
    with open('input.txt', 'r') as file:
        line = file.readline().strip().split()
        n = int(line[0])
        m = int(line[1])

        tableau = [[ratn()] * (n+2*m+1) for _ in range(m+1)]

        line = file.readline().strip().split()
        for i in range(1, m+1):
            tableau[i][0] = ratn(int(line[i-1]))

        cost_red = [ratn()]*(n+m+1)
        line = file.readline().strip().split()
        for j in range(1, n+1):
            cost_red[j] = ratn(int(line[j-1]))

        for i in range(1, m+1):
            line = file.readline().strip().split()
            f = -1 if tableau[i][0].num < 0 else 1
            tableau[i][0].num *= f
            for j in range(1, n+1):
                tableau[i][j] = ratn(f*int(line[j-1]))
            for j in range(n+1, n+m+1):
                tableau[i][j] = ratn(f*(j-n == i))
            for j in range(n+m+1, n+2*m+1):
                tableau[i][j] = ratn(j-n-m == i)



def piv_col_aux(row):
    global tableau
    for col in (1,n+m+1):
        if tableau[row][col].num !=0:
            return col
    return None # never reached based on our formulation 
    
def drive_out_auxillary():
    global n, m, tableau, xB
    remove = [False]*(m+1)
    for row in range (1, m+1):
        if xB[row] > m+n:   # non artificial 
            change_basis(row , piv_col_aux(row))
                         

def erase_auxillary():
    global n, m, tableau, xB
    for row in range (m+1):
        for col in range (n+2*m , m+n,-1):
            tableau[row].pop()


def fill_reduced_costs():
    global n, m, tableau, xB,cost_red
    for col in range(0,n+m+1):
        tableau[0][col] = cost_red[col]
        for row in range (1,m+1):
            tableau[0][col]-=  tableau[row][col]*cost_red[xB[row]]
    
def simplex_phase1():
    global n, m, tableau, xB,cost_red
    xB = [None]  # this later helps in 1 indexing
    for col in range(0, n+m+1):
        for row in range(1,m+1):
            tableau[0][col] -= tableau[row][col]
    for col in range(n+m+1, n+2*m+1):
        xB.append(col)
        tableau[0][col] = ratn(1)
    simplex()  
    
   
    if (tableau[0][0].num < 0):
        print("Infeasible Problem. Detected during simplex Phase 1")
        sys.exit()

  
    drive_out_auxillary()
    erase_auxillary()
    # print(xB)
    # show.show(tableau)
    
    fill_reduced_costs()
    simplex()

  





def divide_row(piv_row, piv_col):
    global tableau
    pivot = tableau[piv_row][piv_col]
    for i in range(0, len(tableau[0])):
        tableau[piv_row][i] /= pivot


def eliminate_rows(piv_row, piv_col):
    global tableau
    for i in range(0, len(tableau)):
        if i != piv_row:
            fac = tableau[i][piv_col]
            for j in range(0, len(tableau[0])):
                tableau[i][j] -= tableau[piv_row][j]*fac



def change_basis(piv_row, piv_col):
    global xB
    xB[piv_row] = piv_col
    divide_row(piv_row, piv_col)
    eliminate_rows(piv_row, piv_col)


def choose_row_dual():
    global tableau
    for i in range(1, len(tableau)):
        if tableau[i][0].num < 0:
            return i
    return None


def lexicography_dual(piv_row, i, j):  # True <==> j is strictly better
    global tableau
    if i == None:
        return True
    for row in range(0, len(tableau)):
        if tableau[row][i]/tableau[piv_row][i].neg() > tableau[row][j]/tableau[piv_row][j].neg():
            return True
        elif tableau[row][i]/tableau[piv_row][i].neg() < tableau[row][j]/tableau[piv_row][j].neg():
            return False
    return False


def choose_col_dual(piv_row):
    global tableau
    id = None
    for j in range(1, len(tableau[0])):
        if tableau[piv_row][j].num < 0 and lexicography_dual(piv_row, id, j):
            id = j   
    return id

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
    




def lexicography_primal(piv_col,i, j):
    if i == None:
        return True  
    z1 =  tableau[j][0]/tableau[j][piv_col] < tableau[i][0]/tableau[i][piv_col]
    z2 =  tableau[j][0]/tableau[j][piv_col] == tableau[i][0]/tableau[i][piv_col] and xB[j] < xB[i]
    return z1 or z2


def choose_row_primal(piv_col):
    global tableau
    id = None
    for j in range(1, len(tableau)):
        if tableau[j][piv_col].num > 0 and lexicography_primal(piv_col,id, j):
            id = j 
    return id

def choose_col_primal():
    global tableau
    for col in range(1, len(tableau[0])):
        if tableau[0][col].num < 0:
            return col
    return None      
   

def simplex():
    while True:
        piv_col = choose_col_primal()
        if piv_col == None:
            return # found optimal 
        
        piv_row = choose_row_primal(piv_col)
        if piv_row == None:
            print("Optimal Value is -Infinity")
            sys.exit()
        change_basis(piv_row, piv_col)
    

        



def check_dual():
    global tableau,xB
    with open('input.txt', 'r') as file:
        line = file.readline().strip().split()
        n = int(line[0])
        m = int(line[1])

        tableau = [[ratn()] * (n+m+1) for _ in range(m+1)]

        line = file.readline().strip().split()

        xB = [None]
        for i in range(1, m+1):
            tableau[i][0] = ratn(int(line[i-1]))
            xB.append(n+i)

        line = file.readline().strip().split()
        for j in range(1, n+1):
            tableau[0][j] = ratn(int(line[j-1]))
        
       
        
        for i in range(1, m+1):
            line = file.readline().strip().split()  
            for j in range(1, n+1):
                tableau[i][j] = ratn(int(line[j-1]))
            for j in range(n+1, n+m+1):
                tableau[i][j] = ratn(j-n == i)
    dual_simplex()


def non_int(tolerate = ratn()):
    for i in range (1,len(tableau)):
        f = tableau[i][0].fractional_part()
        if (f > tolerate  and ratn(1)-f > tolerate):
            return i
    
def build_sol():
    print("Objective_value:", tableau[0][0].neg().num)
    sol = [0]*n
    for i in range (1, len(xB)):
        if xB[i] <= n:
            sol[xB[i]-1] = tableau[i][0].num
    print(sol)
    return sol
def add_cut(r):
    xB.append(len(tableau[0]))
    L = []
    for num in tableau[r]:
        L.append(num.fractional_part().neg())
    L.append(ratn(1))
    tableau.append(L)
    for i in range (len(tableau)-1):
        tableau[i].append(ratn())
    

    
def print_col():
    for i in range(len(tableau)):
        print(tableau[i][0],end  = ' ')
    print()



def gomory(input):
    get_input()
    simplex_phase1()
    while True:
        fr = non_int()
        if fr == None:
            return build_sol() 
        add_cut(fr)
        dual_simplex()
   
        
t = time.time()
gomory("input.txt")
print(time.time()-t)



