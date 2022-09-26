import axios from "axios";

axios.defaults.baseURL = "/api"
axios.defaults.timeout = 1000

axios.interceptors.request.use(
    config => {
        return config
    }
)

axios.interceptors.response.use(
    response => {
        return response
    }, error => {
        if (error.response.status == 401) {
            return error.response
        }
        return Promise.reject(error)
    })


export default axios