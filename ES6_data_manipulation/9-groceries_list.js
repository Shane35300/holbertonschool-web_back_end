export default function groceriesList() {
  // Créer une nouvelle carte (Map) avec les articles d'épicerie et leurs quantités
  const groceryMap = new Map([
    ['Apples', 10],
    ['Tomatoes', 10],
    ['Pasta', 1],
    ['Rice', 1],
    ['Banana', 5],
    // Ajoutez d'autres articles si nécessaire
  ]);

  // Renvoyer la carte des courses
  return groceryMap;
}
