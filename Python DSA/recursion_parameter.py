# print akanksha 5 times using parameters 
# def func(x , n):
#     if n == 0:
#         return
#     print(x)
#     func(x, n-1)
# func("akanksha", 3)
#  print 1 to N using head recursion 
# def func(i,N):
#     if i>N:
#         return
#     print(i)
#     func(i+1, N)
# func(1,9)
# print 1 to N using tail recursion 
# def func(N):
#     if N == 0:
#         return
#     func(N-1)
#     print(N)
# func(9)
# print N to 1 using tail recursion
# def func(i,N):
#     if i>N:
#         return
#     func(i+1, N)
#     print(i)
    
# func(1,9)
# print N to 1 using head recursion
def func(N):
    if N == 0:
        return
    print(N)
    func(N-1)
func(9)
    