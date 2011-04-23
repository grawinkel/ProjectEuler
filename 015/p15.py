'''
Created on 20.04.2011

Solution to http://projecteuler.net/index.php?section=problems&id=15
@author: meatz
'''


def dump(matrix):
    for row in matrix:
        print row
        
            
if __name__ == '__main__':
    
    size=21
    matrix = [[0 for col in range(size)] for row in range(size)]
    
    for i in range(1,size):
        matrix[0][i]=1
        matrix[i][0]=1
        
    for y in range(1,size):
        for x in range(1,size):
            matrix[x][y]= matrix[x-1][y] + matrix[x][y-1]
    
    dump(matrix)
    
    print matrix[size-1][size-1]