from EzFtp2.Main.build_file_list_utils import BuildFileListUtil
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
        super().__init__(ftp_host, ftp_id, ftp_pw)

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
                print("Downloading file : {}".format(R_filename.split('/')[-1]))
                # print("downloading at {}\{}".format(self.local_dir, R_filename.split('/')[-1]))
                # ftp_con.retrbinary("RETR" + file, open("{}\{}".format(self.local_dir, file.split('/')[-1]), 'wb').write)
                ftp_con.retrbinary('RETR ' + R_filename,
                                   open("{}\{}".format(self.local_dir, R_filename.split('/')[-1]), 'wb').write)

