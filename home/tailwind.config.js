/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./templates/**/*.html', './home/templates/**/*.html','./home/static/src/**/*.css'],
  theme: {
    colors: {
      'background': '#e3dcca',
      'button': '#b9bf88',
      'text': '#000000',
      'text-white': '#ffffff',
      'text-blue': '#025373',
    },
    extend: {
      fontFamily: {
        poppins: ['Poppins'],
      }
    },
  },
  plugins: [],
}

