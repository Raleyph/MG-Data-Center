const electron = require('electron')
const app = electron.app
var path = require('path')

const BrowserWindow = electron.BrowserWindow

app.on('ready', function() {
    let window = new BrowserWindow({
        width: 1280,
        height: 720,
        frame: false,

        webPreferences:{
            preload: path.join(__dirname, 'preload.js'),
            enableRemoteModule: true
        }
    })

    window.setMenuBarVisibility(false)
    window.openDevTools({ detach: true })
    window.loadURL('file://' + __dirname + '/app/index.html')

    window.once('ready-to-show', function() {
        window.show()
    })
})

app.on('window-all-closed', function() {
    if(process.platform !== 'darwin') app.quit()
})