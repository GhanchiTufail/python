def main(num):
    class iterator:
        def show(self):
            k = 0
            while k < num:
                if k % 7 == 0:
                    yield k
                k += 1
        result = []
        for i in show(num):
            result.append(str(i))
        
        print(",".join(result))
    
    fun = iterator()
    fun.show()


number = int(input("Enter the number : "))
main(number)