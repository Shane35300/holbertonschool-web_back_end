import { uploadPhoto, createUser } from "./utils.js";

export default function handleProfileSignup() {
	Promise.all([uploadPhoto(), createUser()]).then((results) => {
		const up_ph = results[0];
		const cr_us = results[1];
		const str = up_ph.body + " " + cr_us.firstName + " " + cr_us.lastName;
		console.log(str);
	});
}
