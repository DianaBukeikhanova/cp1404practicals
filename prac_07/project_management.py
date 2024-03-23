"""
Project Management Program
Estimate: 45 minutes
Actual: 125 minutes
"""
import datetime
from project import Project

MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""


def main():
    """Process project information based on user's choice."""
    filename = input(">>> ")
    print("Welcome to Pythonic Project Management")
    projects = load_projects(filename)
    print(f"Loaded {len(projects)} projects from {filename}")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            load_projects(filename)
        elif choice == "S":
            save_projects(filename, projects)
        elif choice == "D":
            finished_projects = []
            unfinished_projects = []
            for project in projects:
                if project.is_unfinished():
                    unfinished_projects.append(project)
                else:
                    finished_projects.append(project)
            sort_projects(unfinished_projects, "Incomplete projects:")
            sort_projects(finished_projects, "Complete projects:")
        elif choice == "F":
            filter_projects(projects)
        elif choice == "A":
            enter_new_project(projects)
        elif choice == "U":
            for i in range(len(projects)):
                print(f"{i} {projects[i]}")
            update_project(projects)
        print(MENU)
        choice = input(">>> ").upper()
    answer = input("Would you like to save to projects.txt? ").upper()
    if "Y" in answer:
        save_projects(filename, projects)
    else:
        new_file = input(">>> ")
        save_projects(new_file, projects)
    print("Thank you for using custom-built project management software.")


def enter_new_project(projects):
    """Ask the user for the inputs and add a new project to memory."""
    print("Let's add a new project")
    name = input("Name: ")
    while name == "":
        print("Input cannot be empty.")
        name = input("Name: ").title()
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))
    projects.append(Project(name, start_date, cost, priority, completion_percentage))
    return projects


def update_project(projects):
    """Choose a project, then modify the completion % and priority - leave blank to retain existing values."""
    valid_statement = True
    project_choice = int(input("Project choice: "))
    print(projects[project_choice])
    while project_choice > len(projects):
        print("Invalid index.")
        project_choice = int(input("Project choice: "))
    while valid_statement:
        try:
            new_percentage = int(input("New Percentage: "))
            new_priority = int(input("New priority: "))
            projects[project_choice].is_updated_percentage(int(new_percentage))
            projects[project_choice].is_updated_priority(int(new_priority))
            valid_statement = False
        except ValueError:
            print("Invalid input.")


def sort_projects(projects, text):
    """Sort projects into two groups: incomplete projects; completed projects, both sorted by priority"""
    projects.sort().__lt__(1)
    print(text)
    for project in projects:
        print(project)


def load_projects(filename):
    """Prompt the user for a filename to load projects from and load them."""
    projects = []
    in_file = open(filename, 'r')
    lines = in_file.readlines()
    for line in lines[1:]:
        parts = line.strip("\n").split("\t")
        name = parts[0]
        start_date = parts[1]
        priority = int(parts[2])
        cost = float(parts[3])
        completion_percentage = int(parts[4])
        project = Project(name, start_date, priority, cost, completion_percentage)
        projects.append(project)
    in_file.close()
    return projects


def filter_projects(projects):
    """Ask the user for a date and display only projects that start after that date, sorted by date."""
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered_projects = [project for project in projects if project.start_date > filter_date]
    filtered_projects.sort().__gt__(filter_date)
    for project in filtered_projects:
        print(project)


def save_projects(filename, projects):
    """Prompt the user for a filename to save projects to and save them."""
    with open(filename, 'w') as out_file:
        out_file.write("Name	Start Date	Priority	Cost Estimate	Completion Percentage\n")
        for project in projects:
            out_file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t"
                           f"{project.cost}\t{project.completion_percentage}\n")


main()
