class Primes:
    def __init__(self):
        # prime numbers start from 2.
        self.start_prime = 2
 
    def __iter__(self):
        """return the class object"""
        return self
 
    def __next__(self):
        """ generate the next prime"""
        while True:
            for i in range(2, self.start_prime):
                if(self.start_prime % i) ==0:
                    self.start_prime += 1
                    break
            else:
                self.start_prime += 1
                return self.start_prime - 1
 
    # each time this class is called as a function, our __next__ function is called       
    __call__ = __next__
 
if __name__ == "__main__":
    # Since we want prime numbers till 31, we define our sentinel to be 37 which is the next prime after 31. 
    prime_iter = iter(Primes(), 37)
    # print items of the iterator
    for prime in prime_iter:
        print(prime)