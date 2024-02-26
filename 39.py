def main():
    right_triangles = []
    for a in range(2,501):
        for b in range(2,a+1):
            c = (a**2 +b**2)**0.5
            if c // 1 == c:
                right_triangles.append((a,b,int(c)))
    
    solutions = {}
    for triplet in right_triangles:
        perimeter = triplet[0] + triplet[1] + triplet[2]
        if perimeter not in solutions:
            solutions[perimeter] = 1
        else:
            solutions[perimeter] += 1

    max_sol = 0
    max_key = 0
    for key in solutions.keys():
        if solutions[key] > max_sol:
            max_sol = solutions[key]
            max_key = key
    print(max_key)

if __name__ == "__main__":
    main()