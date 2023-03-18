#Student Registration

students=["Ayşe Yılmaz","Fatma Şimşek","Deniz Çiçek","Dilan Kaplan","Ahmet Ayvaz"]
number=[1,2,3,4]
print(students)

#öğrenci ekleme:(append)

def student_registration ():
    student = input("Kaydetmek istediğiniz öğrencinin adını ve soyadını giriniz:")
    students.append(student) 

student_registration ()
print(students)

students.append("Mehmet Emin")
print(students)

#birden fazla öğrenci ekleme:

def register_multiple():
    howMany= int(input("Kaydetmek istediğiniz öğrenci sayısını giriniz: "))
    for i in range(howMany):
        print(students)
        register_multiple()

#birden fazla öğrenci silme :
def multiple_delete():
    howMany = int(input("Silmek istediğiniz öğrenci sayısını giriniz:"))
    i=0
    while i < students:
        i+=1
        print(students)
        multiple_delete()
#öğrenci silme(remove):

students=["Ayşe Yılmaz","Fatma Şimşek","Deniz Çiçek","Dilan Kaplan","Ahmet Ayvaz"]
print(students)

def student_delete():
    delete = input("Silmek istediğiniz öğrencinin adını ve soyadını giriniz: ")
    students.remove(delete)
print(students)
student_delete()

#tek tek yazdırma:

def print_person():
    print("Yazdırmak istediğiniz kişilerin adlarını ve soyadlarını giriniz")
for student in students:
    print(students)
print_person()

#numara öğrenme:
def student_number():
    sayi = int(input("Numarasını öğrenmek istediğiniz öğrencinin adını ve soyadını giriniz: "))
    print(students[sayi])
    for i in students:
     print( f"{i} - {students[i]}")
