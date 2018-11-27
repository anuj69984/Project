function formreport()  {
    var e=document.getElementsByTagName('input')
    var m=1;
    for(var i=0;i<e.length;i++)
    {
        if(!e[i].value){
            m=0;
            e[i].style="box-shadow:0 0 5px red;border:solid red 2px;";
        }
    }
    if(!m){
        return false;
    }
 }
 function chk(id){
     if(!id.value){
         id.style="box-shadow:0 0 5px red;border:solid red 2px;";
     }
     else{
         id.style="border:1px solid green;box-shadow:none";
     }
 }
  