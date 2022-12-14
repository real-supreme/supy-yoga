// const signUpButton = document.getElementById('signUp');
// const signInButton = document.getElementById('signIn');
// const container = document.getElementById('container');

// signUpButton.addEventListener('click', () => {
//     console.log("signUpButton clicked");
//     container.classList.add("right-panel-active");
// });

// signInButton.addEventListener('click', () => {
//     console.log("signInButton clicked");
//     container.classList.remove("right-panel-active");
// });

function signupbutt() {
    const container = document.getElementById('container');
    console.log("signUpButton clicked");
    container.classList.add("right-panel-active");
    console.log("signUpButton clicked");
    request = new XMLHttpRequest();
    request.open("GET", "/accounts/?state=register");
    request.send();
}

function signinbutt() {
    const container = document.getElementById('container');
    console.log("signInButton clicked");
    container.classList.remove("right-panel-active");
    console.log("signInButton clicked");
    request = new XMLHttpRequest();
    request.open("GET", "/accounts/?state=login");
    request.send();
}
