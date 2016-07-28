
module.exports = {
  entry: {
    base: ['./src/js/base.js'] 
  },

  output: {
    path: './dist/js/',
    filename: '[name].js'
  },

  module: {
    loaders: [
       {
           test: /\.jsx?$/,
           exclude: /node_modules/,
           loader: 'babel',
           query: { presets: ['es2015', 'react']}
        },
    ]
  },
};
