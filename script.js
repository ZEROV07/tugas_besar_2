
var socket = io();
var username;

//while (username == null || username == "")
//{
	username = prompt("Please enter your nick name:");
//}

socket.on('connect', () =>
{
	socket.emit('join', username);
});

socket.on('disconnect', () =>
{
	alert("Server downed...");
});

socket.on('broadcast', (data) =>
{
	var un = data['username'];
	var msg = data['message'];
	var info = data['info'];
	var pre = document.createElement('pre');
	if (msg !== '')
	{
		if (un === username)
		{
			un = 'You';
		}
		msg = un + ": " + msg;
	}
	else if (un !== username)
	{
		msg = un + info;
	}
	else //if (un === username)
	{
		msg = "You've just " + info;
	}
	pre.innerHTML = msg;
	document.body.appendChild(pre);
});

function writeMessage()
{
	var msg = prompt("Write your message:");
	if (msg != null && msg != "")
	{
		socket.emit('sendMessage', { 'username': username, 'message': msg, 'info': '' });
	}
}
