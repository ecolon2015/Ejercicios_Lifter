
#Eduardo Colon
#Dada n cantidad de notas de un estudiante, calcular:
#Cuantas notas tiene aprobadas (mayor a 70).
#Cuantas notas tiene desaprobadas (menor a 70).
#El promedio de todas.
#El promedio de las aprobadas.
#El promedio de las desaprobadas.@

#grades_total 
#grades_counter
#current_grade
#passing_grades_count
#failing_grades_count
#passing_grades_average
#failing_grade_average
#overall_grade_average

grades_counter = 1
passing_grades_count = 0
failing_grades_count = 0
passing_grades_average = 0
failing_grade_average = 0
overall_grade_average = 0
grades_total = 0

grades_total = int(input ("Enter the number of grades "))

while grades_counter <= grades_total:
    current_grade = int(input ("Enter grade number "))
    print("the grade counter is" ,grades_counter ) 
    grades_counter =grades_counter + 1
    if current_grade < 70:
        failing_grades_count = failing_grades_count + 1
        failing_grade_average = failing_grade_average + current_grade
    else:
        passing_grades_count = passing_grades_count + 1
        passing_grades_average = passing_grades_average + current_grade
    overall_grade_average = overall_grade_average  + (current_grade / grades_total)

failing_grade_average = failing_grade_average / failing_grades_count

passing_grades_average = passing_grades_average / passing_grades_count

print("the student has this number of passing grades ", passing_grades_count)
print("this is the average of passing grades ",passing_grades_average)
print("the student has this number of failing grades ", failing_grades_count )
print("this is the average of failing grades ", failing_grade_average)
print("This is the overall average of grades ", overall_grade_average)




