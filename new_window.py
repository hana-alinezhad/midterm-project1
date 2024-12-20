from PyQt6.QtWidgets import QApplication , QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
import sys
class StudentForm (QWidget):
    def __init__(self) :
        super().__init__()
        self.setWindowTitle("Student Information form")
        self.labelname = QLabel("Name: ")
        self.entryname = QLineEdit()
        self.label_lastname = QLabel ("Last name: ")
        self.entry_lastname = QLineEdit()
        self.label_branch = QLabel("Branch: ")
        self.entry_branch = QLineEdit()
        self.lable_birthdate = QLabel("Birth date: ")
        self.entry_birthdate = QLineEdit()
        self.button_submit = QPushButton("Show Information")
        self.button_submit.clicked.connect(self.show_information)
        self.label_result = QLabel(' ')

        layout = QVBoxLayout()
        layout.addWidget(self.labelname)
        layout.addWidget(self.entryname)
        layout.addWidget(self.label_lastname)
        layout.addWidget(self.entry_lastname)
        layout.addWidget(self.label_branch)
        layout.addWidget(self.entry_branch)
        layout.addWidget(self.lable_birthdate)
        layout.addWidget(self.entry_birthdate)
        layout.addWidget(self.button_submit)
        layout.addWidget(self.label_result)
        self.setLayout(layout)

    def show_information(self):
        name = self.entryname.text()
        last_name = self.entry_lastname.text()
        branch = self.entry_branch.text()
        birthdate = self.entry_birthdate.text()

        #return f"Name:{name} , Last name:{last_name} , Branch:{branch} , Birthdate:{birthdate}"
        self.label_result.setText(f"Name:{name} , Last name:{last_name} , Branch:{branch} , Birthdate:{birthdate}")
            
app = QApplication (sys.argv)  
form = StudentForm()
form.show()
app.exec()  
                       
    
