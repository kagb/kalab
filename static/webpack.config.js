
module.exports = {
  entry: {
    index: './src/js/index.js' 
  },

  output: {
    path: './dist/js/',
    publicPath: './js/',
    filename: '[name].js'
  },

  devServer: {
    inline: true,
    port: 8080
  },

  module: {
    loaders: [
    { test: /\.js?$/, loaders: ['babel'], exclude: /node_modules/ },
    { test: /\.js$/, loader: 'babel-loader', exclude: /node_modules/}
    ]
  },

  resolve:{
    root: '/pomy/github/flux-example/src', 
    extensions:['','.js','.json']
  },
};
