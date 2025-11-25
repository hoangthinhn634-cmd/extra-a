from storage import load_data
from gradebook import add_course, update_course, delete_course, view_gradebook, calculate_gpa

def menu():
    print("""
========= STUDENT GRADEBOOK =========
1. Add course
2. Update course
3. Delete course
4. View gradebook
5. Calculate GPA
0. Exit
====================================
""")

def main():
    data = load_data()

    while True:
        menu()
        choice = input("Choose: ").strip()

        if choice == "1":
            add_course(data)
        elif choice == "2":
            update_course(data)
        elif choice == "3":
            delete_course(data)
        elif choice == "4":
            view_gradebook(data)
        elif choice == "5":
            calculate_gpa(data)
        elif choice == "0":
            print("Bye bye!")
            break
        else:
            print("❌ Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()
