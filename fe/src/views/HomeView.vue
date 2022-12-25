<template>
  <div class="flex flex-row w-full h-screen">
    <!-- Map display -->
    <div class="w-full mt-20 mb-6 mx-6 rounded-lg bg-gray p-8" style="flex: 2">
      <div class="w-full">
        <div class="w-full flex justify-between items-center">
          <h1 class="font-bold text-lg text-blue">Traffic Density Map</h1>
          <div class="flex items-center">

            <!--  Random sampling data -->
            <button class="text-blue mr-8 cursor-pointer hover:text-dark_blue transition ease-in-out duration-500"
              @click="createRandomSamples">
              <font-awesome-icon icon="fa-solid fa-bolt" /> Random 1000 samples
            </button>

            <!-- Add camera -->
            <button class="text-blue mr-8 cursor-pointer hover:text-dark_blue transition ease-in-out duration-500"
              data-bs-toggle="modal" data-bs-target="#exampleModal">
              <font-awesome-icon icon="fa-solid fa-plus" /> Add cameras
            </button>

            <!-- Modal -->
            <div
              class="modal fade fixed top-0 left-0 hidden w-full h-full outline-none overflow-x-hidden overflow-y-auto"
              id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
              <div class="modal-dialog relative w-auto pointer-events-none">
                <div
                  class="modal-content border-none shadow-lg relative flex flex-col w-full pointer-events-auto bg-white bg-clip-padding rounded-md outline-none text-current">
                  <div
                    class="modal-header flex flex-shrink-0 items-center justify-between p-4 border-b border-light_blue rounded-t-md">
                    <h5 class="text-xl font-bold leading-normal text-blue" id="exampleModalLabel">Add new camera</h5>
                    <button type="button"
                      class="btn-close box-content w-4 h-4 p-1 text-light_blue border-none rounded-none opacity-50 focus:shadow-none focus:outline-none focus:opacity-100 hover:text-black hover:opacity-75 hover:no-underline"
                      data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body relative p-4">

                    <!-- IP -->
                    <label class="flex flex-col mt-4" for="username">
                      <span class="text-blue font-semibold text-xl ml-1">Camera IP</span>
                      <input id="username" type="text"
                        class="border-light_blue border-2 shadow-lg placeholder-light_blue text-lg py-2 px-2 rounded-lg outline-none text-blue mt-1.5"
                        v-model="camAdded.camIP" placeholder="Input cam IP address" />
                    </label>

                    <!-- Latitude -->
                    <label class="flex flex-col mt-4" for="latitude">
                      <span class="text-blue font-semibold text-xl ml-1">Latitude</span>
                      <input id="latitude" type="number"
                        class="border-light_blue border-2 shadow-lg placeholder-light_blue text-lg py-2 px-2 rounded-lg outline-none text-blue mt-1.5"
                        v-model="camAdded.camLat" placeholder="Input cam latitude" />
                    </label>

                    <!-- Camera longtitude -->
                    <label class="flex flex-col my-4" for="longitude">
                      <span class="text-blue font-semibold text-xl ml-1">Longtitude</span>
                      <input id="longitude" type="number"
                        class="border-light_blue border-2 shadow-lg placeholder-light_blue text-lg py-2 px-2 rounded-lg outline-none text-blue mt-1.5"
                        v-model="camAdded.camLng" placeholder="Input cam longtide" />
                    </label>

                    <div class="row mt-4" v-if="addError">
                      <span class="text-blue text-base font-semibold ml-2"> {{ addError }} </span>
                    </div>

                    <div class="row mt-4" v-if="addSuccess">
                      <span class="text-blue text-base font-semibold ml-2"> {{ addSuccess }} </span>
                    </div>

                  </div>
                  <div
                    class="modal-footer flex flex-shrink-0 flex-wrap items-center justify-end p-4 border-t border-light_blue rounded-b-md">
                    <button type="button" class="px-6
                      py-2.5
                      bg-purple-600
                      text-white
                      font-bold
                      text-lg
                      leading-tight
                      rounded
                      w-32
                      shadow-md
                      hover:bg-purple-700 hover:shadow-lg
                      focus:bg-purple-700 focus:shadow-lg focus:outline-none focus:ring-0
                      active:bg-purple-800 active:shadow-lg
                      transition
                      duration-150
                      ease-in-out" data-bs-dismiss="modal">Cancel</button>
                    <button type="button" class="px-6
                      py-2.5
                      bg-blue
                      text-white
                      font-bold
                      text-lg
                      w-32
                      leading-tight
                      rounded
                      shadow-md
                      hover:bg-blue hover:shadow-lg
                      focus:bg-blue focus:shadow-lg focus:outline-none focus:ring-0 active:shadow-lg
                      transition
                      duration-150
                      ease-in-out
                      ml-4" @click="onCameraAdd">Add</button>
                  </div>
                </div>
              </div>
            </div>


            <button class="text-blue mr-4 cursor-pointer hover:text-dark_blue transition ease-in-out duration-500"
              @click="onResetMap">
              <font-awesome-icon icon="fa-solid fa-arrow-rotate-left" /> Refresh
            </button>

          </div>
        </div>

        <div class="map w-full mt-2">
          <!-- Show maps -->
          <GMapMap class="w-full object-cover border-2 border-blue" style="height: 360px" :center="mapCenter"
            :zoom="14">

            <GMapMarker v-for="marker, index in mapMarkers" :icon="{
              url: getMarkerColor(marker),
              scaledSize: {
                width: 30,
                height: 30
              }
            }" :position="{ 'lat': marker.position.lat, 'lng': marker.position.lng }" :clickable="true" :key="index"
              @click="onMarkerClick($event, marker)" />

          </GMapMap>

          <!-- Show note -->
          <div class="w-full mt-2 flex items-center justify-end">
            <div class="flex justify-center items-center">
              <div class="flex items-center mr-6">
                <font-awesome-icon class="text-normal text-green-500 mr-2" icon="fa-solid fa-location-dot" />
                <p class="font-normal text-blue text-base">Less than {{ lowerBound }}</p>
              </div>

              <div class="flex items-center mr-6">
                <font-awesome-icon class="text-base text-yellow-500 mr-2" icon="fa-solid fa-location-dot" />
                <p class="font-normal text-blue text-base">From {{ lowerBound }} to {{ upperBound }}</p>
              </div>

              <div class="flex items-center mr-6">
                <font-awesome-icon class="text-base text-red-500 mr-2" icon="fa-solid fa-location-dot" />
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

            <!-- Number of markers -->
            <div class="flex flex-col justify-center items-center">
              <h1 class="font-bold text-3xl text-blue hover:text-dark_blue transition ease-in-out duration-500">
                {{ mapMarkers.length }}
              </h1>
              <p class="font-normal text-base text-blue">Cameras</p>
            </div>

            <!-- Average score -->
            <div v-if="!isNaN(averageStats.score)" class="flex flex-col justify-center items-center">
              <h1
                class="font-bold text-3xl text-blue hover:text-dark_blue transition ease-in-out duration-500"
              >
                {{ round(averageStats.score, 2) }}
              </h1>
              <p class="font-normal text-base text-blue">Avg. Density</p>
            </div>

            <div v-else class="flex flex-col justify-center items-center">
              <h1
                class="font-bold text-3xl text-blue hover:text-dark_blue transition ease-in-out duration-500"
              >
                -|-
              </h1>
              <p class="font-normal text-base text-blue">Avg. Density</p>
            </div>

            <!-- Average temperature -->
            <div v-if="!isNaN(averageStats.temperature)" class="flex flex-col justify-center items-center">
              <h1
                class="font-bold text-3xl text-blue hover:text-dark_blue transition ease-in-out duration-500"
              >
              {{ round(averageStats.temperature, 2) }}
              </h1>
              <p class="font-normal text-base text-blue">Avg. Temp</p>
            </div>

            <div v-else class="flex flex-col justify-center items-center">
              <h1
                class="font-bold text-3xl text-blue hover:text-dark_blue transition ease-in-out duration-500"
              >
                -|-
              </h1>
              <p class="font-normal text-base text-blue">Avg. Density</p>
            </div>

            <!-- Average humidity -->
            <div v-if="!isNaN(averageStats.humidity)" class="flex flex-col justify-center items-center">
              <h1
                class="font-bold text-3xl text-blue hover:text-dark_blue transition ease-in-out duration-500"
              >
              {{ round(averageStats.humidity, 2) }}
              </h1>
              <p class="font-normal text-base text-blue">
                Avg. Humi
              </p>
            </div>

            <div v-else class="flex flex-col justify-center items-center">
              <h1
                class="font-bold text-3xl text-blue hover:text-dark_blue transition ease-in-out duration-500"
              >
                -|-
              </h1>
              <p class="font-normal text-base text-blue">Avg. Density</p>
            </div>

            <!-- Average rain -->
            <div v-if="!isNaN(averageStats.rain)" class="flex flex-col justify-center items-center">
              <h1
                class="font-bold text-3xl text-blue hover:text-dark_blue transition ease-in-out duration-500"
              >
                {{ round(averageStats.rain, 2) }}
              </h1>
              <p class="font-normal text-base text-blue">
                Avg. Rain
              </p>
            </div>

            <div v-else class="flex flex-col justify-center items-center">
              <h1
                class="font-bold text-3xl text-blue hover:text-dark_blue transition ease-in-out duration-500"
              >
                -|-
              </h1>
              <p class="font-normal text-base text-blue">Avg. Density</p>
            </div>

            <!-- Average air quarlity -->
            <div v-if="!isNaN(averageStats.ppm)" class="flex flex-col justify-center items-center">
              <h1
                class="font-bold text-3xl text-blue hover:text-dark_blue transition ease-in-out duration-500"
              >
                {{ round(averageStats.ppm, 2) }}
              </h1>
              <p class="font-normal text-base text-blue">
                Avg. Air
              </p>
            </div>

            <div v-else class="flex flex-col justify-center items-center">
              <h1
                class="font-bold text-3xl text-blue hover:text-dark_blue transition ease-in-out duration-500"
              >
                -|-
              </h1>
              <p class="font-normal text-base text-blue">Avg. Density</p>
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
                <span class="font-semibold text-blue text-normal">District</span>
              </div>
              <div class="flex justify-between" style="flex: 4">
                <select class="text-blue cursor-pointer outline-none font-normal w-32 py-2 rounded-lg mr-4"
                  v-model="district" style="flex: 5">
                  <option v-for="(dist, index) in districtList" :value="dist" :key="index">
                    {{ dist }}
                  </option>
                </select>
                <select class="text-blue cursor-pointer outline-none font-normal w-24 py-2 px-1 rounded-lg"
                  v-model="city" style="flex: 5">
                  <option v-for="(_city, index) in cityList" :value="_city" :key="index">
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
                <p class="text-blue outline-none font-normal w-48 py-2 px-1 rounded-lg">
                  Display markers within
                </p>

                <font-awesome-icon class="text-blue font-normal text-sm" icon="fa-solid fa-plus-minus" />

                <!-- Input time -->
                <input type="number"
                  class="text-blue cursor-pointer text-center outline-none font-normal w-12 py-2 px-1 rounded-lg"
                  v-model="timedelta" />

                <!-- Input time units -->
                <select class="text-blue text-center outline-none font-normal w-20 py-2 rounded-lg" v-model="unit">
                  <option v-for="(unit, index) in unitList" :value="unit" :key="index">
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
                <p style="flex: 1" class="text-blue w-full outline-none font-normal py-2 px-1 rounded-lg mr-4">
                  {{ round(mapCenter.lat, 6) }}
                </p>

                <!-- Longtitude column -->
                <span style="flex: 1" class="font-semibold text-blue text-normal mr-8">Longtitude</span>

                <p style="flex: 1" class="text-blue w-full outline-none font-normal py-2 px-1 rounded-lg mr-4">
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
                <input style="flex: 1" class="text-blue w-full outline-none font-normal py-2 px-1 rounded-lg mr-4"
                  type="number" step="0.1" v-model="lowerBound" />

                <!-- Upper bound column -->
                <span style="flex: 1" class="font-semibold text-blue text-normal mr-8">Upper</span>

                <input style="flex: 1" class="text-blue w-full outline-none font-normal py-2 px-1 rounded-lg mr-4"
                  type="number" step="0.1" v-model="upperBound" />
              </div>
            </label>
          </div>

        </div>
      </div>

      <!-- Button -->
      <div class="row mt-2">
        <button
          class="transition ease-in-out duration-500 bg-blue text-gray font-semibold text-xl w-full p-1 rounded-lg border-blue border-2 hover:text-blue hover:bg-gray"
          type="button" @click="onApplyChange">
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
                  <span class="font-semibold text-blue text-normal">Camera ID</span>
                </div>
                <div class="flex justify-between" style="flex: 4">
                  <p class="text-blue cursor-pointer outline-none font-normal w-32 py-2 px-1 rounded-lg mr-4"
                    style="flex: 5">
                    {{ currentMarker.id }}
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
                  <p style="flex: 1" class="text-blue w-full outline-none font-normal py-2 px-1 rounded-lg mr-4">
                    {{ round(currentMarker.position.lat, 6) }}
                  </p>

                  <!-- Longtitude column -->
                  <span style="flex: 1" class="font-semibold text-blue text-normal mr-8">Longtitude</span>

                  <p style="flex: 1" class="text-blue w-full outline-none font-normal py-2 px-1 rounded-lg mr-4">
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
                  <p style="flex: 1" class="text-blue w-full outline-none font-normal py-2 px-1 rounded-lg mr-4">
                    {{ round(currentMarker.temperature, 2) }} <span>&#176;</span>C
                  </p>

                  <!-- Longtitude column -->
                  <span style="flex: 1" class="font-semibold text-blue text-normal mr-8">Humi</span>

                  <p style="flex: 1" class="text-blue w-full outline-none font-normal py-2 px-1 rounded-lg mr-4">
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
                  <p style="flex: 1" class="text-blue w-full outline-none font-normal py-2 px-1 rounded-lg mr-4">
                    {{ round(currentMarker.rain, 2) }}
                  </p>

                  <!-- Air column -->
                  <span style="flex: 1" class="font-semibold text-blue text-normal mr-8">Air</span>

                  <p style="flex: 1" class="text-blue w-full outline-none font-normal py-2 px-1 rounded-lg mr-4">
                    {{ round(currentMarker.ppm, 2) }}
                  </p>
                </div>
              </label>
            </div>

            <!-- Button -->
            <div class="row mt-2">
              <button
                class="transition ease-in-out duration-500 bg-blue text-gray font-semibold text-xl w-full p-1 rounded-lg border-blue border-2 hover:text-blue hover:bg-gray"
                type="button" @click="onShowDetail">
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
import { ref, computed, watchEffect } from "vue";
import { useRouter } from "vue-router"
import constants from "@/constants";
import { store } from "@/store/store";
import { round } from "@/utils/number"
import { randomSamples } from "@/utils/random"
import instance from "@/utils/axios";
import { getTimeRange, formatUrl } from '@/utils/time'
import { formatMarkers } from '@/utils/preprocess'
import { isOk } from "@/utils/response";

export default {
  setup() {
    const router = useRouter()

    // Location
    const districtList = ref([]);
    const district = ref(null);
    const cityList = ref([]);
    const city = ref(null);
    const locationData = ref(null)

    // Map center coordinate
    const mapCenter = ref({
      lat: 0,
      lng: 0
    })

    // Get location list: Done
    async function getAllCity() {
      const response = await instance.get('/city')
      locationData.value = response.data

      console.log('City data: ', locationData.value)

      // Get city list
      locationData.value.forEach((city) => {
        cityList.value.push(city.name)
      })

      if (cityList.value.length > 0) city.value = cityList.value[0]
    }

    // Setup watch effect on city
    const cityWatcher = watchEffect(() => {
      if (city.value) {
        // Get district list
        locationData.value.forEach((c) => {
          if (c.name === city.value) {
            //Reset district list
            districtList.value = []

            // Update district list
            c.districts.forEach((d => {
              districtList.value.push(d.name)
            }))
          }
        })

        // Init district
        if (districtList.value.length > 0) district.value = districtList.value[0]
      }
    })

    // Get map center coordinate: Done
    // Setup watch effect on district
    const districtWatcher = watchEffect(() => {
      if (city.value && district.value) {
        locationData.value.forEach((c) => {
          if (c.name === city.value) {
            // Update district list
            c.districts.forEach((d => {
              if (d.name === district.value) {
                mapCenter.value = {
                  lat: Number(d.lat),
                  lng: Number(d.lng)
                }

                console.log('Map center: ', mapCenter.value)
              }
            }))
          }
        })
      }
    })

    getAllCity()

    // Time delta
    const unitList = ref([
      constants.__time_unit__.HOUR,
      constants.__time_unit__.MINUTE,
      constants.__time_unit__.SECOND,
    ]);
    const unit = ref(unitList.value[1]);
    const timedelta = ref(constants.__default_time_delta__);

    // List of markers
    const mapMarkers = ref(null)

    // Get data from server
    mapMarkers.value = [
      {
        "id": 1,
        "position": {
          "lat": 0,
          "lng": 0
        },
        "score": 0,
        "temperature": 0,
        "humidity": 0,
        "rain": 0,
        "ppm": 0
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
    function getMarkerColor(marker) {
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

    // Add camera
    const camAdded = ref({
      camIP: "Camera IP",
      camLat: 0,
      camLng: 0
    })

    // Marker hiện tại
    const currentMarker = ref(null)

    function onMarkerClick(event, marker) {
      console.log('Marker Info: ', marker)
      currentMarker.value = marker
    }

    // Get data from server: Done
    async function onApplyChange() {
      console.log('Event: Appply changes!')

      // Request to server to get data
      const timeRange = getTimeRange(timedelta.value, unit.value)

      const url = formatUrl('/cameras/events', timeRange)
      console.log('Url: ', url)
      const response = await instance.get(url)
      const events = formatMarkers(response.data)

      // Update to mapMarkers
      mapMarkers.value = events
      console.log('Markers: ', mapMarkers.value)
    }

    // Next to page detail: Done
    function onShowDetail() {
      console.log('Event: Show detail!')

      // Move to Detail page
      router.push({
        name: 'detail',
        params: {
          id: currentMarker.value.id
        }
      })
    }

    // Add camera: Doing
    const addError = ref(null)
    const addSuccess = ref(null)
    async function onCameraAdd() {
      addError.value = null
      addSuccess.value = null
      console.log('Event: Camera added!')
      try {
        const response = await instance.post('/cameras', {
          "name": "cam",
          "ip": camAdded.value.camIP,
          "lat": camAdded.value.camLat,
          "lng": camAdded.value.camLng,
          "status": "ACTIVE"
        })

        console.log(camAdded.value)

        if (!isOk(response)) {
          throw new Error('Failed to add new camera!')
        }
        else {
          addSuccess.value = 'Success!'
        }

      } catch (error) {
        console.log('Error: ', error)
        addError.value = error.response.data.message
      }
    }

    // Reset maps: Done
    function onResetMap() {
      console.log('Event: Reset map!')
      onApplyChange()
    }

    // Random samples: Done
    function createRandomSamples() {
      console.log('Event: Create 1000 random cameras')
      mapMarkers.value = randomSamples()
    }

    return {
      addSuccess,
      addError,
      cityWatcher,
      districtWatcher,
      locationData,
      camAdded,
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
