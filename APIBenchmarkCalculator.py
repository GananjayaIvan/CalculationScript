from variable import *
os.chdir(path)
result = glob.glob('*.{}'.format(extension))
banyakData = int(len(result))
os.chdir(path_result)

file = open("ResultTable.html","w")
file.write(htmlBegin)
file.close()

file = open("style.css","w")
file.write(cssText)
file.close()

#Save to csvFiles
csvHeaderWriter = open("Results.csv", "w")
writer = csv.DictWriter(
    csvHeaderWriter, fieldnames=['name', 'totalRequest', 'totalSuccessRequest' , 'totalFailedRequest' , 'totalError' , 'totalHit' , 'jenisError', 'TransactionPerSecond' , 'successRate' , 'failureRate' , 'durationTest' , 'errors', 'responseTime' ]
    )
writer.writeheader()
csvHeaderWriter.close()

for i in range (0,banyakData):
    os.chdir(path)
    print(result[i])
    print(" ========================  Hasil Calculation ======================== ")
    #TotalRequest
    banyakRequest = 0
    with open(result[i], 'r') as csv_file:
        namaFile = result[i]
        csv_reader = csv.reader (csv_file)
        #Buat total request
        lines = len(list(csv_reader)) - 1
        banyakRequest = lines
    csv_file.close()

    #RequestBerhasildanGagal
    totalRequestBerhasil = 0
    totalRequestGagal = 0
    successRate = 0
    failureRate = 0
    with open(result[i], 'r') as csv_file:
        csv_reader = csv.reader (csv_file)
        #Karena nilai success true or false, bisa tinggal di cek input datanya true or false, kemudian memakai looping untuk menghitungnya
        for row in csv_reader:
            returnCode = row[3]
            if(returnCode in httpSuccessReturnCode):
                totalRequestBerhasil = totalRequestBerhasil + 1
            elif(returnCode not in httpSuccessReturnCode):
                totalRequestGagal = totalRequestGagal + 1
    totalRequestBerhasil = totalRequestBerhasil - 1
    successRate = (totalRequestBerhasil / (totalRequestBerhasil+totalRequestGagal)) * 100 
    failureRate = (totalRequestGagal / (totalRequestBerhasil+totalRequestGagal)) * 100

    #TotalError
    totalError = 0
    with open(result[i], 'r') as csv_file:
        csv_reader = csv.reader (csv_file)
        #Function untuk membuat isi data unique
        for row in csv_reader:
            if row[3] not in nonErrorResponseCode:
                totalError = totalError + 1
    csv_file.close()

    #Total Hit
    listAllThreads = []
    pointerX = ()
    TotalHit = 0
    with open(result[i], 'r') as csv_file:


    #Membuat List baru untuk All Threads
        csv_reader = csv.reader (csv_file)
        for line in csv_reader:
            pointerX = line[12]
            listAllThreads.append(pointerX)
        #Delete index 0 karena index 0 pada csv outputnya adalah "allThreads"
        del listAllThreads[0]
        #Konversi menjadi int
        listAllThreads = [int(i) for i in listAllThreads]
        #Total Hit
        TotalHit = sum (listAllThreads)
    csv_file.close()

    #TransactionPerSecond
    listTimeStamp = []
    x = str()
    TPS = 0
    transaction = 0
    with open(result[i], 'r') as csv_file:
    #Membuat List baru untuk TimeStamp
        csv_reader = csv.reader (csv_file)
        for line in csv_reader:
            x = line[0]
            listTimeStamp.append(x)
    csv_file.close()

    #Delete index 0 karena index 0 pada csv outputnya adalah "timeStamp"
    del listTimeStamp[0]
    listTimeStamp = [int(i) for i in listTimeStamp]
    maximumTimeStamp = max(listTimeStamp)
    minimumimeStamp = min(listTimeStamp)
    #Timestamp formatnya adalah unix, mili second
    durationTest = 0
    durationTest = maximumTimeStamp - minimumimeStamp
    durationTest = durationTest/1000
    durationTest = "{:.2f}".format(durationTest)
    if durationTest == 0:
        durationTest = 1
    transaction = lines
    TPS = banyakRequest/durationTest
    TPS = "{:.2f}".format(TPS)
    #errorRate
    errorRate = 0
    errorRate = (totalError / banyakRequest) * 100
    errorRate = "{:.2f}".format(errorRate)

    #Response Time
    listResponseTime = []
    pointerX = ()
    TotalResponseTime = 0
    
    with open(result[i], 'r') as csv_file:


    #Membuat List baru untuk Elapsed (ResponseTime)
        minimumResponseTime = 0
        maximumResponseTime = 0
        averageResponseTime = 0
        csv_reader = csv.reader (csv_file)
        for line in csv_reader:
            pointerX = line[1]
            listResponseTime.append(pointerX)
        #Delete index 0 karena index 0 pada csv outputnya adalah "allThreads"
        del listResponseTime[0]
        #Konversi menjadi int
        listResponseTime = [int(i) for i in listResponseTime]
        #ResponseTime min max
        minimumResponseTime = min(listResponseTime)
        maximumResponseTime = max(listResponseTime)
        #Average
        TotalResponseTime = sum (listResponseTime)
        averageResponseTime = TotalResponseTime/banyakRequest
        averageResponseTime = "{:.2f}".format(averageResponseTime)
        
    csv_file.close()


    #Jenis Error
    errorChecker = str()
    jenisError = []
    with open(result[i], 'r') as csv_file:
        csv_reader = csv.reader (csv_file)
        for row in csv_reader:
            errorChecker = row[3]
            #Function untuk membuat isi data unique if(Data tidak ada di list jenisError) -> Append
            if errorChecker not in jenisError and errorChecker not in nonErrorResponseCode:
                jenisError.append(errorChecker)
    csv_file.close()
    separator = ", " 
    end = ""
    jenisError = separator.join(jenisError)
    
    #Error Counter
    ErrorCount = []
    pointerX = ()
    Error400Count = 0
    Error401Count = 0
    Error403Count = 0
    Error404Count = 0
    Error409Count = 0
    Error500Count = 0
    Error502Count = 0
    Error503Count = 0
    Error504Count = 0
    Error505Count = 0
    ErrorNonHttpCount = 0
    with open(result[i], 'r') as csv_file:
        csv_reader = csv.reader (csv_file)
        for line in csv_reader:
            pointerX = line[3]
            if pointerX not in nonErrorResponseCode:
                ErrorCount.append(pointerX)
        listError = (Counter(ErrorCount))
        if(len(listError) != 0):
            listErrorCounter = []
            print("========= Error Counter ==========")
            for key, value in listError.items():
                string1 = str()
                string2 = str()
                string1 = str(key)
                string2 = str(value)
                print (string1 + " \n" + "Count : " + string2)
                listErrorCounter.append(string1 + "," + " Count : " + string2)
                
                if(string1=="400"):
                    Error400Count = string2
                elif(string1=="401"):
                    Error401Count = string2
                elif(string1=="403"):
                    Error403Count = string2
                elif(string1=="404"):
                    Error404Count = string2
                elif(string1=="409"):
                    Error409Count = string2
                elif(string1=="500"):
                    Error500Count = string2
                elif(string1=="502"):
                    Error502Count = string2
                elif(string1=="503"):
                    Error503Count = string2
                elif(string1=="504"):
                    Error504Count = string2
                elif(string1=="505"):
                    Error505Count = string2
                elif(string1=="Non HTTP response code: java.net.ConnectException"):
                    ErrorNonHttpCount = string2
        print("\n")
    csv_file.close()

    #PrintOutput
    print('Total Request yang ditemukan : ' + str(banyakRequest))
    print('Total Request Berhasil : ' + str(totalRequestBerhasil-1))
    print('Total Request Gagal : ' + str(totalRequestGagal))
    print("Total Hit pada Report : " + str(TotalHit))
    print('Jenis Error yang ditemukan : ' + str(jenisError))
    print('Total Error yang ditemukan : ' + str(totalError))
    print('Transaction per Second : ' + str(TPS))
    print('Success Rate : ' + str(successRate) + '%')
    print('Failure Rate : ' + str(failureRate) + '%')
    print('DurationTest : ' + str(durationTest) + ' seconds ')
    print('ErrorRate : ' + str(errorRate) + " %")
    print('Minimum Response Time: ' + str(minimumResponseTime))
    print('Maximum Response Time: ' + str(maximumResponseTime))
    print('Average Response Time: ' + str(averageResponseTime))
    print("\n")

    #Dictionary yang akan di save ke json dan csv
    dictionary ={
    'name' : str(namaFile),
    'totalRequest' : str(banyakRequest), 
    'totalSuccessRequest' : str(totalRequestBerhasil), 
    'totalFailedRequest' : str(totalRequestGagal), 
    'totalError' : str(totalError), 
    'totalHit' : str(TotalHit), 
    'jenisError' : str(jenisError), 
    'TransactionPerSecond' : str(TPS), 
    'successRate' : str(successRate) + '%',
    'failureRate' : str(failureRate)+ '%',
    'errorRate': str(errorRate)+ '%',
    'durationTest' : str(durationTest) + ' seconds ',
    'errors': 
        listErrorCounter
    ,
    'responseTime' : [
        'Min : ' + str(minimumResponseTime) + " ms",
        'Max : ' + str(maximumResponseTime) + " ms",
        'Average : ' + str(averageResponseTime) + " ms",
    ],
    'error400' : str(Error400Count),
    'error401' : str(Error401Count),
    'error403' : str(Error403Count),
    'error404' : str(Error404Count),
    'error409' : str(Error409Count),
    'error500' : str(Error500Count),
    'error502' : str(Error502Count),
    'error503' : str(Error503Count),
    'error504' : str(Error504Count),
    'error505' : str(Error505Count),
    'ErrorNonHttpCount' : str(ErrorNonHttpCount),
        }

    dictionaryCSV =(
    str(namaFile),
    str(banyakRequest), 
    str(totalRequestBerhasil), 
    str(totalRequestGagal), 
    str(totalError), 
    str(TotalHit), 
    str(jenisError), 
    str(TPS), 
    str(successRate) + '%',
    str(failureRate)+ '%',
    str(errorRate)+ '%',
    str(durationTest) + ' seconds ',
    listErrorCounter,
    [   
        'Min : ' + str(minimumResponseTime) + " ms",
        'Max : ' + str(maximumResponseTime) + " ms",
        'Average : ' + str(averageResponseTime) + " ms",
    ]
    )

    os.chdir(path_result)
    # Serializing json 
    json_object = json.dumps(dictionary, indent = 10, separators=(',', ':'))
    
    #Append to .json file
    filename = "Results.json"
    with open(filename , "a") as outfile:
        if i == 0:
            outfile.write('[ \n')
        outfile.write(json_object)
        if i < banyakData-1:
            outfile.write(', \n')
        if i == banyakData-1:
            outfile.write(']')
    
    #Save to csvFiles
    with open('Results.csv', mode='a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(dictionaryCSV)


    #Save to HTML
   
    with open("ResultTable.html","a") as file:
        file.write('<tr>' '<td>'+ str(namaFile) +'</td>' )
        file.write('<td>'+ str(banyakRequest) +'</td>')
        file.write('<td>'+ str(totalRequestBerhasil) +'</td>')
        file.write('<td>'+ str(totalRequestGagal) +'</td>')
        file.write('<td>'+ str(totalError) +'</td>')
        file.write('<td>'+ str(TotalHit) +'</td>')
        file.write('<td>'+ str(TPS) +'</td>')
        file.write('<td>'+ str(successRate)+'%'+'</td>')
        file.write('<td>'+ str(errorRate) +'%'+'</td>')
        file.write('<td>'+ str(durationTest) +'</td>')
        file.write('<td>'+ str(Error400Count) +'</td>')
        file.write('<td>'+ str(Error401Count) +'</td>')
        file.write('<td>'+ str(Error403Count) +'</td>')
        file.write('<td>'+ str(Error404Count) +'</td>')
        file.write('<td>'+ str(Error409Count) +'</td>')
        file.write('<td>'+ str(Error500Count) +'</td>')
        file.write('<td>'+ str(Error502Count) +'</td>')
        file.write('<td>'+ str(Error503Count) +'</td>')
        file.write('<td>'+ str(Error504Count) +'</td>')
        file.write('<td>'+ str(Error505Count) +'</td>')
        file.write('<td>'+ str(ErrorNonHttpCount) +'</td>')

    
file = open("ResultTable.html","a")
file.write(htmlClose)
file.close()

file = open("ResultTable.html","a")
file.write(htmlClose)
file.close()
