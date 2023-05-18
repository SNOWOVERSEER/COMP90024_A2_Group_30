<template>
  <div class="box">
    <div class="title">Data Source: Mastodon</div>
    <div class="sub-title">{{ 'Number of Non-English Toots in Australian server: ' + totalNum }}</div>
    <div id="statChart"></div>

    <div></div>
  </div>
</template>

<script>
import * as echarts from 'echarts/core';
import { GridComponent, TitleComponent } from 'echarts/components';
import { BarChart } from 'echarts/charts';
import { CanvasRenderer, } from 'echarts/renderers';
echarts.use([GridComponent, BarChart, CanvasRenderer, TitleComponent,]);

import { getMastodon } from '@/api/api';

export default {
  name: "StatisticsView",

  data() {
    return {
      totalNum: null,
      myChart: null,
      getDataTimer: null,
      option: {
        title: {
          text: 'Top 10 Non-English Languages on Mastodon',
          left: "center",
          bottom: '0',
          textStyle: {
            fontSize: 18,
            fontWeight: 'bold',
          }
        },
        grid: {
          top: 50,
          left: 100,
          right: 50,
          bottom: 50,
        },
        xAxis: {
          type: 'category',
          data: [],
          axisLine: {
            show: true,
            symbol: ['none', 'arrow'] 
          },
          splitLine: {
            show: false
          },
          axisTick: {
            show: false
          }
        },
        yAxis: {
          name: 'Number of Non-English Toots',
          nameTextStyle: {
            fontSize: 15,
            fontWeight: 'bold',
            padding: [20, 0, 20, 25],
          },
          type: 'value',
          axisLine: {
            show: true,
            symbol: ['none', 'arrow'] 
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
            data: [],
            type: 'bar',
            label: {
              show: true,
              position: 'top',
              valueAnimation: true
            },
            itemStyle: {
              normal: {
                color: '#F97B22'
              }
            }
          }
        ]
      }
    };
  },
  computed: {},
  mounted() {
    this.dealData()
  },
  beforeUnmount() {
    console.log('+++++++++')
    this.getDataTimer = null;
  },
  methods: {
    initChart() {
      const dom = document.getElementById('statChart');
      this.myChart = echarts.init(dom);

      this.myChart.setOption(this.option);
    },
    dealData() {

      getMastodon().then(res => {

        const data = res.data[0].language_count
        this.totalNum = data.total
        delete data.total

        const keys = Object.keys(data)
        const values = Object.values(data)

        this.option.xAxis.data = keys
        this.option.series[0].data = values

        this.initChart()

        this.getDataTimer = setTimeout(() => {
          console.log('========')
          this.dealData()
        }, 9000);
      }).catch(error => {
        console.log(error)
      })
    }
  },
};
</script>

<style lang="less" scoped>
.box {
  position: relative;
  height: 100%;
  width: 100%;
  background-color: white;

  .title {
    padding: 7% 0 0 10%;
    font-size: 20px;
    font-weight: 800;
  }

  .sub-title {
    padding: 20px 0 0 10%;
    font-size: 16px;
  }

  #statChart {
    padding: 20px 0 0 10%;
    width: calc(100% - 40px);
    height: calc(93% - 200px);
  }
}
</style>
