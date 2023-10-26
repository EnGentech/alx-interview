#!/usr/bin/python3
""" 0-validate_utf8.py """


def validUTF8(data):
    """
    Determines if a given data set is a valid utf-8 encoding
    """
    leading_bytes = 0

    for item in data:
        if leading_bytes == 0:
            if (item >> 7) == 0:
                leading_bytes = 0
            elif (item >> 5) == 0b110:
                leading_bytes = 1
            elif (item >> 4) == 0b1110:
                leading_bytes = 2
            elif (item >> 3) == 0b11110:
                leading_bytes = 3
            else:
                return False
        else:
            if (item >> 6) != 0b10:
                return False
            leading_bytes -= 1

    return leading_bytes == 0
