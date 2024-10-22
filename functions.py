
# Fonction several_zeros

def several_zeros():
  zero_list = []
  for i in range(10):
    zero_list.append(0)
  return zero_list
  
# Fonction several_zeros_custom

def several_zeros_custom(nb_zero = 10):
  zero_list = []
  for i in range(nb_zero):
    zero_list.append(0)
  return zero_list

# Fonction matrix

def matrix(rows, cols):
  mat = []
  for i in range (rows):
    row = []
    for j in range (cols):
      row.append(0)
      
    mat.append(row)
    
  return mat
 
# Objet matrix

class Matrix():
  def __init__(self, rows, cols):
    self.rows = rows
    self.cols = cols
    self.__mat = matrix(rows, cols)
    
  def __repr__(self) -> str:
    return str(self.__mat)

  def get_value(self, row, col):
    return int(self.__mat[row][col])
  
  def __eq__(self, other):
    return self.__mat == other.__mat
  
  
# Fonction sort


def my_sort(my_list: [int]) -> [int]:
  new_list = my_list.copy()
  n = len(new_list)
  
  for i in range (n - 1):
    for j in range (0, n - i - 1):
      if new_list[j] > new_list[j+1]:
        new_list[j], new_list[j+1] = new_list[j+1], new_list[j]
        
  return new_list




if __name__ == '__main__':
  print(several_zeros())
  print(several_zeros_custom())
  print(matrix(2,3))
  print(Matrix(2,3))
  print(Matrix(2,3).get_value(1,2))
  print(Matrix(2,3) == Matrix(2,3))
  random_list = [45,12,98,53,77,40,21,8,33,45]
  sort_list = my_sort(random_list)
  print(random_list)
  print(sort_list)
  print("Le nom de cet algorithme est Bubble Sort")
  
  
