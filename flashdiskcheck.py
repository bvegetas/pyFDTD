#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 01:11:40 2019

@author: bvegetas
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 23:12:48 2019
Paket program Anti-Mata-Mata: deteksi mencuri USB flash drive
Memindai jika semua flash drive di Linux dihapus secara paksa,
Jika dihapus secara paksa, catat waktu penghapusan dan nama flash drive,
dan gunakan perangkat kamera untuk menemukan 
Retlatijum yang mencuri flash drive pada saat pertama kali
@author: bvegetas
"""

import os
import time


SLEEPTIME=30
username='bvegetas'
attacks=[]


'''
Titik pemasangan umum untuk flash drive Linux
'''
disklist1=os.listdir('/media/'+username+'/')
disklist2=os.listdir('/mnt/')

'''
Mendeteksi titik pemasangan kosong dan menghapusnya dari daftar deteksi
'''
for i in disklist1:
    a=os.listdir('/media/'+username+'/'+i)
    if len(a)==0:
        disklist1.remove(i) 
for i in disklist2:
    a=os.listdir('/mnt/'+i)
    if len(a)==0:
        disklist2.remove(i)
detected=0
while True:
    banner=0
    w=time.localtime() 
    x=str(w[2])+'/'+str(w[1])+'/'+str(w[0])+', '+str(w[3])+':'+str(w[4])+':'+str(w[5])
    for i in disklist1:
        try:
            a=os.listdir('/media/'+username+'/'+i)       
            if len(a)==0:
                banner+=1
                attacks.append(x+', Flash drive \"'+i+'\" dicuri oleh Mata-Mata')
                disklist1.remove(i)
        except:
            banner+=1
            attacks.append(x+', Flash drive \"'+i+'\" dicuri oleh Mata-Mata')
            disklist1.remove(i)
    for i in disklist2:
        try:
            a=os.listdir('/mnt/'+i)       
            if len(a)==0:
                banner+=1
                attacks.append(x+', Flash drive \"'+i+'\" dicuri oleh Mata-Mata')
                disklist2.remove(i)
        except:
            banner+=1
            attacks.append(x+', Flash drive \"'+i+'\" dicuri oleh Mata-Mata')
            disklist2.remove(i)
    detected+=banner
    print('Pada '+x+', %d pencurian flash drive terdeteksi'%detected)
    time.sleep(SLEEPTIME)
            
