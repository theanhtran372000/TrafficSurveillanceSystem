<template>
  <div
    class="flex flex-row w-full h-screen"
  >
    <!-- Map display -->
    <div class="w-full mt-20 mb-6 mx-6 rounded-lg bg-gray p-8" style="flex: 2">
      <div class="w-full">
        <div class="w-full flex justify-between items-center">
          <h1 class="font-bold text-lg text-blue">Traffic Density Map</h1>
          <div class="flex items-center">
            <label class="font-normal text-blue underline cursor-pointer text-base mr-8" @click="createRandomSamples">
              Random 1000 samples
            </label> 
            <font-awesome-icon
              class="text-blue mr-4 cursor-pointer hover:text-dark_blue transition ease-in-out duration-500"
              icon="fa-solid fa-plus"
              @click="onCameraAdd"
            />
            <font-awesome-icon
              class="text-blue mr-4 cursor-pointer hover:text-dark_blue transition ease-in-out duration-500"
              icon="fa-solid fa-arrow-rotate-left"
              @click="onResetMap"
            />
          </div>
        </div>

        <div class="map w-full mt-2">
          <!-- Show maps -->
          <GMapMap 
            class="w-full object-cover border-2 border-blue"
            style="height: 360px" :center="mapCenter" :zoom="14">

            <GMapMarker
              v-for="marker, index in mapMarkers"
              :icon="{
                url: getMarkerColor(marker),
                scaledSize: {
                  width: 30,
                  height: 30
                }
              }"
              :position="{'lat': marker.position.lat, 'lng': marker.position.lng}"
              :clickable="true"
              :key="index"
              @click="onMarkerClick($event, marker)"
            />

          </GMapMap>

          <!-- Show note -->
          <div class="w-full mt-2 flex items-center justify-end">
            <div class="flex justify-center items-center">
              <div class="flex items-center mr-6">
                <font-awesome-icon class="text-normal text-green-600 mr-2" icon="fa-solid fa-location-dot" />
                <p class="font-normal text-blue text-base">Less than {{ lowerBound }}</p>
              </div>

              <div class="flex items-center mr-6">
                <font-awesome-icon class="text-base text-yellow-600 mr-2" icon="fa-solid fa-location-dot" />
                <p class="font-normal text-blue text-base">From {{ lowerBound }} to {{ upperBound }}</p>
              </div>

              <div class="flex items-center mr-6">
                <font-awesome-icon class="text-base text-red-600 mr-2" icon="fa-solid fa-location-dot" />
                <p class="font-normal text-blue text-base">More than {{ upperBound }}</p>
              </div>
              
            </div>
          </div>
        </div>
      </div>

      <!-- Analytics display -->
      <div class="w-full mt-2">
        <div class="w-full">
          <h1 class="font-bold text-lg text-blue">Analytics</h1>
          <div class="flex justify-between items-center pt-4">

            <div class="flex flex-col justify-center items-center">
              <h1
                class="font-bold text-3xl text-blue hover:text-dark_blue transition ease-in-out duration-500"
              >
                {{ mapMarkers.length }}
              </h1>
              <p class="font-normal text-base text-blue">Cameras</p>
            </div>

            <div class="flex flex-col justify-center items-center">
              <h1
                class="font-bold text-3xl text-blue hover:text-dark_blue transition ease-in-out duration-500"
              >
                {{ round(averageStats.score, 2) }}
              </h1>
              <p class="font-normal text-base text-blue">Avg. Density</p>
            </div>

            <div class="flex flex-col justify-center items-center">
              <h1
                class="font-bold text-3xl text-blue hover:text-dark_blue transition ease-in-out duration-500"
              >
              {{ round(averageStats.temperature, 2) }}
              </h1>
              <p class="font-normal text-base text-blue">Avg. Temp</p>
            </div>

            <div class="flex flex-col justify-center items-center">
              <h1
                class="font-bold text-3xl text-blue hover:text-dark_blue transition ease-in-out duration-500"
              >
              {{ round(averageStats.humidity, 2) }}
              </h1>
              <p class="font-normal text-base text-blue">
                Avg. Humi
              </p>
            </div>

            <div class="flex flex-col justify-center items-center">
              <h1
                class="font-bold text-3xl text-blue hover:text-dark_blue transition ease-in-out duration-500"
              >
                {{ round(averageStats.rain, 2) }}
              </h1>
              <p class="font-normal text-base text-blue">
                Avg. Rain
              </p>
            </div>

            <div class="flex flex-col justify-center items-center">
              <h1
                class="font-bold text-3xl text-blue hover:text-dark_blue transition ease-in-out duration-500"
              >
                {{ round(averageStats.ppm, 2) }}
              </h1>
              <p class="font-normal text-base text-blue">
                Avg. Air
              </p>
            </div>

          </div>
        </div>

        <div class="map"></div>
      </div>
    </div>
    <div class="w-full mt-20 mb-6 mr-6 rounded-lg bg-gray p-8" style="flex: 1">
      <!-- Location and time -->
      <div class="w-full">
        <div class="w-full flex flex-col justify-start">
          <h1 class="font-bold text-lg text-blue">Configuration</h1>

          <!-- Select location -->
          <div class="row mt-2">
            <label class="flex items-center" for="location">
              <!-- Title column -->
              <div style="flex: 1">
                <span class="font-semibold text-blue text-normal"
                  >District</span
                >
              </div>
              <div class="flex justify-between" style="flex: 4">
                <select
                  class="text-blue cursor-pointer outline-none font-normal w-32 py-2 px-1 rounded-lg mr-4"
                  v-model="district"
                  style="flex: 5"
                >
                  <option
                    v-for="(dist, index) in districtList"
                    :value="dist"
                    :key="index"
                  >
                    {{ dist }}
                  </option>
                </select>
                <select
                  class="text-blue cursor-pointer outline-none font-normal w-24 py-2 px-1 rounded-lg"
                  v-model="city"
                  style="flex: 5"
                >
                  <option
                    v-for="(_city, index) in cityList"
                    :value="_city"
                    :key="index"
                  >
                    {{ _city }}
                  </option>
                </select>
              </div>
            </label>
          </div>

          <!-- Select time -->
          <div class="row mt-2">
            <label class="flex items-center" for="location">
              <!-- Title column -->
              <div style="flex: 1">
                <span class="font-semibold text-blue text-normal">Time</span>
              </div>
              <div class="flex justify-between items-center" style="flex: 4">
                <!-- Select date time -->
                <p
                  class="text-blue outline-none font-normal w-48 py-2 px-2 rounded-lg">
                  Display markers within
                </p>

                <font-awesome-icon
                  class="text-blue font-normal text-sm mx-2"
                  icon="fa-solid fa-plus-minus"
                />
                
                <!-- Input time -->
                <input
                  type="number"
                  class="text-blue cursor-pointer text-center outline-none font-normal w-12 py-2 px-1 rounded-lg"
                  v-model="timedelta"
                />

                <!-- Input time units -->
                <select
                  class="text-blue text-center outline-none font-normal w-20 py-2 px-1 rounded-lg"
                  v-model="unit"
                >
                  <option
                    v-for="(unit, index) in unitList"
                    :value="unit"
                    :key="index"
                  >
                    {{ unit }}
                  </option>
                </select>
              </div>
            </label>
          </div>

          <!-- Center coordinate -->
          <div class="row mt-2">
            <label class="flex items-center" for="location">
              <!-- Latitude column -->
              <div style="flex: 1">
                <span class="font-semibold text-blue text-normal">Latitude</span>
              </div>
              <div class="flex items-center" style="flex: 4">
                <p
                  style="flex: 1"
                  class="text-blue w-full outline-none font-normal py-2 px-1 rounded-lg mr-4"
                >
                  {{ round(mapCenter.lat, 6) }}
                </p>

                <!-- Longtitude column -->
                <span style="flex: 1" class="font-semibold text-blue text-normal mr-8"
                  >Longtitude</span
                >

                <p
                  style="flex: 1"
                  class="text-blue w-full outline-none font-normal py-2 px-1 rounded-lg mr-4">
                  {{ round(mapCenter.lng, 6) }}
                </p>
              </div>
            </label>
          </div>

          <!-- Set range -->
          <div class="row mt-2">
            <label class="flex items-center" for="location">
              <!-- Lower bound column -->
              <div style="flex: 1">
                <span class="font-semibold text-blue text-normal">Lower</span>
              </div>
              <div class="flex items-center" style="flex: 4">
                <input
                  style="flex: 1"
                  class="text-blue w-full outline-none font-normal py-2 px-1 rounded-lg mr-4"
                  type="number"
                  step="0.1"
                  v-model="lowerBound"/>

                <!-- Upper bound column -->
                <span style="flex: 1" class="font-semibold text-blue text-normal mr-8">Upper</span>

                <input
                  style="flex: 1"
                  class="text-blue w-full outline-none font-normal py-2 px-1 rounded-lg mr-4"
                  type="number"
                  step="0.1"
                  v-model="upperBound" />
              </div>
            </label>
          </div>

        </div>
      </div>

      <!-- Button -->
      <div class="row mt-2">
        <button
          class="transition ease-in-out duration-500 bg-blue text-gray font-semibold text-xl w-full p-1 rounded-lg border-blue border-2 hover:text-blue hover:bg-gray"
          type="button"
          @click="onApplyChange"
        >
          Apply changes
        </button>
      </div>

      <!-- Marker info -->
      <div class="w-full mt-6">
        <div class="w-full flex flex-col justify-start">
          <h1 class="font-bold text-lg text-blue">Marker info</h1>

          <!-- <div class="row mt-2">
            <label class="flex items-center" for="location">
              Radius column
              <div style="flex: 1">
                <span class="font-semibold text-blue text-normal">Radius(m)</span>
              </div>
              <div class="flex items-center justify-between" style="flex: 4">
                <input
                  class="text-blue w-full outline-none font-normal py-2 px-1 rounded-lg mr-4"
                  type="number"
                  step="0.1"
                  v-model="scanRadius"
                />

                Meters
                <span class="font-semibold text-blue text-normal mr-8"
                  >Threshold</span
                >

                <input
                  class="text-blue w-full outline-none font-normal py-2 px-1 rounded-lg mr-4"
                  type="number"
                  step="0.1"
                  v-model="threshold"
                />
              </div>
            </label>
          </div> -->
          
          <div v-if="currentMarker">
            <div class="row mt-2">
              <label class="flex items-center" for="location">
                <!-- Title column -->
                <div style="flex: 1">
                  <span class="font-semibold text-blue text-normal"
                    >Camera ID</span
                  >
                </div>
                <div class="flex justify-between" style="flex: 4">
                  <p
                    class="text-blue cursor-pointer outline-none font-normal w-32 py-2 px-1 rounded-lg mr-4"
                    style="flex: 5">
                    {{ currentMarker._id }}
                  </p>
                </div>
              </label>
            </div>

            <!-- Marker coordinate -->
            <div class="row mt-2">
              <label class="flex items-center" for="location">
                <!-- Latitude column -->
                <div style="flex: 1">
                  <span class="font-semibold text-blue text-normal">Latitude</span>
                </div>
                <div class="flex items-center" style="flex: 4">
                  <p
                    style="flex: 1"
                    class="text-blue w-full outline-none font-normal py-2 px-1 rounded-lg mr-4"
                  >
                    {{ round(currentMarker.position.lat, 6) }}
                  </p>

                  <!-- Longtitude column -->
                  <span style="flex: 1" class="font-semibold text-blue text-normal mr-8"
                    >Longtitude</span
                  >

                  <p
                    style="flex: 1"
                    class="text-blue w-full outline-none font-normal py-2 px-1 rounded-lg mr-4">
                    {{ round(currentMarker.position.lng, 6) }}
                  </p>
                </div>
              </label>
            </div>
            
            <!-- Temperature and humidity-->
            <div class="row mt-2">
              <label class="flex items-center" for="location">
                <!-- Latitude column -->
                <div style="flex: 1">
                  <span class="font-semibold text-blue text-normal">Temper</span>
                </div>
                <div class="flex items-center" style="flex: 4">
                  <p
                    style="flex: 1"
                    class="text-blue w-full outline-none font-normal py-2 px-1 rounded-lg mr-4"
                  >
                    {{ round(currentMarker.temperature, 2) }} <span>&#176;</span>C
                  </p>

                  <!-- Longtitude column -->
                  <span style="flex: 1" class="font-semibold text-blue text-normal mr-8"
                    >Humi</span
                  >

                  <p 
                    style="flex: 1"
                    class="text-blue w-full outline-none font-normal py-2 px-1 rounded-lg mr-4">
                    {{ round(currentMarker.humidity, 2) }}%
                  </p>
                </div>
              </label>
            </div>


            <!-- Rain and Air-->
            <div class="row mt-2">
              <label class="flex items-center" for="location">
                <!-- Rain column -->
                <div style="flex: 1">
                  <span class="font-semibold text-blue text-normal">Rain</span>
                </div>
                <div class="flex items-center" style="flex: 4">
                  <p
                    style="flex: 1"
                    class="text-blue w-full outline-none font-normal py-2 px-1 rounded-lg mr-4"
                  >
                    {{ round(currentMarker.rain, 2) }}
                  </p>

                  <!-- Air column -->
                  <span style="flex: 1" class="font-semibold text-blue text-normal mr-8"
                    >Air</span
                  >

                  <p 
                    style="flex: 1"
                    class="text-blue w-full outline-none font-normal py-2 px-1 rounded-lg mr-4">
                    {{ round(currentMarker.ppm, 2) }}
                  </p>
                </div>
              </label>
            </div>

            <!-- Button -->
            <div class="row mt-2">
              <button
                class="transition ease-in-out duration-500 bg-blue text-gray font-semibold text-xl w-full p-1 rounded-lg border-blue border-2 hover:text-blue hover:bg-gray"
                type="button"
                @click="onShowDetail"
              >
                Show detail
              </button>
            </div>

          </div>

          <div v-else>
            <p class="font-normal text-blue underline italic text-lg">Select a marker to show info.</p>
          </div>

        </div>

        
      
      </div>
          
    
    </div>
  </div>
</template>

<script>
import { ref, computed } from "vue";
import constants from "@/constants";
import { store } from "@/store/store";
import { round } from "@/utils/number"
import { randomSamples } from "@/utils/random"

export default {
  setup() {
    // Location
    const districtList = ref(null);
    const district = ref(constants.__default_district__);
    const cityList = ref(null);
    const city = ref(constants.__default_city__);

    // Get location list
    districtList.value = ["Ha Dong", "Cau Giay", "Hai Ba Trung"]
    cityList.value = ["Hanoi", "Hai Phong", "Da Nang"]

    // Time delta
    const unitList = ref(["seconds", "minutes", "hours"]);
    const unit = ref(constants.__default_time_unit__);
    const timedelta = ref(constants.__default_time_delta__);

    // // Scan Configuration
    // const scanRadius = ref(constants.__default_scan_radius__);
    // const threshold = ref(constants.__default_congestion_threshold__);

    // // Map configuration
    // const showRedZones = ref(constants.__default_red_zones);
    
    // Map center coordinate
    const mapCenter = ref(null)

    // Get map center value
    mapCenter.value = {
      "lat": 20.995, 
      "lng": 105.8454742
    }

    // List of markers
    const mapMarkers = ref(null)

    // Get data from server
    mapMarkers.value = [
      {
        "_id": 1,
        "position": {
          "lat": 20.9839618, 
          "lng": 105.8354742  
        },
        "score": 4.2,
        "temperature": 27,
        "humidity": 65,
        "rain": 45,
        "ppm": 542
      },
      {
        "_id": 2,
        "position": {
          "lat": 20.99819618, 
          "lng": 105.8354742  
        },
        "score": 2.4,
        "temperature": 27,
        "humidity": 65,
        "rain": 45,
        "ppm": 542
      },
      {
        "_id": 3,
        "position": {
          "lat": 20.92829618, 
          "lng": 105.8154742  
        },
        "score": 4.0,
        "temperature": 27,
        "humidity": 65,
        "rain": 45,
        "ppm": 542
      },
      {
        "_id": 4,
        "position": {
          "lat": 20.998298, 
          "lng": 105.83742  
        },
        "score": 1.2,
        "temperature": 27,
        "humidity": 65,
        "rain": 45,
        "ppm": 542
      },
      {
        "_id": 5,
        "position": {
          "lat": 20.9829618, 
          "lng": 105.8354  
        },
        "score": 3.3,
        "temperature": 17,
        "humidity": 15,
        "rain": 49,
        "ppm": 545
      }
    ]

    // Counting average
    const averageStats = computed(() => {
      let avgScore = 0
      let avgTemp = 0
      let avgHumi = 0
      let avgRain = 0
      let avgPpm = 0

      mapMarkers.value.forEach(marker => {
        avgScore += marker.score
        avgTemp += marker.temperature
        avgHumi += marker.humidity
        avgRain += marker.rain
        avgPpm += marker.ppm
      })

      return {
        score: avgScore / mapMarkers.value.length,
        temperature: avgTemp / mapMarkers.value.length,
        humidity: avgHumi / mapMarkers.value.length,
        rain: avgRain / mapMarkers.value.length,
        ppm: avgPpm / mapMarkers.value.length,
      }
    })

    // Lower and upper bound
    const lowerBound = ref(3.0)
    const upperBound = ref(4.0)

    // HARD CODE HERE
    // Seperate marker to 3 colors
    function getMarkerColor(marker){
      if (marker.score >= upperBound.value) {
        return require('@/assets/images/red.png')
      }
      if (marker.score >= lowerBound.value) {
        return require('@/assets/images/yellow.png')
      }
      if (marker.score < lowerBound.value) {
        return require('@/assets/images/green.png')
      }
    }

    // Marker hiện tại
    const currentMarker = ref(null)

    function onMarkerClick(event, marker) {
      console.log('Info: ', marker)
      currentMarker.value = marker
    }

    function onApplyChange() {
      console.log('Appply changes!')

      // Request to server to get data
    }

    function onShowDetail() {
      console.log('Show detail!')

      // Move to Detail page
    }

    function onCameraAdd() {
      console.log('Camera added!')
    }

    function onResetMap() {
      console.log('Reset map!')
      onApplyChange()
    }

    function createRandomSamples(){
      mapMarkers.value = randomSamples()
    }

    return {
      createRandomSamples,
      onResetMap,
      onCameraAdd,
      onApplyChange,
      onShowDetail,
      currentMarker,
      lowerBound,
      upperBound,
      round,
      getMarkerColor,
      averageStats,
      onMarkerClick,
      mapCenter,
      mapMarkers,
      districtList,
      district,
      cityList,
      city,
      timedelta,
      unitList,
      unit,
    };
  },
  data() {
    return {
      store
    }
  },
  // components: {
  //   FullPageLoading,
  // },
};
</script>
