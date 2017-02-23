def get_digits(A):

    # init returned array
    digits=[]
    
    B=A
    while B > 0:
        int_part=B%10
        digits.insert(0,int_part)
        B=B/10
    return digits

##############

def naive(A,B):

    chars_A=get_digits(A)
    chars_B=get_digits(B)
    
    complex=0
    for j in range(0,len(chars_A)-len(chars_B)+1,1):
        index=j
        for i in range(0,len(chars_B),1):
            complex+=1
            if chars_A[j] != chars_B[i]:
                break
            else:
                # print chars_A[j], chars_B[i]
                if i==len(chars_B)-1:
                    # print "found a match at j=", index
                    return [index,complex]
                j+=1
    return [-1,complex] 
                

    
def native(A,B):
    A=str(A)
    B=str(B)
    
    return A.find(B)


import timeit


A='1'*10**6 # 10**6 digits
A=A+'3'

B='1'*100
B=B+'3'


A=int(A)
B=int(B)

print A
print B

chars_A=get_digits(A)
chars_B=get_digits(B)

native_time=0
naive_time=0

stats=1

for i in range(stats):
    start = timeit.timeit()
    index1=naive(A,B)
    end = timeit.timeit()
    naive_time+=abs(end-start)
    

    start = timeit.timeit()
    index2=native(A,B)
    end = timeit.timeit()
    native_time+=abs(end-start)

print "lengths:",len(chars_A), len(chars_B)
print "pattern found at index", index1, index2
    
naive_time=naive_time/stats
native_time=native_time/stats

print "Naive Method time: ", naive_time
print "Native Method time: ", native_time

print "Ratio: ", naive_time/native_time
