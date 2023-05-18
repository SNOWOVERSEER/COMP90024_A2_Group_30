<template>
    <div class="city-info-box">
        <div class="title">{{ stateName }}</div>
        <div class="info-1">{{ 'Number of Non-English Tweets: ' + data.total }}</div>
        <div id="cityChart"></div>
        <div class="info-2">Top 10 Non-English Languages</div>
    </div>
</template>
  
<script>
import * as echarts from 'echarts/core';
import { GridComponent, LegendComponent } from 'echarts/components';
import { BarChart } from 'echarts/charts';
import { CanvasRenderer } from 'echarts/renderers';

echarts.use([GridComponent, LegendComponent, BarChart, CanvasRenderer]);

export default {
    props: ['stateName', 'data'],
    data() {
        return {
            myChart: null,
            option: {
                // color: ['rbg(249,255,255)'],
                xAxis: {
                    max: 'dataMax',
                    axisLine: {
                        show: false
                    },
                    splitLine: {
                        show: false
                    },
                    axisTick: {
                        show: false
                    }
                },
                grid: {
                    top: 10,
                    left: 35,
                    right: 35,
                    bottom: 20,
                },
                yAxis: {
                    type: 'category',
                    data: [],
                    inverse: true,
                    axisLine: {
                        show: false
                    },
                    splitLine: {
                        show: false
                    },
                    axisTick: {
                        show: false
                    }
                },
                series: [
                    {
                        realtimeSort: true,
                        name: 'X',
                        type: 'bar',
                        data: [],
                        label: {
                            show: true,
                            position: 'right',
                            valueAnimation: true
                        },
                        itemStyle: {
                            normal: {
                                color: '#F97B22'
                            }
                        }
                    }
                ],
            }
        };
    },
    computed: {},
    watch: {
        "data"(value) {
            if (!value) return

            this.initData()

            this.myChart.setOption(this.option);
        }
    },
    mounted() {
        this.initChart()
    },
    methods: {
        initData() {
            if (!this.data) return

            const v = Object.assign({}, this.data)
            delete v.total
            const keys = Object.keys(v)
            const values = Object.values(v)

            this.option.yAxis.data = keys
            this.option.series[0].data = values
        },
        initChart() {
            const dom = document.getElementById('cityChart');
            this.myChart = echarts.init(dom)

            this.initData();
            this.option && this.myChart.setOption(this.option);
        }
    },
};
</script>
  
<style lang="less" scoped>
.city-info-box {
    position: absolute;
    top: 10px;
    left: 10px;
    background-color: rgba(255, 255, 255, 0.792);
    width: 350px;
    height: 470px;

    .title {
        text-align: center;
        font-size: 18px;
        padding: 9px 0px;
        font-weight: 900;
    }

    .info-1 {
        font-size: 16px;
        padding: 4px 18px;
        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    }

    #cityChart {
        position: relative;
        height: 350px;
        width: 100%;
    }

    .info-2 {
        font-size: 16px;
        padding: 15px 18px;
        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    }
}
</style>
  