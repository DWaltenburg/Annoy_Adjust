import subprocess


def set_master_volume(volume):
    val = float(int(volume))
    proc = subprocess.Popen('/usr/bin/amixer sset Master ' + str(val) + '%', shell=True, stdout=subprocess.PIPE)
    proc.wait()


set_master_volume()
