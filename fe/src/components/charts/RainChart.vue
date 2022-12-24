<template>
    <Line :options="chartOptions" :data="chartData" />
</template>

<script>
import { Line } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, CategoryScale, LinearScale, PointElement, LineElement } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, PointElement, LineElement, CategoryScale, LinearScale)

export default {
    name: 'Rain',
    components: { Line },
    data() {
        return {
            chartData: {
                labels: [
                    4.87913971, 3.20345304, 1.92842456, 2.32715841, 1.70288704,
                    2.6610292, 3.36052878, 4.08391068, 4.15704119, 5.,
                    1.6370413, 4.97999329, 1.07490559, 3.54817928, 1.01055169,
                    4.2469145, 4.1990827, 4.19403955, 1., 1.56512295
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
                            4.87913971, 3.20345304, 1.92842456, 2.32715841, 1.70288704,
                            2.6610292, 3.36052878, 4.08391068, 4.15704119, 5.,
                            1.6370413, 4.97999329, 1.07490559, 3.54817928, 1.01055169,
                            4.2469145, 4.1990827, 4.19403955, 1., 1.56512295
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