/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./templates/**/*.html', './home/templates/**/*.html','./home/static/src/**/*.css'],
  theme: {
    colors: {
      'background': '#f2ecce',
      'button': '#cbd966',
      'main': '#5da6a6',
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

