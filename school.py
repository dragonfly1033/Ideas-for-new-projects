class main:
    def __init__(self, a=1, b=1, c=1):
        self.a=a
        self.b=b
        self.c=c
        self.type='main'

    def dis(self):
        print(f'a={self.a}, b={self.b}, c={self.c}, type={self.type}')

class sub(main):
    def __init__(self, a=2, b=2, c=2):
        self.a=a
        self.b=b
        self.c=c
        self.type='sub'

t1=main()
t2=main(1,2,3)
t3=sub()
t4=sub(1,2,3)
t1.dis()
t2.dis()
t3.dis()
t4.dis()
