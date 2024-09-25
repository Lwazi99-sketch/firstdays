#write a program that REPEATEDLY asks the user to enter a year and that prints out the name of the day on which the 1st of January of that year falls. If the user enters ‘-1’ then the program will stop, printing ‘FINISHED’
#Lwazi Somtsewu 
# 22 August 2024

while True:
            year=int(input('Enter the year (or -1 to quit): '))

            if year ==-1:
                print("FINISHED")
                break

            else:

                A=year
                A=A-1
                day=6*(A%400)  # the formula that was given above 
                day+=4*(A%100)
                day+=5*(A%4)
                day=(1+day)%7
                
                if day == 0:
                       print("The 1st of January " + str(year)+ " falls on a Sunday.")
                elif day==1:
                       print(f"The 1st of January {year} falls on a Monday.")
                elif day==2:
                       print(f"The 1st of January {year} falls on a Tuesday.")
                elif  day==3:
                       print(f"The 1st of January {year} falls on a Wednesday.")
                elif day==4:
                       print(f"The 1st of January {year} falls on a Thursday.")
                elif day==5:
                       print(f"The 1st of January {year} falls on a Friday.")
                else:
                       print(f"The 1st of January {year} falls on a Saturday.")