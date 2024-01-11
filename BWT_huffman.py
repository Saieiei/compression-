import heapq
from collections import defaultdict
import lz4.frame

def bwt(text):
    rotations = [text[i:] + text[:i] for i in range(len(text))]
    sorted_rotations = sorted(rotations)
    bwt_result = ''.join(rotation[-1] for rotation in sorted_rotations)
    return bwt_result

def mtf_encode(text):
    alphabet = list(set(text))
    encoded_text = []
    
    for char in text:
        char_index = alphabet.index(char)
        encoded_text.append(char_index)
        # Move the char to the front of the alphabet
        alphabet.pop(char_index)
        alphabet.insert(0, char)
    
    return encoded_text

class HuffmanNode:
    def __init__(self, char, frequency):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

def build_huffman_tree(freq_dict):
    heap = [[weight, [char, ""]] for char, weight in freq_dict.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    
    return heap[0][1:]

def huffman_coding(text):
    frequency_dict = defaultdict(int)
    
    for char in text:
        frequency_dict[char] += 1
    
    huffman_tree = build_huffman_tree(frequency_dict)
    huffman_codes = {char: code for char, code in huffman_tree}
    
    encoded_text = ''.join(huffman_codes[char] for char in text)
    
    return encoded_text, huffman_codes

# Example Usage
input_text = "your_input_text_here"

# Apply BWT
bwt_result = bwt(input_text)

# Apply MTF
mtf_result = mtf_encode(bwt_result)

# Convert MTF result to string for Huffman coding
mtf_result_str = ''.join(map(str, mtf_result))

# Apply Huffman Coding
encoded_text, huffman_codes = huffman_coding(mtf_result_str)

# Calculate metrics
original_size = len(input_text) * 8  # Assuming 8 bits per character
compressed_size = len(encoded_text)
compression_factor = original_size / compressed_size

# Print the results
print("Input Text:", input_text)
print("BWT Result:", bwt_result)
print("MTF Result:", mtf_result)
print("Huffman Codes:", huffman_codes)
print("Encoded Text:", encoded_text)
print("\nMetrics:")
print("Original Size (bits):", original_size)
print("Compression Size (bits):", compressed_size)
print("Compression Factor:", compression_factor)
