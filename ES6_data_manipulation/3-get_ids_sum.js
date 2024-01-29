export default function getStudentIdsSum(arrayOfObj) {
  const value = arrayOfObj.reduce((sum, obj) => sum + obj.id, 0);
  return value;
}
