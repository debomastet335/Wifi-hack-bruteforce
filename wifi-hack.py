from subprocess import check_output
output = check_output('netsh wlan connect SBHG-adm', shell=True)

print output
