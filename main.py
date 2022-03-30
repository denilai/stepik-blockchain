import json
import hashlib as hl
import typing
complexity = 1
blocks_name = 'stepik-block'

def write_to_file(filepath:str, string):
    with open(filepath, 'w') as file:
        file.write(string)

def write_block_to_file(block):
    filepath=block["file"]
    write_to_file(filepath, str(json.dumps(block, sort_keys=True, indent=4))) 

def generate_block(number, last_one, mercls_tree, filepath):  # Генерируем новый блок
    global complexity, blocks_name
    if last_one is None:
        hash_last_one = None
    else:
        hash_last_one = last_one["hash"]
    name = blocks_name
    block_name = name + str(number)
    block = {
        "number": number,
        "name": block_name,
        "file": filepath,
        "nonce": 0,
        "hash_last_one": hash_last_one,
        'transactions_mercls_tree': mercls_tree,
        "complexity": complexity
    }
    hash = hl.sha256(str(block).encode()).hexdigest()
    while hash[0:complexity] != '0' * complexity:
        block['nonce'] += 1
        hash = hl.sha256(str(block).encode()).hexdigest()
    block['hash'] = hash
    # print(json.dumps(block, indent=4))
    return block

if __name__ == "__main__":
    print(json.dumps(generate_block(0, None, None, "default.txt"), indent = 4))
    write_to_file("output.txt", str(json.dumps(generate_block(1, None, None, "default.txt"), sort_keys=True, indent=4)))
