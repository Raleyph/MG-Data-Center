from ftplib import FTP
import logs

ftp = FTP("url")


# подключение к ftp серверу
def ftp_connect(login, password):
    try:
        ftp.login(login, password)
    except:
        logs.add_log("[FTP] Failed connection to FTP server", "CRITICAL")
        return 0


# загрузка файла на сервер
def upload_file(file_name, file_path):
    try:
        file = open(file_path, "wb")
        ftp.storbinary(file_name, file.write, 1024)
        file.close()
        logs.add_log(f"[FTP] User sucessful upload file {file_name}", "INFO")
    except:
        logs.add_log(f"[FTP] File upload error", "ERROR")
        return 0


# скачивание файла с сервера
def download_file(file_name):
    try:
        ftp.storbinary(file_name, open(file_name), 1024)
        logs.add_log(f"[FTP] User sucessful download file {file_name}", "INFO")
    except:
        logs.add_log(f"[FTP] File download error", "ERROR")
        return 0


# удаление файла на сервере
def delete_file(file_name):
    try:
        ftp.delete(file_name)
    except:
        logs.add_log(f"[FTP] File delete error", "ERROR")
        return 0

