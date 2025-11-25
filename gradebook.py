from utils import input_non_empty, input_float, find_course
from storage import save_data

def add_course(data):
    code = input_non_empty("Course code: ")
    if find_course(data, code):
        print("❌ Course code bị trùng!")
        return

    name = input_non_empty("Course name: ")
    credits = input_float("Credits: ", 1, 10)
    semester = input_non_empty("Semester: ")
    score = input_float("Score: ", 0, 10)

    data.append({
        "code": code,
        "name": name,
        "credits": credits,
        "semester": semester,
        "score": score
    })

    save_data(data)
    print("✅ Đã thêm môn học!")

def update_course(data):
    code = input_non_empty("Nhập course code cần sửa: ")
    course = find_course(data, code)
    if not course:
        print("❌ Không tìm thấy môn!")
        return

    print("Nhập thông tin mới (Enter để giữ nguyên):")
    new_name = input("New name: ").strip()
    new_credits = input("New credits: ").strip()
    new_semester = input("New semester: ").strip()
    new_score = input("New score: ").strip()

    if new_name: course["name"] = new_name
    if new_credits:
        try: course["credits"] = float(new_credits)
        except: pass
    if new_semester: course["semester"] = new_semester
    if new_score:
        try: 
            s = float(new_score)
            if 0 <= s <= 10: course["score"] = s
        except: pass

    save_data(data)
    print("✅ Đã cập nhật!")

def delete_course(data):
    code = input_non_empty("Nhập course code cần xóa: ")
    course = find_course(data, code)
    if not course:
        print("❌ Không tìm thấy môn!")
        return

    data.remove(course)
    save_data(data)
    print("✅ Đã xóa môn!")

def view_gradebook(data):
    if not data:
        print("📭 Gradebook trống.")
        return

    print("\n--- GRADEBOOK ---")
    print(f"{'Code':10} {'Name':20} {'Credits':7} {'Semester':10} {'Score':5}")
    print("-"*60)
    for c in data:
        print(f"{c['code']:10} {c['name'][:20]:20} {c['credits']:<7} {c['semester']:<10} {c['score']:<5}")
    print("-"*60)

def calculate_gpa(data):
    if not data:
        print("📭 Chưa có môn để tính GPA.")
        return

    total_points = 0
    total_credits = 0
    for c in data:
        total_points += c["score"] * c["credits"]
        total_credits += c["credits"]

    overall_gpa = total_points / total_credits
    print(f"✅ Overall GPA: {overall_gpa:.2f}")

    semesters = {}
    for c in data:
        sem = c["semester"]
        semesters.setdefault(sem, {"points":0, "credits":0})
        semesters[sem]["points"] += c["score"] * c["credits"]
        semesters[sem]["credits"] += c["credits"]

    print("\n--- GPA by Semester ---")
    for sem, v in semesters.items():
        gpa = v["points"] / v["credits"]
        print(f"{sem}: {gpa:.2f}")
