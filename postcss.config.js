module.exports = {
  plugins: [
    require("autoprefixer"),
    require("@fullhuman/postcss-purgecss")({
      content: ["./templates/**/*.html", "./**/*.js"],
      defaultExtractor: (content) => content.match(/[\w-/:]+(?<!:)/g) || [],
    }),
  ],
};
