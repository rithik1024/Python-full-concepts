from time  import sleep


# def countdown(n):
#     while n>-1:
#         print(f"counting down {n}")
#         sleep(1)
#         n-=1
# def countdown(n):
#     for i in range(n,-1,-1):
#         print(f"counting down {n}")
#         sleep(1)
        
# def countdown1(n):
#     if n>-1:
#         print( f"counting down {n}")
#         sleep(1) 
#         #recursive case
#         countdown1(n-1)
#     return ""
# print(countdown1(5))

def countup(stop):
    def run (start):
        if start <=stop:
            print(f"counting up {start}")
            start+=1
            sleep(.5)
            run(start)
    return run(start=0)
print(countup(10))
    