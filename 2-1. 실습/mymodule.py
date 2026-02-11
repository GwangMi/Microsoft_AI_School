def my_add(a,b):
    return a+b

def my_sub(a,b):
    return a-b

print(f"mymodule안에서의 __name__:{__name__}")

#테스트 코드
if __name__ =="__main__":
    print(my_add(7,3))
    print(my_sub(7,3))