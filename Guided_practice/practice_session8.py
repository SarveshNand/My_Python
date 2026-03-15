# Take your get_average() and assign_grade() functions from before and turn them into methods inside the Student class. Then:

# aryan = Student("Aryan", [88, 92, 79])
# print(aryan.get_average())  # 86.33
# print(aryan.assign_grade()) # B

class Student:
  def __init__(self, name, scores):
    self.name = name
    self.scores = scores

  def __str__(self):
    return f"Student: {self.name} | Average: {self.get_average():.02f} | Grade: {self.assign_grade()}"

  def get_average(self):
    avg_score = sum(self.scores) / len(self.scores)
    return avg_score

  def assign_grade(self):
    avg = self.get_average()
    if avg >= 90:
      return 'A'
    elif avg >= 75:
      return 'B'
    elif avg >= 60:
      return 'C'
    else:
      return 'F'
    
aryan = Student("Aryan", [88, 92, 79])
print(aryan)