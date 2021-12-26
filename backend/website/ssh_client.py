from paramiko import SSHClient, AutoAddPolicy

client = SSHClient()
client.set_missing_host_key_policy(AutoAddPolicy())
#client.load_host_keys('C:/Users/motoc/.ssh/known_hosts')
#client.load_system_host_keys()
client.connect('192.168.1.218', 5022, 'hilbert', key_filename='C:/Users/motoc/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup')

stdin, stdout, stderr = client.exec_command('ls -la')
print(f'stdout: {stdout.read().decode("utf8")}')
print(f'stderr: {stderr.read().decode("utf8")}')

client.close()