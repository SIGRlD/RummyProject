class Card{
	constructor(i){
		if(i==0){
			this.src=String("images/back.png")
		}
		if(i>=1 & i<=13){
			this.src=String("images/club_"+i+".png");
			this.color="club";
		}
		this.number=i%13;
		if(i>=14 & i<=26){
			let a=i-13;
			this.src=String("images/diamond_"+a+".png");
			this.color="diamond";
		}
		if(i>=27 & i<=39){
			let b=i-26;
			this.src=String("images/heart_"+b+".png");
			this.color="heart";
		}
		if(i>=42 & i<=54){
			let c=i-41;
			this.src=String("images/spade_"+c+".png");
			this.color="spades";
		}
		if(i==40){
			this.src=String("images/joker_black.png");
			this.color="joker";
		}
		if(i==41){
			this.src=String("images/joker_red.png");
			this.color="joker";
		}
	}
}	
function allowDrop(ev) {
	ev.preventDefault();
}

function drag(ev) {
  ev.dataTransfer.setData("text", ev.target.id);
  console.log(ev.target.id);
  return ev.target.id
}

function drop(ev) {
	ev.preventDefault();
	var data = ev.dataTransfer.getData("text");
	ev.target.appendChild(document.getElementById(data));
}
let nom=String("spades_"+ 2)
var i=prompt("Choisissez un nombre entre 0 et 54");
var cartes= new Card(i)
let myHeading = document.querySelector('h1');
myHeading.textContent = cartes.src;
let Headingbis = document.querySelector('h3');
Headingbis.textContent = 'This is a drag and drop test before puting it in our "real" HTML page';

let Headingimg = document.getElementById('main1');
Headingimg.setAttribute('src', cartes.src);
Headingimg.setAttribute('draggable', 'true');
Headingimg.setAttribute('ondragstart', 'drag(event)');
Headingimg.setAttribute('id', 'drag1');
Headingimg.setAttribute('width', '100');
Headingimg.setAttribute('height', '130');

let SelectedDiv = document.getElementById('main2');
SelectedDiv.setAttribute('src', "images/joker_red.png");
SelectedDiv.setAttribute('draggable', 'true');
SelectedDiv.setAttribute('ondragstart', 'drag(event)');
SelectedDiv.setAttribute('id', 'drag2');
SelectedDiv.setAttribute('width', '100');
SelectedDiv.setAttribute('height', '130');


let div1=document.getElementById('div1');
let children = div1.childNodes;

console.log(Headingimg.src);
console.log(children);
console.log(document.getElementById('div2').childNodes);
console.log(document.getElementById('div3').childNodes);
let tabtest=[1, 2, 3]
console.log(tabtest.indexOf(1));
console.log(drag);
document.addEventListener('dragenter', function() {
	let i=0;
	let c=0;
	let bodychildren = document.querySelector('body').childNodes;
	console.log(bodychildren);
	for(i; i<(bodychildren.length-1); i++){
		c=0;
		if(bodychildren[i].nodeName=="DIV"){
			let iud = bodychildren[i].id;
			console.log(iud)
			console.log(document.getElementById(iud).childNodes);
			let idchildren = document.getElementById(iud).childNodes;
			console.log(idchildren);
			let j = 0;
			for(j; j<idchildren.length; j++){
				if(idchildren[j].nodeName=="IMG"){
					c=1;
				}
			}
			if(c==0){
				document.getElementById(iud).setAttribute('ondragover', 'allowDrop(event)')
			}
			else{
				document.getElementById(iud).setAttribute('ondragover', '')
			}
		}
	}
});

