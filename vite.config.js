import { defineConfig } from 'vite'
const { resolve } = require('path')

export default defineConfig({
  root: resolve('./theme/static/src'),
  base: '/static/',
  build: {
    outDir: resolve('./theme/static/dist'),
    rollupOptions: {
      input: {
        main: resolve('./theme/static/src/main.js')
        
      }
    }
  }
})
