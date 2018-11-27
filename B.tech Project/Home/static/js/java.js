var n=0;
function Click(n)
{
               if(n){
                    document.getElementById("medial").style="opacity:0;";
                    document.getElementById("change").style="display:none";
               }
               else
               {
                    document.getElementById("medial").style="opacity:1;transition:opacity 1s linear;";
                    document.getElementById("change").style="display:block";
               }
}

function Manage()
{
                var v=document.body.offsetWidth;
                if(v<753){
                    var name=document.getElementsByName("man");
                    for(i=0;i<name.length;i++){
                        name[i].style="visibility:hidden;";
                    }
                }
                else
                {
                    var name=document.getElementsByName("man");
                    for(i=0;i<name.length;i++){
                        name[i].style="visibility:visible";
                    }
                }
}

function ActiveElement(){
                document.getElementById("homet").style="font-size:100%;text-shadow:0px 0px 0px;background:linear-gradient(#222,#222);background-color:#222;";
                Manage();
}

function ActiveElement1(){
               document.getElementById("homet").style="font-size:111%;text-shadow:3px 2px 2px black;background:linear-gradient(#222,#000,#222);background-color:#222;";
               Manage();
}

function slideShow() {
                setInterval(Slide, 5000);
}

function Slide(a=0) {
                n+=a;
                if(n==-2){
                    n=3;
                }
                n=(n+1)%5;
                name="background-image:url('../static/Images/home"+n+".jpg')";
                document.getElementById("home").style=name;
}

function scroll(n)
{
    if(n==1){
         var m=document.getElementById("page1").offsetHeight+80;
         document.getElementById("page2").style="opacity:1;";
         document.getElementById("page1").style="opacity:0;margin-top:-"+m;
         document.getElementById("medial").style="margin-top:90%;";
    }
    else if(n==2){
         document.getElementById("page1").style="opacity:1;margin-top:"+0;
         document.getElementById("page2").style="opacity:0;";
         document.getElementById("medial").style="margin-top:30%;";
    }
   
}
function reunionRtMenu(n){
    if(n){
        v=document.body.offsetWidth;
        v=v-300;
        document.getElementById("a1").style="opacity:1;margin-left:"+v;
    }
    else{
        document.getElementById("a1").style="opacity:0.2;margin-left:96%;";
    }
}
