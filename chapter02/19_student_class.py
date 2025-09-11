class Student:
    """
    A class that represents a student's name

    Attrs: 
        firstname (str): First name
        lastname (str): Last name
    """
    def __init__(self, firstname: str, lastname: str):
        self.firstname = firstname
        self.lastname = lastname

def main():
    st = Student('Bob', 'Marley')
    print(f'First name: {st.firstname}')
    print(f'Last name: {st.lastname}')

if __name__ == '__main__':
    main()