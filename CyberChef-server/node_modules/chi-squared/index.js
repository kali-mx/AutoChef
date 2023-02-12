var gamma = require('gamma');

exports.pdf = function (x, k_) {
    if (x < 0) return 0;
    var k = k_ / 2;
    return 1 / (Math.pow(2, k) * gamma(k))
        * Math.pow(x, k - 1)
        * Math.exp(-x / 2)
    ;
};

exports.cdf = require('./cdf')
