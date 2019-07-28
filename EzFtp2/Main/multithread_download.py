import time
import ftplib
from threading import *


def download_files_1(file_list):
    with ftplib.FTP(host='ftp-emea.teoco.com', user="Airtel3G", passwd="PocAg3") as ftp_con:
        for R_filename in file_list:
            print("{}\{}".format(r'E:\Python\Developement\EzFtp2\EzFtp2\Data_in', R_filename.split('/')[-1]))
            # ftp_con.retrbinary("RETR" + file, open("{}\{}".format(self.local_dir, file.split('/')[-1]), 'wb').write)
            ftp_con.retrbinary('RETR ' + R_filename,
                               open("{}\{}".format(r'E:\Python\Developement\EzFtp2\EzFtp2\Data_in',
                                                   R_filename.split('/')[-1]), 'wb').write)


def atest():
    for i in range(10):
        time.sleep(1)
        print(i)


def atest1():
    for i in range(100, 110):
        print(i)
        time.sleep(1)


def atest2():
    for i in range(10):
        print(i)
        time.sleep(1)


if __name__ == "__main__":

    files_list = ['/Swapan/testfiles/4.xlsx', '/Swapan/testfiles/a.txt', '/Swapan/testfiles/b.txt',
                  '/Swapan/testfiles/c.pub', '/Swapan/testfiles/d.rtf', '/Swapan/testfiles/f.accdb',
                  '/Swapan/testfiles/f.docx', '/Swapan/testfiles/g.bmp', '/Swapan/testfiles/g.docx',
                  '/Swapan/testfiles/j.docx']

    start_time = time.time()
    # download_files_1(files_list)
    # """"
    t1 = Thread(target=download_files_1, args=[files_list[0:3]])
    t2 = Thread(target=download_files_1, args=[files_list[3:6]])
    t3 = Thread(target=download_files_1, args=[files_list[6:9]])
    t4 = Thread(target=download_files_1, args=[files_list[9:-1]])

    t2.start()
    t3.start()
    t4.start()
    t1.start()
    print(active_count())
    t1.join()
    t2.join()
    t3.join()
    t4.join()

    # """
    print("Elapsed time = {}".format(time.time()-start_time))


