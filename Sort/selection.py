class Sort:
    def selection(self, array):
        def swap(i, j):
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
        i=0
        while i < len(array)-1:
            j=i+1
            while j < len(array):
                if array[i] > array[j]:
                    swap(i, j)
                j+=1
            i+=1
        return array
