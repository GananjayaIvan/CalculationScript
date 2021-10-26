import os
import glob
import csv
import sys 
import json
import pandas as pd


#Directory read file dan result
directory = os.path.dirname(os.path.abspath(__file__))
path = directory + '/.csv_files'
path_result = directory + '/Result'
extension = 'csv'
namaFile = str()


#Variable yang digunakan dalam calculation
i = int(0)
banyakRequest = int(0)
totalRequestBerhasil = int(0)
totalRequestGagal = int(0)
search_for = ['400','401','402','403','404','405' '406','407','408','409','410','501','502','503','504','505']
totalError = int(0)
ErrorCount = []
jenisError = []
time = int (0)
TPS = int(0)
pointerX = str()
TotalHit = str()
error400 = int(0)
error401 = int(0)
error402 = int(0)
error403 = int(0)
error404 = int(0)
error405 = int(0)
error406 = int(0)
error407 = int(0)
error408 = int(0)
error409 = int(0)
error410 = int(0)
error502 = int(0)
errornonHTTP = int(0)
