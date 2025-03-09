import paramiko
import logging



class SFTPConnection:
    def __init__(self, host, username, password, port=22):
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.path = "/home/Discord-Bot"

        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(self.host, self.port, self.username, self.password)

        self.sftp = self.client.open_sftp()

    def list_files(self):
        files = self.sftp.listdir(self.path)
        return files
    
    def download_VPN(self):
        try :
            files = self.sftp.listdir(self.path)
            for file in files:
                if file.strip().endswith(".ovpn") :
                    self.sftp.get(f"{self.path}/{file}", f"./dl_files/{file}")
            return True
        except Exception as e:
            return False


    def close(self):
        self.sftp.close()
        self.client.close()
