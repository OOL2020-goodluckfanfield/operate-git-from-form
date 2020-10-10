## -*- coding: utf-8 -*-

import paramiko

#fileよみ込み
file = open('command.data')
ripo = file.read()

def ssh_cmd(ip, user, password, cmd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=user, password=password, port=22)
 
    stdin, stdout, stderr = client.exec_command(cmd)
 
    # 実行結果
    for o in stdout:
        print(o)
    for e in stderr:
        print(e)
    return

# cmd
ssh_cmd('XXX', 'XXX', 'XXX', 'cd /Applications/MAMP/htdocs/operate-git-from-form;git clone ' + ripo)
