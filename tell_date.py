date=input()
year=int(date[:4])
month=int(date[5:7])
day=int(date[8:])
y=2022
m=6
d=20
if year<y:
    print('Before')
else:
    if year>y:
        print('After')
    else:
        if month<m:
            print('Before')
        else:
            if month>m:
                print('After')
            else:
                if day<d:
                    print("Before")
                else:
                    print("After")