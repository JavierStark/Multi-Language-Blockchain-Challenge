import datetime
import hashlib
import json

# h = hashlib.sha256()
# h.update(b"hola")
# print(h.hexdigest())

class Block:

  name = "Block"
  n_hashes = 0
  number = 0
  hash = None  
  transactions = None
  previous_block = None
  next_block = None
  timestamp = datetime.datetime.now()

  def __init__(self ,name, transactions=[]):
    self.name = name
    self.transactions = transactions
    
  
  def get_hash(self):
    self.hash = hashlib.sha256()
    hash_content = (
      str(self.name) + 
      str(self.n_hashes) +
      str(self.transactions) +
      str(self.previous_block) +
      str(self.timestamp)
    )
    
    self.hash.update(hash_content.encode("utf-8"))
      
    self.hash = self.hash.hexdigest()
    return self.hash
    
  def __str__(self):
    return (
      "Name: " + str(self.name) + 
      "\nHash: " + str(self.hash) + 
      "\nNº hashes: " + str(self.n_hashes) + 
      "\nTransactions: " + str(self.transactions) + 
      "\nPrevious block: " + str(self.previous_block) + 
      "\nTimestamp: " + str(self.timestamp) +
      "\n----------------------------------"
    )

  def to_json(self):
    return json.dumps(
      {
        "Name":self.name,
        "Hash":self.hash,
        "N_hashes":self.n_hashes,
        "Transactions":self.transactions,
        "Previous_block":self.previous_block,
        "Timestamp":str(self.timestamp)
      }, indent=4
    )

  
class Blockchain:
    diff = 15
    maxNonce = 2**32
    target = 2 ** (256-diff)

    block = Block("Genesis")
    dummy = head = block

    def add(self, block):
      block.previous_block = self.block.get_hash()
      block.blockNo = self.block.number +1

      self.block.next_block = block
      self.block = self.block.next_block

    def mine(self, block):
      for n in range(self.maxNonce):
        print(block.n_hashes, end='\r')
        if int(block.get_hash(), 16) <= self.target:
          self.add(block)
          print(str(block))
          break
        else:
          block.n_hashes += 1

    
    
blockchain = Blockchain()

for n in range(10):
  blockchain.mine(Block(("Block " + str(n+1)), [1,2,3,4,5,6]))

# Using a JSON string
# with open('json_data.json', 'w') as outfile:
#     outfile.write(json_string)
