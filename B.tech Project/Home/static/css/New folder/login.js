function makelogin(){
    var div=document.createElement('div');
    div.setAttribute('id','faint');
    child=document.createElement('div');
    child.setAttribute('style','opacity:0.8;background-color:black;width:100%;position:absolute;height:100%;z-index:10005;');
    div.appendChild(child);
    child=document.createElement('div');
    child.setAttribute('style','text-align:center;position:absolute;z-index:10006;margin:10% 25%;width:50%;padding:1%;border-radius:12px;box-shadow:0 0 5px white;background-color: #f2f2f2;');
    form=createElement('form');
    
    div.appendChild(child);
    body.appendChild(div);
}