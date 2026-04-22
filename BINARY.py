# # BASIC BINARY 

# def binary_search(arr, target):
#     l=0 
#     r=len(arr)-1

#     while l<=r:   
#         mid=(l+r)//2  

#         if arr[mid]==target:
#             return mid
#         elif arr[mid]<target:
#             l=l+1
#         elif arr[mid]>target:
#             r=r-1 
#     return -1 

# arr = [1,3,3,3,3,11]
# target = 3

# result = binary_search(arr, target)

# print(result) 



# # FIRST OCCURENCE


# def first_occ(arr, x):

#     l=0
#     r=len(arr)
#     ans=-1

#     while l<=r:
#         mid=(l+r)//2

#         if arr[mid]==x:
#             ans=mid
#             r=mid-1

#         elif arr[mid]<x:
#             l=mid+1
        
#         else:
#             r=mid-1
    
#     return ans

# arr=list(map(int,input("Enter the num: ").split()))
# x=int(input("Enter num: "))

# result=first_occ(arr,x)
# print(result)


# # LAST MOST

# def Last_occ(arr, x):
#     l=0
#     r=len(arr)-1
#     ans=-1

#     while l<=r:
#         mid=(l+r)//2

#         if arr[mid]==x:
#             ans=mid
#             l=mid+1
        
#         elif arr[mid]<x:
#             l=mid+1
#         else:
#             r=mid-1
    
#     return ans
# arr=list(map(int,input("Enter the num: ").split()))
# x=int(input("Enter num: ")) 

# result=Last_occ(arr,x)
# print(result)


# # COUNT OCCURANCE  (Think not code like :: first occurance , last occurance ..Formula::first-last+1) :-

# def count_occurance(arr,x):
#     # First

#     l=0
#     r=len(arr)-1
#     first=-1

#     while l<=r:
#         mid=(l+r)//2

#         if arr[mid]==x:
#             first=mid
#             r=mid-1
        
#         elif arr[mid]<x:
#             l=mid+1
        
#         else:
#             r=mid-1
    

#     # Last

#     l=0
#     r=len(arr)-1
#     last=-1

#     while l<=r:
#         mid=(l+r)//2

#         if arr[mid]==x:
#             last=mid
#             l=mid+1
        
#         elif arr[mid]<x:
#             l=mid+1
        
#         else:
#             r=mid-1
    
    
#     if first==-1:
#         return 0
    
#     return last-first +1

# arr = list(map(int, input("Enter sorted array: ").split()))
# x = int(input("Enter element: "))

# print("Count:", count_occurance(arr, x))











































