def student_info(**data):
    for key,value in data.items():
        print(key,":",value)
student_info(name="revi",age=18,marks=85)