class Disk():
  def __init__(self, total, used):
    self.__total = total
    self.__used = used
    
  @property
  def free(self):
    return self.__total - self.__used
  
  def __repr__(self):
    return f'Disk[total: {self.__total} Gb, used: {self.__used} Gb]'
  
  def __lt__(self, other):
    if not isinstance(other, Disk):
      return NotImplemented
    return (self.__used / self.__total) < (other.__used / other.__total)
  
  
if __name__ == '__main__':
  disk = Disk(50,30)
  print(disk) 
  print(disk.free) # 20
  
  disk_array = [Disk(128,30), Disk(512,86), Disk(256,212)]
  print(sorted(disk_array))
  