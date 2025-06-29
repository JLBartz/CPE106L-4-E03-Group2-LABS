"""
File: student.py
Resources to manage a student's name and test scores.
"""

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

import random

def main():
    """Demonstrates comparison, shuffling, and sorting of students."""
    
    # Create several Student objects
    students = [
        Student("Lorenz", 3),
        Student("Albert", 3),
        Student("Ivan", 3),
        Student("Justin", 3),
        Student("Lowell", 3)
    ]
    
    # Set sample scores
    for student in students:
        for i in range(1, 4):
            student.setScore(i, random.randint(70, 100))  # random scores

    print("Original list (before shuffle):\n")
    for s in students:
        print(s)
    print("\n")
    # Shuffle the list
    random.shuffle(students)
    print("Shuffled list:\n")
    for s in students:
        print(s)
    print("\n")
    # Sort the list (by name using __lt__)
    students.sort()
    print("Sorted list (by name):\n")
    for s in students:
        print(s)

if __name__ == "__main__":
    main()

