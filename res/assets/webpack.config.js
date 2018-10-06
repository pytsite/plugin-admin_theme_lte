const path = require('path');
const webpack = require('webpack');
const webpackMerge = require('webpack-merge');

module.exports = env => {
    return webpackMerge(require('@pytsite/assetman/webpack-base.config')(env), {
        entry: [path.join(__dirname, 'index.js')],
        plugins: [
            new webpack.ProvidePlugin({
                jQuery: 'jquery', // Bootstrap 3 expects presence of jQuery global
            }),
        ]
    });
};
