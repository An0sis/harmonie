/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./templates/**/*.html', './home/templates/**/*.html','./home/static/src/**/*.css'],
  theme: {
    colors: {
      'background': '#fef9e7',
      'button': '#631D4C',
      'text': '#000000',
      'text-white': '#ffffff',
      'text-blue': '#8E3557',
    },
    extend: {
      fontFamily: {
        poppins: ['Poppins'],
      }
    },
  },
  plugins: [],
}

