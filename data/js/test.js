"use strict";
var page = require('webpage').create();

page.onConsoleMessage = function(msg) {
    console.log('[PhantomJS evaluate] '+msg)
};

function resize(selector, times) {
    var clip = page.evaluate(function(slt){
        var e = document.querySelector(slt);
        // console.log(e.textContent);
        var clipRect = e.getBoundingClientRect();
            return clipRect;
    }, selector);

    // zoom page
    page.zoomFactor = times;

    clip.left = times * clip.left;
    clip.top = times * clip.top;
    clip.width = times * clip.width;
    clip.height = times * clip.height;

    return clip;
}

page.viewportSize = { width: 1600, height: 800 };
// var url = 'http://localhost:8888/unicode/u234ef';
// var url = 'http://localhost:8888/unicode/u6C38';
var url = 'http://localhost:8888/unicode/list/cjk-ideo-a';
page.open(url, function (status) {
    if (status !== 'success') {
        console.log('Unable to load the address!');
        phantom.exit(1);
    } else {
        page.clipRect = resize('td.u span', 10);
        page.render('test.png');
        phantom.exit();

        // var clip = page.evaluate(function() {
        //     return {
        //         left: document.body.clientLeft,
        //         top: document.body.clientTop,
        //         width: document.body.clientWidth,
        //         height: document.body.clientHeight
        //     }
        // });

        // console.log(clip.left, clip.top, clip.width, clip.height);

        // window.setTimeout(function () {
        //     //page.render(output);  
        //     phantom.exit();
        // }, 200);
    }
});