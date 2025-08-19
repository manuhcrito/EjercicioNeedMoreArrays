def solve_case(a):
    last = -10**18
    ans = 0
    for x in a:
        if x > last + 1:
            ans += 1
            last = x
    return ans

def main():
    t = int(input("Número de casos de prueba: "))
    for i in range(t):
        n = int(input(f"Largo del arreglo #{i+1}: "))
        a = list(map(int, input("Arreglo: ").split()))
        print(f"Cantidad máxima de arreglos: {solve_case(a)}")

if __name__ == "__main__":
    main()
