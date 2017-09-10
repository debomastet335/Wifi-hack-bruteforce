from subprocess import check_output
import os

xmlfile = open("D:\Wi-Fi-telenet-6101F.xml")

with open('D:\Wi-Fi-telenet-6101F.xml', 'r') as input_file, open('D:\Wi-Fi-telenet-6101Fnew.xml', 'w') as output_file:
    for line in input_file:
        if 'keyMaterial' in line:
            output_file.write('				<keyMaterial>Heyhoegaathetmetjou</keyMaterial>\n')
        else:
            output_file.write(line)

os.popen('netsh wlan add profile filename="D:\Wi-Fi-telenet-6101Fnew.xml"')
output = check_output('netsh wlan connect SBHG-adm', shell=True)

print output
