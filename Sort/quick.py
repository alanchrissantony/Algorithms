class Sort:
    def helper(self, array, start, end):
        def swap(i, j):
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
        if start >= end:
            return array

        pivot = start
        left = start+1
        right = end

        while left <= right:
            if array[left] > array[pivot] and array[right] < array[pivot]:
                swap(left, right)
                left+=1
                right-=1
            if array[left] <= array[pivot]:
                left+=1
            if array[right] >= array[pivot]:
                right-=1
        swap(pivot, right)
        self.helper(array, start, right-1)
        self.helper(array, right+1, end)
        return array
            
    def quick(self, array):
        return self.helper(array, 0, len(array)-1)
