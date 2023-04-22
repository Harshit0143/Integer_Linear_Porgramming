import rational_numbers as rnum
import show
import sys
import testing
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

        tableau = [[rnum.rationals()] * (n+2*m+1) for _ in range(m+1)]

        line = file.readline().strip().split()
        for i in range(1, m+1):
            tableau[i][0] = rnum.rationals(int(line[i-1]))

        cost_red = [rnum.rationals()]*(n+m+1)
        line = file.readline().strip().split()
        for j in range(1, n+1):
            cost_red[j] = rnum.rationals(int(line[j-1]))

        for i in range(1, m+1):
            line = file.readline().strip().split()
            f = -1 if tableau[i][0].num < 0 else 1
            tableau[i][0].num *= f
            for j in range(1, n+1):
                tableau[i][j] = rnum.rationals(f*int(line[j-1]))
            for j in range(n+1, n+m+1):
                tableau[i][j] = rnum.rationals(f*(j-n == i))
            for j in range(n+m+1, n+2*m+1):
                tableau[i][j] = rnum.rationals(j-n-m == i)



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
        tableau[0][col] = rnum.rationals(1)
    # show.show(tableau)
    simplex()  
    
   
    if (tableau[0][0].num > 0):
        print("Infeasible ProbleM. Detected during simplex Phase 1")
        sys.exit()
    drive_out_auxillary()
    erase_auxillary()
    
    fill_reduced_costs()
    simplex()
    print(tableau[0][0].num/tableau[0][0].den)

    return 
    tableau[0] = cost_red


    show.show(tableau)

    #     for j in range():
    # for i in range(m):
  





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
            print("Optimal Value if +INFINITY")
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
            print("Optimal Value if -INFINITY")
            sys.exit()
        change_basis(piv_row, piv_col)
    

        



def gomory(input):
    get_input()
    simplex_phase1()
    pass




def check_dual():
    global tableau,xB
    with open('input.txt', 'r') as file:
        line = file.readline().strip().split()
        n = int(line[0])
        m = int(line[1])

        tableau = [[rnum.rationals()] * (n+m+1) for _ in range(m+1)]

        line = file.readline().strip().split()

        xB = [None]
        for i in range(1, m+1):
            tableau[i][0] = rnum.rationals(int(line[i-1]))
            xB.append(n+i)

        line = file.readline().strip().split()
        for j in range(1, n+1):
            tableau[0][j] = rnum.rationals(int(line[j-1]))
        
       
        
        for i in range(1, m+1):
            line = file.readline().strip().split()  
            for j in range(1, n+1):
                tableau[i][j] = rnum.rationals(int(line[j-1]))
            for j in range(n+1, n+m+1):
                tableau[i][j] = rnum.rationals(j-n == i)
          
    

    dual_simplex()





# gomory("heelo")

check_dual()
print(tableau[0][0].num/tableau[0][0].den)


   
# n = int(input())
# m = int(input())
# tableau = []
# for i in range (n):
#     tableau.append(input().split())
# for i in range (n):
#     for j in range (m):
#         tableau[i][j] = rnum.rationals(int(tableau[i][j]))



# xB = list(map(int, input().split()))
# print()
# print()

# xB.insert(0,None)
# simplex()
# print(xB)
# show.show(tableau)
