<template>
  <div
    :style="{
      backgroundImage: 'url(' + require('@/assets/images/home_bg.jpg') + ')',
    }"
    class="w-full h-full"
  >
    <slot />
    <div class="w-full flex justify-center items-center fixed bottom-4">
      <p class="font-normal text-lg text-blue">
        Designed by <span class="font-bold text-gray ml-1">B2K Team</span>
      </p>
    </div>
  </div>
</template>
