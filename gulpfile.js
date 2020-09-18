const { dest, src, series, watch } = require('gulp');
const less = require('gulp-less');


const BASE_DIR = './ckanext/biskit/fanstatic';

function build(cb) {
  src(`${BASE_DIR}/styles/less/biskit.less`)
    .pipe(less())
    .pipe(dest(`${BASE_DIR}/styles`));

  cb();
}

function watchSource(cb) {
  watch(`${BASE_DIR}/**/*.less`, build);
  cb();
}

exports.build = build;
exports.watch = watchSource;
exports.default = series(build, watchSource);
