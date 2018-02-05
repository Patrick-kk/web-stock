<template>
  <div>
    <navigator ref="nav"></navigator>
  </div>
</template>

<script>
import navigator from '@/components/navigator.vue'
export default {
  name: 'home',
  data () {
    return {
    }
  },
  components: {
    navigator
  },
  mounted: function () {
    this.$refs.nav.setActiveIndex('1-2')
  }
}
</script>
