from EzFtp2.Main.build_file_list_utils import BuildFileListUtil
from multiprocessing.dummy import Pool
import ftplib


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


    def download_file_list(self):
        file_list = self.full_file_list()
        print(file_list)
        # with ftplib.FTP(host="ftp-emea.teoco.com", user="Airtel3G", passwd="PocAg3") as ftp_con:
        # TODO : Multi threading need to apply
        with ftplib.FTP(host=self.ftp_host, user=self.ftp_id, passwd=self.ftp_pw) as ftp_con:
            for R_filename in file_list:
                print("Transferring {} ".format(R_filename))
                # TODO: Local directory is hard coded here, need to be dynamic based on input param, for a particular base_dir all the files recursively, will be downloaded at the directory provided as argument
                ftp_con.retrbinary('RETR ' + R_filename,
                                   open("{}{}".format(self.local_dir, R_filename.split('/')[-1]), 'wb').write)

##################################################################################################################################
    def download_file_list_mt(self, file_list):
        # file_list = self.full_file_list()
        print(file_list)
        # with ftplib.FTP(host="ftp-emea.teoco.com", user="Airtel3G", passwd="PocAg3") as ftp_con:
        # TODO : Multi threading need to apply
        with ftplib.FTP(host=self.ftp_host, user=self.ftp_id, passwd=self.ftp_pw) as ftp_con:
            for R_filename in file_list:
                print("Transferring {} ".format(R_filename))
                # TODO: Local directory is hard coded here, need to be dynamic based on input param, for a particular base_dir all the files recursively, will be downloaded at the directory provided as argument
                ftp_con.retrbinary('RETR ' + R_filename,
                                   open("{}{}".format(self.local_dir, R_filename.split('/')[-1]), 'wb').write)


    def mt_download(self):
        file_list = self.full_file_list()
        p = Pool(20)
        p.map(self.download_file_list_mt, file_list)
