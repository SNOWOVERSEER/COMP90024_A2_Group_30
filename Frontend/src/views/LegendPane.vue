<template>
    <div class="legend-box">
        <div class='exa-title'>The number of new immigrants in 2021</div>
        <div class='exa-gra'>
            <div class='box-color'></div>
            <div class='box-com'>
                <div class='com-top' style="margin-top:10px">70000</div>
                <div class='com-top' style="margin-top:10px">30000</div>
                <div class='com-top' style="margin-top:10px">20000</div>
                <div class='com-top' style="margin-top:10px">10000</div>
                <div class='com-bottom' style="position: absolute; bottom: 0px; margin-bottom: 8px;">0</div>
            </div>
        </div>
    </div>
</template>
  
<script>

export default {
    props: ['cityName', 'data'],
    data() {
        return {

        };
    },
    computed: {},
    watch: {
    },
    mounted() {
    },
    methods: {
    },
};
</script>
  
<style lang="less" scoped>
.legend-box {
    position: absolute;
    right: 10px;
    bottom: 29px;
    background-color: rgba(255, 255, 255, 0.792);
    width: 156px;
    height: 200px;

    .exa-title {
        text-align: center;
        font-size: 14px;
        padding: 9px 0px;
    }

    .exa-gra {
        display: flex;
        width: calc(100% - 20px);
        height: calc(100% - 43px);
        margin: 0px 6px;

        .box-color {
            margin: 10px;
            height: 80%;
            width: 25px;
            background-image: linear-gradient(#070A52, #D21312, #ED2B2A, #F15A59, #FFFFFF);
        }

        .box-com {
            flex: 1;
            font-size: 12px;
        }
    }
}
</style>
  