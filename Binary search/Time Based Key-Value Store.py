"""
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
"""
class TimeMap:

    def __init__(self):
        self.data={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key]=[]
        self.data[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""

        liste=self.data[key]
        left=0
        right=len(liste)-1
        value=""
        while left <= right:
            mid=(right+left)//2
            if timestamp < liste[mid][0]:
                right=mid-1
            elif timestamp>=liste[mid][0]:
                value=liste[mid][1]
                left=mid+1
        return value
        


                

                

