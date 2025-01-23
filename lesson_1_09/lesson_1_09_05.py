# Урок 9: Принципи SOLID в ООП.
# ➢ Принцип інверсії залежностей (Dependency Inversion Principle).
# Класи вищого рівня не повинні залежати від класів нижчого рівня
# Обидва типи класів повинні залежати від абстракцій

from enum import Enum
from abc import ABC, abstractclassmethod

class Teams(Enum):
    TEAM_RED = 1
    TEAM_BLUE = 2
    TEAM_GREEN = 3

class TeamMembershipLookUp:
    @abstractclassmethod
    def find_all_students(self, team):
        pass

class Student:
    def __init__(self, name):
        self.name = name

class TeamMemberShips(TeamMembershipLookUp):
    def __init__(self):
        self.team_memberships = []

    def add_team_memberships(self, student, team):
        self.team_memberships.append((student, team))

    def find_all_students(self, team):
        for members in self.team_memberships:
            if members[1] == team:
                yield members[0].name

class Analysis:
    def __init__(self, team_student_membership):
        memberships = team_student_membership.team_memberships
        for member in memberships:
            if member[1] == Teams.TEAM_RED:
                print(f"{member[0].name} is in RED team")

student_1 = Student('Mykhailo')
student_2 = Student('Michael')
student_3 = Student('Mike')

team_memberships = TeamMemberShips()

team_memberships.add_team_memberships(student_1, Teams.TEAM_RED)
team_memberships.add_team_memberships(student_2, Teams.TEAM_RED)
team_memberships.add_team_memberships(student_3, Teams.TEAM_RED)

Analysis(team_memberships)