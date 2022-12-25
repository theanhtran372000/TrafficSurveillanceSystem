<template>
    <!-- <Line :options="chartConfig.data" :data="chartConfig.options" /> -->
    <canvas id="chart"></canvas>
</template>

<script>
import { ref, onMounted } from 'vue';
import Chart from 'chart.js/auto';
import { Line } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, CategoryScale, LinearScale, PointElement, LineElement, ChartData } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, PointElement, LineElement, CategoryScale, LinearScale)

export default {
    name: 'LineChart',
    components: { Line },
    props: {
        data: Object,
    },
    data() {
        return {
            myChart: null,
            chartConfig: {
                type: 'line',
                data: {
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
                options: {
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
            },
        }
    },

    mounted() {
        console.log(this.chartConfig.data.labels)
        this.renderLineChart()
    },
    
    methods: {
        renderLineChart() {
            const ctx_live = document.getElementById('chart')
            this.myChart = new Chart(ctx_live, this.chartConfig)
        }
    },

    watch: {
        data(newval) {
            this.myChart.data.labels = Object.keys(newval)
            this.myChart.data.datasets[0].data = Object.values(newval)
            // console.log(this.myChart.data.labels)
            // console.log(this.myChart.data.datasets[0].data)
            // this.myChart.clear()
            this.myChart.destroy()
            this.renderLineChart()
        }
    },
}
</script>