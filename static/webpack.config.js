
module.exports = {
  entry: {
    index: './src/js/index.js' 
  },

  output: {
    path: './dist/js/',
    filename: '[name].js'
  },

  devServer: {
    inline: true,
    port: 8080
  },

  module: {
    loaders: [
       {
           test: /\.jsx?$/,
           exclude: /node_modules/,
           loader: 'babel',
           query: { presets: ['es2015', 'react']}
        }
    ]
  },
};
