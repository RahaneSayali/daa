import heapq

class HuffmanNode:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ""
        
    def __lt__(self, other):
        return self.freq < other.freq
    
def printNode(node, val=""):
    newnode = val + node.huff
    if node.left:
        printNode(node.left, newnode)
    if node.right:
        printNode(node.right, newnode)
    if not node.left and not node.right:
        print(f"{node.symbol} -> {newnode}")
    
def main():
    symbols = ["a", "b", "c", "d", "e", "f"]
    freqs = [50, 10, 30, 5, 3, 2]
    
    # Priority queue
    huffman_nodes = []
    
    for i in range(len(symbols)):
        node = HuffmanNode(freqs[i], symbols[i])
        heapq.heappush(huffman_nodes, node)
    
    while len(huffman_nodes) > 1:
        left = heapq.heappop(huffman_nodes)
        right = heapq.heappop(huffman_nodes)
        
        left.huff = "0"
        right.huff = "1"
        
        newnode = HuffmanNode(left.freq + right.freq, left.symbol + right.symbol, left, right)
        heapq.heappush(huffman_nodes, newnode)
        
    printNode(huffman_nodes[0])

if __name__ == "__main__":
    main()
