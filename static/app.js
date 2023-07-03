import Header from './components/Header.js'
import Blog from './components/Blog.js'

new Vue({
  el: '#app',
  template: `
  <div> 
    <Header />
    <Blog v-for="blog in blogs" :blog='blog' />
  </div>`,
  data: {
    blogs: [],
  },
  components: {
    Header,
    Blog,
  },

  mounted() {
    fetch('api/blogs')
      .then((res) => {
        return res.json()
      })
      .then((data) => {
        this.blogs = data
      })
  },
})
