c.NotebookApp.tornado_settings = {
    'headers': {
        'Content-Security-Policy': "frame-ancestors https://7chats.example.com 'self' "
    }
}
define(['base/js/namespace'], function(Jupyter){
    Jupyter._target = '_self';
});
