import pandas as pd
class course():
    def __init__(self,id,title,professor,capacity,description, meetingTimes, meetingLocation):
        self.id = id
        self.title = title
        self.professor = professor
        self.capacity = capacity
        self.description = description
        self.meetingTimes = meetingTimes
        self.meetingLocation = meetingLocation
    def getDict(self):
        return {"id": self.id, "title": self.title, "professor" : self.professor,
                 "capacity": self.capacity, "description" : self.description,
                 "meetingTimes": self.meetingTimes, "meetingLocation": self.meetingLocation}
    
def populateCourses():
    course_df = pd.read_csv("../data/cure_courses_2023.csv")
    courseDict = {i : course(row['id'],row['title'],row['professor'],row['capacity'],
                    row['description'],row['meetingTimes'],row['meetingLocation']).getDict()
                    for i, row in course_df.iterrows()}
    print(courseDict)
    return courseDict

if __name__ == "__main__":
    populateCourses()