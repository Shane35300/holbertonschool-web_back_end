export default function getListStudentIds(arrayOfObj) {
  let array = [];
  if (Array.isArray(arrayOfObj)) {
    array = arrayOfObj.map((obj) => obj.id);
  }
  return array;
}
