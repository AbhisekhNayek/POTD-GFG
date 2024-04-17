class Solution:
    def merge(self, arr, temp_arr, left, mid, right):
        pairs_count = 0
        i = left
        j = mid + 1
        k = left

        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp_arr[k] = arr[i]
                pairs_count += (j - (mid + 1))
                i += 1
            else:
                temp_arr[k] = arr[j]
                j += 1
            k += 1

        while i <= mid:
            temp_arr[k] = arr[i]
            pairs_count += (right - mid)
            i += 1
            k += 1

        while j <= right:
            temp_arr[k] = arr[j]
            j += 1
            k += 1

        for i in range(left, right + 1):
            arr[i] = temp_arr[i]

        return pairs_count

    def mergeSort(self, arr, temp_arr, left, right):
        inv_count = 0
        if left < right:
            mid = (left + right) // 2
            inv_count += self.mergeSort(arr, temp_arr, left, mid)
            inv_count += self.mergeSort(arr, temp_arr, mid + 1, right)
            inv_count += self.merge(arr, temp_arr, left, mid, right)
        return inv_count

    def countPairs(self, arr, n):
        temp_arr = [0] * n
        return self.mergeSort(arr, temp_arr, 0, n - 1)
