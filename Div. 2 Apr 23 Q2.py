def main():
    t = int(input())
    lst2 = []
    for x in range(t):

        n, k = list(map(int, input().split()))
        lst1 = list(input())

        for number in lst1:
            if number != ' ':
                lst2.append(int(number))
            else:
                pass
        for x in range(n - k + 1):
            end = x + k
            peaks_found, left_index = get_peaks(lst2, x, end)

        print(peaks_found + 1, left_index)   


def get_peaks(lst, start_index, end_index):
    peaks = 0
    index = 0
    section = []
    for x in lst[start_index:end_index]:
        counted_peaks = count_peaks(lst[start_index:end_index])
        if counted_peaks > peaks:
            peaks = counted_peaks
            index = start_index

    return peaks, index


def count_peaks(lst):
    peaks = 0
    for item in lst[1:(len(lst) - 1)]:
        if (lst[lst.index(item) - 1]) < item > (lst[lst.index(item) + 1]):
            peaks += 1
    return peaks


main()
