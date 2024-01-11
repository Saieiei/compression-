import heapq
from collections import defaultdict

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
    freq_dict = defaultdict(int)
    for char in text:
        freq_dict[char] += 1
    
    huffman_tree = build_huffman_tree(freq_dict)
    
    huffman_codes = {char: code for char, code in huffman_tree}
    
    encoded_text = ''.join(huffman_codes[char] for char in text)
    
    original_size = len(text) * 8  # Assuming 8 bits per character
    compressed_size = sum(freq_dict[char] * len(huffman_codes[char]) for char in freq_dict)
    
    compression_factor = original_size / compressed_size
    
    return huffman_codes, encoded_text, original_size, compressed_size, compression_factor

if __name__ == "__main__":
    input_text = "your_input_text_here"
    
    huffman_codes, encoded_text, original_size, compressed_size, compression_factor = huffman_coding(input_text)
    
    # Print the results
    print("Input Text:", input_text)
    print("Huffman Codes:", huffman_codes)
    print("Encoded Text:", encoded_text)
    print("\nMetrics:")
    print("Original Size (bits):", original_size)
    print("Compression Size (bits):", compressed_size)
    print("Compression Factor:", compression_factor)
