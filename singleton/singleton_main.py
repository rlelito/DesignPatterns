from singleton import Singleton

if __name__ == "__main__":
    s1 = Singleton.get_instance()
    s1.message_1()
    s1.message_2()
    print(s1)

    s2 = Singleton.get_instance()
    s2.message_1()
    s2.message_2()
    print(s2)
