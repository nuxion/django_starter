const colors = require("tailwindcss/colors");

module.exports = {
  content: ['./home/templates/**/*.{js,ts,jsx,tsx,html}'],
  darkMode: "class", // or 'media' or 'class'
  theme: {
    extend: {
      fontFamily: {
        sans: ["Nunito Sans"],
        serif: ["Nunito"],
        mono: ["Roboto Mono"],
      },
      colors: {
        lime: colors.lime,
        orange: colors.orange,
      },
    },
  },
  variants: {
    extend: {
      animation: ["group-hover", "hover", "focus"],
      textColor: ["group-hover", "hover", "focus"],
    },
  },
  plugins: [require("@tailwindcss/forms")],
};
