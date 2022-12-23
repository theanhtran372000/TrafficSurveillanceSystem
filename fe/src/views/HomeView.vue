<template>
  <div class="flex flex-row w-full h-screen">
    <!-- Map display -->
    <div class="w-full mt-20 mb-6 mx-6 rounded-lg bg-gray p-8" style="flex: 2">
      <div class="w-full">
        <div class="w-full flex justify-between items-center">
          <h1 class="font-bold text-lg text-blue">Traffic Map</h1>
          <div class="flex">
            <font-awesome-icon
              class="text-blue mr-4 cursor-pointer hover:text-dark_blue transition ease-in-out duration-500"
              icon="fa-solid fa-plus"
            />
            <font-awesome-icon
              class="text-blue mr-4 cursor-pointer hover:text-dark_blue transition ease-in-out duration-500"
              icon="fa-solid fa-arrow-rotate-left"
            />
            <font-awesome-icon
              class="text-blue mr-4 cursor-pointer hover:text-dark_blue transition ease-in-out duration-500"
              icon="fa-solid fa-arrow-right"
            />
          </div>
        </div>

        <div class="map w-full mt-2">
          <img
            class="w-full object-cover border-2 border-blue"
            style="height: 360px"
            :src="require('@/assets/images/ggmap.jpg')"
            alt="Google map"
          />
          <div class="w-full mt-2 flex items-center justify-end">
            <input
              class="accent-blue mr-2"
              type="checkbox"
              checked
              v-model="showRedZones"
            /><label>Show red zones</label>
          </div>
        </div>
      </div>

      <!-- Analytics display -->
      <div class="w-full mt-6">
        <div class="w-full">
          <h1 class="font-bold text-lg text-blue">Analytics</h1>
          <div class="flex justify-between items-center pt-4">
            <div class="flex flex-col justify-center items-center">
              <h1
                class="font-bold text-3xl text-blue hover:text-dark_blue transition ease-in-out duration-500"
              >
                202
              </h1>
              <p class="font-normal text-base text-blue">Cameras</p>
            </div>
            <div class="flex flex-col justify-center items-center">
              <h1
                class="font-bold text-3xl text-blue hover:text-dark_blue transition ease-in-out duration-500"
              >
                3.14
              </h1>
              <p class="font-normal text-base text-blue">Avg. Camera density</p>
            </div>
            <div class="flex flex-col justify-center items-center">
              <h1
                class="font-bold text-3xl text-blue hover:text-dark_blue transition ease-in-out duration-500"
              >
                14
              </h1>
              <p class="font-normal text-base text-blue">Congestions</p>
            </div>
            <div class="flex flex-col justify-center items-center">
              <h1
                class="font-bold text-3xl text-blue hover:text-dark_blue transition ease-in-out duration-500"
              >
                21.45
              </h1>
              <p class="font-normal text-base text-blue">
                Avg. Congestion density
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
          <h1 class="font-bold text-lg text-blue">Location & Time</h1>

          <!-- Select location -->
          <div class="row mt-4">
            <label class="flex items-center" for="location">
              <!-- Title column -->
              <div style="flex: 1">
                <span class="font-semibold text-blue text-normal"
                  >District</span
                >
              </div>
              <div class="flex justify-between" style="flex: 4">
                <select
                  class="text-blue outline-none font-normal w-32 py-2 px-1 rounded-lg"
                  v-model="district"
                >
                  <option
                    v-for="(district, index) in districtList"
                    :value="district"
                    :key="index"
                  >
                    {{ district }}
                  </option>
                </select>
                <select
                  class="text-blue outline-none font-normal w-24 py-2 px-1 rounded-lg"
                  v-model="city"
                >
                  <option
                    v-for="(city, index) in cityList"
                    :value="city"
                    :key="index"
                  >
                    {{ city }}
                  </option>
                </select>

                <button
                  class="font-normal outline-none text-gray bg-blue py-2 px-2 rounded-lg"
                >
                  My location
                </button>
              </div>
            </label>
          </div>

          <!-- Select time -->
          <div class="row mt-4">
            <label class="flex items-center" for="location">
              <!-- Title column -->
              <div style="flex: 1">
                <span class="font-semibold text-blue text-normal">Time</span>
              </div>
              <div class="flex justify-between items-center" style="flex: 4">
                <!-- Select date time -->
                <input
                  class="text-blue outline-none font-normal w-48 py-2 px-1 rounded-lg"
                  type="datetime-local"
                  v-model="time"
                />

                <font-awesome-icon
                  class="text-blue font-normal text-sm mx-2"
                  icon="fa-solid fa-plus-minus"
                />

                <input
                  type="number"
                  class="text-blue text-center outline-none font-normal w-12 py-2 px-1 rounded-lg"
                  v-model="timedelta"
                />

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
        </div>
      </div>

      <!-- Configuration -->
      <div class="w-full mt-8">
        <div class="w-full flex flex-col justify-start">
          <h1 class="font-bold text-lg text-blue">Configuration</h1>

          <!-- Select location -->
          <div class="row mt-4">
            <label class="flex items-center" for="location">
              <!-- Radius column -->
              <div style="flex: 1">
                <span class="font-semibold text-blue text-normal">Radius</span>
              </div>
              <div class="flex items-center justify-between" style="flex: 4">
                <input
                  class="text-blue w-full outline-none font-normal py-2 px-1 rounded-lg mr-4"
                  type="number"
                  step="0.1"
                  v-model="scanRadius"
                />

                <!-- Meters -->
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
          </div>
        </div>
      </div>

      <!-- Button -->
      <div class="row mt-12">
        <button
          class="transition ease-in-out duration-500 bg-blue text-gray font-bold text-2xl w-full p-2 rounded-lg border-blue border-4 hover:text-blue hover:bg-gray"
          type="button"
        >
          Apply changes
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
import constants from "@/constants";

export default {
  setup() {
    // Location
    const districtList = ["Ha Dong", "Cau Giay", "Hai Ba Trung"];
    const district = ref(constants.__default_district__);
    const cityList = ["Hanoi", "Hai Phong", "Da Nang"];
    const city = ref(constants.__default_city__);

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

    const time = ref(localDatetime);
    const unitList = ["seconds", "minutes", "hours"];
    const unit = ref(constants.__default_time_unit__);
    const timedelta = ref(constants.__default_time_delta__);

    // Scan Configuration
    const scanRadius = ref(constants.__default_scan_radius__);
    const threshold = ref(constants.__default_congestion_threshold__);

    // Map configuration
    const showRedZones = ref(constants.__default_red_zones);

    return {
      districtList,
      district,
      cityList,
      city,
      time,
      timedelta,
      unitList,
      unit,
      scanRadius,
      threshold,
      showRedZones,
    };
  },
};
</script>
