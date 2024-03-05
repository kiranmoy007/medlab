import { initializeApp } from "https://www.gstatic.com/firebasejs/10.3.1/firebase-app.js";
import { getAuth, createUserWithEmailAndPassword } from "https://www.gstatic.com/firebasejs/10.3.1/firebase-auth.js";


  // Your web app's Firebase configuration
  const firebaseConfig = {
    apiKey: "AIzaSyAvkRLN1Kt04DPLd6d3a6s_bWbxG717F6k",
    authDomain: "medical-app-sign-up.firebaseapp.com",
    projectId: "medical-app-sign-up",
    storageBucket: "medical-app-sign-up.appspot.com",
    messagingSenderId: "1001176669564",
    appId: "1:1001176669564:web:9997104e8e6c3cb17cd8f9" 
  }; 

  // Initialize Firebase with your configuration
  firebase.initializeApp(firebaseConfig);

  // Reference to the Firebase Realtime Database
  const database = firebase.database();

  // Function to handle form submission
  function submitForm(event) {
    event.preventDefault();

    // Get form values
    const name = document.getElementById("Username").value;
    const email = document.getElementById("Email").value;
    const phoneNumber = document.getElementById("Number").value;
    const address = document.getElementById("message").value;
    const symptoms = document.getElementById("symptoms").value;

    // Create a data object
    const formData = {
      name,
      email,
      phoneNumber,
      address,
      symptoms
    };

    // Push the data to the database
    const newFormRef = database.ref("forms").push();
    newFormRef.set(formData);

    // Reset the form
    document.getElementById("myForm").reset();

    alert("Form data submitted successfully!");
  }

  // Add event listener to the form submit button
  document.getElementById("insbtn").addEventListener("click", submitForm);

