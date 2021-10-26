from variable import *
os.chdir(path)
result = glob.glob('*.{}'.format(extension))
banyakData = int(len(result))

os.chdir(path_result)

#Make Results.html file
a = {
"Test No." : [" File Name "," totalRequest ", " totalSuccessRequest "," totalFailedRequest " , " totalHit "," Transaction Per Second "," Jenis Error "]
}
data = ""
for k in a:
    data += "<td width = 200px>" + k + "</td>"
    for d in a[k]:
        data += "<td width = 200px>" + d + "</td>"
    data += "<tr width = 200px>"


    data = "<table border=1;>" + data + "<table>"
    with open("Results.html", "a") as file:
        file.write(data)

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
    csv_file.close()
        
    
    
    #TotalError
    totalError = 0
    with open(result[i], 'r') as csv_file:
        csv_reader = csv.reader (csv_file)
        #Function untuk membuat isi data unique
        for row in csv_reader:
            if row[3] in search_for:
                totalError = totalError + 1
    csv_file.close()

    #Jenis Error
    jenisError = []
    with open(result[i], 'r') as csv_file:
        csv_reader = csv.reader (csv_file)
        for row in csv_reader:
            if row[3] in search_for:
            #Function untuk membuat isi data unique if(Data tidak ada di list jenisError) -> Append
                if row[3] not in jenisError:
                    jenisError.append(row[3])
    csv_file.close()

    separator = ", " 
    end = ""
    jenisError = separator.join(jenisError)

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

    #Error Counter
    ErrorCount = []
    pointerX = ()
    with open(result[i], 'r') as csv_file:
        csv_reader = csv.reader (csv_file)
        for line in csv_reader:
            pointerX = line[3]
            ErrorCount.append(pointerX)
    csv_file.close()
    
    error400 = 0
    error401 = 0
    error402 = 0
    error403 = 0
    error404 = 0
    error405 = 0
    error406 = 0
    error407 = 0
    error408 = 0
    error409 = 0
    error410 = 0
    error502 = 0
    errornonHTTP = 0

    error400 = ErrorCount.count('400')
    error401 = ErrorCount.count('401')
    error402 = ErrorCount.count('402')
    error403 = ErrorCount.count('403')
    error404 = ErrorCount.count('404')
    error405 = ErrorCount.count('405')
    error406 = ErrorCount.count('406')
    error407 = ErrorCount.count('407')
    error408 = ErrorCount.count('408')
    error409 = ErrorCount.count('409')
    error410 = ErrorCount.count('410')
    error502 = ErrorCount.count('502')
    errornonHTTP = ErrorCount.count('nonHTTP')
    
    print("========== Error Counter ==========")
    print("Error 400 : " + str(error400))
    print("Error 401 : " + str(error401))
    print("Error 402 : " + str(error402))
    print("Error 403 : " + str(error403))
    print("Error 404 : " + str(error404))
    print("Error 405 : " + str(error405))
    print("Error 406 : " + str(error406))
    print("Error 407 : " + str(error407))
    print("Error 408 : " + str(error408))
    print("Error 409 : " + str(error409))
    print("Error 410 : " + str(error410))
    print("Error 502 : " + str(error502))

    

    os.chdir(path_result)
    dictionary ={
'name' : str(namaFile),
'totalRequest' : str(banyakRequest), 
'totalSuccessRequest' : str(totalRequestBerhasil), 
'totalFailedRequest' : str(totalRequestGagal), 
'totalError' : str(totalError), 
'totalHit' : str(TotalHit), 
'jenisError' : str(jenisError), 
'tps' : str(TPS), 
'errors': [
     {
        "errorCode": 400,
        "total": error400
    },
     {
        "errorCode": 401,
        "total": error401
    },
     {
        "errorCode": 402,
        "total": error402
    },
     {
        "errorCode": 403,
        "total": error403
    },
     {
        "errorCode": 404,
        "total": error404
    },
     {
        "errorCode": 405,
        "total": error405
    },
     {
        "errorCode": 406,
        "total": error406
    },
     {
        "errorCode": 407,
        "total": error407
    },
     {
        "errorCode": 408,
        "total": error408
    },
     {
        "errorCode": 409,
        "total": error409
    },
    {
        "errorCode": 410,
        "total": error410
    },
    
    {
        "errorCode": 502,
        "total": error502
    },
     {
        "errorCode": "nonHTTP",
        "total": 0
    }
]
    },
    
    # Serializing json 
    json_object = json.dumps(dictionary, indent = 10)
    
    #Append to .json file
    filename = "Results.json"
    with open(filename , "a") as outfile:
        outfile.write(json_object)
    
    #Make Results.html file
    a = {
	str(i+1) : [str(namaFile), str(banyakRequest), str(totalRequestBerhasil), str(totalRequestGagal), str(TotalHit), str(TPS), str(jenisError)] 
    }

    data = ""
    for k in a:
        data += "<td width = 200px>" + k + "</td>"
        for d in a[k]:
            data += "<td width = 200px>" + d + "</td width>"
        data += "<tr width = 200px>"



    
    data = "<table border=1;>" + data + "<table>"
    with open("Results.html", "a") as file:
        file.write(data)

