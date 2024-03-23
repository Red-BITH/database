import subprocess
import socket
import random
import os
try:
  os.system("netstat -a")
  result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
  if result.returncode == 0:
    print("\nAğ bağlantıları başarıyla listelendi. Sonuçlar:\n{result.stdout}")
    print(" ")
    return
  else:
    print("\nAğ bağlantıları listelenirken bir hata oluştu. Hata:\n{result.stderr}")
except Exception as e:
  print("\nBir hata oluştu: {e}")
