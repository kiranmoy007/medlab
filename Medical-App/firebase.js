

document.getElementById("myForm").addEventListener("submit", function(event) {
  event.preventDefault(); // Prevent the default form submission behavior

  // Get form values
  var name = document.getElementById("Username").value;
  var email = document.getElementById("Email").value;
  var phoneNumber = document.getElementById("Number").value;
  var address = document.getElementById("message").value;
  var symptoms = document.getElementById("symptoms").value;

  // Reference to your Firebase database
  var database = firebase.database();
  var dataRef = database.ref("user"); // Replace with your desired collection name

  // Push data to Firebase
  dataRef.push({
    Name: name,
    Email: email,
    PhoneNumber: phoneNumber,
    Address: address,
    Symptoms: symptoms
  });

  // Clear the form
  document.getElementById("myForm").reset();

  // Optionally, you can display a success message to the user
  alert("Data submitted successfully!");
});
