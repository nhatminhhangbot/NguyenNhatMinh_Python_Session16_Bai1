# Hai dòng raw_diagnosis.strip() và raw_diagnosis.title() không làm thay đổi giá trị của biến raw_diagnosis vì String trong Python là một đối tượng bất biến, không thể thay đổi
# Cú pháp gán biến đúng: raw_diagnosis = raw_diagnosis.strip().title()
# Khi truyền raw_diagnosis vào extend(), Python sẽ lặp qua từng ký tự một và chuyển các ký tự đó thành các phần tử riêng biệt trong current_list
# Để khắc phục lỗi "vỡ vụn" chữ cái và đưa nguyên vẹn một chuỗi vào danh sách, cần thay extend() bằng append()
# Code đúng:

patient_diagnoses = ["Sốt Xuất Huyết"]

def add_diagnosis(raw_diagnosis, current_list):
    raw_diagnosis = raw_diagnosis.strip().title()

    current_list.append(raw_diagnosis)
    return current_list

new_diagnosis = "  viEm phE QUan  "

updated_diagnoses = add_diagnosis(new_diagnosis, patient_diagnoses)
print("Hồ sơ bệnh án (Các chẩn đoán):", updated_diagnoses)