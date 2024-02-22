class Sort:
    def insertion(self, array):
        def swap(i, j):
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
        i=1
        while i<len(array):
            j=i-1
            while j>=0 and array[j] > array[j+1]:
                swap(j, j+1)
                j-=1
            i+=1
        return array
