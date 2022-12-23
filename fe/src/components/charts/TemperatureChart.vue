<template>
    <Line :options="chartOptions" :data="chartData" />
</template>

<script>
import { Line } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, CategoryScale, LinearScale, PointElement, LineElement } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, PointElement, LineElement, CategoryScale, LinearScale)

export default {
    name: 'TemperatureChart',
    components: { Line },
    data() {
        return {
            chartData: {
                labels: [
                    2.05254312, 2.72304548, 2.34615657, 2.52706301, 1.77471926,
                    4.74387723, 1.07245478, 3.98738784, 4.44451536, 3.75109127,
                    2.01832581, 1.79741293, 4.12948367, 1.88547683, 4.83569445,
                    2.65002563, 3.48484834, 1.67618699, 4.92198873, 4.00021838,
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
                            2.05254312, 2.72304548, 2.34615657, 2.52706301, 1.77471926,
                            4.74387723, 1.07245478, 3.98738784, 4.44451536, 3.75109127,
                            2.01832581, 1.79741293, 4.12948367, 1.88547683, 4.83569445,
                            2.65002563, 3.48484834, 1.67618699, 4.92198873, 4.00021838,
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