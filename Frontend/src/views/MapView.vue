<template>
  <div class="box">
    <div id="map"></div>
    <state-info-pane v-if="currentState" :state-name="currentState" :data="stateData || {}"></state-info-pane>
    <legend-pane></legend-pane>
  </div>
</template>

<script>
import mapboxgl from 'mapbox-gl'
import 'mapbox-gl/dist/mapbox-gl.css'
import StateInfoPane from './StateInfoPane.vue';
import LegendPane from './LegendPane.vue';

import { getStateData, getImmigration, getStateGeodata } from '@/api/api';

export default {
  name: "MapView",
  components: { StateInfoPane, LegendPane, },
  data() {
    return {
      map: null,
      popup: null,
      currentState: null,
      stateData: null,
      allStateData: null
    };
  },
  computed: {},
  mounted() {
    this.initMap()
    this.initEvent()
  },
  methods: {
    // init the map, include source and layer
    initMap() {
      // Get a mapbox API access token
      mapboxgl.accessToken = 'pk.eyJ1IjoidWJlcmRhdGEiLCJhIjoiY2pudzRtaWloMDAzcTN2bzN1aXdxZHB5bSJ9.2bkj3IiRC8wj3jLThvDGdA';

      // Initialize mapbox map
      this.map = new mapboxgl.Map({
        container: 'map',
        style: 'mapbox://styles/mapbox/streets-v12',
        center: [137.970223, -27.578757],
        zoom: 2.5,
        // projection: 'mercator'
      });

      this.map.on('load', () => {

        this.$axios.all([getImmigration(), getStateGeodata()])
          .then(this.$axios.spread((immgRes, geoRes) => {

            const immgData = immgRes.data[0]
            const stateGeo = geoRes.data
          
            for (let i = 0; i < stateGeo.features.length; i++) {
              const sName = stateGeo.features[i].properties.ste_name16
              stateGeo.features[i].properties.value = immgData[sName]
            }


            this.map.addSource('state-geodata', {
              type: 'geojson',
              data: stateGeo
            });

            this.map.addLayer({
              id: 'province-layer',
              type: 'fill',
              source: 'state-geodata',
              layout: {},
              'paint': {
                // 'fill-color': [
                //   'step',
                //   ['get', 'value'],
                //   '#FFFFFF',
                //   2000, '#FFE1E1',
                //   8000, '#FF74B1',
                //   16000, '#ED2B2A',
                //   20000, '#070A52',
                // ],
                'fill-color': [
                  'interpolate',
                  ['linear'],
                  ['to-number', ['get', 'value']],
                  0, '#FFFFFF',
                  10000, '#F15A59',
                  20000, '#ED2B2A',
                  30000, '#D21312',
                  70000, '#070A52'
                ],
                'fill-opacity': 0.77
              }
            })

            this.map.addLayer({
              'id': 'province-outline',
              'type': 'line',
              'source': 'state-geodata',
              'layout': {},
              'paint': {
                'line-color': '#000',
                'line-width': 2,
                'line-opacity': 0.5
              }
            });

            this.$axios.get('./data/provinceSymb.geojson').then(res => {
              this.map.addSource('provinceSymb-geodata', {
                type: 'geojson',
                data: res.data
              });

              this.map.addLayer({
                id: 'province-symbel-layer',
                type: 'symbol',
                'source': 'provinceSymb-geodata',
                layout: {
                  'text-field': ['get', 'ste_name16'],
                  'text-size': 18
                },
                paint: {
                  'text-halo-color': '#fff',
                  'text-halo-width': 2
                }
              })
            })

            this.$axios.get('./data/city.geojson').then(res => {
              this.map.addSource('city-geodata', {
                type: 'geojson',
                data: res.data
              });

              this.map.addLayer({
                'id': 'city-layer',
                'type': 'circle',
                'source': 'city-geodata',
                'paint': {
                  'circle-color': '#4264fb',
                  'circle-radius': 6,
                  'circle-stroke-width': 2,
                  'circle-stroke-color': '#ffffff'
                }
              })

              this.map.addLayer({
                id: 'city-symbel-layer',
                type: 'symbol',
                'source': 'city-geodata',
                layout: {
                  'text-field': ['get', 'name'],
                  'text-size': 14,
                  'text-offset': [0, 1]
                },
                paint: {
                  'text-halo-color': '#fff',
                  'text-halo-width': 2
                }
              })
            })

          }))
      })
    },
    // init events , click event and pop
    async initEvent() {
      const res = await getStateData()
      console.log(res)
      this.allStateData = res.data[0]

      this.popup = new mapboxgl.Popup({
        closeButton: false,
        closeOnClick: false
      });

      this.map.on('click', ['province-layer', 'province-symbel-layer'], (e) => {
        const cityName = e.features[0].properties.ste_name16
        this.currentState = cityName
        this.stateData = this.allStateData[cityName]
      })

      this.map.on('mouseenter', ['province-layer', 'province-symbel-layer'], (e) => {
        // Change the cursor style as a UI indicator.
        this.map.getCanvas().style.cursor = 'pointer';

        // Copy coordinates array.
        const coordinates = e.features[0].geometry.coordinates.slice();

        // Ensure that if the map is zoomed out such that multiple
        // copies of the feature are visible, the popup appears
        // over the copy being pointed to.
        while (Math.abs(e.lngLat.lng - coordinates[0]) > 180) {
          coordinates[0] += e.lngLat.lng > coordinates[0] ? 360 : -360;
        }

        // Populate the popup and set its coordinates
        // based on the feature found.
        //this.popup.setLngLat(coordinates).setHTML('').addTo(this.map);
      })

      this.map.on('mouseleave', ['province-layer', 'province-symbel-layer'], () => {
        this.map.getCanvas().style.cursor = '';
        this.popup.remove();
      });
    }
  },
};
</script>

<style lang="less" scoped>
.box {
  position: relative;
  height: 100%;
  width: 100%;

  #map {
    position: relative;
    height: 100%;
    width: 100%;
  }
}
</style>
