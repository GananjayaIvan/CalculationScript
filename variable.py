import os
import glob
import csv
import sys 
import json
import pandas as pd
from collections import Counter

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
nonErrorResponseCode = ('responseCode','100', '101', '102', '103', '200', '201', '202', '203', '204', '205', '206', '207', '208', '226', '300', '301', '302', '303', '304', '305' , '306', '307', '308')
totalError = int(0)
ErrorCount = []
jenisError = []
time = int (0)
TPS = int(0)

#Pointer untuk cek element dalam list
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
