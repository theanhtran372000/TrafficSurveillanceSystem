<template>
    <Line :options="chartOptions" :data="chartData" />
</template>

<script>
import { Line } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, CategoryScale, LinearScale, PointElement, LineElement } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, PointElement, LineElement, CategoryScale, LinearScale)

export default {
    name: 'Temperature',
    components: { Line },
    props: {
        data: Object,
    },
    data() {
        return {
            chartData: {
                labels: Object.keys(this.data),
                datasets: [
                    {
                        backgroundColor: 'blue',
                        borderColor: 'lightblue',
                        pointBorderColor: 'blue',
                        pointBorderWidth: 2,
                        data: Object.values(this.data),
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