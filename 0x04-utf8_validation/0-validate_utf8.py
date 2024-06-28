#!/usr/bin/python3
"""UTF-8 validation module.
"""


def validUTF8(data):
    """Checks if a list of integers are valid UTF-8 codepoints."""
    def check_continuation_bytes(start, num_bytes):
        """Checks continuation bytes UTF-8 codepoints."""
        for i in range(start + 1, start + num_bytes):
            if i >= len(data) or (data[i] & 0b11000000) != 0b10000000:
                return False
        return True
    i = 0
    while i < len(data):
        byte = data[i]
        if (byte & 0b10000000) == 0:
            # 1-byte character (0xxxxxxx)
            i += 1
        elif (byte & 0b11100000) == 0b11000000:
            # 2-byte character (110xxxxx 10xxxxxx)
            if not check_continuation_bytes(i, 2):
                return False
            i += 2
        elif (byte & 0b11110000) == 0b11100000:
            # 3-byte character (1110xxxx 10xxxxxx 10xxxxxx)
            if not check_continuation_bytes(i, 3):
                return False
            i += 3
        elif (byte & 0b11111000) == 0b11110000:
            # 4-byte character (11110xxx 10xxxxxx 10xxxxxx 10xxxxxx)
            if not check_continuation_bytes(i, 4):
                return False
            i += 4
        else:
            return False
    return True
