from variable import *
os.chdir(path)
result = glob.glob('*.{}'.format(extension))
banyakData = int(len(result))

os.chdir(path_result)

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
        for line in csv_reader:
            if(line [7] == "true"):
                totalRequestBerhasil = totalRequestBerhasil + 1
            elif(line [7] == "false"):
                totalRequestGagal = totalRequestGagal + 1
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
    if durationTest == 0:
        durationTest = 1
    transaction = lines
    TPS = banyakRequest/durationTest
    
    #errorRate
    errorRate = 0
    errorRate = (totalError / banyakRequest) * 100

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
                print ("{Code: " + string1 + " \n " + "Count: " + string2 + "}")
                listErrorCounter.append("{ Code: " + string1 + "," + " Count: " + string2 + "}")
        print("\n")
    csv_file.close()

    #PrintOutput
    print('Total Request yang ditemukan : ' + str(banyakRequest))
    print('Total Request Berhasil : ' + str(totalRequestBerhasil))
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
    'errors': [
        listErrorCounter
    ],
    'responseTime' : [
        'Minimum Response Time : ' + str(minimumResponseTime) + " ms",
        'Maximum Response Time : ' + str(maximumResponseTime) + " ms",
        'Average Response Time : ' + str(averageResponseTime) + " ms",
    ]
        },

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
        'Minimum : ' + str(minimumResponseTime) + " ms",
        'Maximum : ' + str(maximumResponseTime) + " ms",
        'Average : ' + str(averageResponseTime) + " ms",
    ]
    )
        

    os.chdir(path_result)
    # Serializing json 
    json_object = json.dumps(dictionary, indent = 5, separators=(',', ':'))
    
    #Append to .json file
    filename = "Results.json"
    with open(filename , "a") as outfile:
        outfile.write(json_object)
    
    #Save to csvFiles
    with open('Results.csv', mode='a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(dictionaryCSV)
