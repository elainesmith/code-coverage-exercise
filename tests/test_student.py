from student.student import Student, get_student_with_more_classes

def test_init():
    name = "Ada Lovelace"
    level = "sophomore"
    courses = ["mathematics", "foundations of computing"]

    ada = Student(name, level, courses)

    assert ada.name == name
    assert ada.level == level
    assert ada.courses == courses

def test_add_class():
    new_class = 'Intro to Feminism'
    charles = Student("Charles Babbage", "senior", ["mechanical engineering"])
    charles.add_class(new_class)

    assert len(charles.courses) == 2
    assert new_class in charles.courses

def test_get_num_classes():
    george = Student("George Byron", "senior", ["advanced poetry"])

    assert george.get_num_classes() == 1

def test_summary():
    anne = Student(
        "Anne Byron",
        "senior",
        ["theory of religion", "theory of morality"]
    )

    assert anne.summary() == "Anne Byron is a senior enrolled in 2 classes"

def test_get_student_b_with_more_classes():
    charles = Student("Charles Babbage", "senior", ["mechanical engineering"])
    ada = Student(
        "Ada Lovelace",
        "sophomore",
        ["mathematics", "foundations of computing"]
    )
    # Act
    output = get_student_with_more_classes(charles, ada)

    # TODO: write assertions
    assert output == ada

def test_get_student_a_with_more_classes():
    mary = Student("Mary Smith", "junior", ["mechanical engineering", "python basics"])
    david = Student("David Brown", "sophomore", ["mathematics"])
    # Act
    output = get_student_with_more_classes(mary, david)

    # TODO: write assertions
    assert output == mary
def test_init_no_courses():
    # Arrange
    name = "Elaine"
    level = "Unit 1"

    # Act
    Elaine = Student(name, level)

    # Assert 
    assert Elaine.name == name
    assert Elaine.level == level