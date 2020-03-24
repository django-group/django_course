console.log(window.location);

var endpoint = '';
var wsStart = 'ws://'; + window.location.host + window.location.pathname
var socket = new WebSocket(endpoint);

socket.onmessage = function(e){
    console.log('message', e)
};
socket.onclose = function(e){
    console.log('close', e)
};
socket.onopen = function(e){
    console.log('open', e)
};
socket.onerror = function(e){
    console.log('error', e)
};