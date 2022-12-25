# CLI application to perform tasks on csv file of employee details
from pprint import pprint
from task_one import do_task_one
from task_two import do_task_two


if __name__ == '__main__':
    print("Employees who's salary is >9000")
    print(do_task_one())
    print()
    print("\nEmployee who's department is within range (30 - 110) "
          "AND who's salary is >4200")
    pprint(do_task_two())
