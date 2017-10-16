"use strict";
var page = require('webpage').create(),
    system = require('system'),
    fs = require('fs');

//capture and captureSelector functions adapted from CasperJS - https://github.com/n1k0/casperjs
// var captureSelector = function(targetFile, selector) {

//     return capture(targetFile, page.evaluate(function(slt) {  
//         try { 
//             var clipRect = document.querySelector(slt).getBoundingClientRect();
//             return {
//                 top: clipRect.top,
//                 left: clipRect.left,
//                 width: clipRect.width,
//                 height: clipRect.height
//             };
//         } catch (e) {
//             console.log("Unable to fetch bounds for element " + slt, "warning");
//         }
//     }, selector));
// }

// var capture = function(targetFile, clipRect) {
//     if (clipRect) {
//         console.log('Capturing page to ' + targetFile + ' with clipRect' + JSON.stringify(clipRect), "debug");
//         try {
//             page.clipRect = clipRect;
//             page.render(targetFile);
//         } catch (e) {
//             console.log('Failed to capture screenshot as ' + targetFile + ': ' + e, "error");
//         }

//         return this;
//     }
//     else{
//         console.log('clipRect is null');
//     }
// }

page.onConsoleMessage = function(msg) {
    console.log('[PhantomJS evaluate] '+msg)
};

function resize_rect(zoomfactor, rect) {
    rect.left = zoomfactor * rect.left;
    rect.top = zoomfactor * rect.top;
    rect.width = zoomfactor * rect.width;
    rect.height = zoomfactor * rect.height;
    return rect
}

if (system.args.length < 3 || system.args.length > 5) {
    console.log('Usage: capture_element.js URL selector output [zoom] [size]');
    console.log('         selector: css selector');
    console.log('         output: directory');
    console.log("Note: captures will be named by element's id, name attribute or textContent");
    phantom.exit(1);
} else {
    var address = system.args[1];
    var selector = system.args[2];
    var outputdir = fs.absolute(system.args[3]);
    

    // viewportSize effectively simulates the size of the window like in a traditional browser
    // var pageWidth = 800;
    // var pageHeight = 600;
    // if (system.args.length > 5 && system.args[5].indexOf('*') != -1) {
    //     size = system.args[5].split('*');
    //     pageWidth = parseInt(size[0], 10);
    //     pageHeight = parseInt(size[1], 10);
    // }
    // page.viewportSize = { width: pageWidth, height: pageHeight };
    
    // clipRect defines the rectangular area of the web page to be rasterized 
    // when page.render is invoked. 
    // If no clipping rectangle is set, page.render will process the entire web page. so the 
    // size of screenshot is controlled by clipRect
    // page.clipRect = { top: 0, left: 0, width: pageWidth, height: pageHeight };
    
    if (system.args.length > 4) {
        var zoomfactor = parseInt(system.args[4], 10);
    }
    else {
        var zoomfactor = 1;
    }

    page.zoomFactor = zoomfactor;

    page.open(address, function (status) {
        if (status !== 'success') {
            console.log('Unable to load the address!');
            phantom.exit(1);
        } else {
            // window.setTimeout(function () {
            //     page.render(output);
            //     phantom.exit();
            // }, 200);
            var clipRects = page.evaluate(function(slt) {
                var elelist = document.querySelectorAll(slt);
                var rects = [];
                for (var i=0; i<elelist.length; i++) {
                    var e = elelist[i];
                    if (e.hasAttribute('name')) {
                        rects.push([e.getAttribute('name'), e.getBoundingClientRect()]);
                    }
                    else if (e.hasAttribute('id')) {
                        rects.push([e.getAttribute('id'), e.getBoundingClientRect()]);
                    }
                    else {
                        rects.push([e.textContent, e.getBoundingClientRect()]);
                    }
                }
                return rects;
            }, selector);
            for(var i=0; i<clipRects.length; i++) {
                var clipRect = clipRects[i];
                page.clipRect = resize_rect(zoomfactor, clipRect[1]);
                var filename = [outputdir, clipRect[0]+'.png'].join(fs.separator);
                page.render(filename);
            }
            phantom.exit();
        }
    });
}