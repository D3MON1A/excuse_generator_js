/* eslint-disable */

import "../assets/img/rigo-baby.jpg";
import "../assets/img/4geeks.ico";
//import 'breathecode-dom'; //DOM override to make JS easier to use
import "../style/index.scss";

window.onload = async function() {
  console.log("Hello Rigo from the console!");
  const r = await fetch(
    "https://3000-c53d1b0b-b53e-45cf-b9a5-bbb861d12eb9.ws-us02.gitpod.io/api/excuse"
  );
  document.querySelector(".alert").innerHTML = await r.json();
};
