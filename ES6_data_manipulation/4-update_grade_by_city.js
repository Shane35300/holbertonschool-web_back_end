export default function updateStudentGradeByCity(arrayOfObj, city, newGrades) {
  const newArray = arrayOfObj
    .filter((obj) => obj.location === city)
    .map((obj) => {
      const updatedObj = { ...obj };
      let trap = 0;
      for (let i = 0; i < newGrades.length; i += 1) {
        if (obj.id === newGrades[i].studentId) {
          updatedObj.grade = newGrades[i].grade;
          trap = 1;
        }
      }
      if (trap === 0) {
        updatedObj.grade = 'N/A';
      }
      return updatedObj;
    });
  return newArray;
}
