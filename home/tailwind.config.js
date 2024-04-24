/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./templates/**/*.html', './home/templates/**/*.html','./home/static/src/**/*.css'],
  theme: {
    colors: {
      'background': '#fef9e7',
      'button': '#631d4c',
      'main': '#8e3557',
      'footer': '#631d4c',
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

