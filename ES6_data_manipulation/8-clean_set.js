export default function cleanSet(set, startString) {
  let str = '';
  if (startString !== '') {
    set.forEach((elem) => {
      if (elem.startsWith(startString)) {
        if (elem.length > startString.length) {
          if (str !== '') {
            str += '-';
          }
          for (let i = startString.length; i < elem.length; i += 1) {
            str += elem[i];
          }
        }
      }
    });
  }
  return str;
}
