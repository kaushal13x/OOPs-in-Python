# Topic: Class and Object in Python (OOPs - Day 1)
||Hostel Student Gate Pass Varification||
class GatePass:
    Name = None
    Enrollment = None
    RoomNo = None
    Purpose = None
    InDate = None
    OutTime = None
    InTime = None
    Hostel = None
    Signature = None


# Creating object (Instance)
kaushal = GatePass()

# Assigning values to attributes
kaushal.Name = "Kaushal Kumar"
kaushal.Enrollment = 224
kaushal.RoomNo = 314
kaushal.Purpose = "Semester Holiday So I am Going to My Home"
kaushal.InDate = "30-02-2026"
kaushal.OutTime = "9 PM"
kaushal.InTime = "7 PM"
kaushal.Hostel = "Singar Two"
kaushal.Signature = "kumarkaushalranjh"

# Printing values
print(kaushal.Name)
print(kaushal.RoomNo)
print(kaushal.Signature)
print(kaushal.InDate)

#Tips for print all valule in single time
kaushal.__dict__
Output ---
{'name': 'Kaushal Kumar',
 'Enrollment': 224,
 'RoomNo': 314,
 'Purpose': 'Semester Holiday So I am Goint to My Home',
 'InDate': '30 -02-2026',
 'OutTime': '9 PM',
 'InTime': '7 PM',
 'Hostel': 'Singar Two',
 'Signature': 'kumarkaushalranjh'}



