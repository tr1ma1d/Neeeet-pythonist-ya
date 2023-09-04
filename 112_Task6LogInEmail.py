login = input()
res_email = input()
if "@" not in login and "@" in res_email:
    print("Добро пожаловать")
else: 
    print("неверный логин или не правльно указана почта")
    