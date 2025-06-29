class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name

    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]

    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self.scores)

    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)

    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))

    def __eq__(self, other):
        """Returns True if names are equal."""
        return self.name == other.name

    def __lt__(self, other):
        """Returns True if this student's name is less than the other's name."""
        return self.name < other.name

    def __ge__(self, other):
        """Returns True if this student's name is greater than or equal to the other's name."""
        return self.name >= other.name


def main():
    """A simple test."""
    student1 = Student("Albert", 5)
    student2 = Student("Ivan", 5)
    student3 = Student("Albert", 5)

    for i in range(1, 6):
        student1.setScore(i, 90)
        student2.setScore(i, 80)
        student3.setScore(i, 95)

    print("Student 1:", student1)
    print("Student 2:", student2)
    print("Student 3:", student3)
    print()

    # Test equality
    print("student1 == student2:", student1 == student2)  # False
    print("student1 == student3:", student1 == student3)  # True

    # Test less than
    print("student2 < student1:", student2 < student1)    # True (Anna < Ken)

    # Test greater than or equal
    print("student1 >= student2:", student1 >= student2)  # True (Ken >= Anna)
    print("student2 >= student3:", student2 >= student3)  # False (Anna < Ken)


if __name__ == "__main__":
    main()
