import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

// Import CSS file
import "./assets/styles/tailwind.css";
import "./assets/styles/global.css";

import { registerGlobalComponents } from "./utils/import";

// Import font awesome
import { library } from "@fortawesome/fontawesome-svg-core";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import {
  faUserSecret,
  faArrowRight,
  faArrowRotateLeft,
  faTrash,
  faPlus,
  faPlusMinus,
  faRightFromBracket,
  faLocationDot,
} from "@fortawesome/free-solid-svg-icons";

library.add([
  faUserSecret,
  faArrowRight,
  faArrowRotateLeft,
  faTrash,
  faPlus,
  faPlusMinus,
  faRightFromBracket,
  faLocationDot,
]);

import VueGoogleMaps from '@fawmi/vue-google-maps'
import C from "./constants";

// Create app
const app = createApp(App);

registerGlobalComponents(app);

app.use(VueGoogleMaps, {
  load: {
      key: C.__map_api_key__,
  },
})
app.use(router);
app.component("font-awesome-icon", FontAwesomeIcon);

app.mount("#app");
