# Student = [id, name, DoB]
# Course = [id, name,]
# nb = [Number of students/courses, etc.]
# stlst = [Student list, etc.]
# cslst = [Course list, etc.]

def std_inpf(stlst):
    print("---")
    nb = int(input("Number of students: "))
    for idx in range (nb):
        print(f"Student number: {idx}")
        n = input ("Student name: ")
        i = input ("Student id: ")
        b = input ("Student DoB: ")
        print("---")
        stlst.append([n, i, b])

def cst_inpf(cslst):
    print("---")
    nb = int(input("Number of courses: "))
    for idx in range (nb):
        print(f"Course number: {idx}")
        n = input ("Course id: ")
        i = input ("Course name: ")
        print("---")
        cslst.append([n, i, {}])

def mrk_inpf(cslst, stlst):
    print("---")
    csid = input("Select the course by course ID: ")
    cs = [cs for cs in cslst if cs[0] == csid] [0]
    print("+++")
    print("Please insert student marks: ")
    for st in stlst:
        print("+++")
        mrk = float(input(f"Student {st[1]} [{st[0]}] mark: "))
        cs[2][st[0]] = mrk
    print("---")

def std_lstf(stlst):
    print("---")
    print(f"There are {len(stlst)} students in system: ")
    for st in stlst:
        print("+++")
        print(f"Student id: {st[0]}")
        print(f"Student name: {st[1]}")
        print(f"Student DoB: {st[2]}")
    print("---")

def cst_lstf(cslst):
    print("---")
    print(f"There are {len(cslst)} courses in system: ")
    for cs in cslst:
        print("+++")
        print(f"Course id: {cs[0]}")
        print(f"Course name: {cs[1]}")
        print(f"Course marks: ")
        for k, v in cs[2].items():
            print(f"Student [{k}] has mark: {v}")
    print("---")

if __name__ == "__main__":
    stlst = []
    cslst = []

    while True:
        opt = int(input(
                  
        """
        [Students mark management]
        1. Insert students.
        2. Insert courses.
        3. List students info.
        4. List courses info.
        5. Add mark.
        6. List mark.
        7. Exit.
        Opt:

        """))

        if opt == 1:
            std_inpf(stlst)
        elif opt == 2:
            cst_inpf(cslst)
        elif opt == 3:
            std_lstf(stlst)
        elif opt == 4:
            cst_lstf(cslst)
        elif opt == 5:
            mrk_inpf(cslst, stlst)
        elif opt == 6:
            cst_lstf(cslst)
        elif opt == 7:
            break
        else:
            print("Option not supported")