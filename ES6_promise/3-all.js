import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  Promise.all([uploadPhoto(), createUser()]).then((results) => {
    const upPh = results[0];
    const crUs = results[1];
    const str = `${upPh.body} ${crUs.firstName} ${crUs.lastName}`;
    console.log(str);
  });
}