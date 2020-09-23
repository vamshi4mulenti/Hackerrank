D = "PM5163"
print(D[2:4])
if int(D[2:4]) >=  55 :
    D1="PM55XX"
elif int(D[2:4]) <= 53:
    D1="PM53XX"
print(D)
folder = r"C:\Users\pdadmin\Box\ReleaseBinaries\OptimumBasicRange"
folder = folder+"\\"+D1+"\\"+"NIGHTLY"+"\\"+D
print(folder)