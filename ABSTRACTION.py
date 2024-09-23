from abc import ABC , abstractmethod

class Kalyani(ABC):
    @abstractmethod
    def breakfast(self):
        pass

    @abstractmethod
    def lunch(self):
        pass

    def dinner(self):
        pass
class Guna(Kalyani):
    def breakfast(self):
        print('idly with beer')


    def lunch(self):
        print('biryani with blenders pride')

    def dinner(self):
        print('chilli chicken with ballentine')
G=Guna()
G.breakfast()
G.lunch()
class Krithika(Kalyani):
    def breakfast(self):
        print('dosa with chutney')
    def lunch(self):
        print('sambar rice')
    def dinner(self):
        print('chapathi with french fries Tomato sauce')

k=Krithika()



