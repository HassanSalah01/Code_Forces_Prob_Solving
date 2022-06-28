def typ(argument):
    match argument:
        case "Tetrahedron":
            return 4
        case "Cube":
            return 6
        case "Octahedron":
            return 8
        case "Dodecahedron":
            return 12
        case "Icosahedron":
            return 20
        case default:
            return 0

def main():
    x = int(input())
    count = 0 
    for i in range(x):
        count+=typ(input())
    print(count)
main()
