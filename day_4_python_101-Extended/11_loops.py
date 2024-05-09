# While and For Loops
# While Loops
# x = 0
# while(x<5):
#     print(x)
#     x=x+1   # if this command will not be used, the loop will continue for infinite time.


# For Loops

# for x in range(4,11):
#     print(x)

# array
days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
print(type(days))
for d in days:
    print(d)

#  break and continue

# days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
# for d in days:
#     # if(d=="Thu"):break   #breaks the loop at d
#     if(d=="Wed"):continue   #skips the d
#     print(d)