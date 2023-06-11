import React, {useState, useEffect} from 'react'

function App() {
  const [courses, setCourses] = useState([{}])
  useEffect(() => {
    fetch("/courses").then(
      res => res.json(),
    ).then(
      data => {
        setCourses(data)
        console.log(data)
      }
    )
  }, [])
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
          </div>
        ))}
      </div>
    );
  };
  
    return (
      <div>
        <h1>Course List</h1>
        <CourseList courses={courses} />
      </div>
    );
  }
  
  export default App;