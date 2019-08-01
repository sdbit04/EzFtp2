from EzFtp2.Main.final_list import *
import time
from threading import *


def check_run_time_thread_count():
    while True:
        AC = active_count()
        if AC <= 1:
            break
        else:
            print("{} Threads are running".format(AC))
            time.sleep(2)


def drive_the_download(base_dir, retention, pattern, local_directory, ftp_host, ftp_id, ftp_pw):
    base_dir = base_dir
    retention = retention
    pattern = pattern
    local_directory = local_directory
    ftp_host = ftp_host
    ftp_id = ftp_id
    ftp_pw = ftp_pw
    # TODO Create the object based on input parameters stored into xls.x file
    bfl = BuildFileList(base_dir, retention, pattern,
                        local_directory,
                        ftp_host, ftp_id, ftp_pw)
    files_list = bfl.full_file_list()
    print(files_list)

    start_time = time.time()
    files_per_thread = 3
    file_count = len(files_list)
    thread_count =0
    files_in_additional_thread = 0
    if file_count > files_per_thread:
        thread_count = file_count // files_per_thread
        files_in_additional_thread = file_count % files_per_thread

    threads_list = []
    for i in range(1,thread_count):
        threads_list.append(Thread(target=bfl.download_files, args=[files_list[i*files_per_thread:i*files_per_thread + files_per_thread]]))

    additional_thread = None
    if files_in_additional_thread > 0:
        additional_thread = Thread(target=bfl.download_files, args=[files_list[files_per_thread * thread_count:-1]])

    for thread in threads_list:
        thread.start()
    additional_thread.start()

    check_run_time_thread_count()

    for thread in threads_list:
        thread.join()
    additional_thread.join()

    print("Elapsed time = {}".format(time.time() - start_time))


if __name__ == "__main__":
    job1 = ['/Swapan', 86400, "*.*", r'D:\D_drive_BACKUP\Study\PycharmProjects\EzFtp2\EzFtp2\Data_in','ftp-emea.teoco.com', 'Airtel3G', 'PocAg3' ]
    drive_the_download(base_dir=job1[0], retention=job1[1], pattern=job1[2],
                        local_directory=job1[3],
                        ftp_host=job1[4], ftp_id=job1[5], ftp_pw=job1[6])
