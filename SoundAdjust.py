from __future__ import print_function
import subprocess


def get_master_volume():
    proc = subprocess.Popen('/usr/bin/amixer sget Master'"""windows sti til lyd værdi""", shell=True, stdout=subprocess.PIPE)
    amixer_stdout = proc.communicate()[0].split('\n'.encode())[4]
    proc.wait()

    find_start = amixer_stdout.find('['.encode()) + 1
    find_end = amixer_stdout.find('%]'.encode(), find_start)

    return float(amixer_stdout[find_start:find_end])


def set_master_volume(volume):
    val = float(int(volume))

    proc = subprocess.Popen('/usr/bin/amixer sset Master ' + str(val) + '%', shell=True, stdout=subprocess.PIPE)
    proc.wait()


get_master_volume()
