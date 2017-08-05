import block
import blockchain

chain = blockchain.Blockchain()

first = block.Block('first')
second = block.Block('second')
third = block.Block('third')
fourth = block.Block('fourth')

chain.add_block(first)
chain.add_block(second)
chain.add_block(third)
chain.add_block(fourth)

third.update_data('new content')

print(chain.broken)  # True

chain.repair()

print(chain.broken)  # False