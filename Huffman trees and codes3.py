import heapq
from collections import defaultdict, Counter

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    frequency = Counter(text)
    priority_queue = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(priority_queue)
    
    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged_node = HuffmanNode(None, left.freq + right.freq)
        merged_node.left = left
        merged_node.right = right
        heapq.heappush(priority_queue, merged_node)

    return priority_queue[0]

def encode_huffman_tree(node, code, huffman_codes):
    if node is None:
        return
    if node.char is not None:
        huffman_codes[node.char] = code
        return
    encode_huffman_tree(node.left, code + "0", huffman_codes)
    encode_huffman_tree(node.right, code + "1", huffman_codes)

def huffman_encoding(text):
    if len(text) == 0:
        return "", None

    root = build_huffman_tree(text)
    huffman_codes = {}
    encode_huffman_tree(root, "", huffman_codes)

    encoded_text = ''.join(huffman_codes[char] for char in text)
    return encoded_text, root

def huffman_decoding(encoded_text, root):
    if len(encoded_text) == 0:
        return ""

    decoded_text = ""
    current_node = root
    for bit in encoded_text:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            decoded_text += current_node.char
            current_node = root

    return decoded_text

# Contoh penggunaan:
text = "hello world"
encoded_text, tree = huffman_encoding(text)
print("Encoded text:", encoded_text)
decoded_text = huffman_decoding(encoded_text, tree)
print("Decoded text:", decoded_text)
