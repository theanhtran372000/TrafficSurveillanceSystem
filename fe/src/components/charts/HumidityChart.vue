<template>
    <Line :options="chartOptions" :data="chartData" />
</template>

<script>
import { Line } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, CategoryScale, LinearScale, PointElement, LineElement } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, PointElement, LineElement, CategoryScale, LinearScale)

export default {
    name: 'HumidityChart',
    components: { Line },
    data() {
        return {
            chartData: {
                labels: [
                    3.85015652, 3.57445791, 1.05507904, 4.37997848, 2.5340432,
                    1.68445696, 2.15727183, 2.59316109, 1.48577393, 4.66938808,
                    3.63582428, 1.27011403, 1., 3.24080799, 5.,
                    1.16972822, 2.77439722, 4.99238511, 2.2806182, 1.07315399
                ],
                datasets: [
                    {
                        // label: 'Data One',
                        backgroundColor: 'blue',
                        // showLine: false,
                        // pointBackgroundColor: 'blue',
                        borderColor: 'lightblue',
                        pointBorderColor: 'blue',
                        pointBorderWidth: 2,
                        data: [
                            3.85015652, 3.57445791, 1.05507904, 4.37997848, 2.5340432,
                            1.68445696, 2.15727183, 2.59316109, 1.48577393, 4.66938808,
                            3.63582428, 1.27011403, 1., 3.24080799, 5.,
                            1.16972822, 2.77439722, 4.99238511, 2.2806182, 1.07315399
                        ],
                    },
                    // {
                    //   label: 'Data Two',
                    //   backgroundColor: 'black',
                    //   data: [10, 39, 10, 40, 39, 80, 40]
                    // }
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