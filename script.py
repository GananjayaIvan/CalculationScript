from variable import*
os.chdir(path)
result = glob.glob('*.{}'.format(extension))
banyakData = int(len(result))
os.mkdir(path_result)
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
    csvHeaderWriter, fieldnames=['name', 'totalRequest', 'totalSuccessRequest' , 'totalFailedRequest' , 'totalError' , 'totalHit' , 'jenisError', 'TransactionPerSecond' , 'successRate' , 'failureRate' ,'errorRate', 'durationTest' , 'errors', 'responseTime' ]
    )

writer.writeheader()
csvHeaderWriter.close()



for i in range (0,banyakData):
    #Buka Folder Directory hasil testing dan di sort by name (Descending)  
    os.chdir(path)
    files =  os.listdir()
    sorted_files =  sorted(files)
    #File yang telah di sort, namanya akan dimasukan ke variable namaFile
    namaFile = sorted_files[i]
    
    #TotalRequest
    banyakRequest = 0
    lines = int(0)
    with open(namaFile, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        #Menghitung jumlah total request yang ditembakan oleh jmeter, yang dihitung adalah length dari list
        lines = len(list(csv_reader)) - 1
        banyakRequest = lines
    csv_file.close()
    namaFile = os.path.splitext(namaFile)[0]

    #RequestBerhasildanGagal
    totalRequestBerhasil = 0
    totalRequestGagal = 0
    successRate = 0
    failureRate = 0

    with open(result[i], 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        #Karena nilai success true or false, di cek apakah input ada di nonErrorResponseCode atau tidak, kemudian memakai looping untuk menghitungnya
        for row in csv_reader:
            returnCode = row[3]
            if(returnCode in nonErrorResponseCode):
                totalRequestBerhasil = totalRequestBerhasil + 1
            elif(returnCode not in nonErrorResponseCode):
                totalRequestGagal = totalRequestGagal + 1
                
    #Row Request yang berhasil dikurangi header 
    totalRequestBerhasil = totalRequestBerhasil - 1
    failureRate = (totalRequestGagal / (totalRequestBerhasil+totalRequestGagal))
    failureRate = "{:.5f}".format(failureRate)
    successRate = (totalRequestBerhasil /(totalRequestBerhasil+totalRequestGagal))
    successRate = "{:.5f}".format(successRate)
    
    #TotalError
    totalError = 0
    with open(result[i], 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
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
        csv_reader = csv.reader(csv_file)
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

    #MenghitungTransactionPerSecond
    listTimeStamp = []
    lastLine = []
    lastLineElapsedTime = []
    x = str()
    TPS = 0
    transaction = 0
    durationTest = int(0)
    with open(result[i], 'r') as csv_file:

    #Membuat List baru untuk TimeStamp
    
        csv_reader = csv.reader(csv_file)
        next(csv_reader, None)
        for line in csv_reader:
            x = line[0]
            #Timestamp formatnya milisecond
            listTimestamp = listTimeStamp.append(x)
    csv_file.close()
    with open(result[i], 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            lastLineElapsedTime = row[1]
 
    minimumTimeStamp = int(min(listTimeStamp))
    maximumTimeStamp = int(max(listTimeStamp))+int(lastLineElapsedTime)
    
    if durationTest == 0:
        durationTest = 1

    #Convert to Date Time
    durationTest = (maximumTimeStamp-minimumTimeStamp)
    #Harus dibagi 1000 agar bisa di konversikan
    minimumTimeStamp = minimumTimeStamp/1000
    date_conv = dt.datetime.utcfromtimestamp(minimumTimeStamp).strftime('%Y-%m-%d %H:%M:%S')
    

    transaction = lines
    TPS = banyakRequest / (durationTest) * 1000
    TPS = float(TPS)


    #Response Time
    listResponseTime = []
    pointerX = ()
    TotalResponseTime = 0

    with open(result[i], 'r') as csv_file:
    #Membuat List baru untuk Elapsed (ResponseTime)
        minimumResponseTime = 0
        maximumResponseTime = 0
        averageResponseTime = 0
        csv_reader = csv.reader(csv_file)

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
            for key, value in listError.items():
                string1 = str()
                string2 = str()
                string1 = str(key)
                string2 = int(float((value)))
                errorDictionary = {
                    "httpCode" : string1,
                    "total": string2
                    }
                listErrorCounter.append(errorDictionary)
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
                else:
                    ErrorNonHttpCount = string2

    csv_file.close()
    #Dictionary yang akan di save ke json dan csv

    path_File = path_result + '/' +namaFile
    os.mkdir(path_File)
    os.chdir(path_File)
    dictionary ={
    'testDate' : str(date_conv),
    'threads' : ((namaFile)),
    'testDuration(ms)' : int(float(durationTest)),   
    'requestTotal' : int(float(banyakRequest)), 
    'requestSuccess' : int(float(totalRequestBerhasil)), 
    'requestFailed' : int(float(totalRequestGagal)), 
    'ratioSuccess' : float(successRate),
    'ratioError' : float(failureRate),
    'transactionPerSecond' : float(TPS),   
    'error': 
        listErrorCounter
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

    os.chdir(path_File)
    # Serializing json 
    json_object = json.dumps(dictionary, indent = 10, separators=(',', ':'))
    
    #Append to .json file
    filename = "Results.json"
    with open(filename , "a") as outfile:
        outfile.write(json_object)

    #Save to csvFiles
    os.chdir(path_File)
    with open('Results.csv', mode='a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(dictionaryCSV)

    #Save to HTML
    os.chdir(path_File)
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

    file = open(namaFile + ".html","w")
    file.write(htmlBegin)
    file.close()

    with open(namaFile + ".html","a") as file:

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

    file = open("style.css","w")
    file.write(cssText)
    file.close()
    file = open(namaFile + ".html","a")
    file.write(htmlClose)
    file.close()
    #PrintOutput
os.chdir(path_result)
file = open("ResultTable.html","a")
file.write(htmlClose)
file.close()

print('File read from Directory  :' + path)
print('File Written in Directory :' + path_result)

