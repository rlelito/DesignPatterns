from component_checkbox import CheckboxComponent
from mediator_dialog import DialogMediator

if __name__ == "__main__":
    opt1 = CheckboxComponent("1", "Exercises passed.")
    opt2 = CheckboxComponent("2", "Lecture (exam) passed.")
    opt3 = CheckboxComponent("3", "Subject passed (contest won).")

    mediator = DialogMediator(opt1, opt2, opt3)

    program = True
    while program:
        print('_ ' * 4, "<< Grade Transcript: Menu >>", ' _' * 4)
        print(opt1)
        print(opt2)
        print(opt3)
        print("\t4) Exit program.")
        opt = input(">>> ")

        if opt == '1':
            opt1.check()
        elif opt == '2':
            opt2.check()
        elif opt == '3':
            opt3.check()
        elif opt == '4':
            program = False
