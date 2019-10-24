'use strict';

var gulp = require('gulp'),
    gp   = require('gulp-load-plugins')(),
    bs   = require('browser-sync').create();

gulp.task('serve', function() {
    bs.init({
        server: {
            baseDir: "./build"
        }
    });
});

gulp.task('watch', function() {
    gulp.watch('static/pug/**/*.pug', gulp.series('pug'));
    gulp.watch('static/scss/**/*.scss', gulp.series('sass'));
    gulp.watch('static/js/*.js', gulp.series('scripts'));
});

gulp.task('sass', function() {
    return gulp.src('static/scss/*.scss')
        .pipe(gp.sass({
            'include css': true
        }))
        .pipe(gp.csso())
        .pipe(gulp.dest('build/static/css/'))
        .pipe(bs.reload({
            stream: true //После обновления браузера страница не передвинется на самый верх, а останется там же
        }));
});

gulp.task('pug', function() {
    return gulp.src('static/pug/*.pug')
        .pipe(gp.pug({
            pretty: true
        }))
        .pipe(gulp.dest('build'))
        .pipe(bs.reload({
            stream: true //После обновления браузера страница не передвинется на самый верх, а останется там же
        }));
});

gulp.task('scripts', function() {
    return gulp.src('static/js/index.js')
        .pipe(gulp.dest('build/static/js'))
        .pipe(bs.reload({
            stream: true //После обновления браузера страница не передвинется на самый верх, а останется там же
        }));
});

gulp.task('default', gulp.series(
    gulp.parallel('sass', 'pug', 'scripts'),
    gulp.parallel('watch', 'serve')
));
