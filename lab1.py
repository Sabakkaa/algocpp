import random

def increaseSort(arr):
    n = len(arr)
    for i in range(n):
        min_arr = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_arr]:
                min_arr = j
        arr[i],arr[min_arr] = arr[min_arr],arr[i]



def decreasingSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] < arr[j]:
                arr[i],arr[j] = arr[j],arr[i]




def TelephoneSort(phone):
    n = len(phone)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if phone[j] < phone[min_index]:
                min_index = j
        phone[i], phone[min_index] = phone[min_index], phone[i]


phone = ["23-32-65", "98-76-54", "12-34-56", "67-67-78", "89-94-02", "23-45-67", "87-90-41"]
print("Неотсортированный список телефонов:", phone)
TelephoneSort(phone)
print("Отсортированный список телефонов:", phone)
