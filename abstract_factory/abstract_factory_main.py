from app_supervisor import AppSupervisor

if __name__ == "__main__":
    f1 = AppSupervisor("low", "low")
    f1.show()
    f1.print()
    print('-' * 64)
    f2 = AppSupervisor("high", "high")
    f2.show()
    f2.print()
