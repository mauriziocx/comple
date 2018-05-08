
def main():
    tup1 = ('physics', 'chemistry', 1997, 2000)
    tup2 = (1, 2, 3, 4, 5 )
    tup3 = "a", "b", "c", "d";
    print(tup1)
    print(tup2)
    print(tup3)
    #
    l = list()
    l.append(5)
    l.append('a')
    l.append(9)
    l.append("Hola")
    #
    print("Contenido de la Lista: l")
    print(l)
    print("Contenido de cada posicion")
    print("l[0]=> " + str(l[0]))
    print("l[1]=> " + str(l[1]))
    print("l[2]=> " + str(l[2]))
    print("l[3]=> " + str(l[3]))
    # print "z[4]", z[4] error
    print("len(z)=>"+ str(len(l)))

if __name__ == '__main__':
    main()
