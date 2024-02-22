class Sort:
    def bubble(self, array):
        def swap(i, j):
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
        k=1
        while array != sorted(array):
            i=0
            while i < len(array)-k:
                if array[i] > array[i+1]:
                    swap(i, i+1)
                i+=1
            k+=1
        return array
