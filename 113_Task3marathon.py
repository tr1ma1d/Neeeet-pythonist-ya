
n_km = int(input())
m_km = int(input())

def findDay(n_km, m_km):

    finish = n_km / m_km 
    
    if(finish == 2):
        print(f"До финиша осталось {finish} дня")
    else:
        print(f"До финиша осталось {finish} дней")

findDay(n_km, m_km)