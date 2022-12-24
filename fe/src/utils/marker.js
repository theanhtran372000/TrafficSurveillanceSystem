import { deg2rad, coordinateToM } from "./coordinates";

const distPerLat = 111.12 * 10e3 // meter
const radiusAtEquator = 6378 * 10e3 // meter
const equatorPerimeter = 2 * Math.PI * radiusAtEquator
const distPerLongEquator = equatorPerimeter / 360 // meter

function meterToCoordinate(meter, marker) {
  return {
    lat: meter / distPerLat, 
    lng: distPerLongEquator * Math.cos(deg2rad(marker.lat))
  }
}

function getMinMaxCoordinates(markers){
  let minLat = -180
  let maxLat = 180
  let minLng = 0
  let maxLng = 180

  markers.forEach(marker => {
    if (marker.lat > maxLat) maxLat = marker.lat
    if (marker.lat < minLat) minLat = marker.lat
    if (marker.lng > maxLng) maxLng = marker.lng
    if (marker.lng < minLng) minLng = marker.lng
  });

  return minLat, maxLat, minLng, maxLng
}

function weightedSum(markers) {
  const sum = 0
  for(let i = 0; i <= markers.length; i++){
    sum += markers[i].score
  }
  
  const newLat = 0
  for(let i = 0; i <= markers.length; i++){
    newLat += markes[i].lat * markers[i].score / sum
  }
  
  const newLng = 0
  for(let i = 0; i <= markers.length; i++){
    newLng += markes[i].lng * markers[i].score / sum
  }

  return {
    'lat': newLat,
    'lng': newLng
  }
}


export function scanMarker(markerList, radius, step) {
  return
}
