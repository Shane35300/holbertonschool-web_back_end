export default function getStudentsByLocation(arrayOfObj, city) {
  const arrayFiltered = arrayOfObj.filter((obj) => obj.location === city);
  return arrayFiltered;
}
