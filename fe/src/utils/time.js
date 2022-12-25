import constants from "@/constants"

export function getTimeRange(delta, unit) {
  console.log(`Time range: ${delta} ${unit}`)
  const date = new Date()
  const timeMilis = date.getTime()

  var addMilis = delta
  if (unit === constants.__time_unit__.SECOND) {
    addMilis *= 1000
  } 
  else if (unit === constants.__time_unit__.MINUTE) {
    addMilis *= 60 * 1000
  } 
  else {
    addMilis *= 60 * 60 * 1000
  }

  return {
    start: formatTime(new Date(timeMilis - addMilis)),
    end: formatTime(new Date(timeMilis + addMilis))
  }
}

export function formatUrl(timeRange){
  return `/cameras/events/${timeRange.start.replace(/:/g, '%3A')}/${timeRange.end.replace(/:/g, '%3A')}`
}

export function formatTime(date){
  return date.toISOString()
}
