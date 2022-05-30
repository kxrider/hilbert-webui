let rows = 30;
let cols = 90;

		
function rowsToPixel(rows, cols) {
	let heightpx = Math.floor(rows*17.7);
    let widthpx = Math.floor(cols*9.15);
    return [widthpx, heightpx];
}

let terminal = document.getElementById("terminal");
pxs = rowsToPixel(rows, cols);
terminal.style.width = pxs[0].toString() + "px";
terminal.style.height = pxs[1].toString() + "px";
var term = new Terminal({
	cols: cols,
	rows: rows
});

var curr_line= "";
var entries= [];
term.setOption('fontSize', 15);
term.setOption('cursorBlink', true);
term.setOption('cursorStyle', 'none');
term.open(document.getElementById("terminal"));
term.write("HilbertServer-$: ");
		
term.prompt = () => {
	if (curr_line) {
		let data = { method: "command", command: curr_line};
		ws.send(JSON.stringify(data));
	}
};
term.prompt();


let socket = io();
socket.on('termUpdate', msg => {
    term.write(msg);
});



/*
let rows2 = 2;
let cols2 = cols;
	
			
function rowsToPixel(rows, cols) {
	let heightpx = Math.floor(rows*17.7);
	let widthpx = Math.floor(cols*9.15);
	return [widthpx, heightpx];
}

let input = document.getElementById("input");
pxs = rowsToPixel(rows2, cols2);
input.style.width = pxs[0].toString() + "px";
input.style.height = pxs[1].toString() + "px";


if ("{{current_user.typeInput}}"=='True') {
	input.disabled = false;
} else {
	input.disabled = true;
}

input.addEventListener("keyup", function(event) {
	if (event.keyCode === 13) {
   		event.preventDefault();
		term.write(input.value);
		term.write("\r\n" + ">");
   		input.value = "";
  	}
});*/