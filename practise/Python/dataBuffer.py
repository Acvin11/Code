import subprocess
from subprocess import Popen
import pandas as pd
import os, sys


p = Popen(["PGPASSWORD=admin /usr/bin/pg_basebackup -h localhost -p 5432 -U postgres -Ft -Xf -P -D - "], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
#p = Popen(["cat 'C:\Users\acvin.gonsalves\Documents\Acvin\python_saves\' "], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)


print(type(p))
output, errors = p.communicate()




#a= subprocess.Popen("D:\Github\Youtube\Practise\Python")

print("Tar file size:" + str(p))
