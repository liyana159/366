import random

def load_student_ids(filename):
    
        with open(filename, 'r') as file:
            student_ids = [line.strip() for line in file if line.strip()]
        return student_ids
    


def viva_round(student_ids):
    
    
    random.shuffle(student_ids)
    viva_count = 1

    for student in student_ids:
        print(f"Viva #{viva_count}: {student}")
        viva_count += 1

def main():
    filename = 'std.txt'
    student_ids = load_student_ids(filename)

    viva_round(student_ids)

if __name__ == '__main__':
    main()

