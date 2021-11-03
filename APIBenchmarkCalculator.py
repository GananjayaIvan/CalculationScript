from variable import *
os.chdir(path)
result = glob.glob('*.{}'.format(extension))
banyakData = int(len(result))

os.chdir(path_result)
for i in range (0,banyakData):
    os.chdir(path)
    print(" ========================  Hasil Calculation ======================== " + result[i])
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
    maximum = max(listTimeStamp)
    minimum = min(listTimeStamp)
    #Timestamp formatnya adalah unix, mili second
    time = maximum - minimum
    time = time/1000
    if time == 0:
        time = 1
    transaction = lines
    TPS = banyakRequest/time
    

    #PrintOutput
    print('Total Request yang ditemukan : ' + str(banyakRequest))
    print('Total Request Berhasil : ' + str(totalRequestBerhasil))
    print('Total Request Gagal : ' + str(totalRequestGagal))
    print("Total Hit pada Report : " + str(TotalHit))
    print('Jenis Error yang ditemukan : ' + str(jenisError))
    print('Total Error yang ditemukan : ' + str(totalError))
    print('Transaction per Second : ' + str(TPS))
    print("\n")


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
            print("==========Error Counter==========")
            for key, value in listError.items():
                print ("Error Code: " + str(key) + " Error Counted: " + str(value))
        print("\n")
    csv_file.close()

    #Dictionary yang akan di save ke json dan csv
    dictionary_json ={
    'name' : str(namaFile),
    'totalRequest' : str(banyakRequest), 
    'totalSuccessRequest' : str(totalRequestBerhasil), 
    'totalFailedRequest' : str(totalRequestGagal), 
    'totalError' : str(totalError), 
    'totalHit' : str(TotalHit), 
    'jenisError' : str(jenisError), 
    'tps' : str(TPS), 
    'successRate' : str(successRate) + '%',
    'failureRate' : str(failureRate)+ '%',
    'errors': [
    listError
    ]
        },

    dictionary_csv ={
    'name' : str(namaFile),
    'totalRequest' : str(banyakRequest), 
    'totalSuccessRequest' : str(totalRequestBerhasil), 
    'totalFailedRequest' : str(totalRequestGagal), 
    'totalError' : str(totalError), 
    'totalHit' : str(TotalHit), 
    'jenisError' : str(jenisError), 
    'tps' : str(TPS), 
        },


    os.chdir(path_result)
    # Serializing json 
    json_object = json.dumps(dictionary_json, indent = 10)
    
    #Append to .json file
    filename = "Results.json"
    with open(filename , "a") as outfile:
        outfile.write(json_object)
    
    with open('Results.csv', mode='a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(dictionary_csv)
