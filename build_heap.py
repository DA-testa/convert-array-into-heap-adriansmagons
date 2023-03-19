# python3


def build_heap(data):
    swaps = []
    size = len(data)
    for i in range(size//2, -1, -1):
        heapify(size, data, swaps, i)
    return swaps
        
def heapify(size, data, swaps, i):
    left_c = 2*i+1
    right_c = 2*i+2
    min_i = i
    if left_c < size and data[min_i] > data[left_c]:
        min_i = left_c
    if right_c < size and data[min_i] > data[right_c]:
        min_i = right_c
    if min_i != i:
        data[i], data[min_i] = data[min_i], data[i]
        swaps.append((i, min_i))
        heapify(size, data, swaps, min_i)

        
def main():
    
    tekstaievade = input()
    if tekstaievade.__contains__("I"):
        elements = int(input())
        data = list((map(int, input().strip().split())))
        assert len(data) == elements, "Neprecizs elementu daudzums"
        swaps = build_heap(data)
        print(len(swaps))
        for i, j in swaps:
            print(i, j)
        
    elif tekstaievade.__contains__("F"):
        nos = input()
        if "a" not in nos:
            fails = "tests/" + nos
            with open(fails,"r", encoding="utf-8") as f:
                elements = int(f.readline().strip())
                data = list((map(int, f.readline().strip().split())))
                swaps = build_heap(data)
            
            assert len(data) == elements , "Neprecizs elementu daudzums"

            print(len(swaps))
            for i, j in swaps:
                print(i, j)

if __name__ == "__main__":
    main()
