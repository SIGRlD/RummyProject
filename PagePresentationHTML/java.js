class Card{
	constructor(i){
		if(i==0){
			this.src=String("carte/back.png")
		}
		if(i>=1 & i<=13){
			this.src=String("carte/club_"+i+".png");
			this.color="club";
		}
		this.number=i%13;
		if(i>=14 & i<=26){
			let a=i-13;
			this.src=String("carte/diamond_"+a+".png");
			this.color="diamond";
		}
		if(i>=27 & i<=39){
			let b=i-26;
			this.src=String("carte/heart_"+b+".png");
			this.color="heart";
		}
		if(i>=42 & i<=54){
			let c=i-41;
			this.src=String("carte/spade_"+c+".png");
			this.color="spades";
		}
		if(i==40){
			this.src=String("carte/joker_black.png");
			this.color="joker";
		}
		if(i==41){
			this.src=String("carte/joker_red.png");
			this.color="joker";
		}
	}
}	
function allowDrop(ev) {
  ev.preventDefault();
}

function drag(ev) {
  ev.dataTransfer.setData("text", ev.target.id);
}

function drop(ev) {
  ev.preventDefault();
  var data = ev.dataTransfer.getData("text");
  ev.target.appendChild(document.getElementById(data));
}

var i=prompt("Choisissez un nombre entre 0 et 54");
var cartes= new Card(i);

let Headingimg = document.getElementById('main1');
Headingimg.setAttribute('src', cartes.src);
Headingimg.setAttribute('draggable', 'true');
Headingimg.setAttribute('ondragstart', 'drag(event)');
Headingimg.setAttribute('id', 'drag1');
Headingimg.setAttribute('width', '100');
Headingimg.setAttribute('height', '130');