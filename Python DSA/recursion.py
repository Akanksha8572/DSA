# print akanksha four times by using recursion 
# using head recursion 
count = 0
# def func():
#     global count
#     if count == 4:
#         return
#     print("akanksha")
#     count += 1
#     func()

# func()
#using tail recursion 
def name():
    global count
    print(count)
    if count == 4:
        return
    count += 1
    name()
    print("Akanksha")

name()