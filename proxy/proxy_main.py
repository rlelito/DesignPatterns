from real_subject import RealSubject
from proxy import Proxy

if __name__ == "__main__":
    rs1 = RealSubject(1, 4, 2)
    p1 = Proxy(rs1)

    print(p1.request(), "\n")

    p1.real_subject.get_input(1, 4, 2)
    print(p1.request(), "\n")

    p1.real_subject.get_input(0, 0, 1)
    print(p1.request(), "\n")

    print(p1.request(), "\n")
