const signUpButton=document.getElementById('signUpButton');
const signInButton=document.getElementById('signInButton');
const signInForm=document.getElementById('signIn');
const signUpForm=document.getElementById('signup');

signUpButton.addEventListener('click',function(){
    signInForm.style.display="none";
    signUpForm.style.display="block";
})
signInButton.addEventListener('click', function(){
    signInForm.style.display="block";
    signUpForm.style.display="none";
}) 

function handleCredentialResponse(response) {
    console.log("Encoded JWT ID token: " + response.credential);
    // You can send this token to your server for authentication
}

function renderGoogleSignInButton() {
    google.accounts.id.initialize({
        client_id: "102474177293665555785", // Replace with your actual Client ID
        callback: handleCredentialResponse
    });
    google.accounts.id.renderButton(
        document.getElementById("googleLoginBtn"),
        { theme: "outline", size: "large" }
    );
}