class Sort:
    def join(self, left, right):
        array=[]
        i,j = 0,0
        while i<len(left) and j<len(right):
            if left[i] < right[j]:
                array.append(left[i])
                i+=1
            else:
                array.append(right[j])
                j+=1
        while i<len(left):
            array.append(left[i])
            i+=1
        while j<len(right):
            array.append(right[j])
            j+=1
        return array
    def merge(self, array):
        if len(array)<=1:
            return array
        mid = len(array)//2
        left = array[:mid]
        right = array[mid:]

        return self.join(self.merge(left), self.merge(right))
