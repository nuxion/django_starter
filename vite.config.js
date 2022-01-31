import { defineConfig } from 'vite'
const { resolve } = require('path')

export default defineConfig({
  root: resolve('./theme/static/src'),
  base: '/static/',
  build: {
    manifest: true,
    outDir: resolve('./theme/static/dist'),
    emptyOutDir: true,
    target: 'es2015',
    rollupOptions: {
      input: {
        main: resolve('./theme/static/src/main.js')
        
      }
    }
  }
})
