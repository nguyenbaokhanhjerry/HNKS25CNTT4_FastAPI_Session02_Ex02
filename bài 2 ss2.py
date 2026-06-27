from fastapi import FastAPI
app = FastAPI()
students = [
    {"id": 1, "name": "An"},
    {"id": 2, "name": "Binh"},
    {"id": 3, "name": "Cuong"},
]
@app.get("/student")
def get_student():
    return students[0]

# 1. Phân tích lỗi
# Endpoint hiện tại trong source code là gì?
# -> /student
# Vì sao khi gọi GET /students lại bị lỗi 404 Not Found?
# -> Vì trong source code không khai báo endpoint "/students", mà chỉ có endpoint "/student".
# Vì sao tên endpoint /student chưa phù hợp với yêu cầu lấy danh sách sinh viên?
# -> Vì "/student" mang ý nghĩa lấy một sinh viên, trong khi yêu cầu của khách hàng là lấy toàn bộ danh sách sinh viên.
# Vì sao dòng return students[0] chưa đúng với yêu cầu nghiệp vụ?
# -> Vì students[0] chỉ trả về sinh viên đầu tiên trong danh sách, không trả về toàn bộ danh sách sinh viên.
# API đúng theo yêu cầu khách hàng nên có đường dẫn là gì?
# -> GET /students
# 2. Sửa lỗi
from fastapi import FastAPI
app = FastAPI()
students = [
    {"id": 1, "name": "An"},
    {"id": 2, "name": "Binh"},
    {"id": 3, "name": "Cuong"},
]
@app.get("/students")
def get_students():
    return students