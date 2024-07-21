#n = 3
#m = 2
#value = 10
#A = []
def get_matrix(n, m, value):
     matrix = []
     for i in range(n):
         matrix.append([0] * m)
         for j in range(n):
             matrix.append([value]*m)
         return(matrix)
#get_matrix(3, 2, 10)
result1 = get_matrix(2,2,10)
print(result1)
result2 = get_matrix(3,5, 42)
print(result2)
result3 = get_matrix(4,2, 13)
print(result3)
