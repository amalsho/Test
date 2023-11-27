const input1 = document.querySelector(".input1")
const input2 = document.querySelector(".input2")
const nnn = document.querySelector(".nnn")
function send(){
    if(input1.value=="admin" && input2.value=="1234"){
        input1.style="border-bottom: 2px solid green;"
        input1.value="succes"
        input2.style="border-bottom: 2px solid gray;"
        input2.value="succes"
        DelayNode:10000;
        window.location.href="index2.html"
    }
    else{
        nnn.style="box-shadow: inset red 0 0 5px;"
        input2.style="border-bottom: 2px solid red;"
        input2.style.placeholder="succes"
        input2.style.value="succes"
        input1.style="border-bottom: 2px solid red;"
        input1.style.placeholder="succes"
        input1.style.value="succes"
     }
}