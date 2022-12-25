/** @type {import('tailwindcss').Config} */

module.exports = {
  content: [
    "./public/*.{html, js}", 
    "./src/**/*.{vue,js,ts,jsx,tsx}",
    "./src/**/*.{html,js}",
    "./node_modules/tw-elements/dist/js/**/*.js"
  ],
  theme: {
    extend: {
      colors: {
        gray: "#F1F6F5",
        light_blue: "#82C3EC",
        blue: "#4B56D2",
        dark_blue: "#472183",
      },
      backgroundImage: {
        main: "url('@/assets/images/home_bg.jpg')",
      },
    },
  },
  plugins: [
    require('tw-elements/dist/plugin')
  ],
};
