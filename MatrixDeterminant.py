from copy import deepcopy
    
def productOf2x2Matrix(matrix):
    sum = 0
    sum += matrix[0][0] * matrix[1][1]
    sum -= matrix[0][1] * matrix[1][0]
    return sum

def determinant(matrix):
    sum = 0
    if len(matrix) == 1:
        return int(str(matrix)[2:-2])  
    elif len(matrix) == 2:
        return productOf2x2Matrix(matrix)
    elif len(matrix) > 2:
        for i, val in enumerate(matrix): 
            tempArray = deepcopy(matrix)
            if i % 2 == 0: 
                for j in range(len(tempArray)):
                    tempArray[j].pop(i)
                tempArray.pop(0)
                sum += matrix[0][i] * determinant(tempArray)
            else:
                for j in range(len(tempArray)):
                    tempArray[j].pop(i)
                tempArray.pop(0)
                sum -= matrix[0][i] * determinant(tempArray)  
    return sum
