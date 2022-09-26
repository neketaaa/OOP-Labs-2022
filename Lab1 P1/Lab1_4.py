import argparse

def knapsak(W, w, n):
    table = [[0] * (W+1) for i in range(n)]
    for i in range(1,W+1):
        if w[0] < i or w[0] == i:
            table[0][i] = w[0]
    #print(table)

    for j in range(1,n):
        for i in range(1,W+1):
            table[j][i] = table[j-1][i]
            if w[j] < i or w[j] == i:
                temp = table[j-1][i-w[j]] + w[j]
                #print(table)
                if table[j][i] < temp:
                    table[j][i] = temp

    # for i in range(n):
    #         print(w[i],table[i])
    return table[n-1][W]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-W', type=int, default=0)
    parser.add_argument('-w', type=int, nargs="+", default=0)
    parser.add_argument('-n', type=int, default=0)
    args = parser.parse_args()
    print('Max weight is ',knapsak(args.W, args.w, args.n))

if __name__ == "__main__":
    main()


