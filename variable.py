import os
import glob
import csv
import sys 
import json
import pandas as pd
import datetime as dt
from collections import Counter
from fastapi import FastAPI

#Directory read file dan result
namaFile = str()
date = str()
listData123 = str()
directory = os.path.dirname(os.path.abspath(__file__))
path = directory + "/ResultPerformanceTesting" + namaFile
path_result = directory + '/Result'
path_File = path + "ResultPerformanceTesting" + namaFile
extension = 'csv'



#Variable yang digunakan dalam calculation
i = int(0)
banyakRequest = int(0)
totalRequestBerhasil = int(0)
totalRequestGagal = int(0)
nonErrorResponseCode = ('responseCode','100', '101', '102', '103', '200', '201', '202', '203', '204', '205', '206', '207', '208', '226', '300', '301', '302', '303', '304', '305' , '306', '307', '308')
returnCode = str()
totalError = int(0)
ErrorCount = []
jenisError = []
time = int (0)
TPS = float(0)
listErrorCounter = []
errorRate = float()
listResponseTime = []
TotalResponseTime = int()
averageResponseTime = float()

#Pointer untuk cek element dalam list
pointerX = str()
TotalHit = str()

#Save data format json dan csv
headerList = ['name', 'totalRequest', 'totalSuccessRequest', 'totalFailedRequest', 'totalError', 'totalHit', 'jenisError', 'TPS', 'successRate', 'failureRate']
data_csv = []

#ErrorCount
Error400Count = int(0)
Error401Count = int(0)
Error402Count = int(0)
Error403Count = int(0)
Error404Count = int(0)
Error405Count = int(0)
Error406Count = int(0)
Error407Count = int(0)
Error408Count = int(0)
Error409Count = int(0)
Error410Count = int(0)
Error411Count = int(0)
Error412Count = int(0)
Error413Count = int(0)
Error414Count = int(0)
Error415Count = int(0)
Error416Count = int(0)
Error417Count = int(0)
Error418Count = int(0)
Error500Count = int(0)
Error502Count = int(0)
Error503Count = int(0)
Error504Count = int(0)
Error505Count = int(0)
ErrorNonHttpCount = int(0)

htmlBegin = '''
<!DOCTYPE html>
<html>
    <head>
        <title>HTML Table</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <div class = "container">
            <div class="table-responsive">
            </div>
            <table class ="table table-bordered table-striped" id = "resultTable">
                <tr>
                    <th rowspan="2">Name</th>
                    <th rowspan="2">Total Request</th>
                    <th rowspan="2">Total Request Sukses</th>
                    <th rowspan="2">Total Request Failed</th>
                    <th rowspan="2">Total Error</th>
                    <th rowspan="2">Total Hit</th>
                    <th rowspan="2">TransactionPerSecond</th>
                    <th rowspan="2">Success Rate</th>
                    <th rowspan="2">Error Rate</th>
                    <th rowspan="2">Duration Test</th>
                    <th colspan="11">Errors Found</th>
                </tr>
                <tr>
                    <th>400</th>
                    <th>401</th>
                    <th>403</th>
                    <th>404</th>
                    <th>409</th>
                    <th>500</th>
                    <th>502</th>
                    <th>503</th>
                    <th>504</th>
                    <th>505</th>
                    <th>Non-http</th>
                </tr>
'''

htmlClose = '''
</table>
        </div>
    </body>
</html>
'''

cssText = '''
table, th, td { border: 1px solid black; border-collapse: collapse; padding: 8px;}
th { font-weight: bold; text-align: center; font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif; font-size: 22;   padding: 8px; background-color: #939598; color: white; }
table { width: 100%; font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif; font-size: 22;  padding: 8px;}
'''
