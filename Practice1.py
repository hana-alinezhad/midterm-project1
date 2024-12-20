from PyQt6.QtWidgets import QApplication , QBoxLayout ,QLabel , QButtonGroup , QComboBox , QVBoxLayout , QLineEdit , QCheckBox , QWidget , QMessageBox , QPushButton , QRadioButton
import sys

class Register(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("NEW MEMBERR")
        self.label_fname = QLabel("Fist name: ")
        self.entry_fname = QLineEdit()
        self.label_Mname = QLabel("Middle name: ")
        self.entry_Mname = QLineEdit()
        self.label_lname = QLabel("Last name: ")
        self.entry_lname = QLineEdit()
        self.label_Ncode = QLabel("National code: ")
        self.entry_Ncode = QLineEdit()
        self.label_birthdate = QLabel("Birth date: ")
        self.entry_birthdate = QLineEdit()
        self.label_nationality = QLabel("Nationality: ")
        self.entry_nationality = QLineEdit()

        #Radio
        self.label_gender = QLabel("Gender:")
        self.male = QRadioButton("Male")
        self.female = QRadioButton("Female")
        self.other = QRadioButton("Other")
        self.notsay = QRadioButton("Prefer not to say")
        self.label_type = QLabel("Log in as a: ")
        self.teacher = QRadioButton("Teacher")
        self.student = QRadioButton("Student")
        self.label_education = QLabel("Education:")
        self.diploma = QRadioButton("Diploma")
        self.associate = QRadioButton("Associate degree")
        self.bachelor = QRadioButton("Bachelor degree")
        self.doctrol = QRadioButton("Doctrol degree")


        #check_box
        


        layout = QVBoxLayout()
        layout.addWidget(self.label_fname)
        layout.addWidget(self.entry_fname)
        layout.addWidget(self.label_Mname)
        layout.addWidget(self.entry_Mname)
        layout.addWidget(self.label_lname)
        layout.addWidget(self.entry_lname)
        layout.addWidget(self.label_Ncode)
        layout.addWidget(self.entry_Ncode)
        layout.addWidget(self.label_birthdate)
        layout.addWidget(self.entry_birthdate)
        layout.addWidget(self.label_nationality)
        layout.addWidget(self.entry_nationality)
        layout.addWidget(self.label_gender)
        layout.addWidget(self.male)
        layout.addWidget(self.female)
        layout.addWidget(self.other)
        layout.addWidget(self.notsay)
        layout.addWidget(self.label_type)
        layout.addWidget(self.teacher)
        layout.addWidget(self.student)
        layout.addWidget(self.label_education)
        layout.addWidget(self.diploma)
        layout.addWidget(self.associate)
        layout.addWidget(self.bachelor)
        layout.addWidget(self.doctrol)            



        self.setLayout(layout)

    def save_information(self):
        fist_name = self.entry_fname
        last_name = self.entry_lname
        middle_name = self.entrry_Mname
        national_code = self.entry_Ncode
        birth_date = self.entry_birrthdate
        nationality = self.entry_nationality
        gender = "unknown"
        if self.male.isChecked():
            gender = "Male"
        elif self.female.isChecked():
            gender = "Female"
        elif self.other.isChecked():
            gender = "other"
        elif self.other.isChecked():
            gender = "Prefer not to say"

        type = "unknown"
        if self.teacher.isChecked():
            type = "Teacher"
        elif self.student.isChecked():
            type = "Student"
        
        education = "unknown"
        if self.diploma.isChecked():
            education = "Diploma"
        elif self.associate.isChecked():
            education = "Associate degree"
        elif self.bachelor.isChecked():
            education = "Bachelor degree"
        elif self.doctrol.isChecked():
            education = "Doctrol degree"
        
        


             

    
            
app = QApplication(sys.argv)
window = Register()
window.show()
sys.exit(app.exec())
    
        

