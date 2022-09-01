const $ = require('jquery')
const { remote } = require('electron')

var win = remote.getCurrentWindow()

$('minimize').click(function() {
    win.minimize();
});

$('maximize').click(function() {
    if(!win.isMaximized()) {
        win.maximixe();
    } else {
        win.unmaximixe();
    }
});

$('close').click(function() {
    win.close();
});