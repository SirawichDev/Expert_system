def gg():
    for x in range(9):
        yield('GGWP')




ob = gg()
for i in gg():
    print(ob.x+1)
    print (next(ob))
