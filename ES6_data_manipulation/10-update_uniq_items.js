export default function updateUniqueItems(mapObj) {
  if (!(mapObj instanceof Map)) {
    throw new Error('Cannot process');
  }
  mapObj.forEach((value, key) => {
    if (value === 1) {
      mapObj.set(key, 100);
    }
  });
  return mapObj;
}
