import ping3

fread = open("./IPList/Huawei.csv","r")
fwrite = open("./IP_Result/Huawei.csv","w")
TargetIP=fread.readlines()
n = 3
for line in TargetIP:
    location = line.split(',')[0]
    targetIP = line.split(',')[2].replace("\r","").replace("\n","")
    TotalTime = 0.0
    for k in range(n):
        PingTime = ping3.ping(targetIP,timeout=1,unit="ms")
        if not PingTime:
            PingTime=5000.0
        TotalTime = TotalTime + PingTime
    AverageTime = TotalTime/n
    fwrite.write(location+","+str(AverageTime)+"\n")
    print("Finish! ping of "+location+" is "+str(AverageTime))
print("Finish Ping Test!")
