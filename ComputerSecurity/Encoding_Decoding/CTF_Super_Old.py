from pwn import *
from textwrap import wrap
import base64

def main():
    flag = ''

    ascii_upper_s = 65
    ascii_upper_nd = 91 # +1 to include 90 (A - Z)
    ascii_lower_s = 97
    ascii_lower_nd = 123 # +1 to include 122 (a - z)

    upper = range(ascii_upper_s, ascii_upper_nd)
    lower = range(ascii_lower_s, ascii_lower_nd)

    

    try:
        with open("/home/machineName/Documents/Computer_Sec/file.enc", "r") as text_File:
            for line in text_File:
                new_line = base64.b64decode(line)
                print(new_line)
                for character in new_line:
                    flag += "c"


    except IOError as file_Error:
        print(file_Error)

main()
