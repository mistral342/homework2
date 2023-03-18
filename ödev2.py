#Student Registration
   
students=["Ayşe Yılmaz","Fatma Şimşek","Deniz Çiçek","Dilan Kaplan","Ahmet Ayvaz"]
print(students)
number=[1,2,3,4,5]

print(number[0],students[0])
print(number[1],students[1])
print(number[2],students[2])
print(number[3],students[3])
print(number[4],students[4])


#listeye öğrenci ekleme

# insert
students=["Ayşe Yılmaz","Deniz Çiçek","","Ahmet Ayvaz"]
print(students)
students.insert(1,"Veli Aslan")
print(students)

#append
students.append ("Mehmet Umut")
print(students)

#extend(birden fazla öğrenci ekleme)
students.extend(["Veli Aslan","Mehmet Umut"])
print(students)

#listeden öğrenci silme
students=["Ayşe Yılmaz","Fatma Şimşek","Deniz Çiçek","Dilan Kaplan","Ahmet Ayvaz"]
#del
print(students)
del students [4]
print(students)
print("*********************************")
#pop
print(students)
students.pop(2)
print(students)
print("**********************************")
#remove
students=["Ayşe Yılmaz","Fatma Şimşek","Deniz Çiçek","Dilan Kaplan","Ahmet Ayvaz"]
students.remove ("Dilan Kaplan")
print(students)
print("************************************")

#tek tek ekrana yazdırma 

students=["Ayşe Yılmaz","Fatma Şimşek","Deniz Çiçek","Dilan Kaplan","Ahmet Ayvaz"]
for student in students:
    print(student)

print("*******************")

#index sayısına göre tek tek yazdırma(range)

for x in range(len(students)):
    print(students[x])

print ("**************************")

def öğrenci_ekle (students):
    students=["Ayşe Yılmaz","Fatma Şimşek","Deniz Çiçek","Dilan Kaplan","Ahmet Ayvaz"]
   
    print("eklemek istediğiniz öğrencinin adını ve soyadını giriniz")
    students=students.append("Mehmet Umut")
  


def students(ad, soyad):
  print("Adınız: " + ad + ", Soyadınız: " + soyad)
  students = ["Ayşe Yılmaz","Fatma Şimşek","Deniz Çiçek","Dilan Kaplan","Ahmet Ayvaz"]



