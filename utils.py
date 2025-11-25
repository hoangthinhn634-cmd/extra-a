def input_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("❌ Không được để trống!")

def input_float(prompt, min_val=None, max_val=None):
    while True:
        try:
            value = float(input(prompt))
            if min_val is not None and value < min_val:
                print(f"❌ Giá trị phải >= {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"❌ Giá trị phải <= {max_val}")
                continue
            return value
        except:
            print("❌ Nhập số không hợp lệ!")

def find_course(data, code):
    for c in data:
        if c["code"].lower() == code.lower():
            return c
    return None
