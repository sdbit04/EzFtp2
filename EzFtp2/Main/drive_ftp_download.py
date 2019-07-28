from EzFtp2.Main.build_file_list import *
from multiprocessing import Process
import json

if __name__ == "__main__":

# TODO: Load data from a json file into a dictionary object, that will be input to the process
    with open("E:\\Python\\Developement\\Utilities\\EzFtp2\\EzFtp2\\Data\\ftp_input_file", "r") as input_file:
        input_param = json.load(input_file)


    object_list =[]
    for param in input_param.keys():
        BuildListAndDownload = BuildFileList(base_dir=input_param[param]["base_dir"], retention=input_param[param]["retention"], pattern=input_param[param]["pattern"], local_directory=input_param[param]["local_directory"], ftp_host=input_param[param]["ftp_host"], ftp_id=input_param[param]["ftp_id"], ftp_pw=input_param[param]["ftp_pw"])
        print(type(BuildListAndDownload))
        print(BuildListAndDownload)
        print(BuildListAndDownload.pattern)
        object_list.append(BuildListAndDownload)
    #     BuildListAndDownload.download_file_list()

    # for object_item in object_list:
    #     object_item.mt_download()

