import request from "@/util/request";
import axios from "axios";

export function getStateData() {
  return request({
    method: "get",
    url: "/get-state/",
  });
}

export function getMastodon() {
    return request({
      method: "get",
      url: "/get-mastodon/",
    });
}

export function getImmigration() {
    return request({
      method: "get",
      url: "/get-immigration/",
    });
}

export function getStateGeodata() {
  return axios({
    method: "get",
    url: "./data/province.geojson",
  });
}
