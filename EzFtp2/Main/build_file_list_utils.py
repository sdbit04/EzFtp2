import ftplib
import datetime
import fnmatch
"""
Assumption all the files matching the downloading pattern are not older than 1 year 
"""

class BuildFileListUtil(object):


    @staticmethod
    def get_dir_list_ftp_server(base_dir):
        Dir_list = []
        with ftplib.FTP(host="ftp-emea.teoco.com", user="Airtel3G", passwd="PocAg3") as ftp_con:
            ftp_con.cwd(base_dir)
            # Swapan: In the line below split was not working correctly with maxsplit, later I explicitly mark the x as string then it work correct
            ftp_con.retrlines('LIST', lambda x='': Dir_list.append(x.split(maxsplit=8)))
            ftp_con.close()
        return base_dir, Dir_list

    @staticmethod
    def mon2mm(mon=''):
        if mon.lower() == 'jan':
            return 1
        elif mon.lower() == 'feb':
            return 2
        elif mon.lower() == 'mar':
            return 3
        elif mon.lower() == 'apr':
            return 4
        elif mon.lower() == 'may':
            return 5
        elif mon.lower() == 'jun':
            return 6
        elif mon.lower() == 'jul':
            return 7
        elif mon.lower() == 'aug':
            return 8
        elif mon.lower() == 'sep':
            return 9
        elif mon.lower() == 'oct':
            return 10
        elif mon.lower() == 'nov':
            return 11
        else:
            return 12

    # We will run the following method for each dir or file obtained from ftp server
    @staticmethod
    def dir_checker(base_dir, each_dir_attrbt_list=[], file_list_to_downloaed=[],
                    retention_minutes = 60,
                    file_pattern="*.*"):
        oldest_time_under_retention = (datetime.datetime.now() - datetime.timedelta(minutes=retention_minutes))
        if each_dir_attrbt_list[0].startswith('d'):
            # TODO: base_dir_name has become hard-coded by initial base-dir name, need to improve, done
            base_dir_name, sub_dir_list_with_attributes = BuildFileListUtil.get_dir_list_ftp_server(
                base_dir + '/' + each_dir_attrbt_list[-1])
            # print(base_dir_name, end = "\t")
            # print(sub_dir_list_with_attributes)
            for sub_dir_attribute in sub_dir_list_with_attributes:
                BuildFileListUtil.dir_checker(base_dir_name, sub_dir_attribute, file_list_to_downloaed, retention_minutes,
                            file_pattern)
        else:
            #         TODO: In case of file we need to do multiple tasks till ftp download
            #         TODO: Here we will check if the file matching pattern then only be appended to list
            #         TODO: Here we will check time stamp of the file before appending into download list
            # ['-rw-rw----', '1', 'Airtel3G', 'ftpuser', '8746', 'Aug', '22', '09:51', 'test6.xlsx']
            if fnmatch.fnmatch(each_dir_attrbt_list[-1], pat=file_pattern):
                # file_time =
                # print(each_dir_attrbt_list)
                file_time = datetime.datetime(2018, BuildFileListUtil.mon2mm((each_dir_attrbt_list[5])), int(each_dir_attrbt_list[6]),
                                              int(each_dir_attrbt_list[7].split(':')[0]),
                                              int(each_dir_attrbt_list[7].split(':')[1]), second=00, microsecond=0000)
                if file_time > oldest_time_under_retention:
                    # print(each_dir_attrbt_list[-1])
                    each_dir_attrbt_list[-1] = base_dir + "/" + each_dir_attrbt_list[-1]
                    file_list_to_downloaed.extend(each_dir_attrbt_list[-1:])

        return file_list_to_downloaed

