export function randomString(length) {
  var result = "";
  var characters =
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
  var charactersLength = characters.length;
  for (var i = 0; i < length; i++) {
    result += characters.charAt(Math.floor(Math.random() * charactersLength));
  }
  return result;
}

export function randomEmail() {
  return `${randomString(10)}@gmail.com`;
}

function getRandom() {
  return 2 * Math.random() - 1;
}

export function randomSamples(lat=20.995, lng=105.845474, delta=0.1, n_samples=1000){
  const results = []
  for (let i = 0; i < n_samples; i++) {
    results.push({
      "id": randomString(10),
      "position": {
        "lat": lat + getRandom() * delta, 
        "lng": lng + getRandom() * delta
      },
      "score": 3 + getRandom() * 2,
      "temperature": 20 + getRandom() * 20,
      "humidity": 50 + getRandom() * 50,
      "rain": 400 + getRandom() * 200,
      "ppm": 400 + getRandom() * 200
    })
  }

  return results
}
