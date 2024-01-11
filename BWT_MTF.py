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

# Example Usage
input_text = "your_input_text_here"

# Apply BWT
bwt_result = bwt(input_text)

# Apply MTF
mtf_result = mtf_encode(bwt_result)

# Calculate metrics
original_size = len(input_text) * 8  # Assuming 8 bits per character
compressed_size = len(mtf_result) * 4  # Assuming 4 bits per MTF index
compression_factor = original_size / compressed_size

# Print the results
print("Input Text:", input_text)
print("BWT Result:", bwt_result)
print("MTF Result:", mtf_result)
print("\nMetrics:")
print("Original Size (bits):", original_size)
print("Compression Size (bits):", compressed_size)
print("Compression Factor:", compression_factor)
