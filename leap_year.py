years = [2001,2002,2003,2004,-2000]
leap_year = []
for yr in years:
    if yr<0:   
        continue  
    if yr % 400 == 0 or (yr % 4 == 0 and yr % 100 != 0):
        leap_year.append(yr)
print("Leap years:", leap_year)
