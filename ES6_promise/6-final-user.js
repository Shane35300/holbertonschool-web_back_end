import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const signUpPromise = signUpUser(firstName, lastName);
  const uploadPromise = uploadPhoto(fileName);
  return Promise.allSettled([signUpPromise, uploadPromise]).then((results) => {
    const formattedResults = results.map((result) => ({
      status: result.status,
      value: result.status === 'fulfilled' ? result.value : result.reason,
    }));
    return formattedResults;
  }).catch((error) => {
    // Traitement des erreurs ici, si nécessaire
    console.error("Une erreur s'est produite:", error);
    throw error; // Vous pouvez choisir de rejeter l'erreur à ce niveau, si nécessaire
  });
}
