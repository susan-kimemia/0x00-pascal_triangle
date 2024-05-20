#!/usr/bin/python3
"""
UTF-8 Validation Module
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data: A list of integers representing 1 byte of data each.

    Returns:
        True if data is a valid UTF-8 encoding, else False.
    """
    # number of bytes in the current UTF-8 character
    num_bytes = 0

    for byte in data:
        # checking if this is the start of a new character
        if num_bytes == 0:
            # count the number of leading ones in the byte
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask >>= 1

            # if the bytes starts with invalid UTF sequence
            if num_bytes == 0:
                continue

            # for mutiple-byte characters, num_bytes should bebetween 1 and 4
            if num_bytes == 1 or num_bytes > 4:
                return False

        else:
            # If the byte is not in the format 10xxxxxx, return False
            if not (byte & 0b10000000 and not byte & 0b01000000):
                return False

        num_bytes -= 1

    # If there are remaining bytes at the end
    return num_bytes == 0
