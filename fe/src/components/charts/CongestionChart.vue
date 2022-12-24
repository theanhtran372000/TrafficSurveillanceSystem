<template>
    <Line :options="chartOptions" :data="chartData" />
</template>

<script>
import { Line } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, CategoryScale, LinearScale, PointElement, LineElement } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, PointElement, LineElement, CategoryScale, LinearScale)

export default {
    name: 'Congestion',
    components: { Line },
    data() {
        return {
            chartData: {
                labels: [
                    4.38996661, 1.9540627, 2.13747743, 2.62528803, 3.89827909,
                    4.69071024, 4.63563103, 1.89497572, 1.80830698, 1.60445081,
                    5., 1., 1.0505854, 3.44040416, 3.1610601,
                    4.06318557, 1.30991429, 3.29271835, 1.50441718, 1.11916392,
                    1.10355432, 4.93217878, 1.69567784, 4.80203812, 1.86131447,
                    1.04576128, 2.86692299, 1.92455766, 4.40920307, 2.2125558
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
                            4.38996661, 1.9540627, 2.13747743, 2.62528803, 3.89827909,
                            4.69071024, 4.63563103, 1.89497572, 1.80830698, 1.60445081,
                            5., 1., 1.0505854, 3.44040416, 3.1610601,
                            4.06318557, 1.30991429, 3.29271835, 1.50441718, 1.11916392,
                            1.10355432, 4.93217878, 1.69567784, 4.80203812, 1.86131447,
                            1.04576128, 2.86692299, 1.92455766, 4.40920307, 2.2125558
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