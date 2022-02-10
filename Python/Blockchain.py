import datetime
import hashlib

# h = hashlib.sha256()
# h.update(b"hola")
# print(h.hexdigest())

class Block:

  name = "Block"
  number = 0
  hash = None  
  transactions = None
  previous_block = None
  timestamp = datetime.datetime.now()

  def __init__(self ,name, transactions, prev=None):
    self.name = name
    self.transactions = transactions    
    if prev != None:
      self.previous_block = prev
    
  
  def create_hash(self):
    self.hash = hashlib.sha256()
    hash_content = 
      str(self.name) + 
      str(number) +
      str(self.transactions) +
      str(previous_block) +
      str(timestamp)
    
    self.hash.update(hash_content.encode("utf-8"))
      
    self.hash = self.hash.hexdigest()
    
  def __str__(self):
    return self.name + "\n" + str(self.hash)
  
class Blockchain:
    diff = 20
    maxNonce = 2**32
    target = 2 ** (256-diff)

    block = Block("Genesis")
    dummy = head = block
    

block = Block("block 1",[1,1,2,6,5])
block.create_hash()
print(str(block))
