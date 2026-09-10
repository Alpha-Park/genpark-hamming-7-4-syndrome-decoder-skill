class Hamming74:
    """
    Hamming [7, 4] Linear Block Code Engine.
    Encodes 4 data bits into 7 code bits with single-error correction.
    """
    def encode(self, d):
        p0 = d[0] ^ d[1] ^ d[3]
        p1 = d[0] ^ d[2] ^ d[3]
        p2 = d[1] ^ d[2] ^ d[3]
        return [p0, p1, d[0], p2, d[1], d[2], d[3]]

    def decode(self, c):
        s0 = c[0] ^ c[2] ^ c[4] ^ c[6]
        s1 = c[1] ^ c[2] ^ c[5] ^ c[6]
        s2 = c[3] ^ c[4] ^ c[5] ^ c[6]
        err_pos = s0 * 1 + s1 * 2 + s2 * 4
        corrected = list(c)
        if 1 <= err_pos <= 7:
            corrected[err_pos - 1] ^= 1
        data = [corrected[2], corrected[4], corrected[5], corrected[6]]
        return data, err_pos
