def solution():
    N = int(input().strip())
    for n in range(1, N + 1):
        cnt = sum(1 for s in str(n) if s in "369")
        print("-" * cnt if cnt else n, end = " ")


if __name__ == "__main__":
    solution()