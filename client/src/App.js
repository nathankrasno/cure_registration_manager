import React, {useState, useEffect} from 'react'
import './styles/App.css'

const CourseList = ({ courses }) => {
  return (
    <div>
      {courses.map(course => (
        <div key={course.id} className="course-item">
          <h2>{course.title}</h2>
          <p>{course.description}</p>
          <p>Professor: {course.professor}</p>
          <p>Capacity: {course.capacity}</p>
          <p>Course ID: {course.id}</p>
          <p>Meeting Times: {course.meetingTimes}</p>
          <p>Meeting Location: {course.meetingLocation}</p>
        </div>
      ))}
    </div>
  );
};

function App() {
  const [courses, setCourses] = useState([])
  useEffect(() => {
    fetch("/courses").then(
      res => res.json(),
    ).then(data => {
      const courseList = Object.values(data); // Extract the values of the outer dictionary
      setCourses(courseList);
      console.log(courseList);
    })
  }, [])
   
    return (
      <div className='course-container'>
        <CourseList className="course-item" courses={courses} />
      </div>
    );
  }
  
  export default App;