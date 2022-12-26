export default {
  __version__: "v1.0.0",
  __default_layout__: "EmptyLayout",
  __default_city__: "Hanoi",
  __default_district__: "Hai Ba Trung",
  __default_time_delta__: 10, // minute
  __default_time_unit__: "minutes",
  __default_scan_radius__: 200, // meter
  __default_congestion_threshold__: 20.0,
  __default_red_zones: true,
  __baseURL__: "http://34.143.229.9:8800",
  __access_token__: null,
  __token_key__: '__token_key__',
  __request_status__: {
    REQUEST: "REQUEST",
    SUCCESS: "SUCCESS",
    ERROR: "ERROR",
  },
  __map_api_key__: 'AIzaSyDWGL-ISSbv_dGbG69PZR5Xs19d_vU2Ous',
  __time_unit__: {
    SECOND: "seconds",
    MINUTE: "minutes",
    HOUR: "hours"
  },
  __data_period__: 5 * 60, // seconds
  __refresh_time__: 1, // seconds
  __default_map__: 'traffic',
  __default_traffic_lower__: 3.0,
  __default_traffic_higher__: 4.0,
  __default_temp_threshold__: 25,
  __default_rain_threshold__: 400,
  __default_air_threshold__: 1000
};
