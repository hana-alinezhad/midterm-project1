from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QMessageBox, QRadioButton, QComboBox , QCheckBox
import sys


class Teacher(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Record Information")
        
        self.labelname = QLabel("First name: ")
        self.entryname = QLineEdit()
        self.label_lastname = QLabel("Last name: ")
        self.entry_lastname = QLineEdit()
        self.label_experience = QLabel("How many years you have been a teacher? ")
        self.entry_experience = QLineEdit()

        self.label_gender = QLabel("Gender: ")
        self.male_radio = QRadioButton("Male")
        self.female_radio = QRadioButton("Female")

        self.label_education = QLabel("Education:")
        self.education_checkboxes = [QCheckBox("Diploma"), QCheckBox("Associate degree"), QCheckBox("Bachelor degree"), QCheckBox("Doctoral degree")]

        self.job_combo = QComboBox()
        self.job_combo.addItem("Teacher")
        self.job_combo.addItem("Teacher Assistant")

        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_data)

        layout = QVBoxLayout()
        layout.addWidget(self.labelname)
        layout.addWidget(self.entryname)
        layout.addWidget(self.label_lastname)
        layout.addWidget(self.entry_lastname)
        layout.addWidget(self.label_experience)
        layout.addWidget(self.entry_experience)
        layout.addWidget(self.label_gender)
        layout.addWidget(self.male_radio)
        layout.addWidget(self.female_radio)
        layout.addWidget(self.label_education)
        
        for checkbox in self.education_checkboxes:
            layout.addWidget(checkbox)
        
        layout.addWidget(QLabel("Type of teaching: "))
        layout.addWidget(self.job_combo)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def save_data(self):
        firstname = self.entryname.text()
        lastname = self.entry_lastname.text()
        experience = self.entry_experience.text()
        gender = 'unknown'
        
        if self.male_radio.isChecked():
            gender = 'male'
        elif self.female_radio.isChecked():
            gender = 'female'
        
        education = [checkbox.text() for checkbox in self.education_checkboxes if checkbox.isChecked()]
        teaching_type = self.job_combo.currentText()
        
        with open('main.txt', 'w') as file:
            file.write(f"First name: {firstname}\nLast name: {lastname}\nExperience: {experience}\nGender: {gender}\nEducation: {', '.join(education)}\nType of teaching: {teaching_type}\n")
        
        QMessageBox.information(self, "Information", "******** Information was saved successfully ********")


app = QApplication(sys.argv)
window = Teacher()
window.show()
sys.exit(app.exec())
