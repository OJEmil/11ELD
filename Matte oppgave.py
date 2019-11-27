

def finnKonstant(var1, var2):
    konstant = var1 / var2
    return konstant

def konst():
    var1 = float(input("Tast inn første variabel "))
    var2 = float(input("Tast inn andre variabel "))
    print("Konstanten mellom første og andre variabel er ", finnKonstant(var1, var2))
    return

def prop():
    var1 = float(input("Tast inn x1 "))
    var2 = float(input("Tast inn y1 "))
    var3 = float(input("Tast inn x2 "))
    var4 = float(input("Tast inn x3 "))
    if var1/var2 == var3/var4:
        print("Tallene er proposjonale ")
        return

    else:
        print("Tallene er ikke proposjonale ")
        return

while True:
    print("Hva vill du finne ut? ")
    valg = input("Du kan velge mellom 'konstant' eller 'proposjon' ")
    if valg == "konstant":
        konst()
    elif valg == "proposjon":
        prop()

    elif valg == "slutt":
        end
