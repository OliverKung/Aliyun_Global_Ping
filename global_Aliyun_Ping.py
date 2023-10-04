import ping3

fread = open("./Aliyun_Domestic.csv","r")
fwrite = open("./IP_Result.csv","w")
TargetIP=fread.readlines()
n = 3
for line in TargetIP:
    location = line.split(',')[0]
    targetIP = line.split(',')[1].replace("\r","").replace("\n","")
    print("Ping "+targetIP+" at "+location)
    TotalTime = 0.0
    for k in range(n):
        PingTime = ping3.ping(targetIP,timeout=1,unit="ms")
        if not PingTime:
            PingTime=5000.0
        TotalTime = TotalTime + PingTime
    AverageTime = TotalTime/n
    fwrite.write(location+","+str(AverageTime)+"\n")
    print("Finish!")
print("Finish Ping Test!")
