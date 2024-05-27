/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./templates/**/*.html', './home/templates/**/*.html','./home/static/src/**/*.css'],
  theme: {
    colors: {
      'background': '#f2f2f2',
      'button': '#cbd966',
      'main': '#733f5c',
      'footer': '#cbd966',
      'white': '#ffffff',
      'black': '#000000',
    },
    extend: {
      fontFamily: {
        poppins: ['Poppins'],
      }
    },
  },
  plugins: [],
}

