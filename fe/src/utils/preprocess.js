export function formatMarkers(receivedMarkers) {
  const results = []
  receivedMarkers.forEach(marker => {
    results.push({
      "id": marker.id,
      "position": {
        "lat": marker.lat, 
        "lng": marker.lng  
      },
      "score": marker.event.score,
      "temperature": marker.event.temperature,
      "humidity": marker.event.humidity,
      "rain": marker.event.rain,
      "ppm": marker.event.ppm
    })
  });

  return results
}
