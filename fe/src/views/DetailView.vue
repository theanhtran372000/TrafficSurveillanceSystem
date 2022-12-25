<template>
  <!-- Body -->
  <div class="flex flex-row w-full h-screen">
    <!-- Chart display -->
    <div class="w-full mt-20 mb-6 mx-6 rounded-lg bg-gray p-8" style="flex: 2">

      <!-- Chart -->
      <div class="w-full">
        <div class="w-full flex justify-between items-center">
          <h1 class="font-bold text-xl text-blue">Statistics</h1>
          <div class="flex items-center">

            <button @click="isRefresh = !isRefresh" class="flex flex-row items-center font-normal underline text-base text-red-500 cursor-pointer hover:text-dark_blue mr-4" v-if="isRefresh">
              <font-awesome-icon 
                class="mr-4 cursor-pointer"
                icon="fa-solid fa-arrow-rotate-left" />
              
              Turn off refresh
            </button>

            
            <button @click="isRefresh = !isRefresh" class="flex flex-row items-center font-normal underline text-base text-green-500 cursor-pointer hover:text-dark_blue mr-4" v-else>
              <font-awesome-icon 
                class="mr-4 cursor-pointer text-green-500 mr-4"
                icon="fa-solid fa-arrow-rotate-left" />
              
              Turn on refresh
            </button>

          </div>
        </div>

        <div class="w-full flex flex-col items-center" style="height: 500px">
          <div class="map w-full flex flex-col mt-2 flex items-center" style="flex: 1">
            <div class="w-full object-fit" style="flex: 1">
              <Line :data="chartData" :options="chartOptions" />
            </div>
            <div class="w-full my-3 flex items-center justify-center">
              <h1 class="font-bold text-blue text-xl">Traffic density</h1>
            </div>
          </div>

          <div class="flex flex-row items-center justify-between w-full" style="flex: 1">
            <div class="w-full mr-6" style="flex: 1">
              <div class="w-full object-fit">
                <Line :data="temphumi" :options="subOptions" />
              </div>
              <div class="w-full my-4 flex items-center justify-center">
                <h1 class="font-bold text-blue text-xl">Temperature and Humidity</h1>
              </div>
            </div>

            <div class="w-full" style="flex: 1">
              <div class="w-full object-fit">
                <Line :data="rainppm" :options="subOptions" />
              </div>
              <div class="w-full my-4 flex items-center justify-center">
                <h1 class="font-bold text-blue text-xl">Rain and Air quality</h1>
              </div>
            </div>
          </div>

        </div>


      </div>

      <!-- Config display -->
      <div class="w-full mt-0">
        <div class="flex justify-between items-center pt-4">
          <!-- <div class="flex items-center justify-center">
            <p class="font-semibold text-lg text-blue mr-4">Average</p>
            <span class="bg-white px-6 py-1 rounded-lg text-blue font-normal text-lg">{{ average }}</span>
          </div> -->

          <div class="flex items-center justify-center">
            <p class="font-semibold text-lg text-blue mx-4">From</p>
            <input type="datetime-local" class="text-blue outline-none text-lg font-normal w-72 py-1 px-6 rounded-lg"
              v-model="from" />
            <p class="font-semibold text-lg text-blue mx-4">to</p>
            <input type="datetime-local" class="text-blue outline-none text-lg font-normal w-72 py-1 px-6 rounded-lg"
              v-model="to" />
            <button
              class="ml-10 font-semibold text-lg text-gray w-40 px-6 py-2 bg-blue text-white rounded cursor-pointer hover:bg-dark_blue"
              @click="filterCameraInfo">
              Get data
            </button>
          </div>

        </div>
        <div class="map"></div>
      </div>

    </div>

    <!-- Camera display -->
    <div class="w-full mt-20 mb-6 mr-6 rounded-lg bg-gray p-5" style="flex: 1">
      <!-- Camera image -->
      <div class="w-full">
        <div class="w-full flex flex-col justify-start">
          <h1 class="font-bold text-xl text-blue">Camera image</h1>
          <img class="w-full object-cover border-2 border-blue mt-2" style="height: 300px"
          v-bind:src="'data:image/png;base64,'+ cameraImage"
            alt="Traffic image" />
        </div>
      </div>

      <!-- Camera info -->
      <div class="w-full mt-5">
        <div class="w-full flex flex-col justify-start">
          <h1 class="font-bold text-xl text-blue">Camera infomation</h1>

          <!-- Cam ids -->
          <div class="row mt-4">
            <label class="flex items-center" for="location">
              <!-- Radius column -->
              <div style="flex: 1">
                <span class="text-lg font-semibold text-blue text-normal mr-4">Cam ID</span>
              </div>
              <div class="flex items-center justify-between" style="flex: 3">
                <p class="w-full bg-white px-4 py-1 rounded-lg text-blue font-normal text-lg">
                  {{ camid }}
                </p>
              </div>
            </label>
          </div>

          <!-- Coordinate -->
          <div class="row mt-4">
            <label class="flex items-center" for="location">
              <!-- Radius column -->
              <div style="flex: 1">
                <span class="text-lg font-semibold text-blue text-normal mr-4">Latitude</span>
              </div>
              <div class="flex items-center justify-between" style="flex: 3">
                <p class="bg-white px-4 py-1 rounded-lg text-blue font-normal text-lg" style="flex: 1">
                  {{ latitude }}
                </p>

                <!-- Meters -->
                <span class="text-lg font-semibold text-blue text-normal mx-4" style="flex: 1">Longtitude</span>
                <p class="bg-white px-4 py-1 rounded-lg text-blue font-normal text-lg" style="flex: 1">
                  {{ longtitude }}
                </p>
              </div>
            </label>
          </div>

          <!-- Cam ids -->
          <div class="row mt-4">
            <label class="flex items-center" for="location">
              <!-- Radius column -->
              <div style="flex: 1">
                <span class="text-lg font-semibold text-blue text-normal mr-4">Updated</span>
              </div>
              <div class="flex items-center justify-between" style="flex: 3">
                <p class="w-full bg-white px-4 py-1 rounded-lg text-blue font-normal text-lg">
                  {{ lastUpdated }}
                </p>
              </div>
            </label>
          </div>

          <div class="row w-full flex justfy-center items-center bg-red">
            <button class="mt-4 w-full bg-red-500 px-10 py-2 rounded font-semibold text-lg text-gray hover:bg-red-800"
              @click="alert">Alert !</button>
          </div>

        </div>
      </div>


    </div>
  </div>
</template>

<script>
import { ref, computed } from "vue";
import { Line } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, CategoryScale, LinearScale, PointElement, LineElement, ChartData } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, PointElement, LineElement, CategoryScale, LinearScale)

import instance from "@/utils/axios";
import { useRoute } from "vue-router";
import { isOk } from "@/utils/response";
// import { resolveNaptr } from "dns";
import constants from "@/constants";

export default {
  components: { Line },
  setup() {
    const average = ref(0.0);
    const route = useRoute()

    // reset mode
    const isRefresh = ref(true);

    // Camera info
    const longtitude = ref(null);
    const latitude = ref(null);
    const cameraImage = ref(null)
    const camid = ref(route.params.id);
    const ip = ref(null)

    const labels = ref([])
    const currentChart = ref('Temperature')
    const charts = ref({
      'Score': [],
      'Temperature': [],
      'Humidity': [],
      'Rain': [],
      'PPM': []
    })

    // Get current time
    // Time
    var now = new Date();
    var year = now.getFullYear();
    var month = now.getMonth() + 1;
    var day = now.getDate();
    var hour = now.getHours();
    var minute = now.getMinutes();
    var localDatetime =
      year +
      "-" +
      (month < 10 ? "0" + month.toString() : month) +
      "-" +
      (day < 10 ? "0" + day.toString() : day) +
      "T" +
      (hour < 10 ? "0" + hour.toString() : hour) +
      ":" +
      (minute < 10 ? "0" + minute.toString() : minute);

    // Time
    const from = ref(localDatetime);
    const to = ref(localDatetime);

    const lastUpdated = ref('No data')

    async function getCameraInfo() {
      // Reset array
      labels.value = []
      charts.value["Temperature"] = []
      charts.value["Humidity"] = []
      charts.value["Rain"] = []
      charts.value["Score"] = []
      charts.value["PPM"] = []

      const response = await instance.get('/cameras/' + route.params.id)
      cameraImage.value = response.data.image
      longtitude.value = response.data.lng
      latitude.value = response.data.lat
      ip.value = response.data.ip

      const current = new Date().getTime()
      response.data.event.forEach((e, i) => {
        if (current - new Date(e.timeStamp).getTime() < constants.__data_period__ * 1000) {
          labels.value.push(e.timeStamp)
          charts.value["Temperature"].push(e.temperature)
          charts.value["Humidity"].push(e.humidity)
          charts.value["Rain"].push(e.rain)
          charts.value["Score"].push(e.score)
          charts.value["PPM"].push(e.ppm)
        }

        if(i === response.data.event.length - 1) {
          lastUpdated.value = new Date(e.timeStamp).toLocaleString()
        }
      })
    }

    async function alert() {
      const response = await instance.post('/sensors')
      if (!isOk(response)) { console.log('ok') }

    }

    async function filterCameraInfo() {
      const response = await instance.get('/cameras/ip/' + ip.value + '/' + from.value + '/' + to.value)
      // console.log(response.data)
      labels.value = []
      charts.value["Temperature"] = []
      charts.value["Humidity"] = []
      charts.value["Rain"] = []
      charts.value["Score"] = []
      charts.value["PPM"] = []

      response.data.event.forEach((e) => {
        labels.value.push(e.timeStamp)
        charts.value["Temperature"].push(e.temperature)
        charts.value["Humidity"].push(e.humidity)
        charts.value["Rain"].push(e.rain)
        charts.value["Score"].push(e.score)
        charts.value["PPM"].push(e.ppm)
      })

      isRefresh.value = false
    }

    async function getCurrentCameraInfo(from, to) {
      const response = await instance.get('/cameras/ip/' + ip.value + '/' + from + '/' + to)
      labels.value = []
      charts.value["Temperature"] = []
      charts.value["Humidity"] = []
      charts.value["Rain"] = []
      charts.value["Score"] = []
      charts.value["PPM"] = []
      cameraImage.value = response.data.image

      // console.log('Image: ', cameraImage.value)

      response.data.event.forEach((e, i) => {
        labels.value.push(e.timeStamp)
        charts.value["Temperature"].push(e.temperature)
        charts.value["Humidity"].push(e.humidity)
        charts.value["Rain"].push(e.rain)
        charts.value["Score"].push(e.score)
        charts.value["PPM"].push(e.ppm)

        if(i === response.data.event.length - 1) {
          lastUpdated.value = new Date(e.timeStamp).toLocaleString()
        }
      })
    }

    getCameraInfo()

    async function refresh() {
      if(!isRefresh.value) return

      console.log('Event: Reset!')
      // getCameraInfo()

      const today = new Date()
      const to = today.toISOString()
      const from = new Date(today.getTime() - constants.__data_period__ * 1000)

      getCurrentCameraInfo(from, to)

    }

    const chartData = computed(() => {
      return {
        labels: Object.values(labels.value),
        datasets: [
          {
            backgroundColor: 'blue',
            borderColor: 'lightblue',
            pointBorderColor: 'blue',
            pointBorderWidth: 2,
            data: Object.values(charts.value.Score),
          },
        ]
      }
    })

    const chartOptions = computed(() => {
      return {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          x: {
            ticks: {
              display: false,
            }
          }
        },
        plugins: {
          legend: {
            display: false,
          }
        }
      }
    })

    const subOptions = computed(() => {
      return {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          x: {
            ticks: {
              display: false,
            }
          }
        },
      }
    })

    const temphumi = computed(() => {
      return {
        labels: Object.values(labels.value),
        datasets: [
          {
            label: 'Temp',
            backgroundColor: '#ff0000',
            borderColor: '#fa9191',
            pointBorderColor: '#ff0000',
            pointBorderWidth: 0.1,
            data: Object.values(charts.value.Temperature),
          },
          {
            label: 'Humi',
            backgroundColor: 'green',
            borderColor: 'lightgreen',
            pointBorderColor: 'green',
            pointBorderWidth: 0.1,
            data: Object.values(charts.value.Humidity),
          },
        ]
      }
    })

    const rainppm = computed(() => {
      return {
        labels: Object.values(labels.value),
        datasets: [
          {
            label: 'Rain',
            backgroundColor: '#f77002',
            borderColor: '#f7bcbc',
            pointBorderColor: '#f77002',
            pointBorderWidth: 0.1,
            data: Object.values(charts.value.Rain),
          },
          {
            label: 'PPM',
            backgroundColor: '#f702d6',
            borderColor: '#ff9ef2',
            pointBorderColor: '#f702d6',
            pointBorderWidth: 0.1,
            data: Object.values(charts.value.PPM),
          },
        ]
      }
    })

    setInterval(refresh, constants.__refresh_time__ * 1000 * 2)

    return {
      isRefresh,
      refresh,
      average,
      from,
      to,
      camid,
      longtitude,
      latitude,
      lastUpdated,
      cameraImage,
      chartData,
      chartOptions,
      currentChart,
      charts,
      temphumi,
      rainppm,
      subOptions,
      alert,
      filterCameraInfo
    };
  },
};
</script>
