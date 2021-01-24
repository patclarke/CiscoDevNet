# This code was copied and modified from https://www.cbtnuggets.com/ DevNet training video 22 Observer Design Pattern by Ben Finkel
class Observer():
    def update(self, subject):
        print("Observer: My subject just updated and told me about it")
        print("Observer: It's state is now - {}".format(subject._state))


class Subject():

    _state = 0
    _observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        print("Subject: I'm notifyinh my observers... ")
        for observer in self._observers:
            observer.update(self)

    def updateState(self,n):
        print("Subject: I've received a state update!")
        self._state = n
        self.notify()


s = Subject()

ob1 = Observer()
ob2 = Observer()
ob3 = Observer()

s.attach(ob1)
s.attach(ob2)
s.attach(ob3)

s.updateState(5)
