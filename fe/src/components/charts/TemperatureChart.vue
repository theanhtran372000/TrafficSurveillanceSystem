<template>
    <Line :options="chartOptions" :data="chartData" />
</template>

<script>
import { Line } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, CategoryScale, LinearScale, PointElement, LineElement } from 'chart.js'
import temp from './data/TemperatureData'

ChartJS.register(Title, Tooltip, Legend, PointElement, LineElement, CategoryScale, LinearScale)

export default {
    name: 'Temperature',
    components: { Line },
    data() {
        return {
            chartData: {
                labels: Object.keys( temp ),
                datasets: [
                    {
                        // label: 'Data One',
                        backgroundColor: 'blue',
                        // pointBackgroundColor: 'blue',
                        borderColor: 'lightblue',
                        pointBorderColor: 'blue',
                        pointBorderWidth: 2,
                        data: Object.values( temp ),
                    },
                ]
            },
            chartOptions: {
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
        }
    },
}
</script>