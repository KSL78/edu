const ckl = document.querySelector("h2#ckl");
function getClock()
{
    const date = new Date();
    ckl.innerText =`${date.getHours()}:${date.getMinutes()}:${date.getSeconds()}`
}
getClock();
setInterval(getClock,1000);