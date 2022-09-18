import argparse

def knapsak(W, w, n):
    print(W, w, n)
    table = [[0] * (W-1) for i in range(n)]
    for i in range(1,W-1):
        if w[0] < i or w[0] == i:
            print(w[0],i, w[0]>i)
            table[0][i] = w[0]
    print(table)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-W', type=int, default=0)
    parser.add_argument('-w', type=int, nargs="+", default=0)
    parser.add_argument('-n', type=int, default=0)
    args = parser.parse_args()
    knapsak(args.W, args.w, args.n)

if __name__ == "__main__":
    main()


