# Student Gradebook CLI (Extra-A)

## 1. Overview
This is a Python CLI application to manage a student gradebook.  
Users can add, update, delete, and view courses, and calculate weighted GPA overall and by semester.  
All data is stored in `gradebook.json` and automatically loaded when the program starts.

## 2. Folder Structure
```text
gradebook-cli/
├── main.py
├── gradebook.py
├── storage.py
├── utils.py
├── gradebook.json
└── README.md
```

## 3. Features Implemented
- Add course (code, name, credits, semester, score)
- Update course by course code
- Delete course by course code
- View gradebook in table format
- Calculate GPA:
  - Overall weighted GPA (by credits)
  - GPA by semester
- Persistent storage with JSON (`load_data`, `save_data`)
- Input validation:
  - No empty input
  - No duplicate course codes
  - Score range validation
  - Credits must be positive

## 4. How to Run
### Requirements
- Python 3.x

### Run
```bash
python main.py
```

## 5. Sample Data
The file `gradebook.json` includes 3 courses:
1. Introduction of Technology — Code: AU005.2  
2. English for Purpose — Code: AU004.2  
3. Sustainable Development — Code: AU008.2  

## 6. Testing
Tested cases:
- Display menu correctly
- View gradebook with existing courses
- Update a course successfully
- Delete a course successfully
- Calculate overall GPA and GPA by semester
- Reopen the program and confirm data persistence

Screenshots are included in `report.pdf`.

---
**Author:** Nguyen Luong Nhat (AUS14988)  
**Year:** 2025
