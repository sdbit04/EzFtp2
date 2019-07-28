from EzFtp2.Main.build_file_list_utils import BuildFileListUtil
import ftplib
import time
from threading import *

class BuildFileList(BuildFileListUtil):

    def __init__(self, base_dir='', retention=0, pattern="*.*", local_directory='', ftp_host='', ftp_id='', ftp_pw=''):
        self.base_dir = base_dir
        self.retention = retention
        self.pattern = pattern
        self.local_dir = local_directory
        self.ftp_host = ftp_host
        self.ftp_id = ftp_id
        self.ftp_pw = ftp_pw

    def full_file_list(self):
        base_dir_name, all_dir_attribute_list = self.get_dir_list_ftp_server(self.base_dir)
        # print(all_dir_attribute_list)
        # input("Wait and see the all dir attributes list, and press any key to proceed")
        full_list = []
        print(full_list)
        # oldest_time_under_retention = (datetime.datetime.now() - datetime.timedelta(minutes=look_back_minuts))
        for each_dir_attribute_list in all_dir_attribute_list:
            # The next line is working correctly, but it shouldn't, need to check later
            full_list.extend(self.dir_checker(base_dir_name, each_dir_attribute_list, retention_minutes=self.retention, file_pattern=self.pattern))
        # pool_object = Pool()
        # pool_object.map(download_file_list, full_list)
        return full_list

    def download_files(self, file_list):
        with ftplib.FTP(host=self.ftp_host, user="Airtel3G", passwd="PocAg3") as ftp_con:
            for R_filename in file_list:
                print("{}\{}".format(self.local_dir, R_filename.split('/')[-1]))
                # ftp_con.retrbinary("RETR" + file, open("{}\{}".format(self.local_dir, file.split('/')[-1]), 'wb').write)
                ftp_con.retrbinary('RETR ' + R_filename,
                                   open("{}\{}".format(self.local_dir, R_filename.split('/')[-1]), 'wb').write)


if __name__ == "__main__":
    bfl = BuildFileList(base_dir='/Swapan', retention=600, pattern="*.*", local_directory=r'E:\Python\Developement\EzFtp2\EzFtp2\Data_in', ftp_host='ftp-emea.teoco.com', ftp_id='Airtel3G', ftp_pw='PocAg3')
    files_list = bfl.full_file_list()
    print(files_list)

    def download_files_1(file_list):
        with ftplib.FTP(host='ftp-emea.teoco.com', user="Airtel3G", passwd="PocAg3") as ftp_con:
            for R_filename in file_list:
                print("{}\{}".format(r'E:\Python\Developement\EzFtp2\EzFtp2\Data_in', R_filename.split('/')[-1]))
                # ftp_con.retrbinary("RETR" + file, open("{}\{}".format(self.local_dir, file.split('/')[-1]), 'wb').write)
                ftp_con.retrbinary('RETR ' + R_filename,open("{}\{}".format(r'E:\Python\Developement\EzFtp2\EzFtp2\Data_in', R_filename.split('/')[-1]), 'wb').write)

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
