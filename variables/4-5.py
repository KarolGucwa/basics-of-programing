###
# Calculates the final grade for a test based
# on the number of points obtained
#
def pts_to_grade(points):
    grade = ''
    if points >= 18:
        grade = 'Excellent'
    elif 18 > points >= 14 :
        grade = 'Good'
    elif 14 > points >= 10:
        grade = 'dostateczna'
    elif points <= 10:
        grade = 'niedostateczna'
    return grade

test_result = 9
final_grade = pts_to_grade(test_result)
print(f'You scored {test_result} points on the test. Your final grade is {final_grade}')