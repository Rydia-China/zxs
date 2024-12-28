const base = {
    get() {
                return {
            url : "http://localhost:8080/springboot3fy99/",
            name: "springboot3fy99",
            // 退出到首页链接
            indexUrl: 'http://localhost:8080/springboot3fy99/front/index.html'
        };
            },
    getProjectName(){
        return {
            projectName: "付费自习室管理系统"
        }
    }
}
export default base
