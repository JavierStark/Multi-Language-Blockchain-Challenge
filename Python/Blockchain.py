import datetime
import hashlib
import json
import os
from collections import namedtuple


def clear_console():
    os.system("cls")


# --------------------------------------------------

def block_decoder(block_dict):
    return namedtuple('block', block_dict.keys())(*block_dict.values())

class Block:

    name = "Block"
    n_hashes = 0
    number = 0
    hash = None
    transactions = None
    previous_block = None
    timestamp = datetime.datetime.now()

    def __init__(self, name, transactions=[]):
        self.name = name
        self.transactions = transactions

    def get_hash(self):
        self.hash = hashlib.sha256()
        hash_content = (
            str(self.name)
            + str(self.n_hashes)
            + str(self.transactions)
            + str(self.previous_block)
            + str(self.timestamp)
        )

        self.hash.update(hash_content.encode("utf-8"))

        self.hash = self.hash.hexdigest()
        return self.hash

    def __str__(self):
        return (
            "Name: "
            + str(self.name)
            + "\nHash: "
            + str(self.hash)
            + "\nNº hashes: "
            + str(self.n_hashes)
            + "\nTransactions: "
            + str(self.transactions)
            + "\nPrevious block: "
            + str(self.previous_block)
            + "\nTimestamp: "
            + str(self.timestamp)
            + "\n----------------------------------"
        )

    def to_json(self):
        return {
                "name": str(self.name),
                "hash": str(self.get_hash()),
                "n_hashes": str(self.n_hashes),
                "number": str(self.number),
                "transactions": str(self.transactions),
                "previous_block": str(self.previous_block),
                "timestamp": str(self.timestamp),
              }


class Blockchain:
    diff = 15
    maxNonce = 2**32
    target = 2 ** (256 - diff)

    blockchain_list = None
    last = None

    def __init__(self):
        with open("blockchain.json") as blockchain_file:
          self.blockchain_list = json.load(blockchain_file)
        if len(self.blockchain_list) == 0:
          initial_block = Block("Genesis", [])
          self.last = initial_block
          self.add(initial_block)
        else:
          self.last = block_decoder(self.blockchain_list[-1])

    def add(self, block):
        block.previous_block = self.last.hash
        block.blockNo = int(self.last.number) + 1

        self.blockchain_list.append(block.to_json())

        with open("blockchain.json", 'w') as blockchain_file:
          json.dump(self.blockchain_list, blockchain_file)

    def mine(self, block):
        for n in range(self.maxNonce):
            print(block.n_hashes, end="\r")
            if int(block.get_hash(), 16) <= self.target:
                self.add(block)
                current_user.balance += 15
                print(str(block))
                break
            else:
                block.n_hashes += 1
        with open("user.json", "+") as user_file:
            user_dic = json.load(user_file)
            for i in user_dic:
                if i["name"] == current_user.name:
                  i["balance"] = current_user.balance
            user_file.write(json.dumps(user_str))
            

# --------------------------------------------------


def enter_account():
    clear_console()

    option = input("Register or Login (R/L) ")
    option = str(option).lower()
    clear_console()
    if option == "l":
        login()
    else:
        register()


def login():
    clear_console()
    print("----Login----\n")
    name = input("Enter username: ")
    password = input("Enter password: ")
    user = {"name": name, "password": password}
    users = None

    with open("users.json") as file:
        json_file = json.load(file)
        users = json_file
#BALANCE IS NOT TAKED INTO ACCOUNT HERE
    if user in users:
        global current_user
        current_user = user
    else:
        enter_account()


def register():
    clear_console()
    print("----Register----\n")
    name = input("Enter username: ")
    password = input("Enter password: ")
    user = {"name": name, "password": password, "balance":0}
    if input("Enter password again: ") != password:
        register()
    else:
        add_user(user)
        login()


def add_user(user):
    users = None
    with open("users.json", "r") as file:
        json_file = json.load(file)
        users = json_file

    if user in users:
        register()

    with open("users.json", "w") as file:
        users.append(user)
        file.write(json.dumps(users, indent=4))


# --------------------------------------------------


def interface():
    clear_console()
    print("----Menu----\n")

    print("1. Show blockchain")
    print("2. Make transaction")
    print("3. Mine blocks")

    option = input("\nEnter option number: ")
    option = int(option)
    if option == 1:
        show_blockchain()

    if option == 2:
       make_transaction()

    if option == 3:
        mine_blocks()



def show_blockchain():
    with open("blockchain.json") as blockchain_file:
        blockchain = json.load(blockchain_file)
        blockchain = json.dumps(blockchain, indent=2)
        print(blockchain)

def mine_blocks():
    clear_console()
    print("----Mining----")
    n_blocks = input("Number of blocks to mine: ")
    for n in range(int(n_blocks)):
        block = Block("Block", get_transactions_from_pending)
        blockchain.mine(block)

def get_transactions_from_pending():
    return []

def make_transaction():
    print("transaction")    
    pass




def main():
    global blockchain
    blockchain = Blockchain()
    enter_account()
    interface()
    # for n in range(10):
    #     blockchain.mine(Block(("Block " + str(n + 1)), [1, 2, 3, 4, 5, 6]))

    # Using a JSON string
    # with open("pending_transactions.json") as transactions_file:
    #     y = json.load(transactions_file)
    #     print(y["transactions"][1])


if __name__ == "__main__":
    main()
