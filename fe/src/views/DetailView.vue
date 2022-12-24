<template>
  <!-- Body -->
  <div class="flex flex-row w-full h-screen">
    <!-- Chart display -->
    <div class="w-full mt-20 mb-6 mx-6 rounded-lg bg-gray p-8" style="flex: 2">

      <!-- Chart -->
      <div class="w-full">
        <div class="w-full flex justify-between items-center">
          <h1 class="font-bold text-lg text-blue">Statistics</h1>
          <div class="flex">
            <button>
              <font-awesome-icon
                class="text-blue mr-4 cursor-pointer hover:text-dark_blue transition ease-in-out duration-500"
                icon="fa-solid fa-arrow-rotate-left" />
            </button>

            <button
              v-for="chart in charts"
              :key="chart"
              class="mx-2 text-blue hover:text-dark_blue transition ease-in-out duration-500"
              @click="currentChart = chart"
            >
              <!-- <font-awesome-icon
                class="text-blue mr-4 cursor-pointer hover:text-dark_blue transition ease-in-out duration-500"
                icon="fa-solid fa-arrow-right" /> -->
                {{ chart }}
            </button>

          </div>
        </div>

        <div class="map w-full mt-2">
          <!-- <img class="w-full object-fit border-2 border-blue" style="height: 360px"
            :src="require('@/assets/images/linechart.png')" alt="Google map" /> -->
          <div class="h-64 w-full object-fit">
            <component :is="currentChart"></component>
          </div>
          <div class="w-full mt-6 flex items-center justify-center">
            <h1 class="font-bold text-blue text-2xl">{{ currentChart }} Line Chart</h1>
          </div>
        </div>
      </div>

      <!-- Config display -->
      <div class="w-full mt-6">
        <div class="flex justify-between items-center pt-4">
          <div class="flex items-center justify-center">
            <p class="font-semibold text-lg text-blue mr-4">Average</p>
            <span class="bg-white px-6 py-1 rounded-lg text-blue font-normal text-lg">{{ average }}</span>
          </div>

          <div class="flex items-center justify-center">
            <p class="font-semibold text-lg text-blue mx-4">From</p>
            <input type="datetime-local" class="text-blue outline-none text-lg font-normal w-72 py-1 px-6 rounded-lg"
              v-model="from" />
            <p class="font-semibold text-lg text-blue mx-4">to</p>
            <input type="datetime-local" class="text-blue outline-none text-lg font-normal w-72 py-1 px-6 rounded-lg"
              v-model="to" />
          </div>
        </div>

        <div class="map"></div>
      </div>
      <button class="flex float-right mt-7 mr-2 bg-blue py-2 px-7 text-white rounded">
        OK
      </button>
    </div>

    <!-- Camera display -->
    <div class="w-full mt-20 mb-6 mr-6 rounded-lg bg-gray p-8" style="flex: 1">
      <!-- Camera image -->
      <div class="w-full">
        <div class="w-full flex flex-col justify-start">
          <h1 class="font-bold text-lg text-blue">Camera image</h1>
          <img class="w-full object-cover border-2 border-blue" style="height: 300px"
            :src="require('@/assets/images/traffic.jpg')" alt="Traffic image" />
        </div>
      </div>
      <!-- Camera info -->
      <div class="w-full mt-8">
        <div class="w-full flex flex-col justify-start">
          <h1 class="font-bold text-lg text-blue">Camera infomation</h1>

          <!-- Cam ids -->
          <div class="row mt-4">
            <label class="flex items-center" for="location">
              <!-- Radius column -->
              <div style="flex: 1">
                <span class="text-lg font-semibold text-blue text-normal mr-4">Cam ID</span>
              </div>
              <div class="flex items-center justify-between" style="flex: 4">
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
                <span class="text-lg font-semibold text-blue text-normal mr-4">Longtitude</span>
              </div>
              <div class="flex items-center justify-between" style="flex: 4">
                <p class="bg-white px-4 py-1 rounded-lg text-blue font-normal text-lg">
                  {{ longtitude }}
                </p>

                <!-- Meters -->
                <span class="text-lg font-semibold text-blue text-normal mr-4">Latitude</span>

                <p class="bg-white px-4 py-1 rounded-lg text-blue font-normal text-lg">
                  {{ latitude }}
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
              <div class="flex items-center justify-between" style="flex: 4">
                <p class="w-full bg-white px-4 py-1 rounded-lg text-blue font-normal text-lg">
                  {{ lastUpdated }}
                </p>
              </div>
            </label>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
import Temperature from '@/components/charts/TemperatureChart.vue'
import Humidity from '@/components/charts/HumidityChart.vue'
import Rain from '@/components/charts/RainChart.vue'
import Congestion from '@/components/charts/CongestionChart.vue'
// import constants from "@/constants";

export default {
  components: { Temperature, Humidity, Rain, Congestion },
  data() {
    return {
      currentChart: 'Temperature',
      charts: ['Temperature', 'Humidity', 'Rain', 'Congestion']
    }
  },
  setup() {
    const average = ref(0.0);

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

    // Camera info
    const camid = ref("askdnashdoasj89a09u0");
    const longtitude = ref(128.131);
    const latitude = ref(90.123);

    const lastUpdated = ref(localDatetime);

    console.log(localDatetime);
    // console.log(typeof localDatetime)

    return {
      average,
      from,
      to,
      camid,
      longtitude,
      latitude,
      lastUpdated,
    };
  },
};
</script>
