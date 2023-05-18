<template>
  <div class="box">
    <h2 class="h2">About the Project</h2>
    <p class="desc">
      This project utilizes Nginx as a proxy for the CouchDB cluster and employs Docker Swarm to manage the backend. 
      Mastodon harvesters deployed using Ansible and Docker.
      This architecture achieves a highly available and scalable system. 
      Nginx acts as a load balancer and reverse proxy, distributing traffic to different nodes in the CouchDB cluster,
      thereby enhancing performance and reliability. The backend is powered by Django, a high-level Python web framework, 
      while the frontend is developed using Vue, a popular JavaScript framework.<br>
      As for the story, we would like to discuss the relationship between immigration numbers in Australia in 2021 and 
      the number of non-English tweets by state. The immigration data for each state in 2021 and 
      non-English tweets are sourced from "sudo" and "twitter-huge." We have visualized this data on the map page of our platform. 
      Additionally, we have collected the number of non-English toots from Mastodon and presented it on the statistics page, 
      which is continuously updated.
    </p>
    <h2 class="h2">About Us</h2>

    <div class="picBox">
      <div class="picItem">
        <img class="picItemImg" src="../assets/XuChuyuan.png" />
        <div class="picItemName">Chuyuan Xu</div>
        <div class="picItemId">1398756</div>
        <div class="picItemDesc">Project Manager</div>
      </div>
      <div class="picItem">
        <img class="picItemImg" src="../assets/HetongWang.jpg" />
        <div class="picItemName">Hetong Wang</div>
        <div class="picItemId">1398479</div>
        <div class="picItemDesc">Tester</div>
      </div>
      <div class="picItem">
        <img class="picItemImg" src="../assets/JinhuaFan.png" />
        <div class="picItemName">Jinhua Fan</div>
        <div class="picItemId">1398524</div>
        <div class="picItemDesc">Backend Development</div>
      </div>
      <div class="picItem">
        <img class="picItemImg" src="../assets/XingkaiZhou.png" />
        <div class="picItemName">Xingkai Zhou</div>
        <div class="picItemId">1318620</div>
        <div class="picItemDesc">Frontend Development</div>
      </div>
      <div class="picItem">
        <img class="picItemImg" src="../assets/YuxuanZeng.png" />
        <div class="picItemName">Yuxuan Zeng</div>
        <div class="picItemId">1358012</div>
        <div class="picItemDesc">Deployment</div>
      </div>

    </div>
  </div>
</template>

<script>
export default {
  name: "HomeView",

  data() {
    return {};
  },
  computed: {},
  mounted() {},
  methods: {},
};
</script>

<style scoped>
.h2 {
    text-align: center;
    color: rgb(28, 54, 114);
    text-align: center;
    margin: 30px 0;
}

.desc {
    background: #fff;
    border-radius: 5px;
    padding: 20px;
    /* margin: auto; */
    color: #666;
}

.picBox {
    display: flex;
    justify-content: space-between;
    /* margin: auto; */
    flex-wrap: wrap;
}

.picItem {
    padding: 10px 15px;
    display: flex;
    align-items: center;
    flex-direction: column;
    background: #fff;
    border-radius: 5px;
    height: 300px;
    margin-bottom: 20px;
}

.picItemImg {
    width: 150px;
    height: 150px;
    border-radius: 50%;
}

.picItemName {
    color: rgb(28, 54, 114);
    font-weight: bold;
    margin: 10px 0;
}

.picItemId {
    font-size: 12px;
    margin-bottom: 10px;
}

.picItemDesc {
    font-size: 14px;
    color: #666;
}
</style>
