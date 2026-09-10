from client import Hamming74

def main():
    print("=== Testing Hamming [7, 4] Syndrome Decoder ===")
    ham = Hamming74()
    data = [1, 0, 1, 1]
    enc = ham.encode(data)
    print("Encoded codeword:", enc)
    assert len(enc) == 7

    # Corrupt bit index 2 (1-based index 3)
    enc[2] ^= 1
    rec_d, err_pos = ham.decode(enc)
    print(f"Decoded data: {rec_d}, Detected error position: {err_pos}")
    assert err_pos == 3
    assert rec_d == data
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
